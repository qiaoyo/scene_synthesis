"""Tool abstraction layer for the ReAct agent."""

from .base import BaseTool, ToolResult, ToolRegistry
from .retrieve_assets import RetrieveAssetsTool
from .place_instance import PlaceInstanceTool
from .move_asset import MoveAssetTool
from .delete_asset import DeleteAssetTool
from .query_scene import QuerySceneTool
from .check_collision import CheckCollisionTool
from .check_support import CheckSupportTool
from .set_support import SetSupportTool
from .simulate_step import SimulateStepTool


def build_default_registry() -> ToolRegistry:
    """Create a registry with all built-in tools."""
    registry = ToolRegistry()
    for tool_cls in [
        RetrieveAssetsTool,
        PlaceInstanceTool,
        MoveAssetTool,
        DeleteAssetTool,
        QuerySceneTool,
        CheckCollisionTool,
        CheckSupportTool,
        SetSupportTool,
        SimulateStepTool,
    ]:
        registry.register(tool_cls())
    return registry


__all__ = [
    "BaseTool",
    "ToolResult",
    "ToolRegistry",
    "build_default_registry",
]
