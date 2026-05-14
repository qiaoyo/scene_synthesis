# observer.py
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from .data_models import Instance, SceneState
from .scene_state import SceneStateManager
# =========================================================
# Observation
# =========================================================
@dataclass
class Observation:
    ok: bool
    current_state: Dict[str, Any]
    validation: Dict[str, Any] = field(default_factory=dict)
    support_state: Dict[str, Any] = field(default_factory=dict)
    physics_feedback: Dict[str, Any] = field(default_factory=dict)
    scene_semantics: Dict[str, Any] = field(default_factory=dict)
    suggestions: List[str] = field(default_factory=list)
    error: Optional[str] = None
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
# =========================================================
# Observer
# =========================================================
class Observer:
    """
    场景观察器：
    - collision validation
    - support validation
    - lightweight physics
    - semantic analysis
    """
    # -----------------------------------------------------
    # semantic config
    # -----------------------------------------------------
    def __init__(
        self,
        scene: SceneStateManager,
    ):
        self.scene = scene
    # =====================================================
    # Public API
    # =====================================================

    def observe(self) -> Observation:
        state = self.scene.state
        # -------------------------------------------------
        # Validation
        # -------------------------------------------------
        validation = self._validate_collisions(state)
        # -------------------------------------------------
        # Support
        # -------------------------------------------------
        support_state = self._evaluate_support_state(state)
        # -------------------------------------------------
        # Physics
        # -------------------------------------------------

        # -------------------------------------------------
        # Semantics
        # -------------------------------------------------

        # -------------------------------------------------
        # Overall OK
        # -------------------------------------------------
        ok = (
            validation["collision_free"]
            #and physics_feedback["stable"]
            and not support_state["invalid_relations"]
        )
        return Observation(
            ok=ok,
            current_state=state.to_dict(),
            validation=validation,
            support_state=support_state,
            #physics_feedback=physics_feedback,
            #scene_semantics=scene_semantics,
        )
    # =====================================================
    # Collision Validation
    # =====================================================
    def _validate_collisions(self,state: SceneState,) -> Dict[str, Any]:
        instances = list(state.instances.values())
        collisions: List[Dict[str, Any]] = []
        for i in range(len(instances)):
            a = instances[i]
            a_min, a_max = a.aabb()
            for j in range(i + 1, len(instances)):
                b = instances[j]
                if a.instance_id and b.instance_id and (b.instance_id in state.support_children.get(a.instance_id, []) or a.instance_id in state.support_children.get(b.instance_id, [])):
                    continue
                b_min, b_max = b.aabb()
                tol = 1e-4
                for i in range(3):
                    if a_max[i] <= b_min[i] + tol:
                        collision_value = False
                    elif b_max[i] <= a_min[i] + tol:
                        collision_value = False
                    else:
                        collision_value = True
                if collision_value:
                    collisions.append({
                        "a": a.instance_id,
                        "b": b.instance_id,
                        "a_type": a.asset_type,
                        "b_type": b.asset_type,
                    })
        return {
            "collision_free": len(collisions) == 0,
            "collisions": collisions,
        }
    # =====================================================
    # Support Validation
    # =====================================================
    def _evaluate_support_state(
        self,
        state: SceneState,
    ) -> Dict[str, Any]:
        valid: List[Dict[str, Any]] = []
        invalid: List[Dict[str, Any]] = []
        for parent_id, children in state.support_children.items():
            if parent_id not in state.instances:
                continue
            parent = state.instances[parent_id]
            for child_id in children:
                if child_id not in state.instances:
                    continue
                child = state.instances[child_id]
                
                z_tolerance = 0.05,
                overlap_threshold = 0.4,
                c_min, c_max = child.aabb()
                p_min, p_max = parent.aabb()
                # Z gap
                z_gap = c_min[2] - p_max[2]
                z_aligned = abs(z_gap) <= z_tolerance
                # XY overlap
                dx = max(
                    0.0,
                    min(c_max[0], p_max[0])
                    - max(c_min[0], p_min[0]),
                )
                dy = max(
                    0.0,
                    min(c_max[1], p_max[1])
                    - max(c_min[1], p_min[1]),
                )
                overlap_area = dx*dy
                child_area = max(
                    1e-9,
                    (c_max[0] - c_min[0]) *(c_max[1] - c_min[1]),
                )
                coverage = overlap_area / child_area
                inside = coverage >= overlap_threshold
                ok = z_aligned and inside
                issues = []
                if not z_aligned:
                    issues.append(
                        f"z_gap={z_gap:.3f} exceeds tolerance"
                    )
                if not inside:
                    issues.append(
                        f"xy_coverage={coverage:.2f} below threshold"
                    )
                entry = {
                    "child": child_id,
                    "parent": parent_id,
                    "ok": ok,
                    "z_gap": round(z_gap, 4),
                    "xy_coverage": round(coverage, 3),
                    "issues": issues,
                }
                if entry["ok"]:
                    valid.append(entry)
                else:
                    invalid.append(entry)
        return {
            "valid_relations": valid,
            "invalid_relations": invalid,
        }
    # =====================================================
    # Static Physics
    # =====================================================


    # =====================================================
    # Semantic Analysis
    # =====================================================


    # =====================================================
    # Support Helpers
    # =====================================================