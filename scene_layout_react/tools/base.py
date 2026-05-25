from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Optional
import logging
import traceback
import uuid
from jsonschema import validate
from jsonschema.exceptions import ValidationError
if TYPE_CHECKING:
    from ..rag import AssetRAG
    from ..scene_state import SceneStateManager
logger = logging.getLogger(__name__)
@dataclass
class ToolContext:
    """工具运行所需的运行时上下文。"""
    
    scene: SceneStateManager
    rag: AssetRAG
    config: Any = None
    physics_enabled: bool = False
    extras: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ToolResult:
    """所有工具的统一返回结构。"""
    
    ok: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    error_type: Optional[str] = None
    trace_id: Optional[str] = None
    debug: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self, include_debug: bool = False) -> Dict[str, Any]:
        payload = {
            "ok": self.ok,
            "data": self.data,
            "error": self.error,
        }
        if self.error_type is not None:
            payload["error_type"] = self.error_type
        if self.trace_id is not None:
            payload["trace_id"] = self.trace_id
        if include_debug and self.debug:
            payload["debug"] = self.debug
        return payload

class Tool:
    schema: Dict[str, Any] = {}
    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        raise NotImplementedError
    
    def validate(self, kwargs: Dict[str, Any]) -> Optional[str]:
        function_spec = self.schema.get("function", {})
        parameters = function_spec.get("parameters", {}) or {}
        try:
            validate(instance=kwargs, schema=parameters)
        except ValidationError as exc:
            return exc.message
        return None
        
    def __call__(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        err = self.validate(kwargs)
        if err is not None:
            return ToolResult(
                ok=False,
                error=err,
                error_type="ToolArgumentValidationError",
            )
        try:
            return self.run(context, **kwargs)
        except Exception as exc:
            trace_id = uuid.uuid4().hex[:12]
            tool_name = self.schema.get("function", {}).get("name", self.__class__.__name__)
            tb = traceback.format_exc()
            logger.error(
                "Tool %s failed unexpectedly trace_id=%s error_type=%s error=%s\n%s",
                tool_name,
                trace_id,
                exc.__class__.__name__,
                str(exc),
                tb,
            )
            return ToolResult(
                ok=False,
                error=f"unexpected tool error in {tool_name}; trace_id={trace_id}",
                error_type=exc.__class__.__name__,
                trace_id=trace_id,
                debug={
                    "tool": tool_name,
                    "kwargs": kwargs,
                    "traceback": tb,
                },
            )

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
