"""
Isaac Sim worker for scene_synthesis physics tools.
This script is launched by `isaac_bridge.py` with the SimKit Python environment.
It intentionally does not import `scene_layout_react`.
Request JSON is read from stdin and one response JSON object is written to stdout.
"""
from __future__ import annotations
import json
import re
import sys
import tempfile
import traceback
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def _safe_name(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9-_]+", "_", value.strip()).strip("_")
    return safe or "instance"


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


def _aabb_overlap(
    a_min: List[float],
    a_max: List[float],
    b_min: List[float],
    b_max: List[float],
    tol: float = 1e-4,
) -> bool:
    for axis in range(3):
        if a_max[axis] < b_min[axis] - tol:
            return False
        if b_max[axis] < a_min[axis] - tol:
            return False
    return True


def xy_overlap_area(
    a_min: List[float],
    a_max: List[float],
    b_min: List[float],
    b_max: List[float],
) -> float:
    dx = max(0.0, min(a_max[0], b_max[0]) - max(a_min[0], b_min[0]))
    dy = max(0.0, min(a_max[1], b_max[1]) - max(a_min[1], b_min[1]))
    return dx * dy


def _set_transform(
    prim, position: Iterable[float], rotation_deg: float = None
) -> None:
    from pxr import Gf, UsdGeom
    
    xformable = UsdGeom.Xformable(prim)
    xformable.ClearXformOpOrder()
    xformable.AddTranslateOp().Set(Gf.Vec3d(*(float(v) for v in position)))
    if rotation_deg is not None:
        xformable.AddRotateZOp().Set(float(rotation_deg))


def _world_bbox(stage, prim_path: str) -> Tuple[List[float], List[float]]:
    from pxr import Usd, UsdGeom

    prim = stage.GetPrimAtPath(prim_path)
    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_, UsdGeom.Tokens.render, UsdGeom.Tokens.proxy],
        useExtentsHint=True,
    )
    bbox = bbox_cache.ComputeWorldBound(prim).ComputeAlignedRange()
    if bbox.IsEmpty():
        raise RuntimeError(f"empty bbox for {prim_path}")
    min_pt = bbox.GetMin()
    max_pt = bbox.GetMax()
    return (
        [float(min_pt[0]), float(min_pt[1]), float(min_pt[2])],
        [float(max_pt[0]), float(max_pt[1]), float(max_pt[2])],
    )


def _fallback_bbox(inst: Dict[str, Any]) -> Tuple[List[float], List[float]]:
    position = [float(v) for v in inst.get("position", [0.0, 0.0, 0.0])]
    size = [float(v) for v in inst.get("bbox_size", [1.0, 1.0, 1.0])]
    half = [v / 2.0 for v in size]
    return (
        [position[i] - half[i] for i in range(3)],
        [position[i] + half[i] for i in range(3)],
    )


def _build_stage(request: Dict[str, Any]) -> Tuple[str, Dict[str, str]]:
    from pxr import Sdf, Usd, UsdGeom
    
    temp_dir = Path(request.get("temp_dir") or tempfile.gettempdir())
    temp_dir.mkdir(parents=True, exist_ok=True)
    stage_path = temp_dir / f"scene_synthesis_{uuid.uuid4().hex}.usd"

    scene = request.get("scene", {})
    stage = Usd.Stage.CreateNew(str(stage_path))
    UsdGeom.SetStageMetersPerUnit(stage, 1.0)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.Z)
    world = UsdGeom.Xform.Define(stage, "/World")
    stage.SetDefaultPrim(world.GetPrim())
    instances_root = UsdGeom.Xform.Define(stage, "/World/Instances")

    prim_paths: Dict[str, str] = {}
    used_names: set[str] = set()

    for instance_id, inst in _instances(scene).items():
        base_name = _safe_name(instance_id)
        suffix = 1
        while name in used_names:
            suffix += 1
            name = f"{base_name}_{suffix}"
        used_names.add(name)

        prim_path = instances_root.GetPath().AppendChild(name)
        prim = stage.DefinePrim(prim_path, "Xform")
        usd_path = inst.get("usd_path")
        if usd_path:
            prim.GetReferences().AddReference(str(usd_path))

        _set_transform(
            prim,
            inst.get("position", [0.0, 0.0, 0.0]),
            inst.get("rotation_deg", 0.0),
        )
        prim_paths[instance_id] = prim_path

    stage.GetRootLayer().Save()
    return str(stage_path), prim_paths


