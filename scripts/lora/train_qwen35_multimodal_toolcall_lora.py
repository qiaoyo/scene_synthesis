from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.nn.utils.rnn import pad_sequence
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)


IGNORE_INDEX = -100
LANGUAGE_MODULE_HINTS = (
    "language_model",
    "text_model",
    "model.layers",
    "model.decoder.layers",
)
DEFAULT_TARGET_SUFFIXES = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOSS_MODES = ("plain", "toolcall", "role_aware")
PLAN_TOOLS = {"retrieve_asset", "place_instance"}
TERMINATION_TOOLS = {"save_scene_usd"}
ROLE_ORDER = ("plan", "correction", "termination", "final")
DEFAULT_OUTPUT_DIRS = {
    "plain": Path("outputs/lora/qwen35_plain_lora"),
    "toolcall": Path("outputs/lora/qwen35_toolcall_lora"),
    "role_aware": Path("outputs/lora/qwen35_roleaware_toolcall_lora"),
}


if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Train a Qwen3.5 multimodal tool-call LoRA adapter using text-only "
            "scene_layout_react SFT records. This is separate from the CausalLM "
            "trainer because Qwen3.5-27B is an ImageTextToText model."
        )
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/lora/jsonl/toolcall_sft_all.jsonl"),
        help="Training JSON or JSONL file containing messages and assistant tool-call targets.",
    )
    parser.add_argument(
        "--eval-data-path",
        type=Path,
        default=None,
        help=(
            "Optional validation JSON or JSONL file. When provided, eval loss "
            "is logged during training."
        ),
    )
    parser.add_argument(
        "--model-name-or-path",
        type=str,
        required=True,
        help="Qwen3.5-27B model path or Hugging Face model id.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Directory for LoRA checkpoints and final adapter. Defaults to a "
            "mode-specific directory under outputs/lora."
        ),
    )
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--logging-steps", type=int, default=1)
    parser.add_argument("--save-steps", type=int, default=20)
    parser.add_argument(
        "--loss-mode",
        choices=LOSS_MODES,
        default="toolcall",
        help=(
            "Training objective variant: plain assistant-only SFT, current "
            "tool-call function-name weighting, or role-aware tool-call weighting."
        ),
    )
    parser.add_argument(
        "--tca-loss-weight",
        type=float,
        default=3.0,
        help=(
            "Loss multiplier for assistant tool function-name tokens. "
            "Use 1.0 for standard assistant-only SFT."
        ),
    )
    parser.add_argument(
        "--role-alpha",
        type=float,
        default=0.5,
        help="Role reweighting exponent for --loss-mode role_aware.",
    )
    parser.add_argument(
        "--role-weight-normalize",
        dest="role_weight_normalize",
        action="store_true",
        default=True,
        help="Normalize role weights to keep the train-set mean near 1.0.",
    )
    parser.add_argument(
        "--no-role-weight-normalize",
        dest="role_weight_normalize",
        action="store_false",
        help="Disable role-weight mean normalization.",
    )
    parser.add_argument(
        "--eval-steps",
        type=int,
        default=None,
        help="Evaluate every N optimizer steps. Defaults to --save-steps.",
    )
    parser.add_argument(
        "--metric-log-path",
        type=Path,
        default=None,
        help=(
            "JSONL path for train/eval loss logs. Defaults to "
            "<output-dir>/metrics_log.jsonl."
        ),
    )
    parser.add_argument("--no-4bit", action="store_true", help="Disable QLoRA 4-bit loading.")
    parser.add_argument("--bf16", action="store_true", help="Use bf16 training.")
    parser.add_argument("--fp16", action="store_true", help="Use fp16 training.")
    parser.add_argument(
        "--disable-thinking",
        dest="enable_thinking",
        action="store_false",
        help="Render Qwen chat templates with enable_thinking=False.",
    )
    parser.add_argument(
        "--gradient-checkpointing",
        action="store_true",
        help="Enable gradient checkpointing to reduce memory use.",
    )
    parser.add_argument(
        "--resume-from-checkpoint",
        type=Path,
        default=None,
        help="Resume Trainer state from a checkpoint directory.",
    )
    parser.add_argument(
        "--target-suffixes",
        nargs="+",
        default=list(DEFAULT_TARGET_SUFFIXES),
        help="Linear module name suffixes to adapt on the language side.",
    )
    parser.set_defaults(enable_thinking=True)
    args = parser.parse_args()
    if args.output_dir is None:
        args.output_dir = DEFAULT_OUTPUT_DIRS[args.loss_mode]
    return args


