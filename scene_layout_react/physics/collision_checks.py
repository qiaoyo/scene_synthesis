"""
Collision validation helpers for the Isaac Sim worker.

This module is intentionally standalone so worker.py can import it when run as
a script by the Isaac Python process.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, Iterable, List, Tuple


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


def _collision_pairs(
    scene: Dict[str, Any],
    bboxes: Dict[str, Dict[str, List[float]]],
    pair: List[str] | None = None,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any] | None]:
    ids = [
        instance_id
        for instance_id in _instances(scene).keys()
        if instance_id in bboxes
    ]
    if pair:
        ids = [item for item in pair if item in bboxes]

    collisions = _collision_details(ids, bboxes)
    suggested_move = _suggest_collision_moves(scene, bboxes, ids, collisions)

    return collisions, suggested_move

def _collision_details(
    ids: List[str],
    bboxes: Dict[str, Dict[str, List[float]]],
    *,
    penetration_tolerance: float = 1e-5,
) -> List[Dict[str, Any]]:
    axis_names = ["x", "y", "z"]
    collisions: List[Dict[str, Any]] = []

    for idx, a_id in enumerate(ids):
        if a_id not in bboxes:
            continue
        for b_id in ids[idx + 1:]:
            if b_id not in bboxes:
                continue

            a_bbox = bboxes[a_id]
            b_bbox = bboxes[b_id]
            overlaps = _bbox_overlap_depth(a_bbox, b_bbox)

            if not _is_penetrating(
                overlaps,
                penetration_tolerance,
            ):
                continue

            axis = _collision_axis(overlaps, penetration_tolerance)
            collisions.append({
                "a": a_id,
                "b": b_id,
                "method": "isaac_world_bbox",
                "axis": axis_names[axis],
                "axis_idx": axis,
                "overlap": overlaps[axis],
                "overlap_depth": overlaps,
            })

    return collisions


def _is_penetrating(
    overlaps: List[float],
    penetration_tolerance: float,
) -> bool:
    """
    True:
        三个轴均存在超过阈值的重叠

    False:
        任意轴未重叠或仅接触
    """
    return all(
        overlap > penetration_tolerance
        for overlap in overlaps
    )


def _bbox_overlap_depth(
    a_bbox: Dict[str, List[float]],
    b_bbox: Dict[str, List[float]],
) -> List[float]:
    return [
        max(
            0.0,
            min(a_bbox["max"][i], b_bbox["max"][i])
            - max(a_bbox["min"][i], b_bbox["min"][i]),
        )
        for i in range(3)
    ]


def _collision_axis(
    overlaps: List[float],
    penetration_tolerance: float,
) -> int:
    candidates = [
        axis
        for axis, overlap in enumerate(overlaps)
        if overlap > penetration_tolerance
    ]
    return min(candidates, key=lambda axis: overlaps[axis])


def _suggest_collision_moves(
    scene: Dict[str, Any],
    bboxes: Dict[str, Dict[str, List[float]]],
    ids: List[str],
    collisions: List[Dict[str, Any]],
    *,
    margin: float = 0.05,
    max_iterations: int = 12,
    penetration_tolerance: float = 1e-5,
    damping: float = 0.5,
    min_offset_epsilon: float = 1e-4,
) -> Dict[str, Any] | None:
    if not collisions:
        return None

    axis_names = ["x", "y", "z"]
    instances = _instances(scene)
    original_bboxes = {
        instance_id: _copy_bbox(bboxes[instance_id])
        for instance_id in ids
        if instance_id in bboxes
    }

    offsets = {
        instance_id: [0.0, 0.0, 0.0]
        for instance_id in original_bboxes
    }
    
    iterations = 0
    for iteration in range(max_iterations):
        working_bboxes = {
            instance_id: _bbox_with_offset(
                original_bboxes[instance_id],
                offsets[instance_id],
            )
            for instance_id in original_bboxes
        }

        active_collisions = _collision_details(
            ids,
            working_bboxes,
            penetration_tolerance=penetration_tolerance,
        )

        if not active_collisions:
            break

        iterations = iteration + 1
        pending_offsets = defaultdict(
            lambda: [0.0, 0.0, 0.0]
        )

        for collision in active_collisions:
            a_id = collision["a"]
            b_id = collision["b"]

            axis = collision["axis_idx"]
            overlap = collision["overlap"]
            separation = (overlap + margin) * damping

            if separation <= penetration_tolerance:
                continue

            a_bbox = working_bboxes[a_id]
            b_bbox = working_bboxes[b_id]
            a_center = _bbox_center(a_bbox)
            b_center = _bbox_center(b_bbox)

            direction = 1.0 if b_center[axis] >= a_center[axis] else -1.0
            a_weight, b_weight = _collision_move_weights(a_id, b_id, scene)
            total_weight = a_weight + b_weight

            if total_weight <= 0.0:
                a_weight = 1.0
                b_weight = 1.0
                total_weight = 2.0

            a_delta = -direction * separation * (a_weight / total_weight)
            b_delta = direction * separation * (b_weight / total_weight)

            pending_offsets[a_id][axis] += a_delta
            pending_offsets[b_id][axis] += b_delta

        total_pending_offset = sum(
            abs(value)
            for move_vector in pending_offsets.values()
            for value in move_vector
        )

        if total_pending_offset < min_offset_epsilon:
            break

        for instance_id, move_vector in pending_offsets.items():
            offsets[instance_id][0] += move_vector[0]
            offsets[instance_id][1] += move_vector[1]
            offsets[instance_id][2] += move_vector[2]

    working_bboxes = {
        instance_id: _bbox_with_offset(
            original_bboxes[instance_id],
            offsets[instance_id],
        )
        for instance_id in original_bboxes
    }

    unresolved = _collision_details(
        ids,
        working_bboxes,
        penetration_tolerance=penetration_tolerance,
    )

    moves: List[Dict[str, Any]] = []
    final_positions: Dict[str, Dict[str, Any]] = {}

    for instance_id in ids:
        if instance_id not in working_bboxes:
            continue

        old_position = [
            float(value)
            for value in instances.get(instance_id, {}).get(
                "position",
                _bbox_center(bboxes[instance_id]),
            )
        ]
        move_vector = offsets[instance_id]
        new_position = [
            old_position[axis] + move_vector[axis]
            for axis in range(3)
        ]
        final_positions[instance_id] = {
            "instance_id": instance_id,
            "final_position": new_position,
        }

        if not any(abs(value) > penetration_tolerance for value in move_vector):
            continue

        moves.append({
            "instance_id": instance_id,
            "old_position": old_position,
            "move_vector": move_vector,
            "final_position": new_position,
        })

    return {
        "moves": moves,
        "final_positions": final_positions,
        "unresolved_collisions": unresolved,
        "resolved_collision_free": not unresolved,
        "iterations": iterations,
    }

def _copy_bbox(bbox: Dict[str, List[float]]) -> Dict[str, List[float]]:
    return {
        "min": [float(value) for value in bbox["min"]],
        "max": [float(value) for value in bbox["max"]],
    }

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
        (bbox["min"][i] + bbox["max"][i]) / 2.0
        for i in range(3)
    ]


def _collision_move_weights(
    a_id: str,
    b_id: str,
    scene: Dict[str, Any],
    available_ids: Iterable[str] | None = None,
) -> Tuple[float, float]:
    support_children = _normalized_support_children(scene)

    a_children = support_children.get(a_id, [])
    b_children = support_children.get(b_id, [])

    # Direct support collision: keep the support parent stable and move the child.
    if b_id in a_children:
        return 0.0, 1.0
    if a_id in b_children:
        return 1.0, 0.0

    def weight(instance_id: str) -> float:
        descendant_count = len(
            _support_descendants(
                scene,
                instance_id,
                available_ids=available_ids,
            )
        )
        return 1.0 / (1.0 + float(descendant_count))

    return weight(a_id), weight(b_id)


def _normalized_support_children(scene: Dict[str, Any]) -> Dict[str, List[str]]:
    raw = scene.get("support_children", {}) or {}
    if not isinstance(raw, dict):
        return {}

    normalized: Dict[str, List[str]] = {}
    for parent_id, children in raw.items():
        if not isinstance(parent_id, str):
            continue
        if not isinstance(children, list):
            continue

        valid_children = [
            child_id
            for child_id in children
            if isinstance(child_id, str) and child_id != parent_id
        ]
        if valid_children:
            normalized[parent_id] = valid_children

    return normalized


def _support_descendants(
    scene: Dict[str, Any],
    instance_id: str,
    available_ids: Iterable[str] | None = None,
) -> List[str]:
    support_children = _normalized_support_children(scene)

    if available_ids is None:
        available = set(_instances(scene).keys())
    else:
        available = set(available_ids)

    descendants: List[str] = []
    seen = {instance_id}
    stack = list(support_children.get(instance_id, []))

    while stack:
        child_id = stack.pop()
        if child_id in seen:
            continue

        seen.add(child_id)

        if child_id in available:
            descendants.append(child_id)
        stack.extend(support_children.get(child_id, []))
    return descendants


__all__ = ["_collision_pairs"]
