"""Prompt templates used by the ReAct agent and LLM planner."""
from __future__ import annotations

import json
from typing import Any, Dict, List

# =====================================================================
# System prompt -- injected once at the start of the conversation
# =====================================================================

SYSTEM_PROMPT = """\
你是一名工业场景布局规划专家。你将使用工具逐步构建 3D 工业场景。

## 工作流程
1. 分析用户需求，确定需要哪些资产
2. 使用 retrieve_assets 工具检索合适的资产
3. 使用 place_instance 工具逐个放置资产
4. 使用 query_scene / check_collision 等工具验证布局
5. 根据观测反馈调整位置，直到布局合理
6. 完成后输出 finish

## 重要规则
- 放置资产前，先用 retrieve_assets 检索确认可用资产
- 放置承载物（如 Box）前，先用 query_scene 查询父物体的尺寸和位置
- 坐标系：X 轴向右，Y 轴向前，Z 轴向上；坐标范围建议在 -10 到 10 米
- 注意资产间留出足够通道（AGV 至少 2m）
- 每次只执行一个工具调用

## 可用工具
{tools_description}

## 资产库概况
{catalog_summary}
"""

# =====================================================================
# Per-step prompt -- sent each iteration of the ReAct loop
# =====================================================================

STEP_PROMPT = """\
## 用户需求
{command}

## 当前场景状态
{scene_state}

## 上一步观测结果
{last_observation}

## 已检索到的资产（工作记忆）
{retrieved_assets}

## 历史教训
{lessons_learned}

{strategy_section}

请输出你的下一步决策，严格使用以下 JSON 格式：
```json
{{
  "thought": "你的推理过程（中文）",
  "action": "工具名称",
  "action_input": {{参数字典}}
}}
```

当场景已满足所有需求时，输出：
```json
{{
  "thought": "场景已完成，满足所有需求",
  "action": "finish",
  "action_input": {{}}
}}
```"""

# =====================================================================
# Reflection prompt
# =====================================================================

REFLECT_PROMPT = """\
你是一名场景布局专家，正在分析上一步操作失败的原因。

## 你的推理
{thought}

## 你执行的操作
工具: {action}
参数: {action_input}

## 观测结果（包含问题）
{observation}

请分析失败原因并总结经验教训，严格使用以下 JSON 格式：
```json
{{
  "mistake": "具体错误描述",
  "root_cause": "根本原因分析",
  "correction": "下次应该怎么做"
}}
```"""

# =====================================================================
# Strategy adjustment prompt
# =====================================================================

STRATEGY_PROMPT = """\
你在场景布局过程中连续遇到了问题，需要调整整体策略。

## 用户需求
{command}

## 累积的教训
{lessons}

## 最近的观测
{observation}

请制定新的布局策略（用一段简短中文描述），重点说明：
1. 接下来应该优先做什么
2. 应该避免什么
3. 关键的约束条件"""

# =====================================================================
# Support decision prompt (Phase 4)
# =====================================================================

SUPPORT_PROMPT = """\
你需要决定一个物体的支撑关系。

## 子物体（需要被支撑的）
ID: {child_id}
类型: {child_type}
位置: {child_position}
包围盒: {child_bbox}

## 候选父物体（可能提供支撑的）
{candidates}

## 当前场景上下文
{context}

请选择最合适的父物体，输出 JSON：
```json
{{
  "parent_id": "选中的父物体实例 ID",
  "confidence": 0.0到1.0的置信度,
  "reason": "选择理由"
}}
```"""


# =====================================================================
# Formatting helpers
# =====================================================================

def _json_compact(obj: Any) -> str:
    """Return compact JSON string for prompt injection."""
    return json.dumps(obj, ensure_ascii=False, indent=None, default=str)


def format_step_prompt(
    command: str,
    scene_state: dict,
    last_observation: dict,
    retrieved_assets: list,
    lessons_learned: list,
    strategy: str | None = None,
) -> str:
    strategy_section = ""
    if strategy:
        strategy_section = f"## 当前策略\n{strategy}"

    lessons_text = "无" if not lessons_learned else _json_compact(lessons_learned)
    assets_text = "尚未检索" if not retrieved_assets else _json_compact(retrieved_assets)

    return STEP_PROMPT.format(
        command=command,
        scene_state=_json_compact(scene_state),
        last_observation=_json_compact(last_observation),
        retrieved_assets=assets_text,
        lessons_learned=lessons_text,
        strategy_section=strategy_section,
    )


def format_reflect_prompt(
    thought: str,
    action: str,
    action_input: dict,
    observation: dict,
) -> str:
    return REFLECT_PROMPT.format(
        thought=thought,
        action=action,
        action_input=_json_compact(action_input),
        observation=_json_compact(observation),
    )


def format_strategy_prompt(
    command: str,
    lessons: list,
    observation: dict,
) -> str:
    return STRATEGY_PROMPT.format(
        command=command,
        lessons=_json_compact(lessons),
        observation=_json_compact(observation),
    )


def format_support_prompt(
    child_id: str,
    child_type: str,
    child_position: list,
    child_bbox: list,
    candidates: list,
    context: dict,
) -> str:
    cand_text = "\n".join(
        f"- {c['instance_id']} ({c['asset_id']}): "
        f"top_z={c.get('top_z', '?')}, overlap={c.get('xy_overlap_ratio', '?')}"
        for c in candidates
    )
    return SUPPORT_PROMPT.format(
        child_id=child_id,
        child_type=child_type,
        child_position=child_position,
        child_bbox=child_bbox,
        candidates=cand_text or "无候选",
        context=_json_compact(context),
    )