def load_tool_specs() -> list[dict[str, Any]]:
    from scene_layout_react.tools import TOOL_REGISTRY

    return [
        json.loads(json.dumps(tool.schema, ensure_ascii=False))
        for tool in TOOL_REGISTRY.values()
    ]


def load_records(path: Path) -> list[dict[str, Any]]:
    path = path.expanduser()
    if path.is_dir():
        raise IsADirectoryError(
            f"{path} is a directory, but --data-path/--eval-data-path must be a "
            "JSON or JSONL file. If you used $TRAIN_DATA or $TEST_DATA, export "
            "those variables before running the command."
        )
    if not path.exists():
        raise FileNotFoundError(
            f"{path} does not exist. Check --data-path/--eval-data-path or "
            "export the TRAIN_DATA/TEST_DATA variables first."
        )
    if path.suffix == ".jsonl":
        records = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                records.append(json.loads(line))
        return records

    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("samples"), list):
        return payload["samples"]
    if isinstance(payload, dict) and isinstance(payload.get("messages"), list):
        return [payload]
    raise ValueError(f"Unsupported dataset format: {path}")


def normalize_tool_calls(tool_calls: Any) -> list[dict[str, Any]]:
    if not isinstance(tool_calls, list) or not tool_calls:
        raise ValueError("assistant.tool_calls must be a non-empty list.")

    normalized = []
    for call in tool_calls:
        if not isinstance(call, dict):
            raise ValueError(f"tool call must be an object: {call!r}")

        function = call.get("function")
        if isinstance(function, dict):
            name = function.get("name")
            arguments = function.get("arguments", "{}")
        else:
            name = call.get("name")
            arguments = call.get("arguments", {})

        if not isinstance(name, str) or not name:
            raise ValueError(f"tool call function name must be a non-empty string: {call!r}")

        if arguments is None:
            arguments_obj: dict[str, Any] = {}
        elif isinstance(arguments, str):
            try:
                parsed_arguments = json.loads(arguments or "{}")
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"tool call arguments for {name} must be valid JSON."
                ) from exc
            if not isinstance(parsed_arguments, dict):
                raise ValueError(
                    f"tool call arguments for {name} must decode to a JSON object."
                )
            arguments_obj = parsed_arguments
        elif isinstance(arguments, dict):
            arguments_obj = arguments
        else:
            raise ValueError(
                f"tool call arguments for {name} must be a dict or JSON object string."
            )

        normalized_call = {
            "type": call.get("type", "function"),
            "function": {
                "name": name,
                "arguments": arguments_obj,
            },
        }
        if isinstance(call.get("id"), str):
            normalized_call["id"] = call["id"]
        normalized.append(normalized_call)

    return normalized


def serialize_tool_calls(tool_calls: list[dict[str, Any]]) -> str:
    return json.dumps(
        {"tool_calls": tool_calls},
        ensure_ascii=False,
        separators=(",", ":"),
    )


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    messages = record.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        raise ValueError("Each record must contain a messages list.")
    if messages[-1].get("role") != "assistant":
        raise ValueError("The last message must be the assistant target.")

    messages = [dict(item) for item in messages]
    assistant = messages[-1]
    if assistant.get("tool_calls"):
        assistant["tool_calls"] = normalize_tool_calls(assistant["tool_calls"])
        if not isinstance(assistant.get("content"), str):
            assistant["content"] = ""
        return {"messages": messages}

    if not isinstance(assistant.get("content"), str):
        target = record.get("expected_output")
        if target is None:
            raise ValueError("Assistant target must be content string or expected_output.")
        assistant["content"] = json.dumps(target, ensure_ascii=False, separators=(",", ":"))
    return {"messages": messages}


