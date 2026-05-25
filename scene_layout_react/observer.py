# observer.py
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple
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
    error: Optional[str] = None
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
# =========================================================
# Observer
# =========================================================
class Observer:
    def __init__(
        self,
        scene: SceneStateManager,
        scene_observer: Optional[Callable[[SceneState], Dict[str, Any]]] = None,
        physics_required: bool = False,
    ):
        self.scene = scene
        self.scene_observer = scene_observer
        self.physics_required = physics_required

    def observe(self) -> Observation:
        state = self.scene.state
        local = self._observe_local_state(state)

        external = {
            "ok": None,
            "validation": {
                "backend": "not_observed",
                "authoritative": False,
                "collision_free": None,
                "collisions": [],
                "suggested_move": None,
                "suggested_moves": [],
                "suggested_final_positions": {},
            },
            "support_state": {
                "backend": "local_structure_only",
                "authoritative": False,
                "valid_relations": [],
                "invalid_relations": [],
            },
            "physics_feedback": {
                "backend": "not_observed",
                "authoritative": False,
                "stable": None,
                "fallen_assets": [],
            },
            "error": None,
        }

        if self.scene_observer is not None:
            try:
                external = self.scene_observer(state)
            except Exception as exc:
                external["ok"] = False
                external["error"] = str(exc)

        validation = external.get("validation", {})
        support_state = external.get("support_state", {})
        physics_feedback = external.get("physics_feedback", {})

        support_state["invalid_relations"] = (
            local["invalid_relations"]
            + support_state.get("invalid_relations", [])
        )
        support_state["declared_relations"] = local["declared_relations"]
        support_state["graph_complete"] = local["ok"]

        if self.physics_required and self.scene_observer is None:
            ok = False
            error = "physics observation is required but no scene_observer is configured"
        elif self.scene_observer is not None:
            ok = (
                local["ok"]
                and external.get("ok") is True
                and validation.get("collision_free") is True
                and not support_state["invalid_relations"]
                and physics_feedback.get("stable") is True
            )
            error = external.get("error")
        else:
            ok = local["ok"]
            error = external.get("error")

        return Observation(
            ok=ok,
            current_state=state.to_dict(),
            validation=validation,
            support_state=support_state,
            physics_feedback=physics_feedback,
            scene_semantics={"state_integrity": local},
            error=error,
        )

    def _observe_local_state(self, state: SceneState) -> Dict[str, Any]:
        invalid = []
        declared = []
        child_to_parent = {}

        for parent_id, children in state.support_children.items():
            if parent_id not in state.instances:
                invalid.append({"parent": parent_id, "issue": "missing parent instance"})
                continue

            for child_id in children:
                declared.append({"child": child_id, "parent": parent_id})

                child = state.instances.get(child_id)
                if child is None:
                    invalid.append({
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "missing child instance",
                    })
                    continue

                if child_id == parent_id:
                    invalid.append({"child": child_id, "parent": parent_id, "issue": "self support"})

                if child_id in child_to_parent:
                    invalid.append({"child": child_id, "parent": parent_id, "issue": "multiple parents"})

                if child.parent_instance_id != parent_id:
                    invalid.append({
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "parent link mismatch",
                        "instance_parent": child.parent_instance_id,
                    })

                child_to_parent[child_id] = parent_id

        for child_id, inst in state.instances.items():
            parent_id = inst.parent_instance_id
            if parent_id is None:
                continue
            if parent_id not in state.instances:
                invalid.append({"child": child_id, "parent": parent_id, "issue": "missing parent instance"})
            elif child_id not in state.support_children.get(parent_id, []):
                invalid.append({"child": child_id, "parent": parent_id, "issue": "missing support_children edge"})

        return {
            "backend": "local_state",
            "ok": len(invalid) == 0,
            "instance_count": len(state.instances),
            "support_edge_count": sum(len(v) for v in state.support_children.values()),
            "declared_relations": declared,
            "invalid_relations": invalid,
        }
