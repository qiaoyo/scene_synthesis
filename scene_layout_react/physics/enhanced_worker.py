"""
Optional Isaac Sim worker with PhysX contact-based collision refinement.

This file is a drop-in worker_path replacement for worker.py. It leaves the
existing worker and tool wrappers unchanged, while overriding only the
check_collision operation.
"""
from __future__ import annotations

import json
import sys
from typing import Any, Dict, List

try:
    import worker as base_worker
    from container_inner_support import (
        SUPPORT_TYPE_CONTAINER_INNER,
        SUPPORT_TYPE_SURFACE,
        normalize_support_type,
        run_container_inner_support_check,
        support_type_for_child,
    )
    from enhanced_support_checks import run_enhanced_support_check
    from physx_contact_checks import run_enhanced_collision_check
except ModuleNotFoundError:
    from . import worker as base_worker
    from .container_inner_support import (
        SUPPORT_TYPE_CONTAINER_INNER,
        SUPPORT_TYPE_SURFACE,
        normalize_support_type,
        run_container_inner_support_check,
        support_type_for_child,
    )
    from .enhanced_support_checks import run_enhanced_support_check
    from .physx_contact_checks import run_enhanced_collision_check


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

_APPROXIMATION_KEYS = {
    "none": "none",
    "convexhull": "convexhull",
    "convexdecomposition": "convexdecomposition",
    "meshsimplification": "meshsimplification",
    "boundingcube": "boundingcube",
    "boundingsphere": "boundingsphere",
}


def _normalized_approximation_key(value: Any, *, default: str = "convexhull") -> str:
    text = str(value or default).strip().replace("_", "").replace("-", "").lower()
    aliases = {
        "convex": "convexhull",
        "hull": "convexhull",
        "decomposition": "convexdecomposition",
        "convexdecomp": "convexdecomposition",
        "mesh": "meshsimplification",
        "cube": "boundingcube",
        "box": "boundingcube",
        "sphere": "boundingsphere",
    }
    key = aliases.get(text, text)
    return _APPROXIMATION_KEYS.get(key, _APPROXIMATION_KEYS[default])


def _instance_tags(instance: Dict[str, Any]) -> Dict[str, Any]:
    tags = instance.get("tags", {}) or {}
    return tags if isinstance(tags, dict) else {}


def _explicit_instance_approximation(instance: Dict[str, Any]) -> Any:
    tags = _instance_tags(instance)
    for key in (
        "collision_approximation",
        "collisionApproximation",
        "collision_approximation_shape",
        "collisionApproximationShape",
    ):
        if instance.get(key):
            return instance.get(key)
        if tags.get(key):
            return tags.get(key)
    return None


def _hollow_support_instance(instance: Dict[str, Any]) -> bool:
    tags = _instance_tags(instance)
    text_parts = [
        instance.get("asset_type", ""),
        instance.get("asset_doc_id", ""),
        instance.get("usd_path", ""),
        instance.get("description", ""),
    ]
    text_parts.extend(str(key) for key in tags.keys())
    text_parts.extend(str(value) for value in tags.values())
    text = " ".join(str(part).lower() for part in text_parts if part)
    return any(keyword in text for keyword in _HOLLOW_SUPPORT_KEYWORDS)


def _instance_collision_approximation(
    scene: Dict[str, Any],
    instance_id: str,
    request_default: Any,
) -> str:
    instance = (scene.get("instances", {}) or {}).get(instance_id, {}) or {}
    explicit = _explicit_instance_approximation(instance)
    if explicit:
        return _normalized_approximation_key(explicit)
    if _hollow_support_instance(instance):
        return "convexdecomposition"
    return _normalized_approximation_key(request_default)