def tool_calls_from_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    assistant = record["messages"][-1]
    raw_calls = assistant.get("tool_calls")
    if not raw_calls:
        return []
    return normalize_tool_calls(raw_calls)


def tool_names_from_record(record: dict[str, Any]) -> list[str]:
    return [
        call["function"]["name"]
        for call in tool_calls_from_record(record)
    ]


def role_for_tool_names(tool_names: list[str]) -> str:
    if not tool_names:
        return "final"
    if any(name in PLAN_TOOLS for name in tool_names):
        return "plan"
    if any(name in TERMINATION_TOOLS for name in tool_names):
        return "termination"
    return "correction"


def role_for_record(record: dict[str, Any]) -> str:
    return role_for_tool_names(tool_names_from_record(record))


def count_record_roles(records: list[dict[str, Any]]) -> dict[str, int]:
    counts = {role: 0 for role in ROLE_ORDER}
    for record in records:
        role = role_for_record(record)
        counts[role] = counts.get(role, 0) + 1
    return counts


def compute_role_weights(
    role_counts: dict[str, int],
    *,
    alpha: float,
    normalize: bool = True,
) -> dict[str, float]:
    total = sum(max(count, 0) for count in role_counts.values())
    if total <= 0:
        return {role: 1.0 for role in ROLE_ORDER}

    weights: dict[str, float] = {}
    for role in ROLE_ORDER:
        count = max(role_counts.get(role, 0), 0)
        weights[role] = (total / count) ** alpha if count else 1.0

    if normalize:
        weighted_mean = sum(
            weights[role] * role_counts.get(role, 0)
            for role in ROLE_ORDER
        ) / total
        if weighted_mean > 0.0:
            weights = {
                role: weight / weighted_mean
                if role_counts.get(role, 0) > 0
                else 1.0
                for role, weight in weights.items()
            }
    return weights


def render_chat(
    processor: Any,
    messages: list[dict[str, Any]],
    add_generation_prompt: bool,
    *,
    tools: list[dict[str, Any]] | None = None,
    enable_thinking: bool = True,
) -> str:
    return processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
        tools=tools,
        enable_thinking=enable_thinking,
    )


def token_offsets(tokenizer: Any, text: str) -> tuple[list[int], list[tuple[int, int]] | None]:
    try:
        encoded = tokenizer(
            text,
            add_special_tokens=False,
            return_offsets_mapping=True,
        )
    except (NotImplementedError, TypeError):
        encoded = tokenizer(text, add_special_tokens=False)
        return encoded["input_ids"], None
    return encoded["input_ids"], encoded.get("offset_mapping")


def find_tool_name_spans(
    text: str,
    tool_names: list[str],
    start: int,
) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for name in sorted(set(tool_names)):
        if not name:
            continue

        function_tag_pattern = re.compile(r"<function=" + re.escape(name) + r">")
        found_for_name = False
        for match in function_tag_pattern.finditer(text, pos=start):
            value_start = match.start() + len("<function=")
            spans.append((value_start, value_start + len(name)))
            found_for_name = True

        if found_for_name:
            continue

        quoted_name_pattern = re.compile(
            r'"name"\s*:\s*"' + re.escape(name) + r'"'
        )
        found_for_name = False
        for match in quoted_name_pattern.finditer(text, pos=start):
            value_start = match.end() - len(name) - 1
            spans.append((value_start, value_start + len(name)))
            found_for_name = True

        if found_for_name:
            continue

        cursor = start
        while True:
            value_start = text.find(name, cursor)
            if value_start < 0:
                break
            spans.append((value_start, value_start + len(name)))
            cursor = value_start + len(name)
    return spans


