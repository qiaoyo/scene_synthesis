"""ReAct 工具集。每个工具都用统一的 ``Tool`` 接口注册，方便 LLM 调用。"""
from .base import TOOL_REGISTRY, Tool, ToolContext, ToolResult, register_tool
from . import (  # noqa: F401  -- import for registration side-effect
    check_collision,
    check_support,
    delete_asset,
    move_asset,
    place_instance,
    query_scene,
    retrieve_assets,
    set_support,
    simulate_step,
)

__all__ = ["TOOL_REGISTRY", "Tool", "ToolContext", "ToolResult", "register_tool"]
