"""
Isaac Sim worker for scene_synthesis physics tools.
This script is launched by `isaac_bridge.py` with the SimKit Python environment.
It intentionally does not import `scene_layout_react`.
Request JSON is read from stdin and one response JSON object is written to stdout.
"""
from __future__ import annotations
import json
import re
import shutil
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

def _is_scene_authored_transform_op(op) -> bool:
    return not op.GetOpName().endswith(":unitsResolve")


def _remove_scene_authored_transform_ops(xformable) -> None:
    preserved_ops = [
        op
        for op in xformable.GetOrderedXformOps()
        if not _is_scene_authored_transform_op(op)
    ]
    for op in xformable.GetOrderedXformOps():
        if _is_scene_authored_transform_op(op):
            xformable.GetPrim().RemoveProperty(op.GetOpName())
    xformable.SetXformOpOrder(preserved_ops)


def _set_transform(
    prim,
    position: list | tuple = None,
    rotation_deg: float = None,
    scale: float = None
) -> None:
    from pxr import Gf, UsdGeom

    xformable = UsdGeom.Xformable(prim)
    _remove_scene_authored_transform_ops(xformable)

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


def _get_stage_unit_info(stage, default: float = 1.0) -> Dict[str, Any]:
    from pxr import UsdGeom

    authored = False
    if hasattr(UsdGeom, "StageHasAuthoredMetersPerUnit"):
        authored = bool(UsdGeom.StageHasAuthoredMetersPerUnit(stage))

    try:
        meters_per_unit = float(UsdGeom.GetStageMetersPerUnit(stage))
    except Exception:
        meters_per_unit = default

    if meters_per_unit <= 0:
        meters_per_unit = default

    return {
        "meters_per_unit": meters_per_unit,
        "authored": authored,
    }



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


def _save_stage(stage, stage_path: Path) -> None:
    try:
        exported = stage.GetRootLayer().Export(str(stage_path))
        if exported is False:
            raise RuntimeError(f"failed to export stage to {stage_path}")
    except Exception as exc:
        raise RuntimeError(f"failed to save stage to {stage_path}: {exc}") from exc


def _add_reference(stage, prim_path, usd_path: str, usd_context=None):
    if usd_context is not None:
        from isaacsim.core.utils.stage import add_reference_to_stage

        return add_reference_to_stage(
            usd_path=str(usd_path),
            prim_path=str(prim_path),
            prim_type="Xform",
        )

    from pxr import Sdf

    prim = stage.GetPrimAtPath(prim_path)
    prim.GetReferences().AddReference(Sdf.Reference(str(usd_path)))
    return prim


def _build_stage(
    request: Dict[str, Any],
    *,
    sim_app=None,
    usd_context=None,
) -> Tuple[str, Dict[str, str]]:
    from pxr import UsdGeom

    temp_dir = Path(request.get("temp_dir") or tempfile.gettempdir())
    temp_dir.mkdir(parents=True, exist_ok=True)
    stage_path = temp_dir / f"scene_synthesis_{uuid.uuid4().hex}.usd"
    scene = request.get("scene", {})
    stage = _create_stage(stage_path, sim_app=sim_app, usd_context=usd_context)

    target_meters_per_unit = 1.0
    UsdGeom.SetStageMetersPerUnit(stage, target_meters_per_unit)
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
            _add_reference(
                stage,
                asset_path,
                str(usd_path),
                usd_context=usd_context,
            )

        prim_paths[instance_id] = prim_path

        

    _save_stage(stage, stage_path)
    return str(stage_path), prim_paths

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


def _open_stage_in_isaac(sim_app, context, stage_path: str):
    context.open_stage(stage_path)
    for _ in range(3):
        sim_app.update()
    stage = context.get_stage()
    if stage is None:
        raise RuntimeError(f"failed to open stage in Isaac: {stage_path}")
    return stage


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

