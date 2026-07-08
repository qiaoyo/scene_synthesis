"""
Container-inner support checks for open Box assets.

This module is intentionally standalone so worker.py and enhanced_worker.py can
import it when launched directly by the Isaac Python process.
"""
from __future__ import annotations

from typing import Any, Dict, List


SUPPORT_TYPE_SURFACE = "surface"
SUPPORT_TYPE_CONTAINER_INNER = "container_inner"
VALID_SUPPORT_TYPES = {
    SUPPORT_TYPE_SURFACE,
    SUPPORT_TYPE_CONTAINER_INNER,
}

BBox = Dict[str, List[float]]


def normalize_support_type(value: Any) -> str:
    text = str(value or SUPPORT_TYPE_SURFACE).strip().lower()
    if text in VALID_SUPPORT_TYPES:
        return text
    return SUPPORT_TYPE_SURFACE


def support_type_for_child(
    scene: Dict[str, Any],
    child_id: str,
    default: str = SUPPORT_TYPE_SURFACE,
) -> str:
    relation_types = scene.get("support_relation_types", {}) or {}
    if not isinstance(relation_types, dict):
        return normalize_support_type(default)
    return normalize_support_type(relation_types.get(child_id, default))


def run_container_inner_support_check(
    *,
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    child_id: str,
    parent_id: str,
    include_suggestions: bool = False,
    z_tolerance: float = 0.08,
    xy_margin_ratio: float = 0.03,
    min_xy_margin: float = 0.015,
) -> Dict[str, Any]:
    child_bbox = bboxes.get(child_id)
    parent_bbox = bboxes.get(parent_id)
    issues: List[str] = []
    warnings: List[str] = []

    if child_bbox is None:
        issues.append(f"missing child bbox: {child_id}")
    if parent_bbox is None:
        issues.append(f"missing parent bbox: {parent_id}")
    if issues:
        return _result(
            child_id=child_id,
            parent_id=parent_id,
            supported=False,
            issues=issues,
            warnings=warnings,
            include_suggestions=include_suggestions,
        )

    parent_inst = _instances(scene).get(parent_id, {}) or {}
    child_inst = _instances(scene).get(child_id, {}) or {}
    if not _is_open_box_container(parent_inst):
        issues.append(
            "container_inner support requires an open Box parent "
            "(tags.Colsure/Closure=Open or open/bin/container description)"
        )

    child_size = _bbox_size(child_bbox)
    parent_size = _bbox_size(parent_bbox)
    margin = max(
        float(min_xy_margin),
        min(parent_size[0], parent_size[1]) * float(xy_margin_ratio),
    )
    inner_min = [
        parent_bbox["min"][0] + margin,
        parent_bbox["min"][1] + margin,
    ]
    inner_max = [
        parent_bbox["max"][0] - margin,
        parent_bbox["max"][1] - margin,
    ]

    if inner_min[0] >= inner_max[0] or inner_min[1] >= inner_max[1]:
        issues.append("parent bbox is too small for container_inner margin")
        inner_min = [parent_bbox["min"][0], parent_bbox["min"][1]]
        inner_max = [parent_bbox["max"][0], parent_bbox["max"][1]]

    fits_xy = (
        child_bbox["min"][0] >= inner_min[0]
        and child_bbox["max"][0] <= inner_max[0]
        and child_bbox["min"][1] >= inner_min[1]
        and child_bbox["max"][1] <= inner_max[1]
    )
    if not fits_xy:
        issues.append(
            "child footprint is not fully inside parent XY bounds with safety margin "
            f"{margin:.3f}"
        )

    bottom_gap = float(child_bbox["min"][2]) - float(parent_bbox["min"][2])
    lower_z_tolerance = max(0.01, float(z_tolerance) * 0.25)
    if bottom_gap < -lower_z_tolerance or bottom_gap > float(z_tolerance):
        issues.append(
            f"inner_bottom_gap={bottom_gap:.3f} outside tolerance "
            f"[-{lower_z_tolerance:.3f}, {float(z_tolerance):.3f}]"
        )

    top_clearance = float(parent_bbox["max"][2]) - float(child_bbox["max"][2])
    if top_clearance < -float(z_tolerance):
        issues.append(
            f"child top is above parent rim by {-top_clearance:.3f}"
        )

    if child_size[0] > max(0.0, inner_max[0] - inner_min[0]):
        warnings.append("child width is larger than estimated container inner width")
    if child_size[1] > max(0.0, inner_max[1] - inner_min[1]):
        warnings.append("child depth is larger than estimated container inner depth")
    if child_size[2] > parent_size[2] + float(z_tolerance):
        warnings.append("child height is larger than parent container height")

    supported = not issues
    payload = _result(
        child_id=child_id,
        parent_id=parent_id,
        supported=supported,
        issues=issues,
        warnings=warnings,
        include_suggestions=include_suggestions,
        bottom_gap=bottom_gap,
        top_clearance=top_clearance,
        xy_coverage=_xy_coverage_against_bounds(child_bbox, inner_min, inner_max),
        contacts=(
            [{
                "child": child_id,
                "parent": parent_id,
                "type": "container_inner_support",
                "support_z": float(parent_bbox["min"][2]),
            }]
            if supported
            else []
        ),
    )

    if include_suggestions:
        payload["suggested_move"] = (
            None
            if supported
            else _suggest_container_inner_move(
                child_id=child_id,
                parent_id=parent_id,
                child_bbox=child_bbox,
                parent_bbox=parent_bbox,
                child_inst=child_inst,
                inner_min=inner_min,
                inner_max=inner_max,
                z_tolerance=float(z_tolerance),
                parent_is_open_box=_is_open_box_container(parent_inst),
            )
        )
    return payload


