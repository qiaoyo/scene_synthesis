"""LLM-backed planner that generates layout proposals from retrieved assets."""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .data_models import AssetDocument
from .config import ProjectConfig

try:
    import requests as _requests
except ImportError:
    _requests = None

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

    # ------------------------------------------------------------------
    # ReAct interface -- single-turn call used by the agent loop
    # ------------------------------------------------------------------

    def react_call(self, system_prompt: str, user_prompt: str) -> str:
        """Run a single LLM turn for the ReAct agent.

        Supports two backends:
        - **Local model** (default): uses the HuggingFace model loaded by ``_ensure_model()``.
        - **Remote API**: if ``config.model.llm_api_url`` is set, sends a POST
          request to an OpenAI-compatible chat completions endpoint.

        Returns the raw text completion.
        """
        api_url = getattr(self.config.model, "llm_api_url", "")
        if api_url:
            return self._react_call_api(system_prompt, user_prompt)
        return self._react_call_local(system_prompt, user_prompt)

    def _react_call_local(self, system_prompt: str, user_prompt: str) -> str:
        self._ensure_model()
        assert self._model is not None and self._tokenizer is not None

        # Build instruction-style prompt
        prompt = f"[INST] {system_prompt}\n\n{user_prompt} [/INST]"
        inputs = self._tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096)
        inputs = {k: v.to(self._device) for k, v in inputs.items()}
        with torch.no_grad():
            generated = self._model.generate(
                **inputs,
                max_new_tokens=self.config.model.max_new_tokens,
                temperature=self.config.model.temperature,
                do_sample=self.config.model.temperature > 0,
            )
        generated_ids = generated[0][inputs["input_ids"].shape[1]:]
        return self._tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

    def _react_call_api(self, system_prompt: str, user_prompt: str) -> str:
        if _requests is None:
            raise ImportError("requests 库未安装，无法调用远程 API")
        api_url = self.config.model.llm_api_url
        api_key = getattr(self.config.model, "llm_api_key", "")
        model_name = getattr(self.config.model, "llm_api_model", "")
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self.config.model.temperature,
            "max_tokens": self.config.model.max_new_tokens,
        }
        resp = _requests.post(api_url, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        choices = data.get("choices", [])
        if choices:
            return choices[0].get("message", {}).get("content", "")
        return ""


__all__ = ["LLMPlanner"]