def build_tca_loss_weights(
    *,
    full_text: str,
    prompt_text: str,
    token_count: int,
    token_spans: list[tuple[int, int]] | None,
    prompt_len: int,
    tool_names: list[str],
    tca_loss_weight: float,
) -> list[float]:
    weights = [1.0] * token_count
    if tca_loss_weight <= 1.0 or token_spans is None or not tool_names:
        return weights

    target_start = len(prompt_text) if full_text.startswith(prompt_text) else 0
    name_spans = find_tool_name_spans(full_text, tool_names, start=target_start)
    if not name_spans:
        return weights

    for token_index, span in enumerate(token_spans):
        if token_index < prompt_len:
            continue
        if not isinstance(span, (list, tuple)) or len(span) != 2:
            continue
        token_start, token_end = int(span[0]), int(span[1])
        if token_start == token_end:
            continue
        if any(token_start < name_end and token_end > name_start for name_start, name_end in name_spans):
            weights[token_index] = tca_loss_weight
    return weights


def build_loss_weight_vectors(
    *,
    full_text: str,
    prompt_text: str,
    token_count: int,
    token_spans: list[tuple[int, int]] | None,
    prompt_len: int,
    tool_names: list[str],
    tca_loss_weight: float,
    loss_mode: str,
    role_weight: float = 1.0,
) -> tuple[list[float], list[float]]:
    if loss_mode not in LOSS_MODES:
        raise ValueError(f"Unsupported loss_mode: {loss_mode}")

    effective_tca_weight = 1.0 if loss_mode == "plain" else tca_loss_weight
    normalizer_weights = build_tca_loss_weights(
        full_text=full_text,
        prompt_text=prompt_text,
        token_count=token_count,
        token_spans=token_spans,
        prompt_len=prompt_len,
        tool_names=tool_names,
        tca_loss_weight=effective_tca_weight,
    )
    if loss_mode == "role_aware":
        loss_weights = [float(role_weight) * weight for weight in normalizer_weights]
    else:
        loss_weights = list(normalizer_weights)
    return loss_weights, normalizer_weights


def tokenize_record(
    record: dict[str, Any],
    processor: Any,
    max_length: int,
    tca_loss_weight: float = 1.0,
    *,
    tools: list[dict[str, Any]] | None = None,
    enable_thinking: bool = True,
    loss_mode: str = "toolcall",
    role_weight: float = 1.0,
) -> dict[str, list[int] | list[float]]:
    tokenizer = processor.tokenizer
    messages = record["messages"]
    prompt_text = render_chat(
        processor,
        messages[:-1],
        add_generation_prompt=True,
        tools=tools,
        enable_thinking=enable_thinking,
    )
    full_text = render_chat(
        processor,
        messages,
        add_generation_prompt=False,
        tools=tools,
        enable_thinking=enable_thinking,
    )
    if not full_text.startswith(prompt_text):
        raise ValueError(
            "Rendered full_text does not start with prompt_text. "
            "Check chat template/tool-call formatting before training."
        )

    prompt_ids = tokenizer(prompt_text, add_special_tokens=False)["input_ids"]
    full_ids, full_offsets = token_offsets(tokenizer, full_text)
    tool_names = tool_names_from_record(record)
    loss_weights, normalizer_weights = build_loss_weight_vectors(
        full_text=full_text,
        prompt_text=prompt_text,
        token_count=len(full_ids),
        token_spans=full_offsets,
        prompt_len=len(prompt_ids),
        tool_names=tool_names,
        tca_loss_weight=tca_loss_weight,
        loss_mode=loss_mode,
        role_weight=role_weight,
    )

    if tokenizer.eos_token_id is not None:
        full_ids = full_ids + [tokenizer.eos_token_id]
        eos_loss_weight = float(role_weight) if loss_mode == "role_aware" else 1.0
        loss_weights = loss_weights + [eos_loss_weight]
        normalizer_weights = normalizer_weights + [1.0]

    labels = list(full_ids)
    prompt_len = min(len(prompt_ids), len(labels))
    labels[:prompt_len] = [IGNORE_INDEX] * prompt_len
    if not any(
        label != IGNORE_INDEX and label != tokenizer.eos_token_id
        for label in labels
    ):
        raise ValueError(
            "assistant target rendered empty. Check the chat template/tool-call format."
        )

    if len(full_ids) > max_length:
        full_ids = full_ids[-max_length:]
        labels = labels[-max_length:]
        loss_weights = loss_weights[-max_length:]
        normalizer_weights = normalizer_weights[-max_length:]
        if all(label == IGNORE_INDEX for label in labels):
            raise ValueError(
                "max_length truncated away the assistant target. Increase --max-length."
            )

    return {
        "input_ids": full_ids,
        "attention_mask": [1] * len(full_ids),
        "labels": labels,
        "loss_weights": loss_weights,
        "normalizer_weights": normalizer_weights,
    }


