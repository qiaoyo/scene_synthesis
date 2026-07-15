"""Pure coordinate helpers for canonical asset bounding boxes."""
from __future__ import annotations

from itertools import product
import math
from typing import Sequence, Tuple


Point3 = Tuple[float, float, float]
BBox = Tuple[Point3, Point3]


def normalize_bbox_to_z_up_meters(
    bbox: Sequence[Sequence[float]],
    source_up_axis: object,
    meters_per_unit: float,
) -> BBox:
    """Return an aligned bbox expressed in a Z-up, meter-based frame.

    ``bbox`` is expected to be an axis-aligned range in the source stage's
    world coordinate system.  Axis conversion can change which source corner
    becomes a target minimum, so all eight corners are transformed before the
    target aligned range is recomputed.
    """
    bbox_min, bbox_max = _validated_bbox(bbox)
    axis = str(source_up_axis).strip().upper()
    if axis not in {"X", "Y", "Z"}:
        raise ValueError(f"unsupported source up axis: {source_up_axis!r}")

    scale = float(meters_per_unit)
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError(
            "meters_per_unit must be finite and positive: "
            f"{meters_per_unit!r}"
        )

    target_corners = [
        _to_z_up((float(x), float(y), float(z)), axis)
        for x, y, z in product(
            (bbox_min[0], bbox_max[0]),
            (bbox_min[1], bbox_max[1]),
            (bbox_min[2], bbox_max[2]),
        )
    ]
    scaled_corners = [
        tuple(component * scale for component in point)
        for point in target_corners
    ]
    target_min: Point3 = (
        min(point[0] for point in scaled_corners),
        min(point[1] for point in scaled_corners),
        min(point[2] for point in scaled_corners),
    )
    target_max: Point3 = (
        max(point[0] for point in scaled_corners),
        max(point[1] for point in scaled_corners),
        max(point[2] for point in scaled_corners),
    )
    return target_min, target_max


def _validated_bbox(bbox: Sequence[Sequence[float]]) -> BBox:
    if len(bbox) != 2:
        raise ValueError("bbox must contain exactly (min, max)")

    points: list[Point3] = []
    for label, point in zip(("min", "max"), bbox):
        if len(point) != 3:
            raise ValueError(f"bbox {label} point must contain exactly 3 values")
        values = tuple(float(value) for value in point)
        if not all(math.isfinite(value) for value in values):
            raise ValueError(f"bbox {label} point must contain only finite values")
        points.append((values[0], values[1], values[2]))

    bbox_min, bbox_max = points
    for axis_idx, (minimum, maximum) in enumerate(zip(bbox_min, bbox_max)):
        if minimum > maximum:
            raise ValueError(
                f"bbox min exceeds max on axis {axis_idx}: {minimum} > {maximum}"
            )
    return bbox_min, bbox_max


def _to_z_up(point: Point3, source_up_axis: str) -> Point3:
    x, y, z = point
    if source_up_axis == "Z":
        return x, y, z
    if source_up_axis == "Y":
        # +90 degrees around X: source Y becomes target Z.
        return x, -z, y
    # -90 degrees around Y: source X becomes target Z.
    return -z, y, x


__all__ = ["BBox", "Point3", "normalize_bbox_to_z_up_meters"]