def _apply_instance_physics_safe(
    stage: Any,
    request: Dict[str, Any],
    prim_paths: Dict[str, str],
) -> List[str]:
    warnings: List[str] = []
    scene = request.get("scene", {}) or {}
    default_approximation = request.get("collision_approximation") or "convexhull"
    support_children = scene.get("support_children", {}) or {}
    parent_ids = set(support_children.keys())
    options = request.get("options", {}) or {}
    if request.get("operation") == "check_support" and options.get("parent_id"):
        parent_ids.add(str(options["parent_id"]))

    for instance_id, prim_path in prim_paths.items():
        prim = stage.GetPrimAtPath(prim_path)
        if not prim or not prim.IsValid():
            warnings.append(f"invalid prim for {instance_id} ({prim_path})")
            continue
        approximation = _instance_collision_approximation(
            scene,
            instance_id,
            default_approximation,
        )
        try:
            _apply_rigid_body_and_colliders_safe(
                prim,
                kinematic=instance_id in parent_ids,
                approximation_shape=approximation,
            )
        except Exception as exc:
            warnings.append(f"physics authoring failed for {instance_id}: {exc}")
    return warnings


def _apply_rigid_body_and_colliders_safe(
    prim: Any,
    *,
    kinematic: bool,
    approximation_shape: str,
) -> None:
    from pxr import UsdGeom, UsdPhysics

    rigid_api = UsdPhysics.RigidBodyAPI.Apply(prim)
    rigid_api.CreateRigidBodyEnabledAttr(True)
    rigid_api.CreateKinematicEnabledAttr(bool(kinematic))

    physx_schema = base_worker._try_import_physx_schema()
    if physx_schema is not None:
        physx_rigid_api = physx_schema.PhysxRigidBodyAPI.Apply(prim)
        physx_rigid_api.CreateEnableCCDAttr(True)

    for member in base_worker._iter_prim_hierarchy(prim):
        if member.IsA(UsdGeom.Gprim) or member.IsInstanceable():
            _apply_collision_api_safe(member, approximation_shape)


def _apply_collision_api_safe(prim: Any, approximation_shape: str) -> None:
    from pxr import UsdGeom, UsdPhysics

    collision_api = UsdPhysics.CollisionAPI.Apply(prim)
    collision_api.CreateCollisionEnabledAttr(True)

    physx_schema = base_worker._try_import_physx_schema()
    if physx_schema is not None:
        physx_schema.PhysxCollisionAPI.Apply(prim)

    if not (prim.IsA(UsdGeom.Mesh) or prim.IsInstanceable()):
        return

    approximation = _normalized_approximation_key(approximation_shape)
    usd_approximation = {
        "none": "none",
        "convexhull": "convexHull",
        "convexdecomposition": "convexDecomposition",
        "meshsimplification": "meshSimplification",
        "boundingcube": "boundingCube",
        "boundingsphere": "boundingSphere",
    }.get(approximation, approximation)
    mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(prim)
    mesh_collision_api.CreateApproximationAttr().Set(usd_approximation)

    if physx_schema is None:
        return

    api_name_by_approximation = {
        "none": "PhysxTriangleMeshCollisionAPI",
        "convexhull": "PhysxConvexHullCollisionAPI",
        "convexdecomposition": "PhysxConvexDecompositionCollisionAPI",
        "meshsimplification": "PhysxTriangleMeshSimplificationCollisionAPI",
    }
    api_name = api_name_by_approximation.get(approximation)
    physx_mesh_api = getattr(physx_schema, api_name, None) if api_name else None
    if physx_mesh_api is not None:
        physx_mesh_api.Apply(prim)


def _position_from_suggestion(suggestion: Dict[str, Any]) -> List[float] | None:
    position = suggestion.get("final_position") or suggestion.get("new_position")
    if not isinstance(position, list) or len(position) != 3:
        return None
    try:
        return [float(value) for value in position]
    except Exception:
        return None


def _support_pairs_for_instance(
    scene: Dict[str, Any],
    instance_id: str,
) -> List[tuple[str, str]]:
    pairs: List[tuple[str, str]] = []
    instances = scene.get("instances", {}) or {}
    support_children = scene.get("support_children", {}) or {}
    if isinstance(support_children, dict):
        for parent_id, children in support_children.items():
            if not isinstance(children, list):
                continue
            if instance_id == str(parent_id):
                pairs.extend((str(child_id), str(parent_id)) for child_id in children)
            elif instance_id in [str(child_id) for child_id in children]:
                pairs.append((instance_id, str(parent_id)))

    parent_id = (instances.get(instance_id, {}) or {}).get("parent_instance_id")
    if parent_id:
        pairs.append((instance_id, str(parent_id)))

    deduped: List[tuple[str, str]] = []
    for pair in pairs:
        if pair not in deduped:
            deduped.append(pair)
    return deduped


