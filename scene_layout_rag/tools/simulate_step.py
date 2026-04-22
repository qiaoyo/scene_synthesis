"""Run a physics simulation step (stub until Phase 5 Isaac Sim integration)."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class SimulateStepTool(BaseTool):
    name = "simulate_step"
    description = "运行物理仿真，检测资产稳定性和接触关系"

    parameters_schema = {
        "duration": {
            "type": "float",
            "required": False,
            "description": "仿真时长（秒），默认 2.0",
        },
    }

    @property
    def modifies_scene(self) -> bool:
        return False

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        # Try to use Isaac Sim physics validator if available
        try:
            from ..physics import ISAAC_AVAILABLE, PhysicsValidator
            if ISAAC_AVAILABLE:
                scene = ctx.get("scene")
                if scene is None:
                    return ToolResult(ok=False, error="scene 未提供")
                duration = float(params.get("duration", 2.0))
                validator = PhysicsValidator()
                feedback = validator.validate(scene, duration=duration)
                return ToolResult(ok=True, result=feedback)
        except ImportError:
            pass

        # Geometric fallback
        return ToolResult(ok=True, result={
            "physics_available": False,
            "message": "物理仿真不可用，请使用 check_collision 进行几何碰撞检测",
            "stable": True,
            "fallen_assets": [],
            "contacts": [],
            "warnings": [],
        })
