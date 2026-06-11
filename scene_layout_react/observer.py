# observer.py
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Dict, Optional
from .data_models import SceneState
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
    retrieval_memory: Dict[str, Any] = field(default_factory=dict)
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
        local = self.scene.validate_integrity()

        external = {
            "ok": None,
            "validation": {
                "backend": "not_observed",
                "authoritative": False,
                "collision_free": None,
                "collision_count": None,
            },
            "support_state": {
                "backend": "local_structure_only",
                "authoritative": False,
                "checked_relation_count": 0,
                "valid_relation_count": 0,
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

        scene_semantics = {}
        if not local["ok"]:
            scene_semantics["state_integrity"] = local
        else:
            scene_semantics["ok"] = True

        retrieval_memory = getattr(self.scene, "retrieval_memory", None) or {}
        retrieval_memory_summary = {
            "asset_queries": list(retrieval_memory.get("asset_queries", []))
        }

        return Observation(
            ok=ok,
            current_state=self._summarize_current_state(state),
            validation=validation,
            support_state=support_state,
            physics_feedback=physics_feedback,
            scene_semantics=scene_semantics,
            retrieval_memory=retrieval_memory_summary,
            error=error,
        )

    def _summarize_current_state(self, state: SceneState) -> Dict[str, Any]:
        instances = {}
        for instance_id, inst in state.instances.items():
            instances[instance_id] = {
                "instance_id": instance_id,
                "asset_type": inst.asset_type,
                "position": list(inst.position),
                "rotation_deg": inst.rotation_deg,
                "bbox": inst.bbox,
                "parent_instance_id": inst.parent_instance_id,
            }

        support_children = {}
        for parent_id, children in state.support_children.items():
            if parent_id not in state.instances:
                continue

            valid_children = [child_id for child_id in children if child_id in state.instances]

            if valid_children:
                support_children[parent_id] = valid_children

        return {
            "instances": instances,
            "support_children": support_children,
        }
