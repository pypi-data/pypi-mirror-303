"""Utils.py module for rtstruct-to-nifti."""

import functools
import logging
import os
import re
import typing as t
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from flywheel import Client
from fw_file.dicom import DICOM, DICOMCollection
from shapely.geometry import Polygon

from fw_gear_rtstruct_to_nifti.prepper import Prepper

log = logging.getLogger(__name__)


def dynamic_search(
    fw_client: Client, work_dir: Path, rtstruct_path: Path, session_id: str
) -> Path:
    """Searches the session container for a matching DICOM.

    Args:
        fw_client: Flywheel Client instance
        work_dir: Path to work directory
        rtstruct_path: Path to input RTStruct
        session_id: Flywheel session id related to input RTStruct

    Returns:
        Path: Path to downloaded matching DICOM
    """
    log.info("Attempting to locate source DICOM...")
    rtstruct_filename = rtstruct_path.name
    sops_to_match = get_rtstruct_referenced_sop(rtstruct_path)
    dicom_file_paths = collect_potential_dicom_files(
        fw_client, work_dir, session_id, rtstruct_filename
    )
    source_dicom = check_all_dicom_files(dicom_file_paths, sops_to_match)
    log.info(f"Identified {source_dicom.name} as source DICOM.")

    return source_dicom


def get_rtstruct_referenced_sop(rtstruct_path: Path) -> list:  # noqa: PLR0912
    """Collects a list of the RTStruct's ReferencedSOPInstanceUIDs.

    Args:
        rtstruct_path: Path to RTStruct

    Returns:
        list: List of all ReferencedSOPInstanceUIDs
    """
    try:
        referenced_sop_instance_uids = []
        if zipfile.is_zipfile(rtstruct_path):
            rtstruct = DICOMCollection.from_zip(rtstruct_path, force=True)
            for refd_frame_of_ref_bulk in rtstruct.bulk_get(
                "ReferencedFrameOfReferenceSequence"
            ):
                for refd_frame_of_ref in refd_frame_of_ref_bulk:
                    for rt_refd_study in refd_frame_of_ref.RTReferencedStudySequence:
                        for rt_refd_series in rt_refd_study.RTReferencedSeriesSequence:
                            for contour_image in rt_refd_series.ContourImageSequence:
                                referenced_sop_instance_uids.append(
                                    contour_image.ReferencedSOPInstanceUID
                                )
        else:
            rtstruct = DICOM(rtstruct_path, force=True)
            for refd_frame_of_ref in rtstruct.ReferencedFrameOfReferenceSequence:
                for rt_refd_study in refd_frame_of_ref.RTReferencedStudySequence:
                    for rt_refd_series in rt_refd_study.RTReferencedSeriesSequence:
                        for contour_image in rt_refd_series.ContourImageSequence:
                            referenced_sop_instance_uids.append(
                                contour_image.ReferencedSOPInstanceUID
                            )
        return referenced_sop_instance_uids
    except:  # noqa: E722
        log.debug("", exc_info=True)
        log.error(
            "Unable to parse ReferencedFrameOfReferenceSequence from RTSTRUCT, "
            "and therefore cannot dynamically identify source_dicom. "
            "source_dicom must be provided via gear input. Exiting."
        )
        os.sys.exit(1)


def collect_potential_dicom_files(
    fw_client: Client, work_dir: Path, session_id: str, rtstruct_filename: str
) -> list:
    """Downloads all DICOM files in the session container for review.

    Args:
        fw_client: Flywheel Client
        work_dir: Path to work directory
        session_id: Flywheel session ID to search
        rtstruct_filename: RTStruct name (to prevent re-download)

    Returns:
        list: Paths to all downloaded DICOM files
    """
    dicom_search_dir = work_dir / "potential_dicoms"
    dicom_search_dir.mkdir(parents=True, exist_ok=True)
    dicom_file_paths = []

    session = fw_client.get_session(session_id)
    acquisitions = session.acquisitions.find()
    for acquisition in acquisitions:
        files = acquisition.get("files")
        for file in files:
            if file.get("type") == "dicom" and file.get("name") != rtstruct_filename:
                filename = file.get("name")
                filepath = dicom_search_dir / filename
                acquisition.download_file(filename, dest_file=filepath)
                dicom_file_paths.append(filepath)

    return dicom_file_paths