def _start_isaac(request: Dict[str, Any]):
    simulation_config = dict(request.get("simulation_config") or {"headless": True})
    simulation_config.setdefault("headless", True)
    from isaacsim import SimulationApp

    sim_app = SimulationApp(simulation_config)
    
    import omni.usd
    context = omni.usd.get_context()
    return sim_app, context


def _open_stage_in_isaac(sim_app, context, stage_path: str):
    context.open_stage(stage_path)
    for _ in range(3):
        sim_app.update()
    stage = context.get_stage()
    if stage_path is None:
        raise RuntimeError(f"failed to open stage in Isaac: {stage_path}")
    return stage, context.get_stage()


def _apply_instance_physics(
    stage, request: Dict[str, Any], prim_paths: Dict[str, str]
) -> List[str]:
    warnings: List[str] = []
    scene = request.get("scene", {})
    #approximation = request.get("collision_approximation", "convexhull")
    approximation = request.get("collision_approximation") or "convexhull"
    support_children = request.get("support_children", {}) or {}
    parent_ids = set(support_children.keys())

    for instance_id, prim_path in prim_paths.items():
        prim = stage.GetPrimAtPath(prim_path)
        if not prim or not prim.IsValid():
            warnings.append(f"invalid prim for {instance_id} ({prim_path})")
            continue
        try:
            _apply_rigid_body_and_colliders(
                prim,
                kinematic=instance_id in parent_ids,
                approximation_shape=approximation,
            )
        except Exception as exc:
            warnings.append(f"physics authoring failed for {instance_id}: {exc}")
    return warnings


def _supported_approximation(requested: str | None) -> str:
    value = (requested or "convexhull").strip()
    mapping = {
        "convexhull": "convexhull",
        "convexdecomposition": "convexdecomposition",
        "meshsimplification": "meshsimplification",
        "convexmeshsimplification": "convexmeshsimplification",
        "boundingcube": "boundingcube",
        "boundingsphere": "boundingsphere",
        "spherefill": "spherefill",
        "sdf": "sdf",
        "none": "none",
    }
    return mapping.get(value.lower(), "convexhull")


def _try_import_physx_schema():
    try:
        from pxr import PhysxSchema

        return PhysxSchema
    except Exception:
        return None


def _apply_collision_api(prim, approximation_shape: str) -> None:
    from pxr import UsdGeom, UsdPhysics

    collision_api = UsdPhysics.CollisionAPI.Apply(prim)
    collision_api.CreateCollisionEnabledAttr(True)

    physx_schema = _try_import_physx_schema()
    if physx_schema is not None:
        physx_schema.PhysxCollisionAPI.Apply(prim)

    if prim.IsA(UsdGeom.Mesh) or prim.IsInstanceable():
        approximation = _supported_approximation(approximation_shape)
        mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(prim)
        mesh_collision_api.CreateApproximationAttr().Set(approximation)

        if physx_schema is None:
            return

        physx_mesh_api = {
            "none": physx_schema.PhysxTriangleMeshCollisionAPI,
            "convexhull": physx_schema.PhysxConvexHullCollisionAPI,
            "convexdecomposition": physx_schema.PhysxConvexDecompositionCollisionAPI,
            "meshsimplification": physx_schema.PhysxTriangleMeshSimplificationCollisionAPI,
            "convexmeshsimplification": physx_schema.PhysxTriangleMeshSimplificationCollisionAPI,
            "spherefill": physx_schema.PhysxSphereFillCollisionAPI,
            "sdf": physx_schema.PhysxSDFCollisionAPI,
        }.get(approximation)
        if physx_mesh_api is not None:
            physx_mesh_api.Apply(prim)