def _bbox_center(bbox: Dict[str, List[float]]) -> List[float]:
    return [
        (bbox["min"][i] + bbox["max"][i]) / 2.0
        for i in range(3)
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

def _copy_bbox(bbox: Dict[str, List[float]]) -> Dict[str, List[float]]:
    return {
        "min": [float(value) for value in bbox["min"]],
        "max": [float(value) for value in bbox["max"]],
    }

def _translate_bbox(
    bbox: Dict[str, List[float]],
    move_vector: List[float],
) -> None:
    for axis in range(3):
        bbox["min"][axis] += move_vector[axis]
        bbox["max"][axis] += move_vector[axis]

def _collision_axis(
    overlaps: List[float],
    penetration_tolerance: float,
) -> int:
    candidates = [
        axis
        for axis, overlap in enumerate(overlaps)
        if overlap > penetration_tolerance
    ]
    if not candidates:
        return min(range(3), key=lambda axis: overlaps[axis])
    return min(candidates, key=lambda axis: overlaps[axis])

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

            if not _aabb_overlap(
                a_bbox["min"],
                a_bbox["max"],
                b_bbox["min"],
                b_bbox["max"],
            ):
                continue

            overlaps = _bbox_overlap_depth(a_bbox, b_bbox)
            if any(overlap <= penetration_tolerance for overlap in overlaps):
                continue

            axis = _collision_axis(overlaps, penetration_tolerance)
            collisions.append({
                "a": a_id,
                "b": b_id,
                "method": "isaac_world_bbox",
                "axis": axis_names[axis],
                "overlap": overlaps[axis],
                "overlap_depth": overlaps,
            })

    return collisions

def _support_children(scene: Dict[str, Any]) -> Dict[str, List[str]]:
    raw = scene.get("support_children", {}) or {}
    if not isinstance(raw, dict):
        return {}
    return raw

def _collision_move_weights(
    a_id: str,
    b_id: str,
    scene: Dict[str, Any],
) -> Tuple[float, float]:
    support_children = _support_children(scene)

    if b_id in (support_children.get(a_id, []) or []):
        return 0.0, 1.0
    if a_id in (support_children.get(b_id, []) or []):
        return 1.0, 0.0

    def weight(instance_id: str) -> float:
        children = support_children.get(instance_id, []) or []
        if children:
            return 0.25
        return 1.0

    return weight(a_id), weight(b_id)

def _bboxes_collide(
    a_bbox: Dict[str, List[float]],
    b_bbox: Dict[str, List[float]],
    *,
    penetration_tolerance: float = 1e-5,
) -> bool:
    if not _aabb_overlap(
        a_bbox["min"],
        a_bbox["max"],
        b_bbox["min"],
        b_bbox["max"],
    ):
        return False

    overlaps = _bbox_overlap_depth(a_bbox, b_bbox)
    return all(overlap > penetration_tolerance for overlap in overlaps)

def _translated_bbox_copy(
    bbox: Dict[str, List[float]],
    move_vector: List[float],
) -> Dict[str, List[float]]:
    translated = _copy_bbox(bbox)
    _translate_bbox(translated, move_vector)
    return translated

def _xy_margin_bbox(
    bbox: Dict[str, List[float]],
    margin: float,
) -> Dict[str, List[float]]:
    padded = _copy_bbox(bbox)
    if margin <= 0.0:
        return padded
    padded["min"][0] -= margin
    padded["min"][1] -= margin
    padded["max"][0] += margin
    padded["max"][1] += margin
    return padded

def _bbox_collides_any(
    candidate_bbox: Dict[str, List[float]],
    obstacle_bboxes: Iterable[Dict[str, List[float]]],
    *,
    margin: float = 0.0,
    penetration_tolerance: float = 1e-5,
) -> bool:
    test_bbox = _xy_margin_bbox(candidate_bbox, margin)
    return any(
        _bboxes_collide(
            test_bbox,
            obstacle_bbox,
            penetration_tolerance=penetration_tolerance,
        )
        for obstacle_bbox in obstacle_bboxes
    )

def _bbox_xy_area(bbox: Dict[str, List[float]]) -> float:
    size = _bbox_size(bbox)
    return max(0.0, size[0]) * max(0.0, size[1])

def _collision_degrees(collisions: List[Dict[str, Any]]) -> Dict[str, int]:
    degrees: Dict[str, int] = {}
    for collision in collisions:
        a_id = collision.get("a")
        b_id = collision.get("b")
        if isinstance(a_id, str):
            degrees[a_id] = degrees.get(a_id, 0) + 1
        if isinstance(b_id, str):
            degrees[b_id] = degrees.get(b_id, 0) + 1
    return degrees

def _collision_components(
    ids: List[str],
    collisions: List[Dict[str, Any]],
) -> List[List[str]]:
    id_set = set(ids)
    graph: Dict[str, set[str]] = {instance_id: set() for instance_id in ids}

    for collision in collisions:
        a_id = collision.get("a")
        b_id = collision.get("b")
        if not isinstance(a_id, str) or not isinstance(b_id, str):
            continue
        if a_id not in id_set or b_id not in id_set:
            continue
        graph[a_id].add(b_id)
        graph[b_id].add(a_id)

    components: List[List[str]] = []
    seen: set[str] = set()
    for instance_id in ids:
        if instance_id in seen or not graph[instance_id]:
            continue

        component: List[str] = []
        stack = [instance_id]
        seen.add(instance_id)
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in sorted(graph[current], reverse=True):
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        if len(component) > 1:
            components.append(component)

    return components

def _candidate_xy_offsets(
    step_x: float,
    step_y: float,
    max_rings: int,
) -> Iterable[Tuple[float, float]]:
    yield 0.0, 0.0

    for ring in range(1, max_rings + 1):
        cells: List[Tuple[int, int]] = []
        for ix in range(-ring, ring + 1):
            for iy in range(-ring, ring + 1):
                if max(abs(ix), abs(iy)) == ring:
                    cells.append((ix, iy))

        cells.sort(
            key=lambda cell: (
                (cell[0] * step_x) ** 2 + (cell[1] * step_y) ** 2,
                abs(cell[0]) + abs(cell[1]),
                cell[0],
                cell[1],
            )
        )

        for ix, iy in cells:
            yield float(ix) * step_x, float(iy) * step_y

def _find_non_colliding_xy_candidate(
    base_bbox: Dict[str, List[float]],
    obstacle_bboxes: Iterable[Dict[str, List[float]]],
    *,
    margin: float,
    max_rings: int,
    penetration_tolerance: float,
) -> Tuple[Dict[str, List[float]], List[float]] | None:
    obstacles = list(obstacle_bboxes)
    size = _bbox_size(base_bbox)
    step_x = max(size[0] + margin, margin * 2.0, 0.1)
    step_y = max(size[1] + margin, margin * 2.0, 0.1)

    for dx, dy in _candidate_xy_offsets(step_x, step_y, max_rings):
        move_vector = [dx, dy, 0.0]
        candidate = _translated_bbox_copy(base_bbox, move_vector)
        if not _bbox_collides_any(
            candidate,
            obstacles,
            margin=margin,
            penetration_tolerance=penetration_tolerance,
        ):
            return candidate, move_vector

    return None

def _component_pack_order(
    component_ids: List[str],
    working_bboxes: Dict[str, Dict[str, List[float]]],
    scene: Dict[str, Any],
    collisions: List[Dict[str, Any]],
) -> List[str]:
    support_children = _support_children(scene)
    degrees = _collision_degrees(collisions)

    return sorted(
        component_ids,
        key=lambda instance_id: (
            -len(support_children.get(instance_id, []) or []),
            -_bbox_xy_area(working_bboxes[instance_id]),
            -degrees.get(instance_id, 0),
            instance_id,
        ),
    )

def _pack_collision_component(
    scene: Dict[str, Any],
    component_ids: List[str],
    working_bboxes: Dict[str, Dict[str, List[float]]],
    offsets: Dict[str, List[float]],
    all_ids: List[str],
    collisions: List[Dict[str, Any]],
    *,
    margin: float,
    max_rings: int,
    penetration_tolerance: float,
) -> Dict[str, Any]:
    component_set = set(component_ids)
    placed: set[str] = set()
    failed: List[str] = []
    ordered_ids = _component_pack_order(
        component_ids,
        working_bboxes,
        scene,
        collisions,
    )

    for instance_id in ordered_ids:
        if instance_id not in working_bboxes:
            continue

        base_bbox = _copy_bbox(working_bboxes[instance_id])
        obstacle_ids = [
            other_id
            for other_id in all_ids
            if other_id != instance_id
            and other_id in working_bboxes
            and (other_id not in component_set or other_id in placed)
        ]
        candidate = _find_non_colliding_xy_candidate(
            base_bbox,
            [working_bboxes[other_id] for other_id in obstacle_ids],
            margin=margin,
            max_rings=max_rings,
            penetration_tolerance=penetration_tolerance,
        )

        if candidate is None:
            failed.append(instance_id)
            placed.add(instance_id)
            continue

        candidate_bbox, move_vector = candidate
        working_bboxes[instance_id] = candidate_bbox
        for axis in range(3):
            offsets[instance_id][axis] += move_vector[axis]
        placed.add(instance_id)

    return {
        "component": component_ids,
        "ordered": ordered_ids,
        "failed": failed,
    }

def _scene_bounds(
    bboxes: Iterable[Dict[str, List[float]]],
) -> Tuple[List[float], List[float]]:
    bbox_list = list(bboxes)
    if not bbox_list:
        return [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]

    return (
        [
            min(bbox["min"][axis] for bbox in bbox_list)
            for axis in range(3)
        ],
        [
            max(bbox["max"][axis] for bbox in bbox_list)
            for axis in range(3)
        ],
    )

def _emergency_pack_unresolved(
    working_bboxes: Dict[str, Dict[str, List[float]]],
    offsets: Dict[str, List[float]],
    move_ids: List[str],
    *,
    margin: float,
) -> Dict[str, Any]:
    move_set = {
        instance_id
        for instance_id in move_ids
        if instance_id in working_bboxes
    }
    if not move_set:
        return {"moved": [], "reason": "no movable unresolved instances"}

    static_bboxes = [
        bbox
        for instance_id, bbox in working_bboxes.items()
        if instance_id not in move_set
    ]
    bounds_source = static_bboxes or list(working_bboxes.values())
    scene_min, scene_max = _scene_bounds(bounds_source)
    anchor_y = (scene_min[1] + scene_max[1]) / 2.0
    cursor_x = scene_max[0] + max(margin, 0.1)
    moved: List[str] = []
    ordered_ids = sorted(
        move_set,
        key=lambda instance_id: (
            -_bbox_xy_area(working_bboxes[instance_id]),
            instance_id,
        ),
    )

    for instance_id in ordered_ids:
        base_bbox = _copy_bbox(working_bboxes[instance_id])
        base_center = _bbox_center(base_bbox)
        cursor_x += margin
        target_min_x = cursor_x
        move_vector = [
            target_min_x - base_bbox["min"][0],
            anchor_y - base_center[1],
            0.0,
        ]
        candidate_bbox = _translated_bbox_copy(base_bbox, move_vector)

        working_bboxes[instance_id] = candidate_bbox
        for axis in range(3):
            offsets[instance_id][axis] += move_vector[axis]
        cursor_x = candidate_bbox["max"][0] + margin
        moved.append(instance_id)

    return {
        "moved": moved,
        "reason": "packed unresolved instances outside the occupied scene bounds",
    }

def _resolve_collision_free_layout(
    scene: Dict[str, Any],
    bboxes: Dict[str, Dict[str, List[float]]],
    ids: List[str],
    collisions: List[Dict[str, Any]],
    *,
    margin: float,
    max_rings: int,
    penetration_tolerance: float,
) -> Dict[str, Any]:
    working_bboxes = {
        instance_id: _copy_bbox(bboxes[instance_id])
        for instance_id in ids
        if instance_id in bboxes
    }
    offsets = {
        instance_id: [0.0, 0.0, 0.0]
        for instance_id in working_bboxes
    }
    components = _collision_components(ids, collisions)
    component_stats: List[Dict[str, Any]] = []

    for component_ids in components:
        component_stats.append(
            _pack_collision_component(
                scene,
                component_ids,
                working_bboxes,
                offsets,
                ids,
                collisions,
                margin=margin,
                max_rings=max_rings,
                penetration_tolerance=penetration_tolerance,
            )
        )

    unresolved = _collision_details(
        ids,
        working_bboxes,
        penetration_tolerance=penetration_tolerance,
    )
    emergency = None
    if unresolved:
        original_collision_ids = {
            instance_id
            for collision in collisions
            for instance_id in (collision.get("a"), collision.get("b"))
            if isinstance(instance_id, str)
        }
        unresolved_ids = {
            instance_id
            for collision in unresolved
            for instance_id in (collision.get("a"), collision.get("b"))
            if isinstance(instance_id, str)
        }
        emergency_ids = sorted(unresolved_ids & original_collision_ids)
        if not emergency_ids:
            emergency_ids = sorted(unresolved_ids)

        emergency = _emergency_pack_unresolved(
            working_bboxes,
            offsets,
            emergency_ids,
            margin=margin,
        )
        unresolved = _collision_details(
            ids,
            working_bboxes,
            penetration_tolerance=penetration_tolerance,
        )

    return {
        "working_bboxes": working_bboxes,
        "offsets": offsets,
        "components": components,
        "component_stats": component_stats,
        "unresolved": unresolved,
        "emergency": emergency,
        "iterations": len(components) + (1 if emergency else 0),
    }

def _suggest_collision_moves(
    scene: Dict[str, Any],
    bboxes: Dict[str, Dict[str, List[float]]],
    ids: List[str],
    collisions: List[Dict[str, Any]],
    *,
    margin: float = 0.05,
    max_iterations: int = 12,
    penetration_tolerance: float = 1e-5,
) -> Dict[str, Any] | None:
    if not collisions:
        return None

    axis_names = ["x", "y", "z"]
    instances = _instances(scene)
    layout = _resolve_collision_free_layout(
        scene,
        bboxes,
        ids,
        collisions,
        margin=margin,
        max_rings=max(max_iterations, 12),
        penetration_tolerance=penetration_tolerance,
    )
    working_bboxes = layout["working_bboxes"]
    offsets = layout["offsets"]
    unresolved = layout["unresolved"]

    collision_refs: Dict[str, List[Dict[str, str]]] = {
        instance_id: []
        for instance_id in working_bboxes
    }
    for collision in collisions:
        ref = {"a": collision["a"], "b": collision["b"]}
        collision_refs.setdefault(collision["a"], []).append(ref)
        collision_refs.setdefault(collision["b"], []).append(ref)

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
            "new_position": new_position,
            "collisions": collision_refs.get(instance_id, []),
        })

    if not moves:
        return {
            "instance_id": None,
            "move_vector": [0.0, 0.0, 0.0],
            "new_position": None,
            "moves": [],
            "final_positions": final_positions,
            "unresolved_collisions": unresolved,
            "resolved_collision_free": not unresolved,
            "iterations": layout["iterations"],
            "margin": margin,
            "method": "component_packing",
            "components": layout["components"],
            "component_stats": layout["component_stats"],
            "emergency_pack": layout["emergency"],
            "reason": "collisions were detected, but no movable AABB separation was found",
        }

    primary_move = max(
        moves,
        key=lambda item: sum(abs(value) for value in item["move_vector"]),
    )

    return {
        "instance_id": primary_move["instance_id"],
        "final_position": primary_move["final_position"],
        "axis": axis_names[
            max(
                range(3),
                key=lambda axis: abs(primary_move["move_vector"][axis]),
            )
        ],
        "move_vector": primary_move["move_vector"],
        "new_position": primary_move["new_position"],
        "primary_move": primary_move,
        "moves": moves,
        "final_positions": final_positions,
        "unresolved_collisions": unresolved,
        "resolved_collision_free": not unresolved,
        "iterations": layout["iterations"],
        "margin": margin,
        "method": "component_packing",
        "components": layout["components"],
        "component_stats": layout["component_stats"],
        "emergency_pack": layout["emergency"],
        "reason": (
            "pack connected collision components in XY, then verify all checked "
            "world AABBs are collision-free"
        ),
    }

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

    if suggested_move:
        move_by_id = {
            move["instance_id"]: move
            for move in suggested_move.get("moves", [])
        }
        for collision in collisions:
            pair_moves = [
                move_by_id[instance_id]
                for instance_id in (collision["a"], collision["b"])
                if instance_id in move_by_id
            ]
            collision["suggested_moves"] = pair_moves
            collision["suggested_move"] = pair_moves[0] if pair_moves else None

    return collisions, suggested_move

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
    move_vector = [0.0, 0.0, 0.0]

    if abs(z_gap) > z_tolerance:
        move_vector[2] = z_gap

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

    return {
        "instance_id": child_id,
        "parent_id": parent_id,
        "move_vector": move_vector,
        "new_position": new_position,
        "z_delta": move_vector[2],
        "xy_delta": [move_vector[0], move_vector[1]],
        "reason": (
            "move child so its bottom rests on parent top and its XY footprint "
            "is inside the parent support area"
        ),
        "z_tolerance": z_tolerance,
        "overlap_threshold": overlap_threshold,
    }