def check_all_dicom_files(dicom_file_paths: list, sops_to_match: list) -> Path:
    """Iterate through all possible DICOMs and check for SOP Instance UID match.

    If no DICOMs match, or more than one matches, instruct user to
    explicitly input source_dicom as gear input and exit.

    Args:
        dicom_file_paths: List of paths to downloaded DICOMs
        sops_to_match: UIDs from RTStruct to match

    Returns:
        Path: Path to source_dicom, if found
    """
    matching_files = []
    for dicom_file in dicom_file_paths:
        dicom_path = check_dicom_file(dicom_file, sops_to_match)
        if dicom_path:
            matching_files.append(dicom_path)

    if len(matching_files) == 1:
        # Only one possible source_dicom found in session,
        # this is what we want.
        source_dicom_path = matching_files[0]
        return source_dicom_path
    else:
        # No possible matching DICOMs, or too many. Raise error.
        log.error(
            "%s potential source_dicom files identified; "
            "gear cannot dynamically identify source_dicom. "
            "source_dicom must be provided via gear input. Exiting.",
            len(matching_files),
        )
        os.sys.exit(1)


def check_dicom_file(dicom_file: Path, sops_to_match: list) -> t.Optional[Path]:
    """Check individual DICOM file and return filepath if match.

    Args:
        dicom_file: Path to downloaded DICOM file being checked
        sops_to_match: RTStruct UIDs to use for check

    Returns:
        Path: If DICOM matches UIDs, path to DICOM file
    """
    if zipfile.is_zipfile(dicom_file):
        dcms = DICOMCollection.from_zip(dicom_file, force=True)
        sops = dcms.bulk_get("SOPInstanceUID")
        if not set(sops).intersection(sops_to_match):
            return None
    else:
        dcm = DICOM(dicom_file, force=True)
        try:
            sop = dcm.SOPInstanceUID
            if sop not in sops_to_match:
                return None
        except AttributeError:
            log.warn(
                f"Encountered DICOM file without SOPInstanceUID: {dicom_file.name}. "
                "Continuing..."
            )
            return None

    return dicom_file


