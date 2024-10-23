"""Prepper.py module for loading in RTStruct and DICOM."""

import logging
import os
import shutil
import zipfile
from abc import ABC
from pathlib import Path

import numpy as np
import SimpleITK as sitk
from fw_file.dicom import DICOMCollection
from fw_file.dicom.utils import sniff_dcm

from fw_gear_rtstruct_to_nifti.fixers import apply_fixers, fix_ROIName
from fw_gear_rtstruct_to_nifti.rt_utils_with_buffer import RTStructBuilder

log = logging.getLogger(__name__)


class Prepper(ABC):
    """Prepares DICOM and RTStruct files for use."""

    def __init__(
        self,
        work_dir: Path,
        rtstruct_path: Path,
        source_dicom_path: Path,
        percent_check: str,
    ):
        """Initalizes Prepper.

        Args:
            work_dir: Path to work directory
            rtstruct_path: Path to RTStruct
            source_dicom_path: Path to source DICOM
            percent_check: Whether to add the pixel percent processing step

        """
        if work_dir is None:
            work_dir = ""

        self.work_dir = Path(work_dir)
        self.dicom_dir = self.work_dir / "dicoms"
        self.source_dicom_path = source_dicom_path
        self.rtstruct_path = rtstruct_path

        self.percent_check = percent_check

        self.rtstruct = None
        self.roi_names = None
        self.masks = None

        self.dicoms = None
        self.shape = None

        self.load_dicoms()
        if zipfile.is_zipfile(self.rtstruct_path):
            self.unzip_rtstruct()
        self.load_rtstruct()

    def load_dicoms(self):
        """Moves DICOM file to work_dir; unzips DICOM if archived, and loads."""
        self.dicom_dir.mkdir(parents=True, exist_ok=True)
        if zipfile.is_zipfile(self.source_dicom_path):
            dicoms = DICOMCollection.from_zip(self.source_dicom_path, force=True)
            dicoms = apply_fixers(dicoms)
            dicoms.save()
            dicoms.to_dir(self.dicom_dir)

        else:
            if not sniff_dcm(self.source_dicom_path):
                log.warning(
                    "Source DICOM is missing file signature, "
                    "attempting to read as a single DICOM."
                )
            shutil.move(self.source_dicom_path.as_posix(), self.dicom_dir.as_posix())
            dicoms = DICOMCollection.from_dir(self.dicom_dir, force=True)
            dicoms = apply_fixers(dicoms)
            dicoms.save()

        self.set_dicom_shape(dicoms)
        self.dicoms = dicoms

        sitk_dicoms = sitk.ImageSeriesReader().GetGDCMSeriesFileNames(
            str(self.dicom_dir)
        )
        self.sitk_dicoms = sitk.ReadImage(sitk_dicoms)

    def set_dicom_shape(self, dicoms: DICOMCollection):
        """Sets DICOM shape."""
        try:
            rows = dicoms.get("Rows")
            cols = dicoms.get("Columns")
            # In a single-frame this will be missing, so frames will be `None`
            num_frames = dicoms.get("NumberOfFrames")
        except ValueError:
            log.warning(
                "Rows, Columns, or NumberOfFrames values not consistent over "
                "all source DICOM files. Exiting."
            )
            os.sys.exit(1)
        if num_frames and num_frames > 1:
            # Multiframe
            if len(dicoms) > 1:
                # Not handling the case where the input is a zip of multiframe images.
                log.warning(
                    "Multiple multiframe DICOMs found, cannot continue. Exiting."
                )
                os.sys.exit(1)
            frames = num_frames
        else:
            # Single frame
            frames = len(dicoms)

        self.shape = (rows, cols, frames)

    def unzip_rtstruct(self):
        """If RTStruct is a zipfile, unzip before loading."""
        rtstruct_dir = self.work_dir / "rtstruct"
        rtstruct_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.rtstruct_path, "r") as z:
            z.extractall(rtstruct_dir)
        rtstruct_files = [f for f in rtstruct_dir.rglob("*") if f.is_file()]
        if len(rtstruct_files) == 1:
            self.rtstruct_path = rtstruct_files[0]
        else:
            log.error(
                f"Error unzipping RTStruct file. {len(rtstruct_files)} "
                "files found in zipfile (expected 1). Exiting."
            )
            os.sys.exit(1)

    def load_rtstruct(self):
        """Loads in the RTStruct, sets self.rtstruct, self.roi_names, and self.masks."""
        # Because rt-utils RTStruct depends on ROIName for mapping to
        # ROI masks, we want to make sure that these names exist and
        # are unique before loading.
        fix_ROIName(self.rtstruct_path)
        try:
            self.rtstruct = RTStructBuilder.create_from(
                dicom_series_path=self.dicom_dir,
                rt_struct_path=self.rtstruct_path,
            )
        except Exception as e:
            if "Please check that the existing RTStruct is valid" in e.args[0]:
                log.error(
                    "RTStruct validation failed. A valid RTStruct adheres to the following:\n"
                    "\tSOPClassUID == '1.2.840.10008.5.1.4.1.1.481.3'\n"
                    "\tROIContourSequence attribute exists\n"
                    "\tStructureSetROISequence attribute exists\n"
                    "\tRTROIObservationsSequence attribute exists\n"
                    "Please check that the inputted RTStruct is valid."
                )
            elif "Problematic image" in e.args[0]:
                log.error(
                    "RTStruct contour image validation failed; one or more RTStruct "
                    "ReferencedSOPInstanceUIDs do not match with the source DICOM SOPInstanceUID. "
                    "Please check that the correct source DICOM was inputted."
                )
            else:
                log.error("Exception raised while loading RTStruct: %s", e)
            os.sys.exit(1)

        self.roi_names = self.rtstruct.get_roi_names()

        if len(self.roi_names) > 0:
            log.info(f"Found {len(self.roi_names)} ROIs: {self.roi_names}")
        else:
            log.error("Found no RTStruct ROIs. Exiting.")
            os.sys.exit(1)

        self.masks = {}

        if self.percent_check == "auto":
            # This currently checks between "MIM" and not-MIM. As different RTStructs
            # are identified, it may be useful to add additional tags/values/settings.
            mfg = self.rtstruct.ds.Manufacturer
            if "MIM" in mfg:
                log.info(
                    "RTStruct identified as MIM-created. Pixel percent processing will be "
                    "set to 'off', as this processing option was created for aTMTV-created "
                    "RTStructs. If desired, `percent_check` can be set to 'on' to manually "
                    "choose this processing option."
                )
                self.percent_check = "off"
            else:
                log.info(
                    "RTStruct identified as non-MIM-created. Pixel percent processing will "
                    "be set to 'on'. If desired, `percent_check` can be set to 'off' to "
                    f"manually skip this processing option.\n(Manufacturer: {mfg})"
                )
                self.percent_check = "on"

        for roi_name in self.roi_names:
            roi_mask = self.rtstruct.get_roi_mask_by_name(roi_name, self.percent_check)
            if np.count_nonzero(roi_mask) == 0:
                log.warning(
                    f"{roi_name} is not associated with any voxels, skipping..."
                )
                continue
            if roi_mask.shape != self.shape:
                log.error(
                    f"{roi_name} mask shape {roi_mask.shape} "
                    f"is incongruent with loaded source DICOM shape, {self.shape}. "
                    "Exiting."
                )
                os.sys.exit(1)
            self.masks[roi_name] = roi_mask