def _iter_prim_hierarchy(root) -> Iterable[Any]:
    stack = [root]
    while stack:
        current = stack.pop()
        if not current or not current.IsValid():
            continue
        yield current
        for child in reversed(current.GetChildren()):
            stack.append(child)

def _apply_rigid_body_and_colliders(
    prim, *, kinematic: bool, approximation_shape: str
) -> None:
    from pxr import UsdPhysics

    rigid_api = UsdPhysics.RigidBodyAPI.Apply(prim)
    rigid_api.CreateRigidBodyEnabledAttr(True)
    rigid_api.CreateKinematicEnabledAttr(bool(kinematic))

    physx_schema = _try_import_physx_schema()
    if physx_schema is not None:
        physx_rigid_api = physx_schema.PhysxRigidBodyAPI.Apply(prim)
        physx_rigid_api.CreateEnableCCDAttr(True)

    for member in _iter_prim_hierarchy(prim):
        if member.IsA(UsdGeom.Gprim) or member.IsInstanceable():
            _apply_collision_api(member, approximation_shape)


def _collect_bboxes(stage, scene: Dict[str, Any], prim_paths: Dict[str, str]
) -> Dict[str, Dict[str, List[float]]]:
    bboxes: Dict[str, Dict[str, List[float]]] = {}
    for instance_id, inst in _instance(scene).items():
        try:
            bbox_min, bbox_max = _world_bbox(stage, prim_paths[instance_id])
        except Exception:
            bbox_min, bbox_max = _fallback_bbox(inst)
        bboxes[instance_id] = {"min": bbox_min, "max": bbox_max}
    return bboxes


def _collision_pairs(
    scene: Dict[str, Any],
    bboxes: Dict[str, Dict[str, List[float]]],
    pair: List[str] | None = None,
) -> List[Dict[str, Any]]:
    ids = list(_instances(scene).keys())
    if pair:
        ids = [item for item in pair if item in bboxes]
    collisions: List[Dict[str, Any]] = []
    for idx, a_id in enumerate(ids):
        for b_id in ids[idx + 1 :]:
            a = bboxes[a_id]
            b = bboxes[b_id]
            if not _aabb_overlap(a["min"], a["max"], b["min"], b["max"]):
                continue
            collisions.append({"a": a_id, "b": b_id, "method": "isaac_world_bbox"})
    return collisions


def _check_support(
    child_id: str,
    parent_id: str,
    bboxes: Dict[str, Dict[str, List[float]]],
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
) -> Dict[str, Any]:
    child = bboxes[child_id]
    parent = bboxes[parent_id]
    c_min = child["min"]
    c_max = child["max"]
    p_min = parent["min"]
    p_max = parent["max"]

    z_gap = p_max[2] - c_min[2]
    child_area = max(1e-9, (c_max[0] - c_min[0]) * (c_max[1] - c_min[1]))
    xy_overlap = xy_overlap_area(c_min, c_max, p_min, p_max)
    coverage = xy_overlap / child_area
    issues: List[str] = []

    if abs(z_gap) > z_tolerance:
        issues.append(f"z_gap={z_gap:.3f} outside tolerance {z_tolerance:.3f}")
    if coverage < overlap_threshold:
        issues.append(f"xy_coverage={coverage:.3f} below threshold {overlap_threshold:.3f}")

    supported = not issues
    return {
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


def _final_positions(stage, prim_paths: Dict[str, str]) -> Dict[str, List[float]]:
    from pxr import UsdGeom

    positions: Dict[str, List[float]] = {}
    for instance_id, prim_path in prim_paths.items():
        prim = stage.GetPrimAtPath(prim_path)
        matrix = UsdGeom.Xformable(prim).ComputeLocalToWorldTransform(
            Usd.TimeCode.Default()
        )
        translation = matrix.ExtractTranslation()
        positions[instance_id] = [
            float(translation[0]),
            float(translation[1]),
            float(translation[2]),
        ]
    return positions


def _run_world_steps(sim_app, duration: float, dt: float) -> None:
    try:
        from isaacsim.core.api import World

        world = World(stage_units_in_meters=1.0)
        world.play()
        steps = max(1, int(duration / max(dt, 1e-6)))
        for _ in range(steps):
            world.step(render=False)
        world.stop()
    except Exception:
        steps = max(1, int(duration / max(dt, 1e-6)))
        for _ in range(steps):
            sim_app.update()


def _emit_payload(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), flush=True)


