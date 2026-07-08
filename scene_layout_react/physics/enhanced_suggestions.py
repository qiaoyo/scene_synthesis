"""
Enhanced movement suggestions for the optional Isaac Sim worker.

These helpers are intentionally standalone so they can be imported when the
enhanced worker is launched as a script by the Isaac Python process.
"""
from __future__ import annotations

import math
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple


BBox = Dict[str, List[float]]
Vec3 = List[float]
ValidationFn = Callable[[Dict[str, Any]], Dict[str, Any]]


_HOLLOW_SUPPORT_KEYWORDS = {
    "bookcase",
    "cabinet",
    "drawer",
    "pallet rack",
    "pallet_rack",
    "rack",
    "shelf",
    "shelving",
    "storage",
}

_MOVABLE_KEYWORDS = {
    "bin",
    "box",
    "cardbox",
    "carton",
    "crate",
    "package",
    "part",
    "tray",
}


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    return raw if isinstance(raw, dict) else {}


def _instance_tags(instance: Dict[str, Any]) -> Dict[str, Any]:
    tags = instance.get("tags", {}) or {}
    return tags if isinstance(tags, dict) else {}


def _instance_text(instance: Dict[str, Any]) -> str:
    tags = _instance_tags(instance)
    parts: List[str] = [
        str(instance.get("asset_type", "")),
        str(instance.get("asset_doc_id", "")),
        str(instance.get("usd_path", "")),
        str(instance.get("description", "")),
    ]
    parts.extend(str(key) for key in tags.keys())
    parts.extend(str(value) for value in tags.values())
    return " ".join(part.lower() for part in parts if part)


def _is_hollow_support(instance: Dict[str, Any]) -> bool:
    text = _instance_text(instance)
    return any(keyword in text for keyword in _HOLLOW_SUPPORT_KEYWORDS)


def _looks_movable(instance: Dict[str, Any]) -> bool:
    text = _instance_text(instance)
    return any(keyword in text for keyword in _MOVABLE_KEYWORDS)


def _support_children(scene: Dict[str, Any]) -> Dict[str, List[str]]:
    raw = scene.get("support_children", {}) or {}
    if not isinstance(raw, dict):
        return {}
    normalized: Dict[str, List[str]] = {}
    for parent_id, children in raw.items():
        if isinstance(children, list):
            normalized[str(parent_id)] = [str(child) for child in children]
    return normalized


def _support_relation(
    scene: Dict[str, Any],
    a_id: str,
    b_id: str,
) -> Tuple[Optional[str], Optional[str]]:
    support_children = _support_children(scene)
    if b_id in support_children.get(a_id, []):
        return b_id, a_id
    if a_id in support_children.get(b_id, []):
        return a_id, b_id

    instances = _instances(scene)
    if (instances.get(a_id) or {}).get("parent_instance_id") == b_id:
        return a_id, b_id
    if (instances.get(b_id) or {}).get("parent_instance_id") == a_id:
        return b_id, a_id
    return None, None


def _bbox_center(bbox: BBox) -> Vec3:
    return [
        (float(bbox["min"][axis]) + float(bbox["max"][axis])) / 2.0
        for axis in range(3)
    ]


def _bbox_size(bbox: BBox) -> Vec3:
    return [
        float(bbox["max"][axis]) - float(bbox["min"][axis])
        for axis in range(3)
    ]


def _bbox_with_offset(bbox: BBox, offset: Vec3) -> BBox:
    return {
        "min": [
            float(bbox["min"][axis]) + float(offset[axis])
            for axis in range(3)
        ],
        "max": [
            float(bbox["max"][axis]) + float(offset[axis])
            for axis in range(3)
        ],
    }


def _bbox_overlap_depth(a_bbox: BBox, b_bbox: BBox) -> Vec3:
    return [
        max(
            0.0,
            min(float(a_bbox["max"][axis]), float(b_bbox["max"][axis]))
            - max(float(a_bbox["min"][axis]), float(b_bbox["min"][axis])),
        )
        for axis in range(3)
    ]


def _bbox_penetrating(a_bbox: BBox, b_bbox: BBox, *, tolerance: float = 1e-5) -> bool:
    return all(value > tolerance for value in _bbox_overlap_depth(a_bbox, b_bbox))


