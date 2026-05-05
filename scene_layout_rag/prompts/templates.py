"""Prompt templates for the ReAct loop.

设计原则：
- LLM 输出必须是 JSON，便于鲁棒解析。
- 每个 prompt 都附上完整的工具规格 + 当前观测，让 LLM 不需要长期记忆历史。
- 反思 prompt 强调「下次怎么做」而不是「为什么会错」，避免空洞自责。
"""
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional


THINK_SYSTEM = (
    "You are a scene-layout planner that designs industrial scenes by calling tools. "
    "Output strictly a single JSON object: {\"thought\": str, \"action\": str, \"action_input\": object}. "
    "`action` must be one of the registered tool names. "
    "`action_input` keys must match the tool's parameters.properties. "
    "Use retrieval in stages: retrieve_scene_prior for scene type; "
    "retrieve_scene_template for a structured template skeleton; retrieve_assets only for concrete placeable assets. "
    "Treat Scene summary.working_memory as authoritative progress state. "
    "Do not repeat a completed retrieval stage. "
    "Only doc_ids returned by retrieve_assets may be used as place_instance.asset_doc_id. "
    "If the goal is already met, set action to \"finish\" with reason in action_input.reason."
)

REFLECT_SYSTEM = (
    "You are a self-critical planning assistant. Given a failed step (thought/action/observation), "
    "produce a JSON object: {\"summary\": str, \"cause\": str, \"next_strategy\": str}. "
    "next_strategy must be a concrete plan the planner can use on the next step."
)

SUPPORT_SYSTEM = (
    "You are deciding which existing instance should support a child instance. "
    "Output strictly: {\"parent_instance_id\": str, \"reason\": str}. "
    "If no instance is suitable, set parent_instance_id to null."
)

STRATEGY_SYSTEM = (
    "You are adjusting the planning strategy after repeated failures. "
    "Output strictly: {\"strategy\": str}. The strategy should be a 1-3 sentence directive "
    "the planner will follow on subsequent steps."
)


def _dump(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def build_think_prompt(
    command: str,
    scene_summary: Dict[str, Any],
    last_observation: Optional[Dict[str, Any]],
    tool_specs: List[Dict[str, Any]],
    lessons: List[Dict[str, Any]],
    strategy: Optional[str],
    step: int,
    max_steps: int,
) -> str:
    parts = [
        f"User command: {command}",
        f"Step {step + 1} / {max_steps}",
        f"Current strategy: {strategy or '(none yet)'}",
        f"Scene summary: {_dump(scene_summary)}",
        f"Last observation: {_dump(last_observation) if last_observation else '(no previous step)'}",
        f"Lessons learned: {_dump(lessons) if lessons else '(empty)'}",
        f"Available tools: {_dump(tool_specs)}",
        "",
        "Pick the next tool call. Remember: "
        "1) if the scene type is unclear, call retrieve_scene_prior; "
        "2) if working_memory.scene_type is filled, do not call retrieve_scene_prior again; "
        "3) after the scene type is known, call retrieve_scene_template to populate working_memory.template_instances; "
        "4) if working_memory.template_instances is filled, iterate those entries: retrieve_assets for the entry's asset_type, then place_instance at the template position when present; "
        "5) before placing an object, call retrieve_assets for that asset_type and use only returned asset doc_ids; "
        "6) never pass scene_prior or scene_template doc_ids to place_instance; "
        "7) call query_scene before move/delete to confirm exact ids and sizes; "
        "8) when you finish, return action='finish'.",
    ]
    return "\n\n".join(parts)


def build_reflect_prompt(
    thought: str,
    action: str,
    action_input: Dict[str, Any],
    observation: Dict[str, Any],
    command: str,
) -> str:
    return "\n\n".join([
        f"User command: {command}",
        f"Thought: {thought}",
        f"Action: {action}",
        f"Action input: {_dump(action_input)}",
        f"Observation: {_dump(observation)}",
        "Why did this step fail or fall short, and what should we try next? "
        "Classify the cause when possible: wrong scene prior, wrong template/layout interpretation, "
        "wrong asset choice, invalid geometry/collision, invalid support relation, or invalid tool input. "
        "If an asset_doc_id was invalid, the next strategy must use retrieve_assets, not scene prior/template retrieval.",
    ])


def build_support_prompt(
    child_id: str,
    child_summary: Dict[str, Any],
    candidates: List[Dict[str, Any]],
    context: str,
) -> str:
    return "\n\n".join([
        f"Child instance: {child_id}",
        f"Child summary: {_dump(child_summary)}",
        f"Candidate parents: {_dump(candidates)}",
        f"Context: {context}",
        "Choose the best parent or null.",
    ])


def build_strategy_prompt(
    command: str,
    recent_observations: List[Dict[str, Any]],
    recent_reflections: List[Dict[str, Any]],
) -> str:
    return "\n\n".join([
        f"User command: {command}",
        f"Recent observations: {_dump(recent_observations)}",
        f"Recent reflections: {_dump(recent_reflections)}",
        "Propose a single, concrete strategy adjustment for the next steps.",
    ])
