"""Local causal LLM wrapper used by both one-shot planners and agents."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class GenerationConfig:
    max_new_tokens: int = 512
    temperature: float = 0.2


class LocalCausalLM:
    def __init__(
        self,
        model_name_or_path: str,
        device: str | None = None,
        *,
        use_8bit: bool = False,
        load_in_4bit: bool = False,
        generation: Optional[GenerationConfig] = None,
    ):
        self.model_name_or_path = model_name_or_path
        self.device = device
        self.use_8bit = use_8bit
        self.load_in_4bit = load_in_4bit
        self.generation = generation or GenerationConfig()

        self._model = None
        self._tokenizer = None
        self._device = None

    def _ensure_model(self) -> None:
        if self._model is not None and self._tokenizer is not None:
            return

        if not self.model_name_or_path:
            raise ValueError("llm_name_or_path 未设置，无法加载本地LLM")

        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path, use_fast=False)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        kwargs: Dict[str, Any] = {}
        if self.use_8bit:
            kwargs["load_in_8bit"] = True
            kwargs["device_map"] = "cuda:0"
        elif self.load_in_4bit:
            kwargs["load_in_4bit"] = True
            kwargs["device_map"] = "cuda:0"
        else:
            target = self.device or ("cuda" if torch.cuda.is_available() else "cpu")
            kwargs["device_map"] = None
            kwargs["torch_dtype"] = torch.float16 if target.startswith("cuda") and torch.cuda.is_available() else torch.float32

        model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path, **kwargs)
        if kwargs.get("device_map") is None:
            target = self.device or ("cuda" if torch.cuda.is_available() else "cpu")
            model.to(target)
            self._device = torch.device(target)
        else:
            self._device = next(model.parameters()).device

        self._model = model
        self._tokenizer = tokenizer

    def generate(
        self,
        prompt: str,
        *,
        max_new_tokens: int | None = None,
        temperature: float | None = None,
    ) -> str:
        self._ensure_model()
        assert self._model is not None and self._tokenizer is not None and self._device is not None

        import torch

        inputs = self._tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self._device) for k, v in inputs.items()}
        with torch.no_grad():
            generated = self._model.generate(
                **inputs,
                max_new_tokens=max_new_tokens if max_new_tokens is not None else self.generation.max_new_tokens,
                temperature=temperature if temperature is not None else self.generation.temperature,
                do_sample=(temperature if temperature is not None else self.generation.temperature) > 0,
            )
        generated_ids = generated[0][inputs["input_ids"].shape[1] :]
        return self._tokenizer.decode(generated_ids, skip_special_tokens=True).strip()


__all__ = ["GenerationConfig", "LocalCausalLM"]

