"""
Enhanced collision helpers for the optional PhysX contact worker.

This module is intentionally standalone so enhanced_worker.py can import it
when launched directly by the Isaac Python process. It does not mutate the
existing worker or tool wrappers.
"""
from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from container_inner_support import (
        SUPPORT_TYPE_CONTAINER_INNER,
        run_container_inner_support_check,
        support_type_for_child,
    )
    from enhanced_suggestions import suggest_collision_resolutions
    from enhanced_support_checks import run_enhanced_support_check
    from support_checks import _check_support
except ModuleNotFoundError:
    from .container_inner_support import (
        SUPPORT_TYPE_CONTAINER_INNER,
        run_container_inner_support_check,
        support_type_for_child,
    )
    from .enhanced_suggestions import suggest_collision_resolutions
    from .enhanced_support_checks import run_enhanced_support_check
    from .support_checks import _check_support


BBox = Dict[str, List[float]]
Pair = Tuple[str, str]


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


def _normalized_pair(a_id: str, b_id: str) -> Pair:
    return tuple(sorted((str(a_id), str(b_id))))  # type: ignore[return-value]


def _bbox_overlap_depth(a_bbox: BBox, b_bbox: BBox) -> List[float]:
    return [
        max(
            0.0,
            min(a_bbox["max"][axis], b_bbox["max"][axis])
            - max(a_bbox["min"][axis], b_bbox["min"][axis]),
        )
        for axis in range(3)
    ]


def _is_penetrating(
    overlaps: List[float],
    penetration_tolerance: float,
) -> bool:
    return all(overlap > penetration_tolerance for overlap in overlaps)


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


def aabb_candidate_collisions(
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    pair: Optional[List[str]] = None,
    *,
    penetration_tolerance: float = 1e-5,
) -> List[Dict[str, Any]]:
    """Return AABB-penetrating pairs used as PhysX narrow-phase candidates."""
    axis_names = ["x", "y", "z"]
    if pair:
        ids = [
            instance_id
            for instance_id in pair
            if isinstance(instance_id, str) and instance_id in bboxes
        ]
    else:
        ids = [
            instance_id
            for instance_id in _instances(scene).keys()
            if instance_id in bboxes
        ]

    candidates: List[Dict[str, Any]] = []
    for idx, a_id in enumerate(ids):
        if a_id not in bboxes:
            continue
        for b_id in ids[idx + 1:]:
            if b_id not in bboxes:
                continue

            overlaps = _bbox_overlap_depth(bboxes[a_id], bboxes[b_id])
            if not _is_penetrating(overlaps, penetration_tolerance):
                continue

            axis = _collision_axis(overlaps, penetration_tolerance)
            candidates.append({
                "a": a_id,
                "b": b_id,
                "method": "isaac_world_bbox",
                "axis": axis_names[axis],
                "axis_idx": axis,
                "overlap": overlaps[axis],
                "overlap_depth": overlaps,
            })
    return candidates


def _support_relation(
    scene: Dict[str, Any],
    a_id: str,
    b_id: str,
) -> Tuple[Optional[str], Optional[str]]:
    support_children = scene.get("support_children", {}) or {}
    if isinstance(support_children, dict):
        if b_id in (support_children.get(a_id) or []):
            return b_id, a_id
        if a_id in (support_children.get(b_id) or []):
            return a_id, b_id

    instances = _instances(scene)
    a_parent = (instances.get(a_id) or {}).get("parent_instance_id")
    b_parent = (instances.get(b_id) or {}).get("parent_instance_id")
    if a_parent == b_id:
        return a_id, b_id
    if b_parent == a_id:
        return b_id, a_id
    return None, None


def is_valid_support_contact(
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    a_id: str,
    b_id: str,
    *,
    stage: Any = None,
    sim_app: Any = None,
    prim_paths: Optional[Dict[str, str]] = None,
) -> bool:
    support = _support_contact_result(
        scene,
        bboxes,
        a_id,
        b_id,
        stage=stage,
        sim_app=sim_app,
        prim_paths=prim_paths,
    )
    return bool(support.get("supported"))