def _run_typed_support_check(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    bboxes: Dict[str, Dict[str, List[float]]],
    child_id: str,
    parent_id: str,
    support_type: str = SUPPORT_TYPE_SURFACE,
    include_suggestions: bool = False,
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
    support_hit_ratio: float = 0.45,
    normal_z_threshold: float = 0.65,
    probe_grid: int = 3,
) -> Dict[str, Any]:
    support_type = normalize_support_type(support_type)
    if support_type == SUPPORT_TYPE_CONTAINER_INNER:
        return run_container_inner_support_check(
            scene=scene,
            bboxes=bboxes,
            child_id=child_id,
            parent_id=parent_id,
            include_suggestions=include_suggestions,
            z_tolerance=z_tolerance,
        )

    support = run_enhanced_support_check(
        stage=stage,
        sim_app=sim_app,
        scene=scene,
        prim_paths=prim_paths,
        bboxes=bboxes,
        child_id=child_id,
        parent_id=parent_id,
        include_suggestions=include_suggestions,
        z_tolerance=z_tolerance,
        overlap_threshold=overlap_threshold,
        support_hit_ratio=support_hit_ratio,
        normal_z_threshold=normal_z_threshold,
        probe_grid=probe_grid,
    )
    support["support_type"] = support_type
    return support


def _with_temporary_position(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    instance_id: str,
    position: List[float],
    callback,
) -> Dict[str, Any]:
    from pxr import Sdf, Usd

    if instance_id not in prim_paths:
        raise RuntimeError(f"missing prim for suggestion target {instance_id}")
    session_layer = Sdf.Layer.CreateAnonymous()
    session_layers = stage.GetSessionLayer().subLayerPaths
    old_edit_target = stage.GetEditTarget()
    session_layers.append(session_layer.identifier)
    stage.SetEditTarget(Usd.EditTarget(session_layer))
    try:
        prim = stage.GetPrimAtPath(prim_paths[instance_id])
        if not prim or not prim.IsValid():
            raise RuntimeError(f"invalid prim for suggestion target {instance_id}")
        instance = (scene.get("instances", {}) or {}).get(instance_id, {}) or {}
        base_worker._set_transform(
            prim,
            position,
            instance.get("rotation_deg", 0.0),
        )
        if sim_app is not None:
            for _ in range(2):
                sim_app.update()
        return callback()
    finally:
        stage.SetEditTarget(old_edit_target)
        try:
            session_layers.remove(session_layer.identifier)
        except ValueError:
            pass
        if sim_app is not None:
            for _ in range(1):
                sim_app.update()


def _validate_support_pairs(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    bboxes: Dict[str, Dict[str, List[float]]],
    instance_id: str,
) -> tuple[bool, List[str]]:
    issues: List[str] = []
    for child_id, parent_id in _support_pairs_for_instance(scene, instance_id):
        if child_id not in bboxes or parent_id not in bboxes:
            issues.append(f"missing bbox for support pair {child_id}->{parent_id}")
            continue
        support_type = support_type_for_child(scene, child_id)
        support = _run_typed_support_check(
            stage=stage,
            sim_app=sim_app,
            scene=scene,
            prim_paths=prim_paths,
            bboxes=bboxes,
            child_id=child_id,
            parent_id=parent_id,
            support_type=support_type,
            include_suggestions=False,
            z_tolerance=(
                0.08
                if support_type == SUPPORT_TYPE_CONTAINER_INNER
                else 0.05
            ),
        )
        if not support.get("supported", False):
            issue_text = "; ".join(support.get("issues", []) or ["unsupported"])
            issues.append(f"{child_id}->{parent_id} ({support_type}): {issue_text}")
    return len(issues) == 0, issues


