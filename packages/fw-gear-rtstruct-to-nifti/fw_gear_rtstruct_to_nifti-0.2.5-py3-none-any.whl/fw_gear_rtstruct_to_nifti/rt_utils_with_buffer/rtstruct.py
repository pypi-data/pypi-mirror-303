"""Truncated RTStruct class that only contains the methods used in this gear."""

from typing import List

import numpy as np
from pydicom.dataset import FileDataset
from rt_utils import ds_helper

from .image_helper import create_series_mask_from_contour_sequence


class RTStruct:
    """
    Wrapper class to facilitate appending and extracting ROI's within an RTStruct
    """

    def __init__(self, series_data, ds: FileDataset, valid=True):
        self.series_data = series_data
        self.ds = ds
        self.frame_of_reference_uid = ds.ReferencedFrameOfReferenceSequence[
            -1
        ].FrameOfReferenceUID  # Use last strucitured set ROI
        self.valid = valid  # True if SOPInstanceUIDs match

    def get_roi_names(self) -> List[str]:
        """
        Returns a list of the names of all ROI within the RTStruct
        """

        if not self.ds.StructureSetROISequence:
            return []

        return [
            structure_roi.ROIName for structure_roi in self.ds.StructureSetROISequence
        ]

    def get_roi_mask_by_name(self, name, percent_check) -> np.ndarray:
        """
        Returns the 3D binary mask of the ROI with the given input name
        """

        for structure_roi in self.ds.StructureSetROISequence:
            if structure_roi.ROIName == name:
                contour_sequence = ds_helper.get_contour_sequence_by_roi_number(
                    self.ds, structure_roi.ROINumber
                )
                # NOTE: percent_check has been added to pass the config option through
                return create_series_mask_from_contour_sequence(
                    self.series_data,
                    contour_sequence,
                    percent_check,
                    self.valid,
                )
