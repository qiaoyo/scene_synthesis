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

try:
    from collision_checks import _collision_pairs
    from support_checks import _check_support
except ModuleNotFoundError:
    from .collision_checks import _collision_pairs
    from .support_checks import _check_support
# stage build
def _start_isaac(request: Dict[str, Any]):
    simulation_config = dict(request.get("simulation_config") or {"headless": True})
    simulation_config.setdefault("headless", True)
    from isaacsim import SimulationApp

    sim_app = SimulationApp(simulation_config)

    import omni.kit.app
    import omni.usd

    context = omni.usd.get_context()
    ext_manager = omni.kit.app.get_app().get_extension_manager()
    ext_manager.set_extension_enabled_immediate(
        "omni.usd.metrics.assembler.ui",
        True,
    )
    return sim_app, context

def _create_stage(stage_path: Path, sim_app=None, usd_context=None):
    from pxr import Usd, UsdGeom

    if usd_context is None:
        return Usd.Stage.CreateNew(str(stage_path))

    usd_context.new_stage()
    if sim_app is not None:
        for _ in range(3):
            sim_app.update()

    stage = usd_context.get_stage()
    if stage is None:
        raise RuntimeError("failed to create new Isaac stage")
    return stage

def _build_stage(
    request: Dict[str, Any],
    *,
    stage_path: Path | None = None,
    sim_app=None,
    usd_context=None,
) -> Tuple[str, Dict[str, str]]:
    from pxr import Sdf, UsdGeom

    if stage_path is None:
        temp_dir = Path(request.get("temp_dir") or tempfile.gettempdir())
        temp_dir.mkdir(parents=True, exist_ok=True)
        stage_path = temp_dir / f"scene_synthesis_{uuid.uuid4().hex}.usd"
    else:
        stage_path = Path(stage_path).expanduser()
        stage_path.parent.mkdir(parents=True, exist_ok=True)

    scene = request.get("scene", {})
    stage = _create_stage(stage_path, sim_app=sim_app, usd_context=usd_context)

    UsdGeom.SetStageMetersPerUnit(stage, 1.0)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

    world = UsdGeom.Xform.Define(stage, "/World")
    stage.SetDefaultPrim(world.GetPrim())

    instances_root = UsdGeom.Xform.Define(stage, "/World/Instances")

    prim_paths: Dict[str, str] = {}
    used_names: set[str] = set()

    for instance_id, inst in _instances(scene).items():
        base_name = _safe_name(instance_id)
        name = base_name
        suffix = 1
        while name in used_names:
            suffix += 1
            name = f"{base_name}_{suffix}"
        used_names.add(name)
        
        prim_path = instances_root.GetPath().AppendChild(name)
        prim = stage.DefinePrim(prim_path, "Xform")
        _set_transform(
            prim,
            inst.get("position", [0.0, 0.0, 0.0]),
            inst.get("rotation_deg", 0.0),
        )

        usd_path = inst.get("usd_path")
        if usd_path:
            asset_path = prim_path.AppendChild("Asset")
            stage.DefinePrim(asset_path, "Xform")

            if usd_context is not None:
                from isaacsim.core.utils.stage import add_reference_to_stage
                add_reference_to_stage(
                    usd_path=str(usd_path),
                    prim_path=str(asset_path),
                    prim_type="Xform",
                )
            else:
                ref_prim = stage.GetPrimAtPath(asset_path)
                ref_prim.GetReferences().AddReference(Sdf.Reference(str(usd_path)))

        prim_paths[instance_id] = prim_path
        
    try:
        exported = stage.GetRootLayer().Export(str(stage_path))
        if exported is False:
            raise RuntimeError(f"failed to export stage to {stage_path}")
    except Exception as exc:
        raise RuntimeError(f"failed to save stage to {stage_path}: {exc}") from exc
    return str(stage_path), prim_paths