def _validate_collision_suggestions(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    suggestions: Dict[str, Dict[str, Any]],
    pair: Any,
    sim_steps: int,
    dt: float,
) -> Dict[str, Dict[str, Any]]:
    if not suggestions:
        return suggestions

    validated: Dict[str, Dict[str, Any]] = {}
    for instance_id, suggestion in suggestions.items():
        position = _position_from_suggestion(suggestion)
        updated = dict(suggestion)
        if position is None:
            updated["validation_backend"] = "predictive_fallback"
            updated.setdefault("unresolved_issues", []).append(
                "suggestion missing final_position/new_position"
            )
            validated[instance_id] = updated
            continue

        try:
            def _callback() -> Dict[str, Any]:
                trial_bboxes = base_worker._collect_bboxes(stage, scene, prim_paths)
                collision = run_enhanced_collision_check(
                    stage=stage,
                    sim_app=sim_app,
                    scene=scene,
                    prim_paths=prim_paths,
                    bboxes=trial_bboxes,
                    pair=pair,
                    include_suggestions=False,
                    sim_steps=sim_steps,
                    dt=dt,
                )
                support_ok, support_issues = _validate_support_pairs(
                    stage=stage,
                    sim_app=sim_app,
                    scene=scene,
                    prim_paths=prim_paths,
                    bboxes=trial_bboxes,
                    instance_id=instance_id,
                )
                unresolved = []
                if not collision.get("collision_free", True):
                    unresolved.append(
                        f"remaining_collisions={len(collision.get('collisions', []) or [])}"
                    )
                unresolved.extend(support_issues)
                return {
                    "validation_backend": "physx_recheck",
                    "expected_collision_free": bool(collision.get("collision_free", True)),
                    "expected_resolved_by_aabb": bool(collision.get("collision_free", True)),
                    "expected_support_valid": support_ok,
                    "unresolved_issues": unresolved,
                }

            updated.update(
                _with_temporary_position(
                    stage=stage,
                    sim_app=sim_app,
                    scene=scene,
                    prim_paths=prim_paths,
                    instance_id=instance_id,
                    position=position,
                    callback=_callback,
                )
            )
        except Exception as exc:
            updated["validation_backend"] = "predictive_fallback"
            updated.setdefault("unresolved_issues", []).append(
                f"suggestion validation unavailable: {exc}"
            )
        validated[instance_id] = updated
    return validated


def _validate_collision_candidate(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    suggestion: Dict[str, Any],
    pair: Any,
    sim_steps: int,
    dt: float,
) -> Dict[str, Any]:
    instance_id = str(suggestion.get("instance_id"))
    position = _position_from_suggestion(suggestion)
    if position is None:
        return {
            "validation_backend": "predictive_fallback",
            "unresolved_issues": ["suggestion missing final_position/new_position"],
        }

    def _callback() -> Dict[str, Any]:
        trial_bboxes = base_worker._collect_bboxes(stage, scene, prim_paths)
        collision = run_enhanced_collision_check(
            stage=stage,
            sim_app=sim_app,
            scene=scene,
            prim_paths=prim_paths,
            bboxes=trial_bboxes,
            pair=pair,
            include_suggestions=False,
            sim_steps=sim_steps,
            dt=dt,
        )
        support_ok, support_issues = _validate_support_pairs(
            stage=stage,
            sim_app=sim_app,
            scene=scene,
            prim_paths=prim_paths,
            bboxes=trial_bboxes,
            instance_id=instance_id,
        )
        unresolved = []
        if not collision.get("collision_free", True):
            unresolved.append(
                f"remaining_collisions={len(collision.get('collisions', []) or [])}"
            )
        unresolved.extend(support_issues)
        return {
            "validation_backend": "physx_recheck",
            "expected_collision_free": bool(collision.get("collision_free", True)),
            "expected_resolved_by_aabb": bool(collision.get("collision_free", True)),
            "expected_support_valid": support_ok,
            "unresolved_issues": unresolved,
        }

    try:
        return _with_temporary_position(
            stage=stage,
            sim_app=sim_app,
            scene=scene,
            prim_paths=prim_paths,
            instance_id=instance_id,
            position=position,
            callback=_callback,
        )
    except Exception as exc:
        return {
            "validation_backend": "predictive_fallback",
            "unresolved_issues": [
                *list(suggestion.get("unresolved_issues") or []),
                f"suggestion validation unavailable: {exc}",
            ],
        }


