"""Base classes for the tool system."""
from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ToolResult:
    """Standardised return value from every tool execution."""
    ok: bool
    result: Dict[str, Any] = field(default_factory=dict)
    error: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"ok": self.ok}
        if self.ok:
            d["result"] = self.result
        else:
            d["error"] = self.error
        return d


class BaseTool(ABC):
    """Abstract base for all agent tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Machine-readable tool name, e.g. ``place_instance``."""

    @property
    @abstractmethod
    def description(self) -> str:
        """One-line Chinese description shown to the LLM."""

    @property
    @abstractmethod
    def parameters_schema(self) -> Dict[str, Any]:
        """JSON-Schema-style dict describing accepted parameters."""

    @property
    def modifies_scene(self) -> bool:
        """Return *True* if execution mutates the scene state."""
        return True

    @abstractmethod
    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        """Run the tool. ``ctx`` carries shared objects (scene, embedder, ...)."""

    # ------------------------------------------------------------------
    # Prompt helpers
    # ------------------------------------------------------------------

    def describe_for_prompt(self) -> str:
        """Render a human/LLM-readable description of the tool."""
        lines = [
            f"工具名: {self.name}",
            f"功能: {self.description}",
            "参数:",
        ]
        for pname, spec in self.parameters_schema.items():
            ptype = spec.get("type", "any")
            required = spec.get("required", False)
            desc = spec.get("description", "")
            tag = "必填" if required else "可选"
            lines.append(f"  - {pname} ({ptype}, {tag}): {desc}")
        lines.append(f"修改场景: {'是' if self.modifies_scene else '否'}")
        return "\n".join(lines)


class ToolRegistry:
    """Holds references to all available tools."""

    def __init__(self) -> None:
        self._tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[BaseTool]:
        return self._tools.get(name)

    def list_names(self) -> List[str]:
        return list(self._tools.keys())

    def is_scene_modifier(self, name: str) -> bool:
        tool = self._tools.get(name)
        return tool.modifies_scene if tool else False

    def generate_tools_prompt(self) -> str:
        """Generate a combined description block for all tools."""
        sections = [t.describe_for_prompt() for t in self._tools.values()]
        return "\n\n".join(sections)

    def execute(
        self,
        tool_name: str,
        params: Dict[str, Any],
        **ctx: Any,
    ) -> ToolResult:
        tool = self._tools.get(tool_name)
        if tool is None:
            return ToolResult(ok=False, error=f"未知工具: {tool_name}")
        try:
            return tool.execute(params, **ctx)
        except Exception as exc:
            return ToolResult(ok=False, error=str(exc))
