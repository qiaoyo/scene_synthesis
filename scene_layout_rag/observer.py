from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
from dataclasses import asdict, dataclass, field
from .data_models import SceneState
from .scene_state import SceneStateManager
from .tools.base import ToolResult
from .validators import (
    aabb_collisions,
    analyze_scene_semantics,
    evaluate_support_state,
    run_static_simulation,
)
PhysicsCallable = Callable[[SceneState], Dict[str, Any]]

@dataclass
class Observation:
    """一次工具执行后的全面观测。结构对齐 ``方案/优化.md`` 中的优化方向 2。"""
    ok: bool = True
    tool_result: Dict[str, Any] = field(default_factory=dict)
    validation: Dict[str, Any] = field(default_factory=dict)
    scene_semantics: Dict[str, Any] = field(default_factory=dict)
    support_state: Dict[str, Any] = field(default_factory=dict)
    physics_feedback: Dict[str, Any] = field(default_factory=dict)
    suggestions: List[str] = field(default_factory=list)
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class Observer:
    def __init__(self,scene: SceneStateManager,physics_callable=None,):
        self.scene = scene
        self.physics_callable = (physics_callable or run_static_simulation)
        
    def observe(self,command: str,tool_results: List[ToolResult],previous_state: SceneState,
    ) -> Observation:
        current_state = self.scene.state
        # -------------------------------------------------
        # Scene Delta
        # -------------------------------------------------
        # scene_delta = self._compute_scene_delta(
        #     previous_state,
        #     current_state,
        # )
        # -------------------------------------------------
        # Validation
        # -------------------------------------------------
        collisions = aabb_collisions(current_state)
        validation = {
            "collision_free": len(collisions) == 0,
            "collisions": collisions,
        }

        # -------------------------------------------------
        # Support
        # -------------------------------------------------
        support_state = evaluate_support_state(
            current_state
        )

        # -------------------------------------------------
        # Physics
        # -------------------------------------------------
        physics_feedback = self.physics_callable(
            current_state
        )

        # -------------------------------------------------
        # Semantics
        # -------------------------------------------------
        scene_semantics = analyze_scene_semantics(
            current_state
        )

        # -------------------------------------------------
        # Task Progress
        # -------------------------------------------------
        # task_progress = self._evaluate_task_progress(
        #     command,
        #     current_state,
        # )

        # -------------------------------------------------
        # Overall OK
        # -------------------------------------------------

        ok = (
            validation["collision_free"]
            and physics_feedback["stable"]
            and not support_state["invalid_relations"]
        )

        return Observation(
            ok=ok,
            tool_result = tool_results,
            #scene_delta=scene_delta,
            validation=validation,
            scene_semantics=scene_semantics,
            support_state=support_state,
            physics_feedback=physics_feedback,
            #task_progress=task_progress,
        )