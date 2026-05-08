"""LLM planner.

支持两种后端：
- ``local``: 本地 transformers
- ``openai_sdk``: 通过 OpenAI SDK 调用 Responses API，并把 tool list 直接传给模型

``LLMPlanner`` 暴露 4 个高层方法：
- ``think_and_decide``: 思考 + 决定下一步工具调用
- ``reflect``: 失败时反思
- ``decide_support``: 选择支撑父项
- ``adjust_strategy``: 累积失败后调整全局策略
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .config import ProjectConfig
from .prompts.templates import (
    REFLECT_SYSTEM,
    STRATEGY_SYSTEM,
    SUPPORT_SYSTEM,
    THINK_SYSTEM,
    build_reflect_prompt,
    build_strategy_prompt,
    build_support_prompt,
    build_think_prompt,
)
from .tools.base import get_tool_function_spec


_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)
_CODE_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def _extract_json(text: str) -> Dict[str, Any]:
    """从模型输出里抠出第一个 ``{...}``，解析失败则抛 ValueError。"""
    text = text.strip()
    fenced = _CODE_FENCE_RE.findall(text)
    if fenced:
        text = "\n".join(part.strip() for part in fenced if part.strip()) or text
    # 先尝试整段解析
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    # 再尝试匹配最大花括号块
    m = _JSON_BLOCK_RE.search(text)
    if m is None:
        raise ValueError(f"输出不是 JSON: {text[:200]}")
    snippet = m.group(0)
    try:
        return json.loads(snippet)
    except json.JSONDecodeError:
        # 兜底：去除可能的尾部多余字符
        for end in range(len(snippet), 0, -1):
            try:
                obj = json.loads(snippet[:end])
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                continue
        raise ValueError(f"无法解析 JSON: {snippet[:200]}")


@dataclass
class LLMResponse:
    raw: str
    parsed: Dict[str, Any]


class LLMPlanner:
    """LLM 推理封装。"""

    def __init__(self, config: ProjectConfig):
        if config.model.llm_backend not in {"local", "openai_sdk"}:
            raise ValueError(f"不支持的 llm_backend: {config.model.llm_backend!r}")
        self.config = config
        self._model = None
        self._tokenizer = None
        self._client = None

    # -- 模型生命周期 --

    def _ensure_loaded(self) -> None:
        if self.config.model.llm_backend != "local":
            return
        if self._model is not None:
            return
        from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433
        import torch  # noqa: WPS433

        cfg = self.config.model
        print(f"[LLMPlanner] 加载本地模型: {cfg.llm_name_or_path} -> {cfg.device}")
        kwargs: Dict[str, Any] = {}
        if cfg.load_in_4bit:
            kwargs["load_in_4bit"] = True
        elif cfg.use_8bit:
            kwargs["load_in_8bit"] = True
        else:
            kwargs["torch_dtype"] = torch.bfloat16 if torch.cuda.is_available() else torch.float32

        tokenizer = AutoTokenizer.from_pretrained(cfg.llm_name_or_path, trust_remote_code=True)
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token = tokenizer.eos_token

        model = AutoModelForCausalLM.from_pretrained(
            cfg.llm_name_or_path, trust_remote_code=True, **kwargs
        )
        # 量化模式下不要再 .to(device)，由 accelerate 接管
        if not (cfg.load_in_4bit or cfg.use_8bit):
            model = model.to(cfg.device)
        model.eval()
        self._tokenizer = tokenizer
        self._model = model

    def _ensure_client(self) -> None:
        if self.config.model.llm_backend != "openai_sdk":
            return
        if self._client is not None:
            return
        if not self.config.model.llm_api_key:
            raise ValueError("llm_api_key 为空，无法使用 openai_sdk 后端")
        from openai import OpenAI  # noqa: WPS433

        self._client = OpenAI(
            api_key=self.config.model.llm_api_key,
            base_url=self.config.model.llm_api_base_url,
        )

    def _generate_local(self, messages: List[Dict[str, str]], force_greedy: bool = False) -> str:
        self._ensure_loaded()
        import torch  # noqa: WPS433

        tokenizer = self._tokenizer
        model = self._model
        cfg = self.config.model
        prompt = self._build_local_prompt(messages)
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        generation_kwargs: Dict[str, Any] = {
            "max_new_tokens": cfg.max_new_tokens,
            "pad_token_id": tokenizer.pad_token_id,
            "do_sample": False if force_greedy else cfg.temperature > 0,
        }
        if generation_kwargs["do_sample"]:
            generation_kwargs["temperature"] = max(cfg.temperature, 1e-5)

        with torch.no_grad():
            outputs = model.generate(**inputs, **generation_kwargs)
        new_tokens = outputs[0, inputs["input_ids"].shape[1]:]
        return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

    def _build_local_prompt(self, messages: List[Dict[str, str]]) -> str:
        tokenizer = self._tokenizer
        model_name = self.config.model.llm_name_or_path.lower()
        if "mistral" in model_name:
            parts = [item["content"].strip() for item in messages if item.get("content")]
            body = "\n\n".join(parts)
            return f"[INST] {body} [/INST]"
        if hasattr(tokenizer, "apply_chat_template"):
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        system = ""
        user = ""
        for item in messages:
            if item.get("role") == "system":
                system = item.get("content", "")
            elif item.get("role") == "user":
                user = item.get("content", "")
        return f"<<SYS>>\n{system}\n<</SYS>>\n\n{user}\n"

    def _local_tool_system_prompt(self, tools: List[Dict[str, Any]]) -> str:
        lines = [
            "You are a tool-calling planner.",
            "Available tools:",
        ]
        for tool in tools:
            function_spec = get_tool_function_spec(tool)
            params = function_spec.get("parameters", {})
            properties = params.get("properties", {})
            required = set(params.get("required", []))
            arg_lines = []
            for param_name, spec in properties.items():
                spec_type = spec.get("type")
                if spec_type is None and "anyOf" in spec:
                    spec_type = "|".join(
                        item.get("type", "any")
                        for item in spec["anyOf"]
                        if isinstance(item, dict)
                    ) or "any"
                desc = spec.get("description", "")
                suffix = "required" if param_name in required else "optional"
                arg_lines.append(f"{param_name}:{spec_type or 'any'} ({suffix}) {desc}")
            args = "; ".join(arg_lines) if arg_lines else "(no parameters)"
            lines.append(
                f"- {function_spec['name']}: {function_spec.get('description', '')} | {args}"
            )
        lines.extend([
            "",
            "Rules:",
            "1. When choosing a tool, output exactly one JSON object and nothing else.",
            "2. Preferred format: {\"thought\":\"...\",\"action\":\"tool_name\",\"action_input\":{...}}.",
            "3. If the task is complete, output: {\"thought\":\"...\",\"action\":\"finish\",\"action_input\":{\"reason\":\"...\"}}.",
            "4. action must be one of the available tool names or finish.",
            "5. action_input may only contain fields defined for the selected tool.",
            "6. Do not use markdown, code fences, or natural-language explanations outside JSON.",
        ])
        return "\n".join(lines)

    @staticmethod
    def _normalize_tool_decision(parsed: Dict[str, Any]) -> Dict[str, Any]:
        if "action" in parsed:
            action_input = parsed.get("action_input")
            if action_input is None:
                parsed["action_input"] = {}
            elif not isinstance(action_input, dict):
                parsed["action_input"] = {"_invalid": action_input}
            parsed["thought"] = str(parsed.get("thought", ""))
            return parsed
        if "name" in parsed:
            parameters = parsed.get("parameters")
            if parameters is None:
                parameters = {}
            elif not isinstance(parameters, dict):
                parameters = {"_invalid": parameters}
            return {
                "thought": str(parsed.get("thought", "")),
                "action": str(parsed.get("name", "")),
                "action_input": parameters,
            }
        return parsed

    # -- 通用 chat 调用 --

    def _chat(self, system: str, user: str) -> LLMResponse:
        if self.config.model.llm_backend == "openai_sdk":
            return self._chat_openai(system, user)
        text = self._generate_local([
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ])
        parsed: Dict[str, Any]
        try:
            parsed = _extract_json(text)
        except ValueError as exc:
            print(f"[LLMPlanner] JSON 解析失败: {exc}")
            parsed = {"_parse_error": str(exc), "_raw": text[:500]}
        return LLMResponse(raw=text, parsed=parsed)

    def _tool_chat_local(self, system: str, user: str, tools: List[Dict[str, Any]]) -> LLMResponse:
        text = self._generate_local([
            {"role": "system", "content": system},
            {"role": "system", "content": self._local_tool_system_prompt(tools)},
            {"role": "user", "content": user},
        ], force_greedy=True)
        try:
            parsed = self._normalize_tool_decision(_extract_json(text))
        except ValueError as exc:
            print(f"[LLMPlanner] Local tool JSON 解析失败: {exc}")
            parsed = {"_parse_error": str(exc), "_raw": text[:500]}
        return LLMResponse(raw=text, parsed=parsed)

    def _chat_openai(self, system: str, user: str) -> LLMResponse:
        self._ensure_client()
        response = self._client.responses.create(
            model=self.config.model.llm_api_model,
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        text = getattr(response, "output_text", "") or ""
        try:
            parsed = _extract_json(text)
        except ValueError as exc:
            print(f"[LLMPlanner] OpenAI JSON 解析失败: {exc}")
            parsed = {"_parse_error": str(exc), "_raw": text[:500]}
        return LLMResponse(raw=text, parsed=parsed)

    def _tool_chat_openai(self, system: str, user: str, tools: List[Dict[str, Any]]) -> LLMResponse:
        self._ensure_client()
        response = self._client.responses.create(
            model=self.config.model.llm_api_model,
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            tools=tools,
            tool_choice="required",
        )
        parsed = self._parse_tool_decision(response)
        raw = getattr(response, "output_text", "") or json.dumps(parsed, ensure_ascii=False)
        return LLMResponse(raw=raw, parsed=parsed)

    def _parse_tool_decision(self, response: Any) -> Dict[str, Any]:
        output = getattr(response, "output", None) or []
        for item in output:
            item_type = getattr(item, "type", None)
            if item_type == "function_call":
                raw_args = getattr(item, "arguments", "") or "{}"
                try:
                    arguments = json.loads(raw_args)
                except json.JSONDecodeError as exc:
                    return {
                        "_parse_error": f"tool arguments 不是合法 JSON: {exc}",
                        "_raw": raw_args[:500],
                    }
                return self._normalize_tool_decision({
                    "thought": "",
                    "name": getattr(item, "name", ""),
                    "parameters": arguments,
                })
        text = getattr(response, "output_text", "") or ""
        try:
            parsed = self._normalize_tool_decision(_extract_json(text))
        except ValueError as exc:
            return {"_parse_error": str(exc), "_raw": text[:500]}
        return parsed

    # -- 高层 API --

    def think_and_decide(
        self,
        command: str,
        scene_summary: Dict[str, Any],
        last_observation: Optional[Dict[str, Any]],
        tool_specs: List[Dict[str, Any]],
        lessons: List[Dict[str, Any]],
        strategy: Optional[str],
        step: int,
        max_steps: int,
    ) -> LLMResponse:
        prompt = build_think_prompt(
            command=command,
            scene_summary=scene_summary,
            last_observation=last_observation,
            tool_specs=tool_specs,
            lessons=lessons,
            strategy=strategy,
            step=step,
            max_steps=max_steps,
        )
        if self.config.model.llm_backend == "openai_sdk":
            return self._tool_chat_openai(THINK_SYSTEM, prompt, tool_specs)
        if self.config.model.llm_backend == "local":
            return self._tool_chat_local(THINK_SYSTEM, prompt, tool_specs)
        return self._chat(THINK_SYSTEM, prompt)

    def reflect(
        self,
        thought: str,
        action: str,
        action_input: Dict[str, Any],
        observation: Dict[str, Any],
        command: str,
    ) -> LLMResponse:
        prompt = build_reflect_prompt(thought, action, action_input, observation, command)
        return self._chat(REFLECT_SYSTEM, prompt)

    def decide_support(
        self,
        child_id: str,
        child_summary: Dict[str, Any],
        candidates: List[Dict[str, Any]],
        context: str,
    ) -> LLMResponse:
        prompt = build_support_prompt(child_id, child_summary, candidates, context)
        return self._chat(SUPPORT_SYSTEM, prompt)

    def adjust_strategy(
        self,
        command: str,
        recent_observations: List[Dict[str, Any]],
        recent_reflections: List[Dict[str, Any]],
    ) -> LLMResponse:
        prompt = build_strategy_prompt(command, recent_observations, recent_reflections)
        return self._chat(STRATEGY_SYSTEM, prompt)


__all__ = ["LLMPlanner", "LLMResponse"]