def _xy_overlap_area(a_bbox: BBox, b_bbox: BBox) -> float:
    dx = max(
        0.0,
        min(float(a_bbox["max"][0]), float(b_bbox["max"][0]))
        - max(float(a_bbox["min"][0]), float(b_bbox["min"][0])),
    )
    dy = max(
        0.0,
        min(float(a_bbox["max"][1]), float(b_bbox["max"][1]))
        - max(float(a_bbox["min"][1]), float(b_bbox["min"][1])),
    )
    return dx * dy


def _xy_coverage(child_bbox: BBox, surface_bbox: BBox) -> float:
    child_size = _bbox_size(child_bbox)
    child_area = max(1e-9, child_size[0] * child_size[1])
    return min(1.0, _xy_overlap_area(child_bbox, surface_bbox) / child_area)


def _clamp(value: float, lower: float, upper: float) -> float:
    if lower > upper:
        return (lower + upper) / 2.0
    return max(lower, min(value, upper))


def _length(vector: Iterable[float]) -> float:
    return math.sqrt(sum(float(value) * float(value) for value in vector))


def _unit_vector(vector: Iterable[float]) -> Optional[Vec3]:
    values = [float(value) for value in vector]
    length = _length(values)
    if length <= 1e-9:
        return None
    return [value / length for value in values]


def _instance_position(scene: Dict[str, Any], instance_id: str, fallback: Vec3) -> Vec3:
    instance = _instances(scene).get(instance_id, {}) or {}
    position = instance.get("position", fallback)
    try:
        return [float(position[axis]) for axis in range(3)]
    except Exception:
        return [float(fallback[axis]) for axis in range(3)]


def _movability_score(scene: Dict[str, Any], instance_id: str) -> float:
    instances = _instances(scene)
    instance = instances.get(instance_id, {}) or {}
    score = 1.0
    if _looks_movable(instance):
        score += 4.0
    if _is_hollow_support(instance):
        score -= 6.0
    descendants = len(_support_children(scene).get(instance_id, []))
    score -= float(descendants) * 1.5
    if instance.get("locked") or instance.get("fixed") or instance.get("kinematic"):
        score -= 10.0
    return score


def _choose_movable_id(scene: Dict[str, Any], a_id: str, b_id: str) -> str:
    child_id, parent_id = _support_relation(scene, a_id, b_id)
    if child_id is not None and parent_id is not None:
        return child_id

    a_score = _movability_score(scene, a_id)
    b_score = _movability_score(scene, b_id)
    if abs(a_score - b_score) > 1e-6:
        return a_id if a_score > b_score else b_id
    return b_id


def _vector_from_payload(value: Any) -> Optional[Vec3]:
    if value is None:
        return None
    try:
        vector = [float(value[axis]) for axis in range(3)]
    except Exception:
        return None
    if _length(vector) <= 1e-9:
        return None
    return vector


def _contact_normal_for_movable(
    collision: Dict[str, Any],
    *,
    movable_id: str,
    other_id: str,
    bboxes: Dict[str, BBox],
) -> Optional[Vec3]:
    normals: List[Any] = []
    details = collision.get("contact_details") or []
    if isinstance(details, list):
        sorted_details = sorted(
            [item for item in details if isinstance(item, dict)],
            key=lambda item: float(item.get("separation", 0.0)),
        )
        normals.extend(item.get("normal") for item in sorted_details if item.get("normal") is not None)
    if isinstance(collision.get("contact_normal"), list):
        normals.append(collision["contact_normal"])
    normals.extend(collision.get("contact_normals") or [])

    movable_center = _bbox_center(bboxes[movable_id])
    other_center = _bbox_center(bboxes[other_id])
    away = [
        movable_center[axis] - other_center[axis]
        for axis in range(3)
    ]
    for normal_value in normals:
        normal = _unit_vector(normal_value)
        if normal is None:
            continue
        if sum(normal[axis] * away[axis] for axis in range(3)) < 0.0:
            normal = [-value for value in normal]
        return normal
    return None