def _support_contact_result(
    scene: Dict[str, Any],
    bboxes: Dict[str, BBox],
    a_id: str,
    b_id: str,
    *,
    stage: Any = None,
    sim_app: Any = None,
    prim_paths: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    child_id, parent_id = _support_relation(scene, a_id, b_id)
    if child_id is None or parent_id is None:
        return {"supported": False, "issues": ["no support relation"]}
    if child_id not in bboxes or parent_id not in bboxes:
        return {"supported": False, "issues": ["missing bbox"]}
    support_type = support_type_for_child(scene, child_id)
    if support_type == SUPPORT_TYPE_CONTAINER_INNER:
        return run_container_inner_support_check(
            scene=scene,
            bboxes=bboxes,
            child_id=child_id,
            parent_id=parent_id,
            include_suggestions=False,
            z_tolerance=0.08,
        )
    if stage is not None and prim_paths is not None:
        try:
            support = run_enhanced_support_check(
                stage=stage,
                sim_app=sim_app,
                scene=scene,
                prim_paths=prim_paths,
                bboxes=bboxes,
                child_id=child_id,
                parent_id=parent_id,
                include_suggestions=False,
            )
            support["support_type"] = support_type
            return support
        except Exception as exc:
            fallback_warning = f"enhanced support contact check unavailable: {exc}"
        else:
            fallback_warning = ""
    else:
        fallback_warning = "enhanced support contact check missing stage"
    try:
        support = _check_support(
            child_id,
            parent_id,
            bboxes,
            scene=scene,
            include_suggestions=False,
        )
    except Exception:
        return {"supported": False, "issues": ["support fallback failed"]}
    support = dict(support)
    support.setdefault("warnings", [])
    if fallback_warning:
        support["warnings"].append(fallback_warning)
    support["support_backend"] = "bbox_fallback"
    support["support_type"] = support_type
    return support


def _apply_contact_report_api(stage: Any, prim_paths: Dict[str, str]) -> None:
    from pxr import PhysxSchema

    for prim_path in prim_paths.values():
        prim = stage.GetPrimAtPath(prim_path)
        if not prim or not prim.IsValid():
            continue
        api = PhysxSchema.PhysxContactReportAPI.Apply(prim)
        create_threshold = getattr(api, "CreateThresholdAttr", None)
        if create_threshold is None:
            create_threshold = getattr(api, "CreatePhysxContactReportThresholdAttr", None)
        if create_threshold is not None:
            create_threshold().Set(0.0)


def _path_to_instance(path: Any, prim_paths: Dict[str, str]) -> Optional[str]:
    path_text = str(path)
    roots = sorted(
        ((instance_id, str(prim_path)) for instance_id, prim_path in prim_paths.items()),
        key=lambda item: len(item[1]),
        reverse=True,
    )
    for instance_id, root_path in roots:
        if path_text == root_path or path_text.startswith(f"{root_path}/"):
            return instance_id
    return None


def _active_contact_type(value: Any) -> bool:
    text = str(value).upper()
    return "FOUND" in text or "PERSIST" in text


def _contact_separation_values(
    contact_header: Any,
    contact_data: Any,
) -> List[float]:
    values: List[float] = []
    try:
        start = int(contact_header.contact_data_offset)
        count = int(contact_header.num_contact_data)
    except Exception:
        return values

    for index in range(start, start + count):
        try:
            values.append(float(contact_data[index].separation))
        except Exception:
            continue
    return values


def _vector_to_list(value: Any) -> Optional[List[float]]:
    if value is None:
        return None
    try:
        return [float(value.x), float(value.y), float(value.z)]
    except Exception:
        pass
    try:
        return [float(value[0]), float(value[1]), float(value[2])]
    except Exception:
        return None


def _first_attr(value: Any, names: Iterable[str]) -> Any:
    for name in names:
        try:
            result = getattr(value, name)
        except Exception:
            continue
        if result is not None:
            return result
    return None


def _contact_details(
    contact_header: Any,
    contact_data: Any,
) -> List[Dict[str, Any]]:
    try:
        start = int(contact_header.contact_data_offset)
        count = int(contact_header.num_contact_data)
    except Exception:
        return []

    details: List[Dict[str, Any]] = []
    for index in range(start, start + count):
        try:
            item = contact_data[index]
        except Exception:
            continue
        detail: Dict[str, Any] = {}
        try:
            detail["separation"] = float(getattr(item, "separation"))
        except Exception:
            pass
        position = _vector_to_list(
            _first_attr(
                item,
                (
                    "position",
                    "point",
                    "contactPoint",
                    "contact_point",
                ),
            )
        )
        normal = _vector_to_list(
            _first_attr(
                item,
                (
                    "normal",
                    "contactNormal",
                    "contact_normal",
                    "worldNormal",
                    "world_normal",
                ),
            )
        )
        if position is not None:
            detail["position"] = position
        if normal is not None:
            detail["normal"] = normal
        if detail:
            details.append(detail)
    return details


def _append_contact_details(record: Dict[str, Any], details: List[Dict[str, Any]]) -> None:
    if not details:
        return
    record.setdefault("contact_details", [])
    record.setdefault("contact_points", [])
    record.setdefault("contact_normals", [])
    for detail in details:
        if len(record["contact_details"]) < 16:
            record["contact_details"].append(detail)
        position = detail.get("position")
        if position is not None and len(record["contact_points"]) < 8:
            record["contact_points"].append(position)
        normal = detail.get("normal")
        if normal is not None and len(record["contact_normals"]) < 8:
            record["contact_normals"].append(normal)


def _collect_contact_report_pairs(
    stage: Any,
    prim_paths: Dict[str, str],
    candidate_pairs: Iterable[Pair],
    *,
    sim_steps: int,
    dt: float,
) -> Dict[Pair, Dict[str, Any]]:
    import carb
    from omni.physx import get_physx_simulation_interface
    from omni.physx.bindings._physx import SETTING_UPDATE_TO_USD
    from pxr import PhysicsSchemaTools, Sdf, Usd, UsdUtils

    candidate_set = set(candidate_pairs)
    if not candidate_set:
        return {}

    stage_id = UsdUtils.StageCache.Get().GetId(stage).ToLongInt()
    session_layer = Sdf.Layer.CreateAnonymous()
    session_layers = stage.GetSessionLayer().subLayerPaths
    old_edit_target = stage.GetEditTarget()
    settings = carb.settings.get_settings()
    old_write_usd = settings.get_as_bool(SETTING_UPDATE_TO_USD)
    old_fabric = settings.get_as_bool("/physics/fabricEnabled")
    simulation = get_physx_simulation_interface()
    was_attached = simulation.get_attached_stage() == stage_id

    reports: Dict[Pair, Dict[str, Any]] = {}
    session_layers.append(session_layer.identifier)
    stage.SetEditTarget(Usd.EditTarget(session_layer))
    try:
        _apply_contact_report_api(stage, prim_paths)
        settings.set(SETTING_UPDATE_TO_USD, False)
        settings.set("/physics/fabricEnabled", False)

        if not was_attached:
            simulation.attach_stage(stage_id)

        for step in range(max(1, int(sim_steps))):
            simulation.simulate(float(dt), float(step) * float(dt))
            simulation.fetch_results()
            report = simulation.get_contact_report()
            if len(report) < 2:
                continue
            contact_headers, contact_data = report[0], report[1]
            for header in contact_headers:
                if not _active_contact_type(getattr(header, "type", "")):
                    continue

                try:
                    collider0 = PhysicsSchemaTools.intToSdfPath(header.collider0)
                    collider1 = PhysicsSchemaTools.intToSdfPath(header.collider1)
                except Exception:
                    continue

                a_id = _path_to_instance(collider0, prim_paths)
                b_id = _path_to_instance(collider1, prim_paths)
                if a_id is None or b_id is None or a_id == b_id:
                    continue

                pair = _normalized_pair(a_id, b_id)
                if pair not in candidate_set:
                    continue

                separations = _contact_separation_values(header, contact_data)
                record = reports.setdefault(
                    pair,
                    {
                        "contact_count": 0,
                        "min_separation": None,
                        "colliders": [],
                        "contact_details": [],
                        "contact_points": [],
                        "contact_normals": [],
                    },
                )
                count = max(1, int(getattr(header, "num_contact_data", 0) or 0))
                record["contact_count"] += count
                if separations:
                    min_sep = min(separations)
                    current = record.get("min_separation")
                    if current is None or min_sep < current:
                        record["min_separation"] = min_sep
                _append_contact_details(
                    record,
                    _contact_details(header, contact_data),
                )
                record["colliders"].append({
                    "collider0": str(collider0),
                    "collider1": str(collider1),
                })
    finally:
        if not was_attached:
            try:
                simulation.detach_stage()
            except Exception:
                pass
        settings.set(SETTING_UPDATE_TO_USD, old_write_usd)
        settings.set("/physics/fabricEnabled", old_fabric)
        stage.SetEditTarget(old_edit_target)
        try:
            session_layers.remove(session_layer.identifier)
        except ValueError:
            pass
    return reports


def _shape_paths_for_instance(stage: Any, root_path: str) -> List[str]:
    from pxr import UsdGeom

    root = stage.GetPrimAtPath(root_path)
    if not root or not root.IsValid():
        return []

    shape_paths: List[str] = []
    stack = [root]
    while stack:
        prim = stack.pop()
        if not prim or not prim.IsValid():
            continue
        if prim.IsA(UsdGeom.Gprim):
            shape_paths.append(str(prim.GetPath()))
        for child in reversed(prim.GetChildren()):
            stack.append(child)
    return shape_paths


def _encoded_sdf_path(path: str) -> Optional[Tuple[int, int]]:
    from pxr import PhysicsSchemaTools, Sdf

    encoded = PhysicsSchemaTools.encodeSdfPath(Sdf.Path(path))
    if isinstance(encoded, (list, tuple)) and len(encoded) >= 2:
        return int(encoded[0]), int(encoded[1])
    return None


def _collect_scene_query_pairs(
    stage: Any,
    prim_paths: Dict[str, str],
    candidate_pairs: Iterable[Pair],
) -> Dict[Pair, Dict[str, Any]]:
    from omni.physx import get_physx_scene_query_interface

    candidate_set = set(candidate_pairs)
    if not candidate_set:
        return {}

    query = get_physx_scene_query_interface()
    shapes_by_instance = {
        instance_id: _shape_paths_for_instance(stage, prim_path)
        for instance_id, prim_path in prim_paths.items()
    }
    reports: Dict[Pair, Dict[str, Any]] = {}

    for pair_key in candidate_set:
        a_id, b_id = pair_key
        a_shapes = shapes_by_instance.get(a_id, [])
        if not a_shapes:
            continue

        for shape_path in a_shapes:
            encoded = _encoded_sdf_path(shape_path)
            if encoded is None:
                continue

            def _report(hit: Any) -> bool:
                hit_path = getattr(hit, "collision", "") or getattr(hit, "rigid_body", "")
                hit_instance_id = _path_to_instance(hit_path, prim_paths)
                if hit_instance_id != b_id:
                    return True
                record = reports.setdefault(
                    pair_key,
                    {
                        "contact_count": 0,
                        "min_separation": None,
                        "colliders": [],
                    },
                )
                record["contact_count"] += 1
                record["colliders"].append({
                    "query_shape": shape_path,
                    "hit": str(hit_path),
                })
                return True

            query.overlap_shape(encoded[0], encoded[1], _report, False)

    return reports


def _fallback_collision(
    candidate: Dict[str, Any],
    reason: str,
) -> Dict[str, Any]:
    collision = dict(candidate)
    collision["method"] = "isaac_world_bbox"
    collision["contact_count"] = None
    collision["is_support_contact"] = False
    collision["issue"] = "aabb_collision_fallback"
    collision["fallback_reason"] = reason
    return collision


def _contact_collision(
    candidate: Dict[str, Any],
    contact: Dict[str, Any],
    *,
    is_support_contact: bool,
    support_result: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    collision = {
        "a": candidate["a"],
        "b": candidate["b"],
        "method": "physx_contact",
        "axis": candidate.get("axis"),
        "axis_idx": candidate.get("axis_idx"),
        "overlap": candidate.get("overlap"),
        "overlap_depth": candidate.get("overlap_depth"),
        "contact_count": contact.get("contact_count", 0),
        "min_separation": contact.get("min_separation"),
        "is_support_contact": is_support_contact,
        "issue": (
            "valid_support_contact"
            if is_support_contact
            else "physx_contact_collision"
        ),
    }
    if support_result:
        collision["support_backend"] = support_result.get("support_backend")
        collision["support_issues"] = support_result.get("issues", [])
    contact_details = contact.get("contact_details") or []
    contact_points = contact.get("contact_points") or []
    contact_normals = contact.get("contact_normals") or []
    if contact_details:
        collision["contact_details"] = contact_details[:8]
    if contact_points:
        collision["contact_points"] = contact_points[:8]
        collision["contact_point"] = contact_points[0]
    if contact_normals:
        collision["contact_normals"] = contact_normals[:8]
        collision["contact_normal"] = contact_normals[0]
    colliders = contact.get("colliders") or []
    if colliders:
        collision["colliders"] = colliders[:4]
    return collision


def run_enhanced_collision_check(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    bboxes: Dict[str, BBox],
    pair: Optional[List[str]] = None,
    include_suggestions: bool = False,
    sim_steps: int = 1,
    dt: float = 1.0 / 60.0,
    suggestion_validator: Any = None,
) -> Dict[str, Any]:
    warnings: List[str] = []
    candidate_collisions = aabb_candidate_collisions(scene, bboxes, pair=pair)
    candidate_by_pair = {
        _normalized_pair(candidate["a"], candidate["b"]): candidate
        for candidate in candidate_collisions
    }
    candidate_pairs = list(candidate_by_pair.keys())

    if not candidate_pairs:
        return {
            "ok": True,
            "collision_backend": "physx_contact_report",
            "collision_free": True,
            "collisions": [],
            "support_contacts": [],
            "candidate_pairs": [],
            "suggested_final_positions": {},
            "warnings": warnings,
        }

    try:
        contact_pairs = _collect_contact_report_pairs(
            stage,
            prim_paths,
            candidate_pairs,
            sim_steps=sim_steps,
            dt=dt,
        )
        missing_pairs = [
            pair_key
            for pair_key in candidate_pairs
            if pair_key not in contact_pairs
        ]
        if missing_pairs:
            try:
                query_pairs = _collect_scene_query_pairs(
                    stage,
                    prim_paths,
                    missing_pairs,
                )
                contact_pairs.update(query_pairs)
                if query_pairs:
                    collision_backend = "physx_contact_report+scene_query"
                else:
                    collision_backend = "physx_contact_report"
            except Exception as exc:
                warnings.append(f"PhysX scene query fallback unavailable: {exc}")
                collision_backend = "physx_contact_report"
        else:
            collision_backend = "physx_contact_report"
        if sim_app is not None:
            for _ in range(2):
                sim_app.update()
    except Exception as exc:
        reason = f"PhysX contact report unavailable: {exc}"
        warnings.append(reason)
        collisions = [
            _fallback_collision(candidate, reason)
            for candidate in candidate_collisions
        ]
        suggested_final_positions = {}
        if include_suggestions:
            suggested_final_positions = suggest_collision_resolutions(
                scene=scene,
                bboxes=bboxes,
                collisions=collisions,
                reason="resolve_aabb_fallback_collision",
                validator=suggestion_validator,
            )
        return {
            "ok": True,
            "collision_backend": "aabb_fallback",
            "collision_free": len(collisions) == 0,
            "collisions": collisions,
            "support_contacts": [],
            "candidate_pairs": [
                {"a": candidate["a"], "b": candidate["b"]}
                for candidate in candidate_collisions
            ],
            "suggested_final_positions": suggested_final_positions,
            "warnings": warnings,
        }

    collisions: List[Dict[str, Any]] = []
    support_contacts: List[Dict[str, Any]] = []
    for pair_key, contact in contact_pairs.items():
        candidate = candidate_by_pair.get(pair_key)
        if candidate is None:
            continue
        support_result = _support_contact_result(
            scene,
            bboxes,
            candidate["a"],
            candidate["b"],
            stage=stage,
            sim_app=sim_app,
            prim_paths=prim_paths,
        )
        support_contact = bool(support_result.get("supported"))
        contact_collision = _contact_collision(
            candidate,
            contact,
            is_support_contact=support_contact,
            support_result=support_result,
        )
        if support_contact:
            support_contacts.append(contact_collision)
        else:
            collisions.append(contact_collision)

    suggested_final_positions = {}
    if include_suggestions:
        suggested_final_positions = suggest_collision_resolutions(
            scene=scene,
            bboxes=bboxes,
            collisions=collisions,
            reason="resolve_physx_contact_collision",
            validator=suggestion_validator,
        )

    return {
        "ok": True,
        "collision_backend": collision_backend,
        "collision_free": len(collisions) == 0,
        "collisions": collisions,
        "support_contacts": support_contacts,
        "candidate_pairs": [
            {"a": candidate["a"], "b": candidate["b"]}
            for candidate in candidate_collisions
        ],
        "suggested_final_positions": suggested_final_positions,
        "warnings": warnings,
    }


__all__ = [
    "aabb_candidate_collisions",
    "is_valid_support_contact",
    "run_enhanced_collision_check",
]