def _validate_support_suggestion(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    support: Dict[str, Any],
    suggestion: Dict[str, Any],
    child_id: str,
    parent_id: str,
    support_type: str = SUPPORT_TYPE_SURFACE,
) -> Dict[str, Any]:
    position = _position_from_suggestion(suggestion)
    updated = dict(suggestion)
    if position is None:
        updated["validation_backend"] = "predictive_fallback"
        updated.setdefault("unresolved_issues", []).append(
            "suggestion missing final_position/new_position"
        )
        return updated

    try:
        def _callback() -> Dict[str, Any]:
            trial_bboxes = base_worker._collect_bboxes(stage, scene, prim_paths)
            trial = _run_typed_support_check(
                stage=stage,
                sim_app=sim_app,
                scene=scene,
                prim_paths=prim_paths,
                bboxes=trial_bboxes,
                child_id=child_id,
                parent_id=parent_id,
                support_type=support_type,
                include_suggestions=False,
                z_tolerance=(
                    0.08
                    if support_type == SUPPORT_TYPE_CONTAINER_INNER
                    else 0.05
                ),
            )
            issues = list(trial.get("issues", []) or [])
            return {
                "validation_backend": "physx_recheck",
                "expected_supported": bool(trial.get("supported", False)),
                "expected_support_valid": bool(trial.get("supported", False)),
                "unresolved_issues": issues,
            }

        updated.update(
            _with_temporary_position(
                stage=stage,
                sim_app=sim_app,
                scene=scene,
                prim_paths=prim_paths,
                instance_id=child_id,
                position=position,
                callback=_callback,
            )
        )
    except Exception as exc:
        updated["validation_backend"] = "predictive_fallback"
        updated.setdefault("unresolved_issues", []).append(
            f"suggestion validation unavailable: {exc}"
        )
    return updated


def _dispatch_with_runtime(
    request: Dict[str, Any],
    *,
    sim_app=None,
    usd_context=None,
) -> Dict[str, Any]:
    operation = request.get("operation")
    if operation not in {"check_collision", "check_support"}:
        return base_worker._dispatch_with_runtime(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )

    scene = request.get("scene", {})
    options = request.get("options", {}) or {}
    warnings: List[str] = []
    stage_path: str | None = None

    try:
        stage_path, prim_paths = base_worker._build_stage(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )
        stage = base_worker._open_stage_in_isaac(sim_app, usd_context, stage_path)
        warnings.extend(_apply_instance_physics_safe(stage, request, prim_paths))

        for _ in range(3):
            sim_app.update()

        bboxes = base_worker._collect_bboxes(stage, scene, prim_paths)
        if operation == "check_collision":
            include_suggestions = bool(options.get("include_suggestions", False))
            sim_steps = int(options.get("physx_contact_steps", 1))
            dt = float(options.get("physx_contact_dt", 1.0 / 60.0))
            suggestion_validator = None
            if include_suggestions:
                suggestion_validator = lambda suggestion: _validate_collision_candidate(
                    stage=stage,
                    sim_app=sim_app,
                    scene=scene,
                    prim_paths=prim_paths,
                    suggestion=suggestion,
                    pair=options.get("pair"),
                    sim_steps=sim_steps,
                    dt=dt,
                )
            enhanced = run_enhanced_collision_check(
                stage=stage,
                sim_app=sim_app,
                scene=scene,
                prim_paths=prim_paths,
                bboxes=bboxes,
                pair=options.get("pair"),
                include_suggestions=include_suggestions,
                sim_steps=sim_steps,
                dt=dt,
                suggestion_validator=suggestion_validator,
            )
            warnings.extend(enhanced.get("warnings", []) or [])
            suggested_final_positions = enhanced.get(
                "suggested_final_positions",
                {},
            )

            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "collision_backend": enhanced.get("collision_backend"),
                "collision_free": bool(enhanced.get("collision_free", True)),
                "collisions": enhanced.get("collisions", []),
                "support_contacts": enhanced.get("support_contacts", []),
                "candidate_pairs": enhanced.get("candidate_pairs", []),
                "warnings": warnings,
                "stage_path": stage_path,
            }

            if include_suggestions:
                payload["suggested_final_positions"] = suggested_final_positions
            return payload

        child_id = options["child_id"]
        parent_id = options["parent_id"]
        support_type = normalize_support_type(
            options.get("support_type")
            or support_type_for_child(scene, child_id)
        )
        default_z_tolerance = (
            0.08
            if support_type == SUPPORT_TYPE_CONTAINER_INNER
            else 0.05
        )
        support = _run_typed_support_check(
            stage=stage,
            sim_app=sim_app,
            scene=scene,
            prim_paths=prim_paths,
            bboxes=bboxes,
            child_id=child_id,
            parent_id=parent_id,
            support_type=support_type,
            include_suggestions=bool(options.get("include_suggestions", False)),
            z_tolerance=float(options.get("support_z_tolerance", default_z_tolerance)),
            overlap_threshold=float(options.get("support_overlap_threshold", 0.4)),
            support_hit_ratio=float(options.get("support_hit_ratio", 0.45)),
            normal_z_threshold=float(options.get("support_normal_z_threshold", 0.65)),
            probe_grid=int(options.get("support_probe_grid", 3)),
        )
        warnings.extend(support.get("warnings", []) or [])
        if bool(options.get("include_suggestions", False)) and support.get("suggested_move"):
            support = dict(support)
            support["suggested_move"] = _validate_support_suggestion(
                stage=stage,
                sim_app=sim_app,
                scene=scene,
                prim_paths=prim_paths,
                support=support,
                suggestion=support["suggested_move"],
                child_id=child_id,
                parent_id=parent_id,
                support_type=support_type,
            )
        payload = {
            "ok": True,
            "operation": operation,
            "backend": "isaacsim",
            "support": support,
            "warnings": warnings,
            "stage_path": stage_path,
        }
        return payload

    except Exception as exc:
        return base_worker._error_payload(operation, exc)
    finally:
        keep_stage = bool(request.get("keep_stage"))
        if operation != "save_scene_usd" and not keep_stage:
            base_worker._cleanup_stage_file(stage_path)
        if usd_context is not None:
            try:
                usd_context.close_stage()
            except Exception:
                pass