@dataclass
class DataCollatorForAssistantOnlyLM:
    processor: Any

    def __call__(
        self,
        features: list[dict[str, list[int] | list[float]]],
    ) -> dict[str, torch.Tensor]:
        tokenizer = self.processor.tokenizer
        input_ids = [
            torch.tensor(feature["input_ids"], dtype=torch.long)
            for feature in features
        ]
        attention_mask = [
            torch.tensor(feature["attention_mask"], dtype=torch.long)
            for feature in features
        ]
        labels = [
            torch.tensor(feature["labels"], dtype=torch.long)
            for feature in features
        ]
        loss_weights = [
            torch.tensor(feature["loss_weights"], dtype=torch.float32)
            for feature in features
        ]
        normalizer_weights = [
            torch.tensor(
                feature.get("normalizer_weights", feature["loss_weights"]),
                dtype=torch.float32,
            )
            for feature in features
        ]

        return {
            "input_ids": pad_sequence(
                input_ids,
                batch_first=True,
                padding_value=tokenizer.pad_token_id,
            ),
            "attention_mask": pad_sequence(
                attention_mask,
                batch_first=True,
                padding_value=0,
            ),
            "labels": pad_sequence(
                labels,
                batch_first=True,
                padding_value=IGNORE_INDEX,
            ),
            "loss_weights": pad_sequence(
                loss_weights,
                batch_first=True,
                padding_value=0.0,
            ),
            "normalizer_weights": pad_sequence(
                normalizer_weights,
                batch_first=True,
                padding_value=0.0,
            ),
        }


class JsonlMetricLogger:
    def __init__(self, path: Path):
        self.path = path.expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, payload: dict[str, Any]) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def weighted_loss_average(
    token_loss: torch.Tensor,
    numerator_weights: torch.Tensor,
    denominator_weights: torch.Tensor,
) -> torch.Tensor:
    return (
        token_loss * numerator_weights
    ).sum() / denominator_weights.sum().clamp_min(1.0)