def _aabb_separation_direction(
    *,
    movable_id: str,
    other_id: str,
    collision: Dict[str, Any],
    bboxes: Dict[str, BBox],
) -> Vec3:
    overlaps = collision.get("overlap_depth")
    if not isinstance(overlaps, list) or len(overlaps) < 3:
        overlaps = _bbox_overlap_depth(bboxes[movable_id], bboxes[other_id])
    xy_axes = [axis for axis in (0, 1) if float(overlaps[axis]) > 1e-6]
    if xy_axes:
        axis = min(xy_axes, key=lambda item: float(overlaps[item]))
    else:
        axis = min(range(3), key=lambda item: float(overlaps[item]))

    movable_center = _bbox_center(bboxes[movable_id])
    other_center = _bbox_center(bboxes[other_id])
    direction = [0.0, 0.0, 0.0]
    direction[axis] = 1.0 if movable_center[axis] >= other_center[axis] else -1.0
    return direction


def _collision_move_distance(collision: Dict[str, Any], direction: Vec3) -> float:
    margin = 0.05
    distance = margin
    min_separation = collision.get("min_separation")
    if min_separation is not None:
        try:
            sep = float(min_separation)
        except Exception:
            sep = 0.0
        if sep < 0.0:
            distance = max(distance, abs(sep) + margin)

    overlaps = collision.get("overlap_depth")
    if isinstance(overlaps, list) and len(overlaps) >= 3:
        weighted_overlap = sum(abs(float(direction[axis])) * float(overlaps[axis]) for axis in range(3))
        if weighted_overlap > 1e-6:
            distance = max(distance, weighted_overlap + margin)
        xy = [float(overlaps[axis]) for axis in (0, 1) if float(overlaps[axis]) > 1e-6]
        if xy and distance <= margin:
            distance = max(distance, min(xy) + margin)
    return distance


def _expected_collision_free(
    *,
    instance_id: str,
    moved_bbox: BBox,
    bboxes: Dict[str, BBox],
    collisions: List[Dict[str, Any]],
) -> bool:
    for collision in collisions:
        a_id = str(collision.get("a"))
        b_id = str(collision.get("b"))
        if instance_id not in {a_id, b_id}:
            continue
        other_id = b_id if a_id == instance_id else a_id
        other_bbox = bboxes.get(other_id)
        if other_bbox is not None and _bbox_penetrating(moved_bbox, other_bbox):
            return False
    return True


def _collision_candidate_for(
    *,
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    collision: Dict[str, Any],
    reason: str,
) -> Optional[Dict[str, Any]]:
    a_id = str(collision.get("a"))
    b_id = str(collision.get("b"))
    if a_id not in bboxes or b_id not in bboxes:
        return None

    movable_id = _choose_movable_id(scene, a_id, b_id)
    other_id = b_id if movable_id == a_id else a_id
    old_position = _instance_position(scene, movable_id, _bbox_center(bboxes[movable_id]))

    normal = _contact_normal_for_movable(
        collision,
        movable_id=movable_id,
        other_id=other_id,
        bboxes=bboxes,
    )
    if normal is not None:
        direction = normal
        basis = "contact_normal"
        suggestion_backend = "physx_contact_surface"
    else:
        direction = _aabb_separation_direction(
            movable_id=movable_id,
            other_id=other_id,
            collision=collision,
            bboxes=bboxes,
        )
        if collision.get("method") == "physx_contact":
            basis = "aabb_fallback_for_contact_without_normal"
            suggestion_backend = "physx_contact_aabb_fallback"
        else:
            basis = "aabb_fallback"
            suggestion_backend = "bbox_fallback"

    distance = _collision_move_distance(collision, direction)
    move_vector = [float(direction[axis]) * distance for axis in range(3)]
    moved_bbox = _bbox_with_offset(bboxes[movable_id], move_vector)
    expected_free = _expected_collision_free(
        instance_id=movable_id,
        moved_bbox=moved_bbox,
        bboxes=bboxes,
        collisions=[collision],
    )
    return normalize_suggestion_payload(
        instance_id=movable_id,
        old_position=old_position,
        move_vector=move_vector,
        reason=reason,
        suggestion_backend=suggestion_backend,
        validation_backend="predictive_fallback",
        basis=basis,
        expected_collision_free=expected_free,
        expected_support_valid=True,
        unresolved_issues=[] if expected_free else ["predicted_aabb_overlap_remains"],
        extra={
            "collision_pair": {"a": a_id, "b": b_id},
            "other_instance_id": other_id,
            "contact_count": collision.get("contact_count"),
            "min_separation": collision.get("min_separation"),
        },
    )


