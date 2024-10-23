"""Parser module to parse gear config.json."""

from pathlib import Path
from typing import Tuple

from flywheel_gear_toolkit import GearToolkitContext

from fw_gear_rtstruct_to_nifti.utils import dynamic_search


# This function mainly parses gear_context's config.json file and returns relevant
# inputs and options.
def parse_config(
    gear_context: GearToolkitContext,
) -> Tuple[bool, dict]:
    """Parses context's config.json file to be used by gear.

    Args:
        gear_context: to provide configuration information

    Returns:
        bool: Debug configuration, default false
        dict: Arguments needed for the gear to run as configured:
            * percent_check: Whether to add the pixel percent processing step
            * save_binary_masks: Whether to save as binary masks or bitmasks
            * save_combined_output: Whether to save as individual files, combined, or both
            * rtstruct_path: Path to input
            * source_dicom_path: Path to source_dicom, if inputted
            * work_dir: Path to work directory
            * output_dir: Path to output directory
    """
    debug = gear_context.config.get("debug")
    gear_args = {
        "percent_check": gear_context.config.get("percent-check"),
        "save_binary_masks": gear_context.config.get("save-binary-masks"),
        "save_combined_output": gear_context.config.get("save-combined-output"),
        "rtstruct_path": Path(gear_context.get_input_path("rtstruct")),
        "source_dicom_path": Path(),
        "work_dir": Path(gear_context.work_dir),
        "output_dir": Path(gear_context.output_dir),
    }

    source_dicom = gear_context.get_input_path("source_dicom")
    if not source_dicom:
        acquisition_id = gear_context.destination.get("id")
        session_id = gear_context.client.get_acquisition(acquisition_id).session
        source_dicom = dynamic_search(
            fw_client=gear_context.client,
            work_dir=gear_context.work_dir,
            rtstruct_path=gear_args["rtstruct_path"],
            session_id=session_id,
        )
    gear_args["source_dicom_path"] = Path(source_dicom)

    return debug, gear_args