class LossLoggingTrainer(Trainer):
    def __init__(
        self,
        *args: Any,
        metric_logger: JsonlMetricLogger | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.metric_logger = metric_logger

    def log(self, logs: dict[str, float], start_time: float | None = None) -> None:
        super().log(logs, start_time=start_time)
        if self.metric_logger is None:
            return
        payload: dict[str, Any] = {
            "step": int(self.state.global_step),
            "epoch": float(self.state.epoch) if self.state.epoch is not None else None,
        }
        payload.update(logs)
        self.metric_logger.write(payload)

    def compute_loss(
        self,
        model: torch.nn.Module,
        inputs: dict[str, torch.Tensor],
        return_outputs: bool = False,
        num_items_in_batch: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, Any]:
        labels = inputs.pop("labels")
        loss_weights = inputs.pop("loss_weights", None)
        normalizer_weights = inputs.pop("normalizer_weights", None)
        outputs = model(**inputs)
        logits = outputs.logits

        labels = labels.to(device=logits.device)
        shift_logits = logits[..., :-1, :]
        shift_labels = labels[..., 1:]
        active = shift_labels.ne(IGNORE_INDEX)
        if not active.any():
            loss = logits.sum() * 0.0
            return (loss, outputs) if return_outputs else loss

        active_logits = shift_logits[active]
        active_labels = shift_labels[active]
        if loss_weights is None:
            active_weights = torch.ones_like(active_labels, dtype=logits.dtype)
            active_normalizer_weights = active_weights
        else:
            active_weights = loss_weights.to(
                device=logits.device,
                dtype=logits.dtype,
            )[..., 1:][active]
            if normalizer_weights is None:
                active_normalizer_weights = active_weights
            else:
                active_normalizer_weights = normalizer_weights.to(
                    device=logits.device,
                    dtype=logits.dtype,
                )[..., 1:][active]
        token_loss = F.cross_entropy(
            active_logits,
            active_labels,
            reduction="none",
        )

        loss = weighted_loss_average(
            token_loss,
            active_weights,
            active_normalizer_weights,
        )
        return (loss, outputs) if return_outputs else loss


def is_language_module(name: str) -> bool:
    return any(hint in name for hint in LANGUAGE_MODULE_HINTS)


def discover_lora_targets(model: torch.nn.Module, suffixes: list[str]) -> list[str]:
    targets = []
    for name, module in model.named_modules():
        if not is_language_module(name):
            continue
        if not isinstance(module, torch.nn.Linear):
            continue
        if any(name.endswith(suffix) for suffix in suffixes):
            targets.append(name)
    if targets:
        return sorted(targets)

    # Some versions expose the language model without a prefix that matches
    # LANGUAGE_MODULE_HINTS. Fall back to suffix matching, but still avoid
    # obvious vision/projector branches.
    blocked = ("vision", "visual", "projector", "multi_modal", "mm_")
    for name, module in model.named_modules():
        if any(part in name.lower() for part in blocked):
            continue
        if isinstance(module, torch.nn.Linear) and any(
            name.endswith(suffix) for suffix in suffixes
        ):
            targets.append(name)
    if not targets:
        raise ValueError(
            "No LoRA target modules were found. Inspect model.named_modules() "
            "and pass compatible --target-suffixes."
        )
    return sorted(targets)


def tokenize_records(
    records: list[dict[str, Any]],
    *,
    processor: Any,
    max_length: int,
    tca_loss_weight: float,
    tools: list[dict[str, Any]] | None,
    enable_thinking: bool,
    loss_mode: str,
    role_weights: dict[str, float],
) -> list[dict[str, list[int] | list[float]]]:
    tokenized = []
    for record in records:
        role = role_for_record(record)
        tokenized.append(
            tokenize_record(
                record,
                processor,
                max_length=max_length,
                tca_loss_weight=tca_loss_weight,
                tools=tools,
                enable_thinking=enable_thinking,
                loss_mode=loss_mode,
                role_weight=role_weights.get(role, 1.0),
            )
        )
    return tokenized


def training_metadata(
    *,
    args: argparse.Namespace,
    train_records: list[dict[str, Any]],
    eval_records: list[dict[str, Any]],
    role_counts: dict[str, int],
    role_weights: dict[str, float],
) -> dict[str, Any]:
    return {
        "loss_mode": args.loss_mode,
        "tca_loss_weight": args.tca_loss_weight,
        "role_alpha": args.role_alpha,
        "role_weight_normalize": args.role_weight_normalize,
        "role_counts": dict(sorted(role_counts.items())),
        "role_weights": {
            role: float(role_weights[role])
            for role in sorted(role_weights)
        },
        "data_path": str(args.data_path),
        "eval_data_path": (
            str(args.eval_data_path)
            if args.eval_data_path is not None
            else None
        ),
        "model_name_or_path": args.model_name_or_path,
        "train_record_count": len(train_records),
        "eval_record_count": len(eval_records),
    }


def write_training_metadata(output_dir: Path, payload: dict[str, Any]) -> Path:
    path = output_dir.expanduser() / "training_metadata.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def main() -> int:
    args = parse_args()

    if args.bf16 and args.fp16:
        raise ValueError("Use only one of --bf16 or --fp16.")
    if args.tca_loss_weight <= 0.0:
        raise ValueError("--tca-loss-weight must be positive.")
    if args.role_alpha < 0.0:
        raise ValueError("--role-alpha must be non-negative.")

    processor = AutoProcessor.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        use_fast=True,
    )
    if not hasattr(processor, "tokenizer"):
        raise ValueError("The loaded processor does not expose a tokenizer.")
    if processor.tokenizer.pad_token_id is None:
        processor.tokenizer.pad_token = processor.tokenizer.eos_token

    train_records = [normalize_record(record) for record in load_records(args.data_path)]
    eval_records = (
        [normalize_record(record) for record in load_records(args.eval_data_path)]
        if args.eval_data_path is not None
        else []
    )
    role_counts = count_record_roles(train_records)
    role_weights = compute_role_weights(
        role_counts,
        alpha=args.role_alpha,
        normalize=args.role_weight_normalize,
    )

    tool_specs = load_tool_specs()
    print(f"[lora] tool_specs={len(tool_specs)}")
    print(f"[lora] loss_mode={args.loss_mode}")
    print("[lora] role_counts=" + json.dumps(role_counts, ensure_ascii=False, sort_keys=True))
    print("[lora] role_weights=" + json.dumps(role_weights, ensure_ascii=False, sort_keys=True))

    train_tokenized_records = tokenize_records(
        train_records,
        processor=processor,
        max_length=args.max_length,
        tca_loss_weight=args.tca_loss_weight,
        tools=tool_specs,
        enable_thinking=args.enable_thinking,
        loss_mode=args.loss_mode,
        role_weights=role_weights,
    )
    train_dataset = Dataset.from_list(train_tokenized_records)
    eval_dataset = None
    if eval_records:
        eval_dataset = Dataset.from_list(
            tokenize_records(
                eval_records,
                processor=processor,
                max_length=args.max_length,
                tca_loss_weight=args.tca_loss_weight,
                tools=tool_specs,
                enable_thinking=args.enable_thinking,
                loss_mode=args.loss_mode,
                role_weights=role_weights,
            )
        )

    quantization_config = None
    if not args.no_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )

    try:
        model = AutoModelForImageTextToText.from_pretrained(
            args.model_name_or_path,
            trust_remote_code=True,
            device_map="auto",
            quantization_config=quantization_config,
            dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )
    except ValueError as exc:
        raise ValueError(
            "Failed to load the model with AutoModelForImageTextToText. "
            "Your Transformers version may not support this Qwen3.5 checkpoint yet. "
            "Install a Transformers version that recognizes model_type qwen3_5, "
            "or use a text CausalLM Qwen checkpoint with train_qwen_toolcall_lora.py."
        ) from exc

    model.config.use_cache = False
    if not args.no_4bit:
        model = prepare_model_for_kbit_training(model)
    if args.gradient_checkpointing:
        model.gradient_checkpointing_enable()

    target_modules = discover_lora_targets(model, args.target_suffixes)
    print(f"[lora] target_modules={len(target_modules)}")
    print("[lora] target_module_examples=" + json.dumps(target_modules[:12], indent=2))

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        target_modules=target_modules,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    eval_steps = args.eval_steps if args.eval_steps is not None else args.save_steps
    metric_log_path = (
        args.metric_log_path.expanduser()
        if args.metric_log_path is not None
        else args.output_dir / "metrics_log.jsonl"
    )
    metric_logger = JsonlMetricLogger(metric_log_path)

    training_args = TrainingArguments(
        output_dir=str(args.output_dir),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_ratio=args.warmup_ratio,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=3,
        do_eval=eval_dataset is not None,
        eval_strategy="steps" if eval_dataset is not None else "no",
        eval_steps=eval_steps if eval_dataset is not None else None,
        bf16=args.bf16,
        fp16=args.fp16,
        optim="paged_adamw_8bit" if not args.no_4bit else "adamw_torch",
        lr_scheduler_type="cosine",
        report_to="none",
        remove_unused_columns=False,
    )

    trainer = LossLoggingTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=DataCollatorForAssistantOnlyLM(processor),
        metric_logger=metric_logger,
    )
    resume_from_checkpoint = None
    if args.resume_from_checkpoint is not None:
        resume_from_checkpoint = str(args.resume_from_checkpoint.expanduser())
    trainer.train(resume_from_checkpoint=resume_from_checkpoint)
    trainer.save_model(str(args.output_dir))
    processor.save_pretrained(str(args.output_dir))
    metadata_path = write_training_metadata(
        args.output_dir,
        training_metadata(
            args=args,
            train_records=train_records,
            eval_records=eval_records,
            role_counts=role_counts,
            role_weights=role_weights,
        ),
    )

    print(f"[lora] saved adapter to {args.output_dir}")
    print(f"[lora] metric log saved to {metric_log_path}")
    print(f"[lora] training metadata saved to {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
