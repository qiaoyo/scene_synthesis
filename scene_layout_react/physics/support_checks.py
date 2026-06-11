"""
Support validation helpers for the Isaac Sim worker.

This module is intentionally standalone so worker.py can import it when run as
a script by the Isaac Python process.
"""
from __future__ import annotations

from typing import Any, Dict, List


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


def _check_support(
    child_id: str,
    parent_id: str,
    bboxes: Dict[str, Dict[str, List[float]]],
    scene: Dict[str, Any],
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
    include_suggestions: bool = False,
) -> Dict[str, Any]:
    child = bboxes[child_id]
    parent = bboxes[parent_id]
    p_min = parent["min"]
    p_max = parent["max"]

    z_gap = p_max[2] - child["min"][2]
    coverage = _xy_coverage(child, parent)
    issues: List[str] = []

    if abs(z_gap) > z_tolerance:
        issues.append(f"z_gap={z_gap:.3f} outside tolerance {z_tolerance:.3f}")
    if coverage < overlap_threshold:
        issues.append(f"xy_coverage={coverage:.3f} below threshold {overlap_threshold:.3f}")

    supported = not issues

    suggested_move = None

    if issues and include_suggestions:
        suggested_move = _suggest_support_move(
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child,
            parent_bbox=parent,
            scene=scene,
            z_tolerance=z_tolerance,
            overlap_threshold=overlap_threshold,
        )

    result = {
        "supported": supported,
        "child": child_id,
        "parent": parent_id,
        "z_gap": z_gap,
        "xy_coverage": round(coverage, 3),
        "contacts": (
            [{"child": child_id, "parent": parent_id, "type": "support"}]
            if supported
            else []
        ),
        "issues": issues,
    }
    if include_suggestions:
        result["suggested_move"] = suggested_move
    return result


def xy_overlap_area(
    a_min: List[float],
    a_max: List[float],
    b_min: List[float],
    b_max: List[float],
) -> float:
    dx = max(0.0, min(a_max[0], b_max[0]) - max(a_min[0], b_min[0]))
    dy = max(0.0, min(a_max[1], b_max[1]) - max(a_min[1], b_min[1]))
    return dx * dy


def _suggest_support_move(
    child_id: str,
    parent_id: str,
    child_bbox: Dict[str, List[float]],
    parent_bbox: Dict[str, List[float]],
    scene: Dict[str, Any],
    *,
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
) -> Dict[str, Any]:
    instances = _instances(scene)
    child_inst = instances.get(child_id, {})

    old_position = [
        float(value)
        for value in child_inst.get("position", [0.0, 0.0, 0.0])
    ]

    child_center = _bbox_center(child_bbox)
    parent_center = _bbox_center(parent_bbox)
    child_size = _bbox_size(child_bbox)
    parent_size = _bbox_size(parent_bbox)

    c_min = child_bbox["min"]
    p_min = parent_bbox["min"]
    p_max = parent_bbox["max"]

    z_gap = p_max[2] - c_min[2]
    xy_coverage = _xy_coverage(child_bbox, parent_bbox)
    move_vector = [0.0, 0.0, 0.0]

    if abs(z_gap) > z_tolerance:
        move_vector[2] = z_gap

    if xy_coverage < overlap_threshold:
        for axis in (0, 1):
            child_half = child_size[axis] / 2.0

            if parent_size[axis] >= child_size[axis]:
                target_center = _clamp(
                    child_center[axis],
                    p_min[axis] + child_half,
                    p_max[axis] - child_half,
                )
            else:
                target_center = parent_center[axis]

            move_vector[axis] = target_center - child_center[axis]

    new_position = [
        old_position[axis] + move_vector[axis]
        for axis in range(3)
    ]
    expected_child_bbox = _bbox_with_offset(child_bbox, move_vector)
    expected_z_gap = p_max[2] - expected_child_bbox["min"][2]
    expected_xy_coverage = _xy_coverage(expected_child_bbox, parent_bbox)
    unresolved_issues: List[str] = []
    recommended_action = None

    if abs(expected_z_gap) > z_tolerance:
        unresolved_issues.append(
            f"expected_z_gap={expected_z_gap:.3f} outside tolerance {z_tolerance:.3f}"
        )
    if expected_xy_coverage < overlap_threshold:
        unresolved_issues.append(
            "expected_xy_coverage="
            f"{expected_xy_coverage:.3f} below threshold {overlap_threshold:.3f}"
        )
        recommended_action = (
            "parent support footprint is too small for the child overlap "
            "threshold; choose a larger support parent or reduce the required "
            "coverage threshold"
        )

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
        "recommended_action": recommended_action,
    }


def _xy_coverage(
    child_bbox: Dict[str, List[float]],
    parent_bbox: Dict[str, List[float]],
) -> float:
    c_min = child_bbox["min"]
    c_max = child_bbox["max"]
    p_min = parent_bbox["min"]
    p_max = parent_bbox["max"]
    child_area = max(1e-9, (c_max[0] - c_min[0]) * (c_max[1] - c_min[1]))
    return xy_overlap_area(c_min, c_max, p_min, p_max) / child_area


def _bbox_with_offset(
    bbox: Dict[str, List[float]],
    offset: List[float],
) -> Dict[str, List[float]]:
    return {
        "min": [
            bbox["min"][axis] + offset[axis]
            for axis in range(3)
        ],
        "max": [
            bbox["max"][axis] + offset[axis]
            for axis in range(3)
        ],
    }


def _bbox_center(bbox: Dict[str, List[float]]) -> List[float]:
    return [
        (bbox["min"][axis] + bbox["max"][axis]) / 2.0
        for axis in range(3)
    ]


def _bbox_size(bbox: Dict[str, List[float]]) -> List[float]:
    return [
        bbox["max"][axis] - bbox["min"][axis]
        for axis in range(3)
    ]


def _clamp(value: float, lower: float, upper: float) -> float:
    if lower > upper:
        return (lower + upper) / 2.0
    return max(lower, min(value, upper))


__all__ = ["_check_support", "xy_overlap_area"]
