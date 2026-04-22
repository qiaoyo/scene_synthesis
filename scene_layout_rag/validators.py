"""Geometric validators for collision, bounds, and support checking."""
from __future__ import annotations

from typing import Any, Dict, List

from .scene_state import SceneState


# ------------------------------------------------------------------
# AABB helpers
# ------------------------------------------------------------------

def aabb_overlap_volume(pos_a: tuple, bbox_a: tuple, pos_b: tuple, bbox_b: tuple) -> float:
    """Return the overlap volume of two axis-aligned bounding boxes (centre + extents)."""
    overlap = 1.0
    for i in range(3):
        a_min = pos_a[i] - bbox_a[i] / 2.0
        a_max = pos_a[i] + bbox_a[i] / 2.0
        b_min = pos_b[i] - bbox_b[i] / 2.0
        b_max = pos_b[i] + bbox_b[i] / 2.0
        lo = max(a_min, b_min)
        hi = min(a_max, b_max)
        if lo >= hi:
            return 0.0
        overlap *= (hi - lo)
    return overlap


# ------------------------------------------------------------------
# Scene-level checks
# ------------------------------------------------------------------

def find_all_collisions(scene: SceneState) -> List[Dict[str, Any]]:
    """Return a list of colliding asset pairs."""
    assets = list(scene.assets.values())
    collisions: List[Dict[str, Any]] = []
    for i, a in enumerate(assets):
        for b in assets[i + 1:]:
            vol = aabb_overlap_volume(a.position, a.bbox, b.position, b.bbox)
            if vol > 1e-6:
                collisions.append({
                    "a": a.instance_id,
                    "b": b.instance_id,
                    "overlap_volume": round(vol, 4),
                })
    return collisions


def check_out_of_bounds(scene: SceneState) -> List[str]:
    """Return instance IDs of assets whose centre is outside the scene bounds."""
    half = [scene.bounds[i] / 2.0 for i in range(3)]
    oob: List[str] = []
    for a in scene.assets.values():
        for i in range(3):
            if abs(a.position[i]) > half[i] + a.bbox[i] / 2.0:
                oob.append(a.instance_id)
                break
    return oob


def check_support_valid(
    child_id: str,
    parent_id: str,
    scene: SceneState,
    min_overlap: float = 0.3,
    max_z_gap: float = 0.1,
) -> Dict[str, Any]:
    """Validate a proposed support relationship geometrically."""
    child = scene.get_asset(child_id)
    parent = scene.get_asset(parent_id)
    if child is None or parent is None:
        return {"ok": False, "reason": "资产不存在"}

    child_bottom = child.position[2] - child.bbox[2] / 2.0
    parent_top = parent.position[2] + parent.bbox[2] / 2.0
    z_gap = abs(child_bottom - parent_top)

    # XY overlap ratio
    overlap_ratio = _xy_overlap_ratio(child.position, child.bbox, parent.position, parent.bbox)

    issues: List[str] = []
    if z_gap > max_z_gap:
        issues.append(f"Z 高度差 {z_gap:.3f}m 超阈值 {max_z_gap}m")
    if overlap_ratio < min_overlap:
        issues.append(f"XY 重叠率 {overlap_ratio:.1%} 低于阈值 {min_overlap:.0%}")

    return {
        "ok": len(issues) == 0,
        "z_gap": round(z_gap, 3),
        "xy_overlap_ratio": round(overlap_ratio, 3),
        "issues": issues,
    }


def find_support_candidates(instance_id: str, scene: SceneState) -> List[Dict[str, Any]]:
    """Find assets that could support *instance_id* (geometrically)."""
    child = scene.get_asset(instance_id)
    if child is None:
        return []
    child_bottom = child.position[2] - child.bbox[2] / 2.0
    candidates: List[Dict[str, Any]] = []
    for a in scene.assets.values():
        if a.instance_id == instance_id:
            continue
        parent_top = a.position[2] + a.bbox[2] / 2.0
        z_gap = abs(child_bottom - parent_top)
        if z_gap > 0.2:
            continue
        ratio = _xy_overlap_ratio(child.position, child.bbox, a.position, a.bbox)
        if ratio > 0.05:
            candidates.append({
                "instance_id": a.instance_id,
                "asset_id": a.asset_id,
                "top_z": round(parent_top, 3),
                "z_gap": round(z_gap, 3),
                "xy_overlap_ratio": round(ratio, 3),
            })
    candidates.sort(key=lambda c: (-c["xy_overlap_ratio"], c["z_gap"]))
    return candidates


# ------------------------------------------------------------------
# Internal helpers
# ------------------------------------------------------------------

def _xy_overlap_ratio(child_pos, child_bbox, parent_pos, parent_bbox) -> float:
    c_xmin = child_pos[0] - child_bbox[0] / 2.0
    c_xmax = child_pos[0] + child_bbox[0] / 2.0
    c_ymin = child_pos[1] - child_bbox[1] / 2.0
    c_ymax = child_pos[1] + child_bbox[1] / 2.0

    p_xmin = parent_pos[0] - parent_bbox[0] / 2.0
    p_xmax = parent_pos[0] + parent_bbox[0] / 2.0
    p_ymin = parent_pos[1] - parent_bbox[1] / 2.0
    p_ymax = parent_pos[1] + parent_bbox[1] / 2.0

    ox = max(0.0, min(c_xmax, p_xmax) - max(c_xmin, p_xmin))
    oy = max(0.0, min(c_ymax, p_ymax) - max(c_ymin, p_ymin))
    child_area = child_bbox[0] * child_bbox[1]
    if child_area <= 0:
        return 0.0
    return (ox * oy) / child_area
