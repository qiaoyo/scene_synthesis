"""LLM-backed planner that generates layout proposals from retrieved assets."""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Sequence, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .data_models import AssetDocument
from .config import ProjectConfig

_PROMPT_TEMPLATE = """你是一名工业场景布局规划助手。你会得到一个自然语言需求和若干资产信息。
每个资产包含唯一ID、USD路径、功能描述以及包围盒尺寸(bbox)。
请综合需求与资产信息，规划这些资产在场景中的位置，输出 JSON 数组，每个元素结构如下：
{{
  "asset_id": "资产编号",
  "usd_path": "USD路径",
  "position": {{"x": 浮点数, "y": 浮点数, "z": 浮点数}},
  "reason": "简短中文说明"
}}
坐标范围建议在 -10 到 10 米。
需求: {command}
资产信息:
{assets}
请只输出上述 JSON 数组，不要添加多余说明。"""


class LLMPlanner:
    """Generate layout proposals with a local CausalLM."""

    def __init__(self, config: ProjectConfig):
        self.config = config
        self._model = None
        self._tokenizer = None
        self._device = config.model.device

    def _ensure_model(self) -> None:
        if self._model is not None and self._tokenizer is not None:
            return
        model_name = self.config.model.llm_name_or_path
        if not model_name:
            raise ValueError("ModelConfig.llm_name_or_path 未设置，无法加载本地LLM")
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        kwargs: Dict[str, Any] = {}
        if self.config.model.use_8bit:
            kwargs["load_in_8bit"] = True
            kwargs["device_map"] = "cuda:0"
        elif self.config.model.load_in_4bit:
            kwargs["load_in_4bit"] = True
            kwargs["device_map"] = "cuda:0"
        else:
            device = self.config.model.device or ("cuda" if torch.cuda.is_available() else "cpu")
            kwargs["device_map"] = None
            kwargs["torch_dtype"] = torch.float16 if device.startswith("cuda") and torch.cuda.is_available() else torch.float32
        model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
        if kwargs.get("device_map") is None:
            target_device = self.config.model.device or ("cuda" if torch.cuda.is_available() else "cpu")
            model.to(target_device)
            self._device = torch.device(target_device)
        else:
            self._device = next(model.parameters()).device
        self._model = model
        self._tokenizer = tokenizer

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

    def plan(self, command: str, documents: Sequence[AssetDocument]) -> Tuple[str, List[Dict[str, Any]]]:
        self._ensure_model()
        assert self._model is not None and self._tokenizer is not None
        assets_text = self._format_assets(documents)
        prompt = _PROMPT_TEMPLATE.format(command=command, assets=assets_text)
        inputs = self._tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self._device) for k, v in inputs.items()}
        with torch.no_grad():
            generated = self._model.generate(
                **inputs,
                max_new_tokens=self.config.model.max_new_tokens,
                temperature=self.config.model.temperature,
                do_sample=self.config.model.temperature > 0,
            )
        generated_ids = generated[0][inputs["input_ids"].shape[1] :]
        completion = self._tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        placements = self._extract_json(completion)
        return completion, placements


__all__ = ["LLMPlanner"]