def _open_stage_in_isaac(sim_app, context, stage_path: str):
    context.open_stage(stage_path)
    for _ in range(3):
        sim_app.update()
    stage = context.get_stage()
    if stage is None:
        raise RuntimeError(f"failed to open stage in Isaac: {stage_path}")
    return stage
#save usd
def _save_scene_usd(
    request: Dict[str, Any],
    *,
    sim_app=None,
    usd_context=None,
) -> Dict[str, Any]:
    options = request.get("options", {}) or {}
    scene = request.get("scene", {}) or {}
    output_path = Path(options["output_path"]).expanduser()
    include_physics = bool(options.get("include_physics", False))
    warnings: List[str] = []

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        output_path.unlink()

    stage_path, prim_paths = _build_stage(
        request,
        stage_path=output_path,
        sim_app=sim_app,
        usd_context=usd_context,
    )

    if include_physics:
        stage = _open_stage_in_isaac(sim_app, usd_context, stage_path)
        warnings.extend(_apply_instance_physics(stage, request, prim_paths))
        if sim_app is not None:
            for _ in range(3):
                sim_app.update()
        try:
            exported = stage.GetRootLayer().Export(str(output_path))
            if exported is False:
                raise RuntimeError(f"failed to export stage to {output_path}")
        except Exception as exc:
            raise RuntimeError(f"failed to save stage to {output_path}: {exc}") from exc

    return {
        "ok": True,
        "save": True,
        "operation": "save_scene_usd",
        "backend": "isaacsim",
        "usd_path": str(output_path),
        "include_physics": include_physics,
        "instance_count": len(_instances(scene)),
        "warnings": warnings,
    }

def _safe_name(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9-_]+", "_", value.strip()).strip("_")
    return safe or "instance"

def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}

def _set_transform(
    prim,
    position: list | tuple = None,
    rotation_deg: float = None,
    scale: float = None
) -> None:
    from pxr import Gf, UsdGeom

    xformable = UsdGeom.Xformable(prim)
    # 保留系统自带的 unitsResolve 变换，删除所有用户自定义变换
    preserved_ops = []
    for op in xformable.GetOrderedXformOps():
        if op.GetOpName().endswith(":unitsResolve"):
            preserved_ops.append(op)
        else:
            # 删除用户添加的 translate/rotate/scale 等
            xformable.GetPrim().RemoveProperty(op.GetOpName())

    # 重新设置保留的系统变换顺序
    xformable.SetXformOpOrder(preserved_ops)

    if position is not None:
        translate_op = xformable.AddTranslateOp(
            precision=UsdGeom.XformOp.PrecisionDouble
        )
        translate_op.Set(Gf.Vec3d(*(float(v) for v in position)))

    if rotation_deg is not None:
        rotate_op = xformable.AddRotateZOp(
            precision=UsdGeom.XformOp.PrecisionDouble
        )
        rotate_op.Set(float(rotation_deg))

    if scale is not None:
        scale_op = xformable.AddScaleOp(
            precision=UsdGeom.XformOp.PrecisionDouble
        )
        scale_op.Set(Gf.Vec3d(float(scale), float(scale), float(scale)))

# physics bridge

def _apply_instance_physics(
    stage, request: Dict[str, Any], prim_paths: Dict[str, str]
) -> List[str]:
    warnings: List[str] = []
    scene = request.get("scene", {}) or {}
    approximation = request.get("collision_approximation") or "convexhull"
    support_children = scene.get("support_children", {}) or {}
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

def _apply_rigid_body_and_colliders(
    prim, *, kinematic: bool, approximation_shape: str
) -> None:
    from pxr import UsdGeom, UsdPhysics

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

def _iter_prim_hierarchy(root) -> Iterable[Any]:
    stack = [root]
    while stack:
        current = stack.pop()
        if not current or not current.IsValid():
            continue
        yield current
        for child in reversed(current.GetChildren()):
            stack.append(child)