def _error_payload(operation: Any, exc: Exception) -> Dict[str, Any]:
    return {
        "ok": False,
        "operation": operation,
        "backend": "isaacsim",
        "error": str(exc),
        "errors": [str(exc)],
        "traceback": traceback.format_exc(limit=20),
    }
    
def _dispatch(
    request: Dict[str, Any],
    *,
    emit_before_shutdown: bool = False,
) -> Dict[str, Any]:
    operation = request.get("operation")
    scene = request.get("scene", {})
    options = request.get("options", {}) or {}
    sim_app = None
    usd_context = None
    warnings: List[str] = []
    payload: Dict[str, Any] | None = None

    try:
        sim_app, usd_context = _start_isaac(request)
        stage_path, prim_paths = _build_stage(request)
        stage = _open_stage_in_isaac(sim_app, usd_context, stage_path)
        warnings.extend(_apply_instance_physics(stage, request, prim_paths))

        for _ in range(3):
            sim_app.update()

        bboxes = _collect_bboxes(stage, scene, prim_paths)

        if operation == "check_collision":
            pair = options.get("pair")
            collisions = _collision_pairs(scene, bboxes, pair=pair)
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "collision_free": len(collisions) == 0,
                "collisions": collisions,
                "warnings": warnings,
                "stage_path": stage_path,
            }
            return payload

        if operation == "check_support":
            child_id = options["child_id"]
            parent_id = options["parent_id"]
            support = _check_support(child_id, parent_id, bboxes)
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                **support,
                "warnings": warnings,
                "stage_path": stage_path,
            }
            return payload

        if operation == "simulate_step":
            duration = float(options.get("duration", 2.0))
            dt = float(options.get("dt", 1.0 / 60.0))
            initial_positons = _final_positions(stage, prim_paths)
            _run_world_steps(sim_app, duration, dt)
            for _ in range(3):
                sim_app.update()
            final_positions = _final_positions(stage, prim_paths)

            fallen_assets = [
            instance_id
            for instance_id, position in final_positions.items()
            if position[2] < initial_positons[instance_id][2] - 0.05
            ]

            contacts = []
            for parent_id, children in (scene.get("support_children", {}) or {}).items():
                for child_id in children:
                    if child_id in bboxes and parent_id in bboxes:
                        support = _check_support(child_id, parent_id, bboxes)
                        contacts.extend(support["contacts"])

            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "stable": len(fallen_assets) == 0,
                "fallen_assets": fallen_assets,
                "contacts": contacts,
                "final_positions": final_positions,
                "warnings": warnings,
                "stage_path": stage_path,
            }
            return payload

        payload = {
            "ok": False,
            "operation": operation,
            "backend": "isaacsim",
            "errors": [f"unknown operation: {operation}"],
            "warnings": warnings,
        }
        return payload

    except Exception as exc:
        # noqa: BLE001 - worker must return structured errors.
        payload = _error_payload(operation, exc)
        return payload
    finally:
        if emit_before_shutdown and payload is not None:
            _emit_payload(payload)
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
        # noqa: BLE001 - worker must return structured errors.
        _emit_payload(_error_payload(None, exc))
        return 0
    _dispatch(request, emit_before_shutdown=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
