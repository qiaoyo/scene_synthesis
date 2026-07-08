"""
Enhanced support checks for the optional Isaac Sim worker.

The legacy support check treats the parent as one world AABB and only validates
against the parent's top face. This module checks real parent surfaces first so
objects can be supported by inner shelf layers without accepting side contacts
as valid support.
"""
from __future__ import annotations

import math
from statistics import median
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from enhanced_suggestions import normalize_suggestion_payload, suggest_support_move
    from support_checks import _check_support, xy_overlap_area
except ModuleNotFoundError:
    from .enhanced_suggestions import normalize_suggestion_payload, suggest_support_move
    from .support_checks import _check_support, xy_overlap_area


BBox = Dict[str, List[float]]
Vec3 = List[float]


def _instances(scene: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    raw = scene.get("instances", {})
    if isinstance(raw, dict):
        return raw
    return {}


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


def _bbox_center(bbox: BBox) -> Vec3:
    return [
        (bbox["min"][axis] + bbox["max"][axis]) / 2.0
        for axis in range(3)
    ]


def _bbox_size(bbox: BBox) -> Vec3:
    return [
        bbox["max"][axis] - bbox["min"][axis]
        for axis in range(3)
    ]


def _bbox_with_offset(bbox: BBox, offset: Vec3) -> BBox:
    return {
        "min": [bbox["min"][axis] + offset[axis] for axis in range(3)],
        "max": [bbox["max"][axis] + offset[axis] for axis in range(3)],
    }


def _xy_coverage(child_bbox: BBox, surface_bbox: BBox) -> float:
    child_area = max(
        1e-9,
        (child_bbox["max"][0] - child_bbox["min"][0])
        * (child_bbox["max"][1] - child_bbox["min"][1]),
    )
    overlap = xy_overlap_area(
        child_bbox["min"],
        child_bbox["max"],
        surface_bbox["min"],
        surface_bbox["max"],
    )
    return min(1.0, overlap / child_area)


def _clamp(value: float, lower: float, upper: float) -> float:
    if lower > upper:
        return (lower + upper) / 2.0
    return max(lower, min(value, upper))


def _vector_to_list(value: Any, default: Iterable[float]) -> Vec3:
    try:
        return [float(value.x), float(value.y), float(value.z)]
    except Exception:
        pass
    try:
        return [float(value[0]), float(value[1]), float(value[2])]
    except Exception:
        return [float(item) for item in default]


def _hit_attr(hit: Any, *names: str, default: Any = None) -> Any:
    if isinstance(hit, dict):
        for name in names:
            if name in hit:
                return hit[name]
        return default
    for name in names:
        try:
            value = getattr(hit, name)
        except Exception:
            continue
        if value is not None:
            return value
    return default


def _hit_to_dict(
    hit: Any,
    prim_paths: Dict[str, str],
    *,
    probe_index: int,
    probe_origin: Vec3,
) -> Dict[str, Any]:
    collision = _hit_attr(hit, "collision", default="")
    rigid_body = _hit_attr(hit, "rigid_body", "rigidBody", default="")
    normal = _vector_to_list(
        _hit_attr(hit, "normal", default=None),
        [0.0, 0.0, 0.0],
    )
    position = _vector_to_list(
        _hit_attr(hit, "position", default=None),
        [probe_origin[0], probe_origin[1], probe_origin[2]],
    )
    distance = float(_hit_attr(hit, "distance", default=math.inf))
    path = collision or rigid_body
    return {
        "probe_index": probe_index,
        "probe_origin": probe_origin,
        "collision": str(collision),
        "rigid_body": str(rigid_body),
        "instance_id": _path_to_instance(path, prim_paths),
        "position": position,
        "normal": normal,
        "distance": distance,
    }


def _probe_points(child_bbox: BBox, *, grid_size: int = 3) -> List[Vec3]:
    c_min = child_bbox["min"]
    c_max = child_bbox["max"]
    if grid_size <= 1:
        center = _bbox_center(child_bbox)
        return [[center[0], center[1], c_min[2]]]

    # Avoid exact edges; edge probes are noisy on bevels and thin shelf lips.
    fractions = [0.15, 0.5, 0.85] if grid_size == 3 else [
        (index + 0.5) / grid_size for index in range(grid_size)
    ]
    return [
        [
            c_min[0] + (c_max[0] - c_min[0]) * fx,
            c_min[1] + (c_max[1] - c_min[1]) * fy,
            c_min[2],
        ]
        for fx in fractions
        for fy in fractions
    ]


def _valid_parent_surface_hit(
    hit: Dict[str, Any],
    *,
    parent_id: str,
    child_bottom_z: float,
    z_tolerance: float,
    normal_z_threshold: float,
) -> bool:
    if hit.get("instance_id") != parent_id:
        return False
    normal = hit.get("normal") or [0.0, 0.0, 0.0]
    position = hit.get("position") or [0.0, 0.0, 0.0]
    if float(normal[2]) < normal_z_threshold:
        return False
    return abs(float(position[2]) - child_bottom_z) <= z_tolerance


def _raycast_support(
    *,
    stage: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    z_tolerance: float,
    support_hit_ratio: float,
    normal_z_threshold: float,
    grid_size: int,
) -> Dict[str, Any]:
    del stage, scene

    from omni.physx import get_physx_scene_query_interface
    from pxr import Gf

    query = get_physx_scene_query_interface()
    probe_lift = max(0.005, min(0.02, z_tolerance * 0.5))
    ray_distance = z_tolerance + probe_lift + 0.03
    child_bottom_z = float(child_bbox["min"][2])
    probes = _probe_points(child_bbox, grid_size=grid_size)
    probe_hits: List[Dict[str, Any]] = []
    valid_hits: List[Dict[str, Any]] = []

    for index, point in enumerate(probes):
        origin = [point[0], point[1], child_bottom_z + probe_lift]
        raw_hits: List[Dict[str, Any]] = []

        def _report(hit: Any) -> bool:
            raw_hits.append(
                _hit_to_dict(
                    hit,
                    prim_paths,
                    probe_index=index,
                    probe_origin=origin,
                )
            )
            return True

        query.raycast_all(
            Gf.Vec3f(*origin),
            Gf.Vec3f(0.0, 0.0, -1.0),
            float(ray_distance),
            _report,
            True,
        )
        raw_hits.sort(key=lambda item: float(item.get("distance", math.inf)))
        parent_hits = [
            hit for hit in raw_hits if hit.get("instance_id") == parent_id
        ]
        best_valid = None
        for hit in parent_hits:
            if _valid_parent_surface_hit(
                hit,
                parent_id=parent_id,
                child_bottom_z=child_bottom_z,
                z_tolerance=z_tolerance,
                normal_z_threshold=normal_z_threshold,
            ):
                best_valid = hit
                break
        if best_valid is not None:
            valid_hits.append(best_valid)
        probe_hits.append({
            "probe_index": index,
            "origin": origin,
            "parent_hits": parent_hits[:3],
            "valid": best_valid is not None,
        })

    return _support_result_from_hits(
        child_id=child_id,
        parent_id=parent_id,
        child_bbox=child_bbox,
        probe_count=len(probes),
        valid_hits=valid_hits,
        probe_hits=probe_hits,
        z_tolerance=z_tolerance,
        support_hit_ratio=support_hit_ratio,
    )


def _support_result_from_hits(
    *,
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    probe_count: int,
    valid_hits: List[Dict[str, Any]],
    probe_hits: List[Dict[str, Any]],
    z_tolerance: float,
    support_hit_ratio: float,
) -> Dict[str, Any]:
    hit_ratio = len(valid_hits) / max(1, probe_count)
    required_hits = max(1, int(math.ceil(max(0.0, support_hit_ratio) * probe_count)))
    support_z = None
    z_gap = None
    if valid_hits:
        support_z = float(median(hit["position"][2] for hit in valid_hits))
        z_gap = support_z - float(child_bbox["min"][2])

    issues: List[str] = []
    if len(valid_hits) < required_hits:
        issues.append(
            "support_hit_ratio="
            f"{hit_ratio:.3f} below threshold {support_hit_ratio:.3f}"
        )
    if z_gap is None:
        issues.append("no upward parent support surface within probe distance")
    elif abs(z_gap) > z_tolerance:
        issues.append(f"z_gap={z_gap:.3f} outside tolerance {z_tolerance:.3f}")

    supported = not issues
    contacts = []
    if supported:
        contacts.append({
            "child": child_id,
            "parent": parent_id,
            "type": "support",
            "method": "physx_raycast_surface",
            "support_z": support_z,
            "hit_ratio": round(hit_ratio, 3),
        })

    return {
        "supported": supported,
        "child": child_id,
        "parent": parent_id,
        "support_backend": "physx_raycast_surface",
        "z_gap": 0.0 if z_gap is None else z_gap,
        "xy_coverage": round(hit_ratio, 3),
        "contacts": contacts,
        "issues": issues,
        "support_surfaces": [
            {
                "position": hit.get("position"),
                "normal": hit.get("normal"),
                "collision": hit.get("collision"),
            }
            for hit in valid_hits[:8]
        ],
        "probe_hits": probe_hits,
        "_valid_hits": valid_hits,
    }


def _mesh_vertices_world(stage: Any, prim: Any) -> Tuple[List[Vec3], List[int], List[int]]:
    from pxr import Usd, UsdGeom

    mesh = UsdGeom.Mesh(prim)
    points_attr = mesh.GetPointsAttr()
    counts_attr = mesh.GetFaceVertexCountsAttr()
    indices_attr = mesh.GetFaceVertexIndicesAttr()
    points = points_attr.Get() or []
    counts = counts_attr.Get() or []
    indices = indices_attr.Get() or []
    matrix = UsdGeom.Xformable(prim).ComputeLocalToWorldTransform(
        Usd.TimeCode.Default()
    )
    world_points: List[Vec3] = []
    for point in points:
        transformed = matrix.Transform(point)
        world_points.append([
            float(transformed[0]),
            float(transformed[1]),
            float(transformed[2]),
        ])
    return world_points, [int(v) for v in counts], [int(v) for v in indices]


def _normal_for_face(vertices: List[Vec3]) -> Vec3:
    if len(vertices) < 3:
        return [0.0, 0.0, 0.0]
    a, b, c = vertices[0], vertices[1], vertices[2]
    ab = [b[i] - a[i] for i in range(3)]
    ac = [c[i] - a[i] for i in range(3)]
    normal = [
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    ]
    length = math.sqrt(sum(value * value for value in normal))
    if length <= 1e-9:
        return [0.0, 0.0, 0.0]
    return [value / length for value in normal]


def _surface_bbox(vertices: List[Vec3]) -> BBox:
    return {
        "min": [
            min(vertex[axis] for vertex in vertices)
            for axis in range(3)
        ],
        "max": [
            max(vertex[axis] for vertex in vertices)
            for axis in range(3)
        ],
    }


def _collect_upward_mesh_surfaces(
    stage: Any,
    parent_root_path: str,
    *,
    normal_z_threshold: float,
    max_surfaces: int = 256,
) -> List[Dict[str, Any]]:
    from pxr import UsdGeom

    root = stage.GetPrimAtPath(parent_root_path)
    if not root or not root.IsValid():
        return []

    surfaces: List[Dict[str, Any]] = []
    stack = [root]
    while stack:
        prim = stack.pop()
        if not prim or not prim.IsValid():
            continue
        if prim.IsA(UsdGeom.Mesh):
            try:
                points, counts, indices = _mesh_vertices_world(stage, prim)
            except Exception:
                points, counts, indices = [], [], []
            cursor = 0
            for face_index, count in enumerate(counts):
                face_indices = indices[cursor:cursor + count]
                cursor += count
                if len(face_indices) < 3:
                    continue
                try:
                    vertices = [points[index] for index in face_indices]
                except Exception:
                    continue
                normal = _normal_for_face(vertices)
                if normal[2] < normal_z_threshold:
                    continue
                bbox = _surface_bbox(vertices)
                surface_z = sum(vertex[2] for vertex in vertices) / len(vertices)
                surfaces.append({
                    "surface_z": float(surface_z),
                    "normal": normal,
                    "bbox": bbox,
                    "mesh_path": str(prim.GetPath()),
                    "face_index": face_index,
                })
                if len(surfaces) >= max_surfaces:
                    return surfaces
        for child in reversed(prim.GetChildren()):
            stack.append(child)
    return surfaces


def _mesh_surface_support(
    *,
    stage: Any,
    prim_paths: Dict[str, str],
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    z_tolerance: float,
    overlap_threshold: float,
    normal_z_threshold: float,
) -> Dict[str, Any]:
    surfaces = _collect_upward_mesh_surfaces(
        stage,
        prim_paths[parent_id],
        normal_z_threshold=normal_z_threshold,
    )
    child_bottom = float(child_bbox["min"][2])
    near_surfaces = [
        surface for surface in surfaces
        if abs(float(surface["surface_z"]) - child_bottom) <= z_tolerance
    ]

    coverage_sum = 0.0
    supporting_surfaces: List[Dict[str, Any]] = []
    for surface in near_surfaces:
        coverage = _xy_coverage(child_bbox, surface["bbox"])
        if coverage <= 1e-6:
            continue
        coverage_sum += coverage
        item = dict(surface)
        item["xy_coverage"] = round(coverage, 3)
        supporting_surfaces.append(item)

    coverage_total = min(1.0, coverage_sum)
    support_z = None
    if supporting_surfaces:
        weighted = sorted(
            supporting_surfaces,
            key=lambda item: float(item["xy_coverage"]),
            reverse=True,
        )
        support_z = float(weighted[0]["surface_z"])
    z_gap = 0.0 if support_z is None else support_z - child_bottom

    issues: List[str] = []
    if coverage_total < overlap_threshold:
        issues.append(
            "surface_xy_coverage="
            f"{coverage_total:.3f} below threshold {overlap_threshold:.3f}"
        )
    if support_z is None:
        issues.append("no upward parent mesh surface near child bottom")
    elif abs(z_gap) > z_tolerance:
        issues.append(f"z_gap={z_gap:.3f} outside tolerance {z_tolerance:.3f}")

    supported = not issues
    contacts = []
    if supported:
        contacts.append({
            "child": child_id,
            "parent": parent_id,
            "type": "support",
            "method": "usd_mesh_surface",
            "support_z": support_z,
            "xy_coverage": round(coverage_total, 3),
        })

    return {
        "supported": supported,
        "child": child_id,
        "parent": parent_id,
        "support_backend": "usd_mesh_surface",
        "z_gap": z_gap,
        "xy_coverage": round(coverage_total, 3),
        "contacts": contacts,
        "issues": issues,
        "support_surfaces": supporting_surfaces[:8],
        "probe_hits": [],
        "_all_surfaces": surfaces,
    }


def _suggest_from_surface(
    *,
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    scene: Dict[str, Any],
    surface: Dict[str, Any],
    overlap_threshold: float,
) -> Dict[str, Any]:
    instances = _instances(scene)
    child_inst = instances.get(child_id, {})
    old_position = [
        float(value)
        for value in child_inst.get("position", [0.0, 0.0, 0.0])
    ]
    child_center = _bbox_center(child_bbox)
    child_size = _bbox_size(child_bbox)
    surface_bbox = surface.get("bbox")
    move_vector = [0.0, 0.0, float(surface["surface_z"]) - child_bbox["min"][2]]

    if isinstance(surface_bbox, dict):
        for axis in (0, 1):
            child_half = child_size[axis] / 2.0
            target_center = _clamp(
                child_center[axis],
                float(surface_bbox["min"][axis]) + child_half,
                float(surface_bbox["max"][axis]) - child_half,
            )
            move_vector[axis] = target_center - child_center[axis]

    new_position = [
        old_position[axis] + move_vector[axis]
        for axis in range(3)
    ]
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
    return {
        "instance_id": child_id,
        "parent_id": parent_id,
        "move_vector": move_vector,
        "new_position": new_position,
        "expected_supported": not unresolved,
        "suggestion_status": (
            "resolved_by_surface_move"
            if not unresolved
            else "unresolved_by_surface_move"
        ),
        "unresolved_issues": unresolved,
        "recommended_action": None if not unresolved else (
            "move child closer to a larger upward parent support surface"
        ),
        "target_surface": {
            "surface_z": surface.get("surface_z"),
            "mesh_path": surface.get("mesh_path"),
            "face_index": surface.get("face_index"),
        },
    }


def _surface_suggestion(
    *,
    child_id: str,
    parent_id: str,
    child_bbox: BBox,
    scene: Dict[str, Any],
    raycast_result: Optional[Dict[str, Any]],
    mesh_result: Optional[Dict[str, Any]],
    overlap_threshold: float,
) -> Optional[Dict[str, Any]]:
    surfaces: List[Dict[str, Any]] = []
    if mesh_result:
        surfaces.extend(mesh_result.get("support_surfaces", []) or [])
        surfaces.extend(mesh_result.get("_all_surfaces", []) or [])
    if raycast_result:
        for hit in raycast_result.get("_valid_hits", []) or []:
            position = hit.get("position") or [0.0, 0.0, child_bbox["min"][2]]
            surfaces.append({
                "surface_z": float(position[2]),
                "bbox": {
                    "min": [child_bbox["min"][0], child_bbox["min"][1], position[2]],
                    "max": [child_bbox["max"][0], child_bbox["max"][1], position[2]],
                },
                "mesh_path": hit.get("collision"),
                "face_index": None,
            })

    if not surfaces:
        return None

    child_bottom = float(child_bbox["min"][2])
    child_center = _bbox_center(child_bbox)

    def _surface_score(surface: Dict[str, Any]) -> Tuple[float, float]:
        coverage = (
            _xy_coverage(child_bbox, surface["bbox"])
            if isinstance(surface.get("bbox"), dict)
            else 0.0
        )
        z_distance = abs(float(surface.get("surface_z", child_bottom)) - child_bottom)
        center_distance = 0.0
        bbox = surface.get("bbox")
        if isinstance(bbox, dict):
            sx = _clamp(child_center[0], bbox["min"][0], bbox["max"][0])
            sy = _clamp(child_center[1], bbox["min"][1], bbox["max"][1])
            center_distance = math.hypot(child_center[0] - sx, child_center[1] - sy)
        return (-coverage, z_distance + center_distance)

    best = sorted(surfaces, key=_surface_score)[0]
    return _suggest_from_surface(
        child_id=child_id,
        parent_id=parent_id,
        child_bbox=child_bbox,
        scene=scene,
        surface=best,
        overlap_threshold=overlap_threshold,
    )


def _strip_private_debug(result: Dict[str, Any]) -> Dict[str, Any]:
    clean = dict(result)
    for key in list(clean.keys()):
        if key.startswith("_"):
            clean.pop(key, None)
    return clean


def _old_bbox_support(
    *,
    child_id: str,
    parent_id: str,
    bboxes: Dict[str, BBox],
    scene: Dict[str, Any],
    include_suggestions: bool,
    z_tolerance: float,
    overlap_threshold: float,
) -> Dict[str, Any]:
    result = _check_support(
        child_id,
        parent_id,
        bboxes,
        scene=scene,
        z_tolerance=z_tolerance,
        overlap_threshold=overlap_threshold,
        include_suggestions=include_suggestions,
    )
    result = dict(result)
    result["support_backend"] = "bbox_fallback"
    result.setdefault("warnings", [])
    result["warnings"].append(
        "enhanced support surface query unavailable; used bbox fallback"
    )
    if include_suggestions and result.get("suggested_move"):
        move = result["suggested_move"]
        old_position = move.get("old_position")
        if old_position is None:
            old_position = _instances(scene).get(child_id, {}).get(
                "position",
                _bbox_center(bboxes[child_id]),
            )
        result["suggested_move"] = normalize_suggestion_payload(
            instance_id=str(move.get("instance_id") or child_id),
            parent_id=str(move.get("parent_id") or parent_id),
            old_position=[float(value) for value in old_position],
            final_position=move.get("final_position") or move.get("new_position"),
            move_vector=move.get("move_vector"),
            reason="move_to_bbox_support_surface",
            suggestion_backend="bbox_fallback",
            validation_backend="predictive_fallback",
            expected_supported=bool(move.get("expected_supported", False)),
            expected_support_valid=bool(move.get("expected_supported", False)),
            unresolved_issues=list(move.get("unresolved_issues") or []),
            extra={
                key: move[key]
                for key in ("suggestion_status", "recommended_action")
                if key in move
            },
        )
    return result


def run_enhanced_support_check(
    *,
    stage: Any,
    sim_app: Any,
    scene: Dict[str, Any],
    prim_paths: Dict[str, str],
    bboxes: Dict[str, BBox],
    child_id: str,
    parent_id: str,
    include_suggestions: bool = False,
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
    support_hit_ratio: float = 0.45,
    normal_z_threshold: float = 0.65,
    probe_grid: int = 3,
) -> Dict[str, Any]:
    del sim_app

    if child_id not in bboxes or parent_id not in bboxes:
        missing = child_id if child_id not in bboxes else parent_id
        return {
            "supported": False,
            "child": child_id,
            "parent": parent_id,
            "support_backend": "enhanced_support_error",
            "z_gap": 0.0,
            "xy_coverage": 0.0,
            "contacts": [],
            "issues": [f"missing bbox for {missing}"],
            "warnings": [],
            "suggested_move": None if include_suggestions else None,
        }

    child_bbox = bboxes[child_id]
    warnings: List[str] = []
    raycast_result: Optional[Dict[str, Any]] = None
    mesh_result: Optional[Dict[str, Any]] = None

    try:
        raycast_result = _raycast_support(
            stage=stage,
            scene=scene,
            prim_paths=prim_paths,
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child_bbox,
            z_tolerance=z_tolerance,
            support_hit_ratio=support_hit_ratio,
            normal_z_threshold=normal_z_threshold,
            grid_size=probe_grid,
        )
        if raycast_result.get("supported"):
            result = _strip_private_debug(raycast_result)
            result["warnings"] = warnings
            if include_suggestions:
                result["suggested_move"] = None
            return result
    except Exception as exc:
        warnings.append(f"PhysX support raycast unavailable: {exc}")

    try:
        mesh_result = _mesh_surface_support(
            stage=stage,
            prim_paths=prim_paths,
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child_bbox,
            z_tolerance=z_tolerance,
            overlap_threshold=overlap_threshold,
            normal_z_threshold=normal_z_threshold,
        )
        if mesh_result.get("supported"):
            result = _strip_private_debug(mesh_result)
            result["warnings"] = warnings
            if include_suggestions:
                result["suggested_move"] = None
            return result
    except Exception as exc:
        warnings.append(f"USD mesh support surface check unavailable: {exc}")

    # If the real-surface probes ran and saw parent surfaces, trust the
    # unsupported result. This prevents old bbox logic from legalizing side hits.
    parent_hit_count = 0
    if raycast_result:
        for probe in raycast_result.get("probe_hits", []) or []:
            parent_hit_count += len(probe.get("parent_hits", []) or [])

    if raycast_result is None and mesh_result is None:
        result = _old_bbox_support(
            child_id=child_id,
            parent_id=parent_id,
            bboxes=bboxes,
            scene=scene,
            include_suggestions=include_suggestions,
            z_tolerance=z_tolerance,
            overlap_threshold=overlap_threshold,
        )
        result["warnings"] = (result.get("warnings", []) or []) + warnings
        return result

    base_result = raycast_result or mesh_result or {
        "supported": False,
        "child": child_id,
        "parent": parent_id,
        "support_backend": "enhanced_support",
        "z_gap": 0.0,
        "xy_coverage": 0.0,
        "contacts": [],
        "issues": ["no enhanced support backend returned a result"],
        "support_surfaces": [],
        "probe_hits": [],
    }

    result = _strip_private_debug(base_result)
    result["warnings"] = warnings
    if mesh_result and mesh_result.get("issues"):
        for issue in mesh_result.get("issues", []):
            if issue not in result["issues"]:
                result["issues"].append(issue)

    if parent_hit_count == 0 and mesh_result is None:
        old = _old_bbox_support(
            child_id=child_id,
            parent_id=parent_id,
            bboxes=bboxes,
            scene=scene,
            include_suggestions=include_suggestions,
            z_tolerance=z_tolerance,
            overlap_threshold=overlap_threshold,
        )
        if old.get("supported"):
            old["warnings"] = (old.get("warnings", []) or []) + warnings
            return old

    if include_suggestions:
        fallback_move = None
        if not (raycast_result or mesh_result):
            old = _old_bbox_support(
                child_id=child_id,
                parent_id=parent_id,
                bboxes=bboxes,
                scene=scene,
                include_suggestions=True,
                z_tolerance=z_tolerance,
                overlap_threshold=overlap_threshold,
            )
            fallback_move = old.get("suggested_move")
        result["suggested_move"] = suggest_support_move(
            scene=scene,
            child_id=child_id,
            parent_id=parent_id,
            child_bbox=child_bbox,
            raycast_result=raycast_result,
            mesh_result=mesh_result,
            fallback_move=fallback_move,
            overlap_threshold=overlap_threshold,
        )
        if result["suggested_move"] is None:
            old = _old_bbox_support(
                child_id=child_id,
                parent_id=parent_id,
                bboxes=bboxes,
                scene=scene,
                include_suggestions=True,
                z_tolerance=z_tolerance,
                overlap_threshold=overlap_threshold,
            )
            result["suggested_move"] = old.get("suggested_move")
    return result


__all__ = ["run_enhanced_support_check"]
