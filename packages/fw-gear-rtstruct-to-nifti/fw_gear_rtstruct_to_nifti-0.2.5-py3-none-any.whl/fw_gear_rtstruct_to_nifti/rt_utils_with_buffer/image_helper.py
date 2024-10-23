"""Adjusted rt_utils image_helper.py that utilizes Shapely to clean up contours before creating pixel arrays."""

import logging

import cv2 as cv
import numpy as np
from pydicom import Dataset, Sequence
from rt_utils.image_helper import (
    apply_transformation_to_3d_points,
    get_patient_to_pixel_transformation_matrix,
    get_slice_contour_data,
)
from shapely.errors import GEOSException
from shapely.geometry import MultiPolygon, Point, Polygon

log = logging.getLogger(__name__)


def get_slice_mask_from_slice_contour_data(
    series_slice: Dataset,
    slice_contour_data,
    transformation_matrix: np.ndarray,
    percent_check,
):
    # NOTE: added percent_check to pass the config through
    # Go through all contours in a slice, create polygons in correct space and with a correct format
    # and append to polygons array (appropriate for fillPoly)
    polygons = []
    for contour_coords in slice_contour_data:
        reshaped_contour_data = np.reshape(
            contour_coords, [len(contour_coords) // 3, 3]
        )

        # Create polygon with shapely, then buffer
        pgon = Polygon(reshaped_contour_data)
        pgon_buffered = pgon.buffer(-0.5)
        if pgon_buffered.is_empty:
            # If buffering fails and the polygon coords are wiped,
            # fall back to using original reshaped_contour_data
            translated_contour_data = apply_transformation_to_3d_points(
                reshaped_contour_data, transformation_matrix
            )
            polygon = [np.around([translated_contour_data[:, :2]]).astype(np.int32)]
            polygon = np.array(polygon).squeeze()
            polygons.append(polygon)
        elif isinstance(pgon_buffered, Polygon):
            pgon_buffered_data = np.array(pgon_buffered.exterior.coords)
            buffered_3d = np.insert(
                pgon_buffered_data, obj=2, values=reshaped_contour_data[0][-1], axis=1
            )
            translated_contour_data = apply_transformation_to_3d_points(
                buffered_3d, transformation_matrix
            )
            polygon = [np.around([translated_contour_data[:, :2]]).astype(np.int32)]
            polygon = np.array(polygon).squeeze()
            polygons.append(polygon)
        else:  # type(pgon_buffered) == MultiPolygon
            # If buffering breaks the polygon into multiple polygons, iterate through the MultiPolygon
            for p in pgon_buffered.geoms:
                pgon_buffered_data = np.array(p.exterior.coords)
                buffered_3d = np.insert(
                    pgon_buffered_data,
                    obj=2,
                    values=reshaped_contour_data[0][-1],
                    axis=1,
                )
                translated_contour_data = apply_transformation_to_3d_points(
                    buffered_3d, transformation_matrix
                )
                polygon = [np.around([translated_contour_data[:, :2]]).astype(np.int32)]
                polygon = np.array(polygon).squeeze()
                polygons.append(polygon)

    slice_mask = create_empty_slice_mask(series_slice).astype(np.uint8)
    cv.fillPoly(img=slice_mask, pts=polygons, color=1)

    # When the RTStruct contours land in the center of the pixels,
    # as with aTMTV created RTStructs, cv.fillPoly fills pixels that
    # are only partially within the bounds of the contour. The below
    # checks the filled pixel array and checks what percentage of
    # the pixel is determined to be within the contour.
    # As a final check, the recalculated mask is only applied if the
    # area of the new array is closer to the area of the contour
    # compared to the original array.
    if percent_check == "on":
        mp = MultiPolygon([Polygon(p) for p in polygons])
        if mp.area:
            recalculated_mask = recalculate_pixels(slice_mask, mp, 0.50)
            area_comparison = np.count_nonzero(slice_mask) / mp.area
            new_area_comp = np.count_nonzero(recalculated_mask) / mp.area
            if abs(new_area_comp - 1) < abs(area_comparison - 1):
                slice_mask = recalculated_mask

    return slice_mask


def recalculate_pixels(slice_mask, mp, threshold) -> np.ndarray:
    """Iterates through filled pixels to determine % of pixel inside contour."""
    recalculated_mask = np.copy(slice_mask)
    y, x = np.nonzero(recalculated_mask)
    for n in range(len(x)):
        xn, yn = x[n], y[n]
        pixel_point = Point(xn, yn)
        distance = pixel_point.distance(mp.boundary)
        if distance < 0.5:
            pixel = Polygon(
                (
                    (xn - 0.5, yn - 0.5),
                    (xn + 0.5, yn - 0.5),
                    (xn + 0.5, yn + 0.5),
                    (xn - 0.5, yn + 0.5),
                )
            )
            try:
                ratio = pixel.intersection(mp).area
                if ratio < threshold:
                    recalculated_mask[yn][xn] = 0
            except GEOSException:
                # Shapely doesn't like it when the geometry gets too weird...
                log.debug("Mask recalculation failed.")
    return recalculated_mask


def create_series_mask_from_contour_sequence(
    series_data, contour_sequence: Sequence, percent_check, valid
):
    # NOTE: Added `percent_check` to pass through config
    # Added `valid` to toggle whether to use the original function (Which uses SOPInstanceUIDs)
    # or an ImagePositionPatient-based function to determine where to draw contours
    mask = create_empty_series_mask(series_data)
    transformation_matrix = get_patient_to_pixel_transformation_matrix(series_data)

    # Iterate through each slice of the series, If it is a part of the contour, add the contour mask
    for i, series_slice in enumerate(series_data):
        if valid:
            slice_contour_data = get_slice_contour_data(series_slice, contour_sequence)
        else:
            slice_contour_data = get_slice_contour_data_ipp(
                series_slice, contour_sequence
            )
        if len(slice_contour_data):
            mask[:, :, i] = get_slice_mask_from_slice_contour_data(
                series_slice,
                slice_contour_data,
                transformation_matrix,
                percent_check,
            )
    return mask


def create_empty_series_mask(series_data):
    # rtutils utilizes (Columns, Rows, len), we need (Rows, Columns, len)
    ref_dicom_image = series_data[0]
    mask_dims = (
        int(ref_dicom_image.Rows),
        int(ref_dicom_image.Columns),
        len(series_data),
    )
    mask = np.zeros(mask_dims).astype(bool)
    return mask


def create_empty_slice_mask(series_slice):
    # rtutils utilizes (Columns, Rows, len), we need (Rows, Columns, len)
    mask_dims = (int(series_slice.Rows), int(series_slice.Columns))
    mask = np.zeros(mask_dims).astype(bool)
    return mask


def get_slice_contour_data_ipp(
    series_slice: Dataset, contour_sequence: Sequence
) -> np.ndarray:
    slice_contour_data = []
    for contour in contour_sequence:
        # In ContourData, points are given in a 1d array with pattern
        # x, y, z, x, y, z...z; we want z to check against the z series_slice ipp
        # Valid contours *should* only have one unique z value, but we do want
        # to make sure we're identifying any weirdness and failing as needed.
        z_vals = set()
        contour_data = contour.ContourData
        for idx in range(2, len(contour_data), 3):
            z_vals.add(contour_data[idx])
        if len(z_vals) == 1:
            contour_position = z_vals.pop()
        else:
            raise ValueError(
                "ImagePositionPatient has multiple z values for a single contour"
            )
        slice_position = series_slice.ImagePositionPatient[2]
        if contour_position == slice_position:
            slice_contour_data.append(contour.ContourData)

    return slice_contour_data
