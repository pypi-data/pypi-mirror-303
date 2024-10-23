"""Creator.py module for creating DICOMs from RTStruct array."""

import logging
import os
import re
from abc import ABC
from pathlib import Path

import numpy as np
import SimpleITK as sitk

from fw_gear_rtstruct_to_nifti.prepper import Prepper
from fw_gear_rtstruct_to_nifti.utils import ROIInfo

log = logging.getLogger(__name__)

MAX_LABELS = 2**5 - 1


class Creator(ABC):
    """Creates DICOM files from source DICOM and RTStruct arrays."""

    def __init__(
        self,
        prepper: Prepper,
        combine: str,
        binary_mask: bool,
        output_dir: Path,
    ):
        """Initializes Creator.

        Args:
            prepper: Prepper as previously initialized
            combine: Whether to save masks as combined, individual, or both
            binary_mask: Whether or not to output binary masks (vs bitmasks)
            output_dir: Path to output directory
        """
        # Useful paths
        self.work_dir = prepper.work_dir
        self.dicom_dir = prepper.dicom_dir
        self.rtstruct_path = prepper.rtstruct_path
        self.output_dir = output_dir

        # Loaded RTStruct and DICOM elements
        self.rtstruct = prepper.rtstruct
        self.roi_names = prepper.roi_names
        self.masks = prepper.masks
        self.dicoms = prepper.dicoms
        self.sitk_dicoms = prepper.sitk_dicoms

        # Config options
        self.combine = combine
        self.binary_mask = binary_mask

        self.dtype = np.uint8
        self.bits = 8
        self.shape = prepper.shape

    def set_bit_level(self):
        """Sets self.bits according to label length if not combining and binary masks are okay."""
        # If we're not combining and binary masks are ok, we don't need to bitmask, we'll leave at default 8 bit.
        # Otherwise, we have to find the datatype:
        if self.combine in ["combined", "both"] or not self.binary_mask:
            if len(self.roi_names) < 8:
                self.dtype = np.uint8
                self.bits = 8
            elif len(self.roi_names) < 16:
                self.dtype = np.uint16
                self.bits = 16
            elif len(self.roi_names) < 32:
                self.dtype = np.uint32
                self.bits = 32

            elif len(self.roi_names) > MAX_LABELS:
                log.exception(
                    f"Due to the maximum integer length ({MAX_LABELS+1} bits), we can "
                    f"only keep track of a maximum of {MAX_LABELS} ROIs with a bitmasked "
                    f"combination. You have {len(self.roi_names)} ROIs. Exiting."
                )
                os.sys.exit(1)

    def generate_name(self, roi_name: str, output_filetype: str) -> str:
        """Create name to be used for output filename.

        Args:
            roi_name: ROI label or "ALL" if generating combined output filename
            output_filetype: Filetype to output, e.g "nii.gz"

        Returns:
            str: output_filename for creation of output file
        """
        # Remove non alphanumeric characters from potential filename
        roi_name = re.sub("[^0-9a-zA-Z]+", "_", roi_name)
        roi_name = roi_name.strip("_")

        base = self.rtstruct_path.name
        for suffix in [".zip", ".dcm", ".dicom"]:
            if base.endswith(suffix):
                base = base.removesuffix(suffix)

        base = re.sub("[^0-9a-zA-Z]+", "_", base)
        base = base.strip("_")

        output_filename = f"ROI_{roi_name}_{base}.{output_filetype}"

        return output_filename

    def make_data(self, roi_info: ROIInfo):
        """Create the array needed for producing the ROI mask output as configured.

        Args:
            roi_info: ROIInfo initialized with useful ROI label info
        """
        self.set_bit_level()

        if self.combine in ["individual", "both"]:
            for roi in self.masks.keys():
                log.info(f"Processing individual ROI: {roi}")
                roi_mask = self.masks[roi]
                roi_mask = roi_mask.astype(self.dtype)

                if not self.binary_mask:
                    roi_mask *= roi_info.get_voxel_value(roi)

                output_filename = self.generate_name(roi, "nii.gz")
                output = self.output_dir.joinpath(output_filename)
                log.info("Saving individual ROI mask...")
                roi_mask = np.transpose(roi_mask, (2, 0, 1))
                struct_image = sitk.GetImageFromArray(roi_mask)
                struct_image.CopyInformation(self.sitk_dicoms)
                sitk.WriteImage(struct_image, output)

        if self.combine in ["combined", "both"]:
            log.info("Processing combined ROIs")
            data = np.zeros(self.shape, dtype=self.dtype)
            for roi in self.masks.keys():
                roi_mask = self.masks[roi]
                roi_mask = roi_mask.astype(self.dtype)
                roi_mask *= roi_info.get_voxel_value(roi)
                data += roi_mask
            output_filename = self.generate_name("ALL", "nii.gz")
            output = self.output_dir.joinpath(output_filename)
            log.info("Saving combined mask...")
            data = np.transpose(data, (2, 0, 1))
            struct_image = sitk.GetImageFromArray(data)
            struct_image.CopyInformation(self.sitk_dicoms)
            sitk.WriteImage(struct_image, output)