def _dispatch(
    request: Dict[str, Any],
    *,
    emit_before_shutdown: bool = False,
) -> Dict[str, Any]:
    sim_app = None
    usd_context = None
    payload: Dict[str, Any] | None = None

    try:
        sim_app, usd_context = base_worker._start_isaac(request)
        payload = _dispatch_with_runtime(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )
        return payload
    except Exception as exc:
        payload = base_worker._error_payload(request.get("operation"), exc)
        return payload
    finally:
        if emit_before_shutdown and payload is not None:
            base_worker._emit_payload(payload)
        try:
            if usd_context is not None:
                usd_context.close_stage()
        finally:
            if sim_app is not None:
                sim_app.close()


def main() -> int:
    request_text = sys.stdin.read()
    try:
        request = json.loads(request_text)
    except Exception as exc:
        base_worker._emit_payload(base_worker._error_payload(None, exc))
        return 0
    _dispatch(request, emit_before_shutdown=True)
    return 0


def serve() -> int:
    sim_app = None
    usd_context = None
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                request = json.loads(line)
            except Exception as exc:
                base_worker._emit_payload(base_worker._error_payload(None, exc))
                continue

            if request.get("operation") == "__shutdown__":
                base_worker._emit_payload({
                    "ok": True,
                    "operation": "__shutdown__",
                    "backend": "isaacsim",
                })
                break

            try:
                if sim_app is None or usd_context is None:
                    sim_app, usd_context = base_worker._start_isaac(request)
                payload = _dispatch_with_runtime(
                    request,
                    sim_app=sim_app,
                    usd_context=usd_context,
                )
            except Exception as exc:
                payload = base_worker._error_payload(request.get("operation"), exc)
            base_worker._emit_payload(payload)
    except Exception as exc:
        base_worker._emit_payload(base_worker._error_payload(None, exc))
        return 0
    finally:
        try:
            if usd_context is not None:
                usd_context.close_stage()
        finally:
            if sim_app is not None:
                sim_app.close()
    return 0


if __name__ == "__main__":
    if "--serve" in sys.argv:
        raise SystemExit(serve())
    raise SystemExit(main())
