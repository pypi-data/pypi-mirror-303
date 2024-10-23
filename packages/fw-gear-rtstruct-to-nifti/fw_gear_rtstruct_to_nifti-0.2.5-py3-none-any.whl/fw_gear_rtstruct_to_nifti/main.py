"""Main module."""

import logging

from fw_gear_rtstruct_to_nifti.creator import Creator
from fw_gear_rtstruct_to_nifti.prepper import Prepper
from fw_gear_rtstruct_to_nifti.utils import ROIInfo

log = logging.getLogger(__name__)


def run(gear_args: dict) -> int:
    """Initializes the needed components and runs.

    Args:
        gear_args: Arguments needed for the gear to run as configured:
            * percent_check: Whether to add the pixel percent processing step
            * save_binary_masks: Whether to save as binary masks or bitmasks
            * save_combined_output: Whether to save as individual files or combined
            * rtstruct_path: Path to input
            * source_dicom_path: Path to source_dicom, if inputted
            * work_dir: Path to work directory
            * output_dir: Path to output directory

    Returns:
        int: Exit code, 0 if success.
    """
    prep = Prepper(
        work_dir=gear_args["work_dir"],
        rtstruct_path=gear_args["rtstruct_path"],
        source_dicom_path=gear_args["source_dicom_path"],
        percent_check=gear_args["percent_check"],
    )
    roi_info = ROIInfo(
        prepper=prep,
        output_dir=gear_args["output_dir"],
        combine=gear_args["save_combined_output"],
        binary_mask=gear_args["save_binary_masks"],
    )
    create = Creator(
        prepper=prep,
        combine=gear_args["save_combined_output"],
        binary_mask=gear_args["save_binary_masks"],
        output_dir=gear_args["output_dir"],
    )

    create.make_data(roi_info=roi_info)
    roi_info.export_to_csv()

    return 0
