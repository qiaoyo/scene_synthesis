"""LLM-backed planner that generates layout proposals from retrieved assets."""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Sequence, Tuple

from .data_models import AssetDocument
from .config import ProjectConfig
from .local_llm import GenerationConfig, LocalCausalLM

# _PROMPT_TEMPLATE = """你是一名工业场景布局规划助手。你会得到一个自然语言需求和若干资产信息。
# 每个资产包含唯一ID、USD路径、功能描述以及包围盒尺寸(bbox)。
# 请综合需求与资产信息以及场景上下文，规划这些资产在场景中的位置，输出 JSON 数组，每个元素结构如下：
# {{
#   "asset_id": "资产编号",
#   "usd_path": "USD路径",
#   "position": {{"x": 浮点数, "y": 浮点数, "z": 浮点数}},
#   "reason": "简短中文说明"
# }}
# 坐标范围建议在 -10 到 10 米。
# 需求: {command}
# 资产信息:
# {assets}
# 场景上下文:
# {scene_context}
# 请只输出上述 JSON 数组，不要添加多余说明。"""

_PROMPT_TEMPLATE ="""You are an industrial scene layout planning assistant. You will receive a natural language requirement along with several asset descriptions.  
Each asset includes a unique ID, USD path, functional description, and bounding box dimensions (bbox).  
You will also receive scene context which may include existing referenced Xforms with world-space bounding boxes/centers.  
Use the scene context as constraints/anchors when relevant (e.g., reuse an existing center as a suggested placement for a similar item type).  
Based on the requirement, asset information, and scene context, plan the placement of these assets within the scene.  
Output a JSON array where each element has the following structure:
{{
  "asset_id": "Asset ID",
  "usd_path": "USD path",
  "position": {{"x": float, "y": float, "z": float}},
  "reason": "Brief explanation in English"
}}
Recommended coordinate range: -10 to 10 meters.  
Requirement: {command}  
Asset Information:  
{assets}  
Scene Context:  
{scene_context}  
Please output only the JSON array above, without any additional explanation.
"""

class LLMPlanner:
    """Generate layout proposals with a local CausalLM."""

    def __init__(self, config: ProjectConfig):
        self.config = config
        self._llm = LocalCausalLM(
            model_name_or_path=config.model.llm_name_or_path,
            device=config.model.device,
            use_8bit=config.model.use_8bit,
            load_in_4bit=config.model.load_in_4bit,
            generation=GenerationConfig(
                max_new_tokens=config.model.max_new_tokens,
                temperature=config.model.temperature,
            ),
        )

    def _format_assets(self, documents: Sequence[AssetDocument]) -> str:
        lines = []
        for doc in documents:
            asset_id = doc.metadata.get("asset_category", doc.doc_id)
            usd_path = doc.metadata.get("usd_path", "未知")
            bbox = doc.metadata.get("bbox") or {"size": [1.0, 1.0, 1.0], "unit": "m"}
            bbox_text = json.dumps(bbox, ensure_ascii=False)
            snippet = doc.content.replace("\n", " ")
            if len(snippet) > 280:
                snippet = snippet[:280] + "..."
            lines.append(f"- ID:{asset_id} | USD:{usd_path} | bbox:{bbox_text} | 描述:{snippet}")
        return "\n".join(lines)

    def _format_scene_context(self, documents: Sequence[AssetDocument], max_items: int = 16) -> str:
        if not documents:
            return "(none)"
        lines: List[str] = []
        for doc in list(documents)[:max_items]:
            kind = doc.metadata.get("md_kind", "md")
            if kind == "referenced_xform":
                prim = doc.metadata.get("prim_path", "")
                payload = doc.metadata.get("payload", "")
                bbox = doc.metadata.get("bbox_world") or {}
                size = bbox.get("size")
                center = bbox.get("center")
                lines.append(f"- Xform:{prim} payload:{payload} bbox_world.size:{size} bbox_world.center:{center}")
            elif kind == "scene_meta":
                usda = doc.metadata.get("usda_path", "")
                unit = doc.metadata.get("meters_per_unit", "")
                axis = doc.metadata.get("up_axis", "")
                lines.append(f"- SceneMeta usda:{usda} meters_per_unit:{unit} up_axis:{axis}")
            else:
                snippet = doc.content.replace("\n", " ").strip()
                if len(snippet) > 280:
                    snippet = snippet[:280] + "..."
                lines.append(f"- {snippet}")
        return "\n".join(lines) if lines else "(none)"

    def _extract_json(self, text: str) -> List[Dict[str, Any]]:
        match = re.search(r"\[[\s\S]*\]", text)
        if not match:
            return []
        segment = match.group(0)
        try:
            data = json.loads(segment)
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict)]
        except json.JSONDecodeError:
            return []
        return []

    def plan(
        self,
        command: str,
        asset_documents: Sequence[AssetDocument],
        scene_documents: Sequence[AssetDocument] | None = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        assets_text = self._format_assets(asset_documents)
        scene_text = self._format_scene_context(scene_documents or [])
        prompt = _PROMPT_TEMPLATE.format(command=command, assets=assets_text, scene_context=scene_text)
        completion = self._llm.generate(prompt)
        placements = self._extract_json(completion)
        return completion, placements

__all__ = ["LLMPlanner"]
