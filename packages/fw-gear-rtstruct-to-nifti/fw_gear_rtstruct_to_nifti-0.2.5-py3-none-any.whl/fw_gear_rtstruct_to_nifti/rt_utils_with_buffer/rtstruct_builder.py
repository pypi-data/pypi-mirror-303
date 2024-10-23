"""rtstruct_builder.py, from commit b70ad40 on qurit's rt_utils. Changes called out via comment"""

import warnings
from pprint import pformat
from typing import List, Optional

from pydicom.dataset import Dataset
from pydicom.filereader import dcmread
from rt_utils import ds_helper, image_helper
from rt_utils.utils import SOPClassUID

from .rtstruct import RTStruct


class RTStructBuilder:
    """
    Class to help facilitate the two ways in one can instantiate the RTStruct wrapper
    """

    @staticmethod
    def create_new(dicom_series_path: str) -> RTStruct:
        """
        Method to generate a new rt struct from a DICOM series
        """

        series_data = image_helper.load_sorted_image_series(dicom_series_path)
        ds = ds_helper.create_rtstruct_dataset(series_data)
        return RTStruct(series_data, ds)

    @staticmethod
    def create_from(dicom_series_path: str, rt_struct_path: str) -> RTStruct:
        """
        Method to load an existing rt struct, given related DICOM series and existing rt struct
        """
        # Original function has `warn_only` arg; this is removed and instead
        # the validate_rtstruct_series_references function is used to determine
        # whether the source DICOM and RTStruct have matching SOPInstanceUIDs
        # and therefore can be matched on these UIDs, or if ImagePositionPatient
        # needs to be used as a fallback

        series_data = image_helper.load_sorted_image_series(dicom_series_path)
        ds = dcmread(rt_struct_path)
        RTStructBuilder.validate_rtstruct(ds)
        valid = RTStructBuilder.validate_rtstruct_series_references(ds, series_data)

        # TODO create new frame of reference? Right now we assume the last frame of reference created is suitable
        return RTStruct(series_data, ds, valid)

    @staticmethod
    def validate_rtstruct(ds: Dataset):
        """
        Method to validate a dataset is a valid RTStruct containing the required fields
        """

        if (
            ds.SOPClassUID != SOPClassUID.RTSTRUCT
            or not hasattr(ds, "ROIContourSequence")
            or not hasattr(ds, "StructureSetROISequence")
            or not hasattr(ds, "RTROIObservationsSequence")
        ):
            raise Exception("Please check that the existing RTStruct is valid")

    @staticmethod
    def validate_rtstruct_series_references(
        ds: Dataset, series_data: List[Dataset]
    ) -> bool:
        """
        Method to validate RTStruct only references dicom images found within the input series_data
        """
        problematic_uids = []
        valid = True
        for refd_frame_of_ref in ds.ReferencedFrameOfReferenceSequence:
            # Study sequence references are optional so return early if it does not exist
            if "RTReferencedStudySequence" not in refd_frame_of_ref:
                return

            for rt_refd_study in refd_frame_of_ref.RTReferencedStudySequence:
                for rt_refd_series in rt_refd_study.RTReferencedSeriesSequence:
                    for contour_image in rt_refd_series.ContourImageSequence:
                        res = RTStructBuilder.validate_contour_image_in_series_data(
                            contour_image, series_data
                        )
                        if res:
                            problematic_uids.append(res)

        # Instead of logging each bad UID in a potential cascade of warnings,
        # this collects all bad UIDs, logs all at once, and notifies the user
        # that ImagePositionPatient will be utilized as a fallback.
        if problematic_uids:
            valid = False
            msg = (
                "Loaded RTStruct references image(s) that are not contained in input series data. "
                f"Problematic SOPInstanceUIDs:\n{pformat(problematic_uids)}\n"
                "As SOPInstanceUIDs cannot be utilized to align the RTStruct, gear will attempt "
                "to utilize ImagePositionPatient to determine where contours should be drawn."
            )
            warnings.warn(msg)

        return valid

    @staticmethod
    def validate_contour_image_in_series_data(
        contour_image: Dataset, series_data: List[Dataset]
    ) -> Optional[str]:
        """
        Method to validate that the ReferencedSOPInstanceUID of a given contour image exists within the series data
        """
        for series in series_data:
            if contour_image.ReferencedSOPInstanceUID == series.SOPInstanceUID:
                return

        # ReferencedSOPInstanceUID is NOT available
        # The following is altered from rt-utils to utilize validation to determine how to proceed
        # and log all bad UIDs at once instead of in a cascade of warnings.
        return contour_image.ReferencedSOPInstanceUID