# collect bbox
def _collect_bboxes(stage, scene: Dict[str, Any], prim_paths: Dict[str, str]
) -> Dict[str, Dict[str, List[float]]]:
    bboxes: Dict[str, Dict[str, List[float]]] = {}
    for instance_id, inst in _instances(scene).items():
        try:
            bbox_min, bbox_max = _world_bbox(stage, prim_paths[instance_id])
        except Exception:
            bbox_min, bbox_max = _fallback_bbox(inst)
        bboxes[instance_id] = {"min": bbox_min, "max": bbox_max}
    return bboxes

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


#simulate_step
def _final_positions(stage, prim_paths: Dict[str, str]) -> Dict[str, List[float]]:
    from pxr import Usd, UsdGeom

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

def _cleanup_stage_file(stage_path: str | None) -> None:
    if not stage_path:
        return

    path = Path(stage_path)
    try:
        if path.exists():
            path.unlink()
    except Exception:
        # Cleanup failure should not change the tool result.
        pass

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
    sim_app = None
    usd_context = None
    payload: Dict[str, Any] | None = None

    try:
        sim_app, usd_context = _start_isaac(request)
        payload = _dispatch_with_runtime(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )
        return payload
    except Exception as exc:
        # noqa: BLE001 - worker must return structured errors.
        payload = _error_payload(request.get("operation"), exc)
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


def _dispatch_with_runtime(
    request: Dict[str, Any],
    *,
    sim_app=None,
    usd_context=None,
) -> Dict[str, Any]:
    operation = request.get("operation")
    scene = request.get("scene", {})
    options = request.get("options", {}) or {}
    warnings: List[str] = []
    stage_path: str | None = None

    try:
        if operation == "save_scene_usd":
            return _save_scene_usd(
                request,
                sim_app=sim_app,
                usd_context=usd_context,
            )

        stage_path, prim_paths = _build_stage(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )

        stage = _open_stage_in_isaac(sim_app, usd_context, stage_path)
        warnings.extend(_apply_instance_physics(stage, request, prim_paths))

        for _ in range(3):
            sim_app.update()

        bboxes = _collect_bboxes(stage, scene, prim_paths)

        if operation == "check_collision":
            pair = options.get("pair")
            include_suggestions = bool(options.get("include_suggestions", False))
            collisions, suggested_move = _collision_pairs(scene, bboxes, pair=pair, include_suggestions=include_suggestions)
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "collision_free": len(collisions) == 0,
                "collisions": collisions,
                "warnings": warnings,
                "stage_path": stage_path,
            }
            
            if include_suggestions:
                payload["suggested_final_positions"] = (
                    suggested_move.get("final_positions", {})
                    if suggested_move
                    else {}
                )
            return payload

        if operation == "check_support":
            child_id = options["child_id"]
            parent_id = options["parent_id"]
            include_suggestions = bool(options.get("include_suggestions", False))
            support = _check_support(child_id, parent_id, bboxes, scene=scene, include_suggestions=include_suggestions)
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "support": support,
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
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "stable": len(fallen_assets) == 0,
                "fallen_assets": fallen_assets,
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
        return _error_payload(operation, exc)
    finally:
        keep_stage = bool(request.get("keep_stage"))
        if operation != "save_scene_usd" and not keep_stage:
            _cleanup_stage_file(stage_path)
        if usd_context is not None:
            try:
                usd_context.close_stage()
            except Exception:
                pass


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
                _emit_payload(_error_payload(None, exc))
                continue

            if request.get("operation") == "__shutdown__":
                _emit_payload({
                    "ok": True,
                    "operation": "__shutdown__",
                    "backend": "isaacsim",
                })
                break

            try:
                if sim_app is None or usd_context is None:
                    sim_app, usd_context = _start_isaac(request)
                payload = _dispatch_with_runtime(
                    request,
                    sim_app=sim_app,
                    usd_context=usd_context,
                )
            except Exception as exc:
                payload = _error_payload(request.get("operation"), exc)
            _emit_payload(payload)
    except Exception as exc:
        _emit_payload(_error_payload(None, exc))
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
