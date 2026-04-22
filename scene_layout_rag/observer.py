"""Scene observer -- generates structured observation reports after each action."""
from __future__ import annotations

from typing import Any, Dict, List

from .scene_state import SceneState
from .validators import find_all_collisions, check_out_of_bounds, find_support_candidates


class SceneObserver:
    """Produces observation dicts consumed by the ReAct agent."""

    def __init__(self, physics_enabled: bool = False):
        self.physics_enabled = physics_enabled

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def observe(self, scene: SceneState) -> Dict[str, Any]:
        """Full observation for scene-modifying actions."""
        validation = self._validate(scene)
        return {
            "validation": validation,
            "scene_semantics": self._analyze_semantics(scene),
            "support_state": self._check_supports(scene),
            "physics_feedback": self._physics_feedback(scene),
            "suggestions": self._generate_suggestions(scene, validation),
        }

    def observe_retrieval(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Lightweight observation for ``retrieve_assets`` results."""
        assets = result.get("assets", [])
        return {
            "type": "retrieval",
            "validation": {"ok": True, "collisions": [], "out_of_bounds": []},
            "query": result.get("query", ""),
            "found_count": result.get("count", len(assets)),
            "assets_summary": [
                f"{a['asset_id']} (bbox={a.get('bbox', {})}, score={a.get('score', 0)})"
                for a in assets[:5]
            ],
        }

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _validate(self, scene: SceneState) -> Dict[str, Any]:
        collisions = find_all_collisions(scene)
        oob = check_out_of_bounds(scene)
        return {
            "ok": len(collisions) == 0 and len(oob) == 0,
            "collisions": collisions,
            "out_of_bounds": oob,
        }

    def _analyze_semantics(self, scene: SceneState) -> Dict[str, Any]:
        """Basic semantic analysis: group assets by type and zone."""
        type_counts: Dict[str, int] = {}
        for a in scene.assets.values():
            type_counts[a.asset_id] = type_counts.get(a.asset_id, 0) + 1

        # Simple corridor estimation: find gaps between assets along X axis
        corridors: List[Dict[str, Any]] = []
        sorted_assets = sorted(scene.assets.values(), key=lambda a: a.position[0])
        for i in range(len(sorted_assets) - 1):
            a = sorted_assets[i]
            b = sorted_assets[i + 1]
            a_right = a.position[0] + a.bbox[0] / 2.0
            b_left = b.position[0] - b.bbox[0] / 2.0
            gap = b_left - a_right
            if gap > 0.5:
                corridors.append({
                    "between": [a.instance_id, b.instance_id],
                    "width": round(gap, 2),
                    "blocked": gap < 1.5,
                })

        return {
            "type_counts": type_counts,
            "total_assets": len(scene.assets),
            "corridors": corridors,
        }

    def _check_supports(self, scene: SceneState) -> Dict[str, Any]:
        """Report existing support relationships and potential issues."""
        valid: List[Dict[str, Any]] = []
        invalid: List[Dict[str, Any]] = []

        for a in scene.assets.values():
            if a.support_parent is None:
                continue
            parent = scene.get_asset(a.support_parent)
            if parent is None:
                invalid.append({
                    "child": a.instance_id,
                    "parent": a.support_parent,
                    "issue": "parent_not_found",
                })
                continue
            # Quick XY check
            from .validators import _xy_overlap_ratio
            ratio = _xy_overlap_ratio(a.position, a.bbox, parent.position, parent.bbox)
            if ratio < 0.3:
                invalid.append({
                    "child": a.instance_id,
                    "parent": parent.instance_id,
                    "issue": "xy_overlap_too_low",
                    "xy_overlap_ratio": round(ratio, 3),
                })
            else:
                valid.append({
                    "child": a.instance_id,
                    "parent": parent.instance_id,
                    "xy_overlap_ratio": round(ratio, 3),
                })

        return {"valid_relations": valid, "invalid_relations": invalid}

    def _physics_feedback(self, scene: SceneState) -> Dict[str, Any]:
        """Physics simulation feedback. Stub unless Isaac Sim is wired in."""
        if self.physics_enabled:
            try:
                from .physics import ISAAC_AVAILABLE, PhysicsValidator
                if ISAAC_AVAILABLE:
                    return PhysicsValidator().validate(scene)
            except ImportError:
                pass

        # Geometric fallback: check if unsupported items are floating
        warnings: List[str] = []
        for a in scene.assets.values():
            bottom_z = a.position[2] - a.bbox[2] / 2.0
            if bottom_z > 0.1 and a.support_parent is None:
                warnings.append(f"{a.instance_id} 悬浮在 z={a.position[2]:.2f}m，无支撑")

        return {
            "physics_available": False,
            "stable": len(warnings) == 0,
            "fallen_assets": [],
            "contacts": [],
            "warnings": warnings,
        }

    def _generate_suggestions(
        self,
        scene: SceneState,
        validation: Dict[str, Any],
    ) -> List[str]:
        suggestions: List[str] = []

        for col in validation.get("collisions", []):
            suggestions.append(
                f"{col['a']} 与 {col['b']} 发生碰撞 (重叠体积 {col['overlap_volume']}m³)，"
                f"建议调整位置"
            )

        for oob_id in validation.get("out_of_bounds", []):
            suggestions.append(f"{oob_id} 超出场景边界，建议移动到边界内")

        # Check for tight corridors
        sem = self._analyze_semantics(scene)
        for corridor in sem.get("corridors", []):
            if corridor.get("blocked"):
                a, b = corridor["between"]
                suggestions.append(
                    f"{a} 和 {b} 之间通道仅 {corridor['width']}m，"
                    f"AGV 可能无法通过，建议增加间距"
                )

        return suggestions


__all__ = ["SceneObserver"]
