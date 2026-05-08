"""Tool ABC + registry.

工具必须把输入 schema 描述成 OpenAI SDK function tool 格式（见 ``Tool.schema``），
方便 LLM 在 prompt 里看到准确的用法说明，也便于运行时校验，对应 ``方案/优化.md``：
「工具输入输出严格限定格式和内容」。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

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

    name: str = ""
    description: str = ""
    # OpenAI Responses API function tool schema. 输出统一是 ToolResult。
    schema: Dict[str, Any] = {}

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        raise NotImplementedError

    def run_test(self, context: ToolContext) -> ToolResult:
        raise NotImplementedError

    # ---- 输入校验 ----

    def validate(self, kwargs: Dict[str, Any]) -> Optional[str]:
        function_spec = get_tool_function_spec(self.schema)
        parameters = function_spec.get("parameters", {})
        properties = parameters.get("properties", {})
        required_fields = parameters.get("required", [])
        for field_name in required_fields:
            if field_name not in kwargs:
                return f"missing required field: {field_name}"
        unknown = set(kwargs) - set(properties)
        if unknown:
            return f"unknown fields: {sorted(unknown)}"
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


def get_tool_function_spec(schema: Dict[str, Any]) -> Dict[str, Any]:
    """返回 function tool 的内部规格，兼容 OpenAI 嵌套格式和旧扁平格式。"""
    function_spec = schema.get("function")
    if isinstance(function_spec, dict):
        return function_spec
    return schema

def make_openai_tool_schema(
    name: str,
    description: str,
    properties: Dict[str, Any],
    required: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """构造可直接传给 OpenAI SDK ``tools`` 参数的 function tool。
    这里显式保留 ``strict=False``：当前工具有不少可选参数，如果让 Responses API
    自动切到 strict 模式，会把可选字段也收紧成必填，改变现有调用语义。
    """
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": list(required or []),
                "additionalProperties": False,
            },
            "strict": False,
        },
    }


def register_tool(tool_cls: type) -> type:
    instance = tool_cls()
    if not instance.name:
        raise ValueError(f"{tool_cls.__name__} 没有定义 name")
    if instance.name in TOOL_REGISTRY:
        raise ValueError(f"工具重复注册: {instance.name}")
    TOOL_REGISTRY[instance.name] = instance
    return tool_cls


def list_tool_specs() -> List[Dict[str, Any]]:
    """供 LLM prompt / OpenAI SDK ``tools`` 参数使用的工具规格列表。"""
    return [tool.schema for tool in TOOL_REGISTRY.values()]


def list_openai_tools() -> List[Dict[str, Any]]:
    """显式语义化的别名：返回可直接传给 OpenAI SDK 的 tools 列表。"""
    return list_tool_specs()


__all__ = [
    "Tool",
    "ToolContext",
    "ToolResult",
    "TOOL_REGISTRY",
    "list_openai_tools",
    "get_tool_function_spec",
    "make_openai_tool_schema",
    "register_tool",
    "list_tool_specs",
]
