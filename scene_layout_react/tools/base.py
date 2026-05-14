from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from ..rag import AssetRAG
from ..scene_state import SceneStateManager

@dataclass
class ToolContext:
    """工具运行所需的运行时上下文。"""
    scene: SceneStateManager
    rag: AssetRAG
    physics_enabled: bool = False
    extras: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ToolResult:
    """所有工具的统一返回结构。"""
    ok: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    def to_dict(self) -> Dict[str, Any]:
        return {"ok": self.ok, "data": self.data, "error": self.error}

class Tool:
    schema: Dict[str, Any] = {}
    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        raise NotImplementedError
    def validate(self, kwargs: Dict[str, Any]) -> Optional[str]:
        function_spec = self.schema.get("function", {})
        parameters = function_spec.get("parameters", {})
        try:
            validate(instance=kwargs, schema=parameters)
        except ValidationError as exc:
            return exc.message
        return None
    def __call__(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        err = self.validate(kwargs)
        if err is not None:
            return ToolResult(ok=False, error=err)
        try:
            return self.run(context, **kwargs)
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))

TOOL_REGISTRY: Dict[str, Tool] = {}

def register_tool(tool_cls: type) -> type:
    instance = tool_cls()
    function_spec = instance.schema.get("function",{})
    tool_name = function_spec.get("name")
    if not tool_name:
        raise ValueError(f"{tool_cls.__name__} schema 缺少 function.name")
    if tool_name in TOOL_REGISTRY:
        raise ValueError(f"工具重复注册: {tool_name}")
    TOOL_REGISTRY[tool_name] = instance
    return tool_cls

__all__ = [
    "Tool",
    "ToolContext",
    "ToolResult",
    "TOOL_REGISTRY",
    "register_tool",
]
