"""Fixers.py module for rtstruct-to-nifti."""

import logging
from collections import Counter
from pathlib import Path

from fw_file.dicom import DICOMCollection
from pydicom import dcmread

log = logging.getLogger(__name__)


def apply_fixers(dicoms: DICOMCollection) -> DICOMCollection:
    """Runs all known fixers for optimal chance of success.

    Args:
        dicoms: source_dicom's DICOMCollection

    Returns:
        DICOMCollection: Post-fix DICOMCollection
    """
    dicoms = fix_StudyTime(dicoms)

    return dicoms


def fix_StudyTime(dicoms: DICOMCollection) -> DICOMCollection:
    """Checks StudyTime and updates to consistent value if applicable.

    If StudyTime varies across the source DICOM, the NIfTI conversion will
    not stack slices as expected; this function is to prevent that outcome.

    Args:
        dicoms: source_dicom's DICOMCollection

    Returns:
        DICOMCollection: Post-fix DICOMCollection
    """
    try:
        dicoms.get("StudyTime")
    except ValueError:
        study_times = Counter(dicoms.bulk_get("StudyTime"))
        mode = study_times.most_common(1)[0][0]
        dicoms.set("StudyTime", mode)
        log.warning(
            "StudyTime not consistent over all source DICOM files. "
            f"Adjusting StudyTime to constant value {mode} "
            "so that slices are stacked during NIfTI conversion."
        )

    return dicoms


def fix_ROIName(rtstruct_path: Path):
    """Iterates through ROINames and fixes potential problems.

    This function looks for blank or duplicated ROIName values.
    Because rt_utils uses ROIName for lookup, duplicated ROIName
    values may cause errors on loading pixel data. Additionally,
    to make sure the user can easily parse which voxel value goes
    with which label when comparing the outputted NIfTI mask and
    CSV file, blank labels are renamed as `unlabeled_<ROINumber>`.

    Args:
        rtstruct_path: Path to RTStruct
    """
    rtstruct = dcmread(rtstruct_path)
    ssrs = rtstruct.StructureSetROISequence
    all_roi_names = []
    log.info("Checking ROI labels for blanks and duplicates...")
    for roi in ssrs:
        if roi.ROIName in all_roi_names:
            log.warning(
                f"Duplicate label name {roi.ROIName} found. Label "
                f"name will be changed to {roi.ROIName}_{roi.ROINumber} "
                "to maintain delineation between ROIs."
            )
            roi.ROIName = f"{roi.ROIName}_{roi.ROINumber}"
        elif roi.ROIName == "":
            log.warning(
                "ROI without ROIName found. Name will be set to "
                f"unlabeled_{roi.ROINumber}."
            )
            roi.ROIName = f"unlabeled_{roi.ROINumber}"

        all_roi_names.append(roi.ROIName)
    rtstruct.save_as(rtstruct_path)
    log.info("ROI Label check complete.")