def _check_support(
    child_id: str,
    parent_id: str,
    bboxes: Dict[str, Dict[str, List[float]]],
    scene: Dict[str, Any],
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

    suggested_move = None

    if issues:
        suggested_move = _suggest_support_move(
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child,
            parent_bbox=parent,
            scene=scene,
            z_tolerance=z_tolerance,
            overlap_threshold=overlap_threshold
        )

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
        "suggested_move": suggested_move,
    }


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
    operation = request.get("operation")
    scene = request.get("scene", {})
    options = request.get("options", {}) or {}
    sim_app = None
    usd_context = None
    warnings: List[str] = []
    payload: Dict[str, Any] | None = None
    stage_path: str | None = None

    try:
        sim_app, usd_context = _start_isaac(request)
        stage_path, prim_paths = _build_stage(
            request,
            sim_app=sim_app,
            usd_context=usd_context,
        )

        if operation == "save_scene_usd":
            output_path = Path(options["output_path"]).expanduser()
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if output_path.exists():
                output_path.unlink()

            shutil.copy2(stage_path, output_path)

            payload = {
                "ok": True,
                "save": True,
                "operation": operation,
                "operations": operation,
                "backend": "isaacsim",
                "usd_path": str(output_path),
                "temp_stage_path": (
                    stage_path
                    if bool(options.get("keep_temp_stage"))
                    else None
                ),
                "instance_count": len(_instances(scene)),
                "exported_count": len(prim_paths),
                "prim_paths": {
                    instance_id: str(prim_path)
                    for instance_id, prim_path in prim_paths.items()
                },
                "warnings": warnings,
                "stage_path": stage_path,
            }
            return payload

        stage = _open_stage_in_isaac(sim_app, usd_context, stage_path)
        warnings.extend(_apply_instance_physics(stage, request, prim_paths))

        for _ in range(3):
            sim_app.update()

        bboxes = _collect_bboxes(stage, scene, prim_paths)

        if operation == "check_collision":
            pair = options.get("pair")
            collisions, suggested_move = _collision_pairs(scene, bboxes, pair=pair)
            payload = {
                "ok": True,
                "operation": operation,
                "backend": "isaacsim",
                "collision_free": len(collisions) == 0,
                "collisions": collisions,
                "suggested_move": suggested_move,
                "suggested_moves": (
                    suggested_move.get("moves", [])
                    if suggested_move
                    else []
                ),
                "suggested_final_positions": (
                    suggested_move.get("final_positions", {})
                    if suggested_move
                    else {}
                ),
                "warnings": warnings,
                "stage_path": stage_path,
            }
            return payload

        if operation == "check_support":
            child_id = options["child_id"]
            parent_id = options["parent_id"]
            support = _check_support(child_id, parent_id, bboxes, scene=scene)
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
                        support = _check_support(child_id, parent_id, bboxes,scene=scene)
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
        #save usd if needed for debugging
        keep_stage = bool(request.get("keep_stage"))
        if not keep_stage:
            _cleanup_stage_file(stage_path)


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