def _result(
    *,
    child_id: str,
    parent_id: str,
    supported: bool,
    issues: List[str],
    warnings: List[str],
    include_suggestions: bool,
    bottom_gap: float | None = None,
    top_clearance: float | None = None,
    xy_coverage: float | None = None,
    contacts: List[Dict[str, Any]] | None = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "supported": supported,
        "child": child_id,
        "parent": parent_id,
        "support_type": SUPPORT_TYPE_CONTAINER_INNER,
        "support_backend": "container_inner_bbox",
        "contacts": contacts or [],
        "issues": issues,
    }
    if warnings:
        payload["warnings"] = warnings
    if bottom_gap is not None:
        payload["inner_bottom_gap"] = bottom_gap
        payload["z_gap"] = bottom_gap
    if top_clearance is not None:
        payload["top_clearance"] = top_clearance
    if xy_coverage is not None:
        payload["xy_coverage"] = round(xy_coverage, 3)
    if include_suggestions and "suggested_move" not in payload:
        payload["suggested_move"] = None
    return payload


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


def _instance_tags(instance: Dict[str, Any]) -> Dict[str, Any]:
    tags = instance.get("tags", {}) or {}
    if isinstance(tags, dict):
        return tags
    return {}


def _is_open_box_container(instance: Dict[str, Any]) -> bool:
    asset_type = str(instance.get("asset_type", "")).strip().lower()
    if asset_type != "box":
        return False

    tags = _instance_tags(instance)
    lower_tags = {
        str(key).strip().lower(): str(value).strip().lower()
        for key, value in tags.items()
    }
    closure = lower_tags.get("colsure")
    if closure is None:
        closure = lower_tags.get("closure")
    if closure is not None:
        return closure == "open"

    text_parts = [
        instance.get("asset_doc_id", ""),
        instance.get("usd_path", ""),
        instance.get("description", ""),
    ]
    text_parts.extend(str(key) for key in tags.keys())
    text_parts.extend(str(value) for value in tags.values())
    text = " ".join(str(part).lower() for part in text_parts if part)
    return any(
        keyword in text
        for keyword in (
            "open box",
            "open-top",
            "open top",
            "container",
            "storage bin",
            "plastic bin",
            "bin",
        )
    )


def _bbox_center(bbox: BBox) -> List[float]:
    return [
        (bbox["min"][axis] + bbox["max"][axis]) / 2.0
        for axis in range(3)
    ]


def _bbox_size(bbox: BBox) -> List[float]:
    return [
        bbox["max"][axis] - bbox["min"][axis]
        for axis in range(3)
    ]


def _xy_coverage_against_bounds(
    child_bbox: BBox,
    inner_min: List[float],
    inner_max: List[float],
) -> float:
    child_area = max(
        1e-9,
        (child_bbox["max"][0] - child_bbox["min"][0])
        * (child_bbox["max"][1] - child_bbox["min"][1]),
    )
    dx = max(
        0.0,
        min(child_bbox["max"][0], inner_max[0])
        - max(child_bbox["min"][0], inner_min[0]),
    )
    dy = max(
        0.0,
        min(child_bbox["max"][1], inner_max[1])
        - max(child_bbox["min"][1], inner_min[1]),
    )
    return min(1.0, (dx * dy) / child_area)


def _suggest_container_inner_move(
    *,
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    parent_bbox: BBox,
    child_inst: Dict[str, Any],
    inner_min: List[float],
    inner_max: List[float],
    z_tolerance: float,
    parent_is_open_box: bool,
) -> Dict[str, Any]:
    old_position = [
        float(value)
        for value in child_inst.get("position", [0.0, 0.0, 0.0])
    ]
    child_center = _bbox_center(child_bbox)
    child_size = _bbox_size(child_bbox)
    target_center = [
        (inner_min[0] + inner_max[0]) / 2.0,
        (inner_min[1] + inner_max[1]) / 2.0,
    ]
    target_bottom_z = parent_bbox["min"][2] + min(max(z_tolerance * 0.25, 0.005), 0.02)
    move_vector = [
        target_center[0] - child_center[0],
        target_center[1] - child_center[1],
        target_bottom_z - child_bbox["min"][2],
    ]
    new_position = [
        old_position[axis] + move_vector[axis]
        for axis in range(3)
    ]

    unresolved_issues: List[str] = []
    if not parent_is_open_box:
        unresolved_issues.append("parent is not recognized as an open Box container")
    if child_size[0] > max(0.0, inner_max[0] - inner_min[0]):
        unresolved_issues.append("child is too wide for estimated container interior")
    if child_size[1] > max(0.0, inner_max[1] - inner_min[1]):
        unresolved_issues.append("child is too deep for estimated container interior")
    if child_size[2] > (parent_bbox["max"][2] - parent_bbox["min"][2]) + z_tolerance:
        unresolved_issues.append("child is too tall for the container rim")

    return {
        "instance_id": child_id,
        "parent_id": parent_id,
        "move_vector": move_vector,
        "new_position": new_position,
        "expected_supported": not unresolved_issues,
        "suggestion_status": (
            "resolved_by_move"
            if not unresolved_issues
            else "unresolved_by_move"
        ),
        "unresolved_issues": unresolved_issues,
        "recommended_action": (
            None
            if not unresolved_issues
            else "choose a smaller child, use an open Box parent, or keep ordinary surface support"
        ),
    }


__all__ = [
    "SUPPORT_TYPE_CONTAINER_INNER",
    "SUPPORT_TYPE_SURFACE",
    "VALID_SUPPORT_TYPES",
    "normalize_support_type",
    "run_container_inner_support_check",
    "support_type_for_child",
]