def normalize_suggestion_payload(
    *,
    instance_id: str,
    old_position: Optional[Vec3] = None,
    final_position: Optional[Vec3] = None,
    new_position: Optional[Vec3] = None,
    move_vector: Optional[Vec3] = None,
    reason: str,
    suggestion_backend: str,
    validation_backend: str = "predictive_fallback",
    basis: Optional[str] = None,
    expected_collision_free: Optional[bool] = None,
    expected_support_valid: Optional[bool] = None,
    expected_supported: Optional[bool] = None,
    unresolved_issues: Optional[List[str]] = None,
    parent_id: Optional[str] = None,
    target_surface: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    if old_position is None:
        old_position = [0.0, 0.0, 0.0]
    old_position = [float(value) for value in old_position]

    if final_position is None and new_position is not None:
        final_position = new_position
    if final_position is None and move_vector is not None:
        final_position = [
            old_position[axis] + float(move_vector[axis])
            for axis in range(3)
        ]
    if final_position is None:
        final_position = list(old_position)
    final_position = [float(value) for value in final_position]

    if new_position is None:
        new_position = list(final_position)
    else:
        new_position = [float(value) for value in new_position]

    if move_vector is None:
        move_vector = [
            final_position[axis] - old_position[axis]
            for axis in range(3)
        ]
    else:
        move_vector = [float(value) for value in move_vector]

    payload: Dict[str, Any] = {
        "instance_id": instance_id,
        "old_position": old_position,
        "final_position": final_position,
        "new_position": new_position,
        "move_vector": move_vector,
        "reason": reason,
        "suggestion_backend": suggestion_backend,
        "validation_backend": validation_backend,
        "requires_recheck_after_move": True,
        "unresolved_issues": list(unresolved_issues or []),
    }
    if parent_id is not None:
        payload["parent_id"] = parent_id
    if basis is not None:
        payload["basis"] = basis
    if expected_collision_free is not None:
        payload["expected_collision_free"] = bool(expected_collision_free)
        payload["expected_resolved_by_aabb"] = bool(expected_collision_free)
    if expected_support_valid is not None:
        payload["expected_support_valid"] = bool(expected_support_valid)
    if expected_supported is not None:
        payload["expected_supported"] = bool(expected_supported)
    if target_surface is not None:
        payload["target_surface"] = target_surface
    if extra:
        payload.update(extra)
    return payload


def rank_candidate_moves(candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    def _score(candidate: Dict[str, Any]) -> Tuple[int, int, int, float]:
        unresolved = len(candidate.get("unresolved_issues") or [])
        collision_penalty = 0 if candidate.get("expected_collision_free", True) else 1
        support_penalty = 0 if candidate.get("expected_support_valid", True) else 1
        distance = _length(candidate.get("move_vector") or [0.0, 0.0, 0.0])
        return unresolved, collision_penalty, support_penalty, distance

    return sorted(candidates, key=_score)


def suggest_collision_resolutions(
    *,
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    collisions: List[Dict[str, Any]],
    reason: str = "resolve_physx_contact_collision",
    validator: Optional[ValidationFn] = None,
    max_suggestions: int = 1,
) -> Dict[str, Dict[str, Any]]:
    candidates = [
        candidate
        for collision in collisions
        for candidate in [
            _collision_candidate_for(
                scene=scene,
                bboxes=bboxes,
                collision=collision,
                reason=reason,
            )
        ]
        if candidate is not None
    ]
    if validator is not None:
        validated: List[Dict[str, Any]] = []
        for candidate in candidates:
            try:
                updated = dict(candidate)
                updated.update(validator(candidate))
                validated.append(updated)
            except Exception as exc:
                updated = dict(candidate)
                updated["validation_backend"] = "predictive_fallback"
                updated.setdefault("unresolved_issues", []).append(
                    f"suggestion validation unavailable: {exc}"
                )
                validated.append(updated)
        candidates = validated

    ranked = rank_candidate_moves(candidates)
    final_positions: Dict[str, Dict[str, Any]] = {}
    for candidate in ranked:
        instance_id = str(candidate.get("instance_id"))
        if instance_id in final_positions:
            continue
        final_positions[instance_id] = candidate
        if len(final_positions) >= max(1, int(max_suggestions)):
            break
    return final_positions


def _surface_from_hit(hit: Dict[str, Any], child_bbox: BBox) -> Optional[Dict[str, Any]]:
    position = hit.get("position")
    if not isinstance(position, list) or len(position) < 3:
        return None
    return {
        "surface_z": float(position[2]),
        "bbox": {
            "min": [float(child_bbox["min"][0]), float(child_bbox["min"][1]), float(position[2])],
            "max": [float(child_bbox["max"][0]), float(child_bbox["max"][1]), float(position[2])],
        },
        "normal": hit.get("normal"),
        "mesh_path": hit.get("collision"),
        "face_index": None,
        "source": "physx_raycast_surface",
    }


def _support_surfaces(
    *,
    child_bbox: BBox,
    raycast_result: Optional[Dict[str, Any]],
    mesh_result: Optional[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    surfaces: List[Dict[str, Any]] = []
    if mesh_result:
        for surface in (mesh_result.get("support_surfaces", []) or []):
            if isinstance(surface, dict):
                item = dict(surface)
                item.setdefault("source", mesh_result.get("support_backend", "usd_mesh_surface"))
                surfaces.append(item)
        for surface in (mesh_result.get("_all_surfaces", []) or []):
            if isinstance(surface, dict):
                item = dict(surface)
                item.setdefault("source", "usd_mesh_surface")
                surfaces.append(item)
    if raycast_result:
        for hit in (raycast_result.get("_valid_hits", []) or []):
            if isinstance(hit, dict):
                surface = _surface_from_hit(hit, child_bbox)
                if surface is not None:
                    surfaces.append(surface)
        for probe in (raycast_result.get("probe_hits", []) or []):
            for hit in (probe.get("parent_hits", []) or []):
                if isinstance(hit, dict):
                    surface = _surface_from_hit(hit, child_bbox)
                    if surface is not None:
                        surfaces.append(surface)
    return surfaces


def _surface_score(child_bbox: BBox, surface: Dict[str, Any]) -> Tuple[float, float]:
    child_bottom = float(child_bbox["min"][2])
    child_center = _bbox_center(child_bbox)
    bbox = surface.get("bbox")
    coverage = _xy_coverage(child_bbox, bbox) if isinstance(bbox, dict) else 0.0
    z_distance = abs(float(surface.get("surface_z", child_bottom)) - child_bottom)
    center_distance = 0.0
    if isinstance(bbox, dict):
        sx = _clamp(child_center[0], float(bbox["min"][0]), float(bbox["max"][0]))
        sy = _clamp(child_center[1], float(bbox["min"][1]), float(bbox["max"][1]))
        center_distance = math.hypot(child_center[0] - sx, child_center[1] - sy)
    return -coverage, z_distance + center_distance


def _suggest_from_surface(
    *,
    scene: Dict[str, Any],
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    surface: Dict[str, Any],
    overlap_threshold: float,
) -> Dict[str, Any]:
    old_position = _instance_position(scene, child_id, _bbox_center(child_bbox))
    child_center = _bbox_center(child_bbox)
    child_size = _bbox_size(child_bbox)
    surface_bbox = surface.get("bbox")

    move_vector = [
        0.0,
        0.0,
        float(surface["surface_z"]) - float(child_bbox["min"][2]),
    ]
    if isinstance(surface_bbox, dict):
        for axis in (0, 1):
            child_half = child_size[axis] / 2.0
            target_center = _clamp(
                child_center[axis],
                float(surface_bbox["min"][axis]) + child_half,
                float(surface_bbox["max"][axis]) - child_half,
            )
            move_vector[axis] = target_center - child_center[axis]

    expected_bbox = _bbox_with_offset(child_bbox, move_vector)
    expected_coverage = (
        _xy_coverage(expected_bbox, surface_bbox)
        if isinstance(surface_bbox, dict)
        else 1.0
    )
    unresolved = []
    if expected_coverage < overlap_threshold:
        unresolved.append(
            "expected_surface_xy_coverage="
            f"{expected_coverage:.3f} below threshold {overlap_threshold:.3f}"
        )

    suggestion_backend = str(surface.get("source") or "usd_mesh_surface")
    return normalize_suggestion_payload(
        instance_id=child_id,
        parent_id=parent_id,
        old_position=old_position,
        move_vector=move_vector,
        reason="move_to_real_support_surface",
        suggestion_backend=suggestion_backend,
        validation_backend="predictive_fallback",
        expected_supported=not unresolved,
        expected_support_valid=not unresolved,
        unresolved_issues=unresolved,
        target_surface={
            "surface_z": surface.get("surface_z"),
            "mesh_path": surface.get("mesh_path"),
            "face_index": surface.get("face_index"),
            "normal": surface.get("normal"),
        },
        extra={
            "suggestion_status": (
                "resolved_by_surface_move"
                if not unresolved
                else "unresolved_by_surface_move"
            ),
            "recommended_action": None if not unresolved else (
                "move child closer to a larger upward parent support surface"
            ),
        },
    )


def _normalize_fallback_support_move(
    *,
    scene: Dict[str, Any],
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    fallback_move: Dict[str, Any],
) -> Dict[str, Any]:
    old_position = fallback_move.get("old_position")
    if old_position is None:
        old_position = _instance_position(scene, child_id, _bbox_center(child_bbox))
    final_position = fallback_move.get("final_position") or fallback_move.get("new_position")
    move_vector = fallback_move.get("move_vector")
    payload = normalize_suggestion_payload(
        instance_id=str(fallback_move.get("instance_id") or child_id),
        parent_id=str(fallback_move.get("parent_id") or parent_id),
        old_position=old_position,
        final_position=final_position,
        move_vector=move_vector,
        reason="move_to_bbox_support_surface",
        suggestion_backend="bbox_fallback",
        validation_backend="predictive_fallback",
        expected_supported=bool(fallback_move.get("expected_supported", False)),
        expected_support_valid=bool(fallback_move.get("expected_supported", False)),
        unresolved_issues=list(fallback_move.get("unresolved_issues") or []),
    )
    for key in ("suggestion_status", "recommended_action"):
        if key in fallback_move:
            payload[key] = fallback_move[key]
    return payload


def suggest_support_move(
    *,
    scene: Dict[str, Any],
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    raycast_result: Optional[Dict[str, Any]] = None,
    mesh_result: Optional[Dict[str, Any]] = None,
    fallback_move: Optional[Dict[str, Any]] = None,
    overlap_threshold: float = 0.4,
    validator: Optional[ValidationFn] = None,
) -> Optional[Dict[str, Any]]:
    surfaces = _support_surfaces(
        child_bbox=child_bbox,
        raycast_result=raycast_result,
        mesh_result=mesh_result,
    )
    suggestion: Optional[Dict[str, Any]] = None
    if surfaces:
        best = sorted(surfaces, key=lambda item: _surface_score(child_bbox, item))[0]
        suggestion = _suggest_from_surface(
            scene=scene,
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child_bbox,
            surface=best,
            overlap_threshold=overlap_threshold,
        )
    elif fallback_move:
        suggestion = _normalize_fallback_support_move(
            scene=scene,
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child_bbox,
            fallback_move=fallback_move,
        )

    if suggestion is None:
        return None
    if validator is not None:
        try:
            updated = dict(suggestion)
            updated.update(validator(suggestion))
            suggestion = updated
        except Exception as exc:
            suggestion.setdefault("unresolved_issues", []).append(
                f"suggestion validation unavailable: {exc}"
            )
            suggestion["validation_backend"] = "predictive_fallback"
    return suggestion


__all__ = [
    "normalize_suggestion_payload",
    "rank_candidate_moves",
    "suggest_collision_resolutions",
    "suggest_support_move",
]
