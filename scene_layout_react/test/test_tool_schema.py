from __future__ import annotations

from scene_layout_react.config import ProjectConfig
from scene_layout_react.llm_planner import LLMPlanner
from scene_layout_react.tools.base import Tool, get_tool_function_spec, make_openai_tool_schema


class DummyTool(Tool):
    name = "dummy_tool"
    description = "Dummy tool for schema validation tests."
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "query": {"type": "string", "description": "Search query."},
            "top_k": {"type": "integer", "description": "Optional result count."},
        },
        required=["query"],
    )


def test_validate_reads_nested_openai_function_schema() -> None:
    tool = DummyTool()

    assert tool.validate({}) == "missing required field: query"
    assert tool.validate({"query": "robot", "extra": True}) == "unknown fields: ['extra']"
    assert tool.validate({"query": "robot", "top_k": 3}) is None


def test_validate_keeps_flat_schema_compatibility() -> None:
    tool = DummyTool()
    tool.schema = {
        "name": "flat_dummy",
        "description": "Legacy flat schema.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "top_k": {"type": "integer"},
            },
            "required": ["query"],
        },
    }

    assert get_tool_function_spec(tool.schema) is tool.schema
    assert tool.validate({}) == "missing required field: query"
    assert tool.validate({"query": "robot", "top_k": 3}) is None


def test_local_tool_prompt_reads_nested_openai_function_schema() -> None:
    planner = LLMPlanner(ProjectConfig())

    prompt = planner._local_tool_system_prompt([DummyTool.schema])

    assert "- dummy_tool: Dummy tool for schema validation tests." in prompt
    assert "query:string (required) Search query." in prompt
    assert "top_k:integer (optional) Optional result count." in prompt
