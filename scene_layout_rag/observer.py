"""Observer: 把工具结果与场景多维度检查打包成 ``Observation``。

对应 ``方案/优化.md`` 优化方向 2「改观测内容」。每次 ReAct 循环执行完工具后，
Observer 都做一次完整观察，给反思器提供充分上下文。
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from .data_models import Observation, SceneState
from .scene_state import SceneStateManager
from .tools.base import ToolResult
from .validators import (
    aabb_collisions,
    analyze_scene_semantics,
    evaluate_support_state,
    run_static_simulation,
)


PhysicsCallable = Callable[[SceneState], Dict[str, Any]]


class Observer:
    """组装观测。``physics_callable`` 默认是 ``run_static_simulation``。"""

    def __init__(
        self,
        scene: SceneStateManager,
        physics_callable: Optional[PhysicsCallable] = None,
    ):
        self.scene = scene
        self.physics_callable = physics_callable or run_static_simulation

    def observe(self, action: str, tool_result: ToolResult) -> Observation:
        state = self.scene.state
        # 1. 静态验证 (碰撞)
        collisions = aabb_collisions(state)
        validation = {
            "ok": tool_result.ok and len(collisions) == 0,
            "tool_ok": tool_result.ok,
            "collisions": collisions,
        }
        # 2. 场景语义
        scene_semantics = analyze_scene_semantics(state)
        # 3. 支撑状态
        support_state = evaluate_support_state(state)
        # 4. 物理反馈
        physics_feedback = self.physics_callable(state)
        # 5. 改进建议
        suggestions = self._generate_suggestions(
            collisions=collisions,
            support_state=support_state,
            physics_feedback=physics_feedback,
            scene_semantics=scene_semantics,
        )
        ok = (
            tool_result.ok
            and not collisions
            and not support_state["invalid_relations"]
            and physics_feedback["stable"]
        )
        return Observation(
            ok=ok,
            tool_result=tool_result.to_dict(),
            validation=validation,
            scene_semantics=scene_semantics,
            support_state=support_state,
            physics_feedback=physics_feedback,
            suggestions=suggestions,
            error=tool_result.error if not tool_result.ok else None,
        )

    @staticmethod
    def _generate_suggestions(
        collisions: List[Dict[str, Any]],
        support_state: Dict[str, Any],
        physics_feedback: Dict[str, Any],
        scene_semantics: Dict[str, Any],
    ) -> List[str]:
        tips: List[str] = []
        if collisions:
            for c in collisions[:5]:
                tips.append(f"AABB 碰撞: {c['a']} ({c['a_type']}) 与 {c['b']} ({c['b_type']})；考虑挪开或调整尺寸。")
        for bad in support_state.get("invalid_relations", [])[:5]:
            tips.append(
                f"支撑关系不稳: {bad['child']} 在 {bad['parent']} 上 - " + "; ".join(bad.get("issues", []))
            )
        for warning in physics_feedback.get("warnings", [])[:5]:
            tips.append(f"物理告警: {warning}")
        for corridor in scene_semantics.get("corridors", []):
            if corridor.get("blocked"):
                tips.append(
                    f"通道 {corridor['from']} → {corridor['to']} 被阻塞，宽度 {corridor['width']}m。"
                )
        return tips


__all__ = ["Observer"]