class ROIInfo:
    """Stores info needed for lookups and CSV output."""

    def __init__(
        self,
        prepper: Prepper,
        output_dir: Path,
        combine: str,
        binary_mask: bool,
    ):
        """Initializes ROIInfo to hold data.

        Args:
            prepper: Prepper as previously initialized
            output_dir: Directory in which to save CSV
            combine: Whether to save masks as individual, combined, or both
            binary_mask: Whether to save individual masks as binary or bitmasks
        """
        self.rtstruct = prepper.rtstruct
        self.roi_names = prepper.roi_names
        self.masks = prepper.masks
        self.dicoms = prepper.dicoms
        self.rtstruct_path = prepper.rtstruct_path
        self.output_dir = output_dir
        self.combine = combine
        self.binary_mask = binary_mask

        self.roi_info = pd.DataFrame(
            columns=[
                "label",
                "reference_number",
                "foreground_voxel_value",
                "voxels",
                "mask_volume(mm^3)",
                "contour_volume(mm^3)",
            ]
        )

        self.populate_roi_info()

    def populate_roi_info(self):
        """For each ROI, calculate info and populate DataFrame."""
        count = 0
        for roi in self.rtstruct.ds.StructureSetROISequence:
            try:
                mask = self.masks[roi.ROIName]
            except KeyError:
                # If label not in self.masks, mask has no voxels
                log.warning(
                    f"{roi.ROIName} will not be included on the ROI_info.csv, "
                    "as the ROI does not correspond with any voxels."
                )
                continue

            num_voxels = np.count_nonzero(mask)
            volume = self.calc_volume(num_voxels)
            if volume is np.nan:
                log.warning(f"Volume could not be calculated for {roi.ROIName}.")
            if self.binary_mask and self.combine == "individual":
                # If only outputting individual binary masks,
                # all foreground values will be 1.
                voxel_value = 1
            else:
                # Else, store bitmasked values of combined mask.
                voxel_value = 2**count

            contour_volume = self.calc_contour_volume(roi.ROINumber)

            roi_dict = {
                "label": [roi.ROIName],
                "reference_number": [roi.ROINumber],
                "foreground_voxel_value": [voxel_value],
                "voxels": num_voxels,
                "mask_volume(mm^3)": [volume],
                "contour_volume(mm^3)": [contour_volume],
            }
            roi_pd = pd.DataFrame.from_dict(roi_dict)
            self.roi_info = pd.concat([self.roi_info, roi_pd])
            count += 1

    @functools.lru_cache()
    def get_z_spacing(self):
        """Gets SpacingBetweenSlices or SliceThickness from DICOM."""
        z_spacing = self.dicoms.get("SpacingBetweenSlices")
        if not z_spacing:
            z_spacing = self.dicoms.get("SliceThickness")
        if not z_spacing:
            z_spacing = get_from_shared(
                self.dicoms[0], ["PixelMeasuresSequence", "SliceThickness"]
            )
        if not z_spacing:
            z_spacing = get_from_per_frame(
                self.dicoms[0],
                ["PixelMeasuresSequence", "SliceThickness"],
                raising=False,
            )
        return z_spacing

    def calc_contour_volume(self, referenced_ROI: int) -> float:
        """Using RTStruct contours and z spacing, calculate volume.

        Args:
            referenced_ROI: ReferencedROINumber of contour

        Returns:
            float: Volume of contour in mm^3
        """
        z_spacing = self.get_z_spacing()
        if not z_spacing:
            return np.nan

        rtstruct = DICOM(self.rtstruct_path, force=True)
        area_xy = 0
        for roics in rtstruct.ROIContourSequence:
            if roics.ReferencedROINumber == referenced_ROI:
                for cs in roics.ContourSequence:
                    contour_data = cs.ContourData
                    reshaped_contour_data = np.reshape(
                        contour_data, [len(contour_data) // 3, 3]
                    )
                    pgon = Polygon(reshaped_contour_data)
                    area_xy += pgon.area

        area = area_xy * z_spacing

        return area

    def calc_volume(self, num_voxels: int) -> float:
        """Using DICOM spacing info and voxel count, calculate volume.

        Args:
            num_voxels: Number of nonzero voxels in ROI mask

        Returns:
            float: Volume of ROI in mm^3
        """
        z_spacing = self.get_z_spacing()

        pixel_spacing = self.dicoms.get("PixelSpacing")
        if not pixel_spacing:
            pixel_spacing = self.dicoms.get("ImagerPixelSpacing")
        if not pixel_spacing:
            pixel_spacing = get_from_shared(
                self.dicoms[0], ["PixelMeasuresSequence", "PixelSpacing"]
            )
        if not pixel_spacing:
            pixel_spacing = get_from_per_frame(
                self.dicoms[0],
                ["PixelMeasuresSequence", "PixelSpacing"],
                raising=False,
            )

        if z_spacing and pixel_spacing:
            voxel_volume = np.prod([*pixel_spacing, z_spacing])
            volume = num_voxels * voxel_volume
            return volume

        return np.nan

    def get_voxel_value(self, label: str) -> int:
        """Retrieves foreground_voxel_value from DataFrame.

        Args:
            label: ROI label name

        Returns:
            int: Voxel value to be used for corresponding ROI
        """
        voxel_value = self.roi_info.loc[
            self.roi_info["label"] == label, "foreground_voxel_value"
        ].item()
        return voxel_value

    def export_to_csv(self):
        """Export roi_info DataFrame to CSV and save in output directory."""
        base = self.rtstruct_path.name
        for suffix in [".zip", ".dcm", ".dicom"]:
            if base.endswith(suffix):
                base = base.removesuffix(suffix)
        base = re.sub("[^0-9a-zA-Z]+", "_", base)
        base = base.strip("_")
        output_filename = f"{base}_ROI_info.csv"

        filepath = self.output_dir / output_filename
        log.info(f"Saving roi_info csv file as {output_filename}.")
        self.roi_info.to_csv(filepath, index=False, float_format="%.3f")


def get_from_shared(dicom: DICOM, steps: t.List[str]):
    """Get a value from the SharedFunctionalGroupsSequence by path.

    Args:
        dicom (DICOM): Input dicom
        steps (t.List[str]): Path steps to a dicom value
            e.g. if you want to get the value of
            dicom.SharedFunctionalGroupsSequence[0].PixelMeasuresSequence[0].SliceThickness
            you would pass in `[PixelMeasuresSequence, SliceThickness]`

    Returns:
        Result
    """
    res = None
    shared = dicom.get("SharedFunctionalGroupsSequence")
    if shared:
        int_ = shared[0].get(steps[0])
        if int_:
            res = int_[0].get(steps[1])
    return res


def get_from_per_frame(dicom: DICOM, steps: t.List[str], raising=True):
    """Get a value from the PerFrameFunctionalGroupsSequence by path.

    Args:
        dicom (DICOM): Input dicom
        steps (t.List[str]): Path steps to a dicom value
            e.g. if you want to get the value of
            dicom.PerFrameFunctionalGroupsSequence[*].PixelMeasuresSequence[*].SliceThickness
            you would pass in `[PixelMeasuresSequence, SliceThickness]`
        raising (bool): Whether to raise an error if the value varies across
            frames. Defaults to True

    Note: This function only returns a value if it is the same across all frames.
        If the value varies, it will either raise an error or return None based on
        the value of the `raising` kwarg.

    Returns:
        Result
    """
    res = None
    per_frame = dicom.get("PerFrameFunctionalGroupsSequence")
    if per_frame:
        results = []
        for frame in per_frame:
            int_ = frame.get(steps[0])
            if int_:
                results.append(int_[0].get(steps[1]))
        # If results are more than one, raise an error according to kwarg
        result_set = set(results)
        if len(result_set) != 1:
            if raising:
                raise RuntimeError(
                    f"{steps[1]} varies across frames, found: {result_set}"
                )
            else:
                return None
        res = results[0]
    return res
