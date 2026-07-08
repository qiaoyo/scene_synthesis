from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import torch
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from peft import PeftModel
from transformers import AutoModelForImageTextToText, AutoProcessor, BitsAndBytesConfig

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LORA_SCRIPT_DIR = PROJECT_ROOT / "scripts" / "lora"
if str(LORA_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(LORA_SCRIPT_DIR))

from train_qwen35_multimodal_toolcall_lora import (  # noqa: E402
    PLAN_TOOLS,
    ROLE_ORDER,
    TERMINATION_TOOLS,
    load_records,
    load_tool_specs,
    normalize_record,
    normalize_tool_calls,
    render_chat,
    role_for_tool_names,
)


NODE_ORDER = ("overall", *ROLE_ORDER, "unknown")


@dataclass
class TcaBucket:
    records: int = 0
    first_correct: int = 0
    all_exact_correct: int = 0
    call_correct: int = 0
    call_total: int = 0
    tool_parse_valid: int = 0
    json_fallback_valid: int = 0
    schema_valid: int = 0
    argument_exact: int = 0
    gold_tool_counts: Counter[str] = field(default_factory=Counter)
    pred_tool_counts: Counter[str] = field(default_factory=Counter)

    def add(
        self,
        *,
        gold_calls: list[dict[str, Any]],
        pred_calls: list[dict[str, Any]],
        tool_parse_valid: bool,
        json_fallback_valid: bool,
        schema_valid: bool,
    ) -> None:
        gold_names = tool_names_from_calls(gold_calls)
        pred_names = tool_names_from_calls(pred_calls)
        self.records += 1
        if gold_names:
            self.first_correct += int(bool(pred_names) and pred_names[0] == gold_names[0])
        else:
            self.first_correct += int(not pred_names)
        self.all_exact_correct += int(pred_names == gold_names)
        self.argument_exact += int(canonical_tool_calls(pred_calls) == canonical_tool_calls(gold_calls))
        aligned = max(len(gold_names), len(pred_names))
        self.call_total += aligned
        for index in range(aligned):
            gold = gold_names[index] if index < len(gold_names) else None
            pred = pred_names[index] if index < len(pred_names) else None
            self.call_correct += int(gold == pred)
        self.tool_parse_valid += int(tool_parse_valid)
        self.json_fallback_valid += int(json_fallback_valid)
        self.schema_valid += int(schema_valid)
        self.gold_tool_counts.update(gold_names)
        self.pred_tool_counts.update(pred_names)

    def to_metrics(self, prefix: str) -> dict[str, Any]:
        return {
            f"{prefix}_records": self.records,
            f"{prefix}_TCA_first": percent(self.first_correct, self.records),
            f"{prefix}_TCA_all_exact": percent(self.all_exact_correct, self.records),
            f"{prefix}_TCA_call_micro": percent(self.call_correct, self.call_total),
            f"{prefix}_argument_exact": percent(self.argument_exact, self.records),
            f"{prefix}_tool_parse_valid": percent(self.tool_parse_valid, self.records),
            f"{prefix}_tool_schema_valid": percent(self.schema_valid, self.records),
            f"{prefix}_tool_json_fallback_valid": percent(self.json_fallback_valid, self.records),
            f"{prefix}_call_total": self.call_total,
            f"{prefix}_gold_tool_counts": dict(sorted(self.gold_tool_counts.items())),
            f"{prefix}_pred_tool_counts": dict(sorted(self.pred_tool_counts.items())),
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate Tool Call Accuracy for Qwen3.5 LoRA checkpoints. "
            "TCA is computed by generation and reported overall plus by "
            "plan/correction/termination node."
        )
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=PROJECT_ROOT / "data" / "lora" / "toolcall_sft_test_8_2.jsonl",
        help="JSON or JSONL SFT records with gold assistant.tool_calls.",
    )
    parser.add_argument(
        "--model-name-or-path",
        type=str,
        required=True,
        help="Base Qwen3.5 model path or Hugging Face model id.",
    )
    parser.add_argument(
        "--adapter-path",
        type=Path,
        default=None,
        help=(
            "Optional LoRA adapter/checkpoint directory to evaluate. "
            "Omit this argument to evaluate the base model without LoRA."
        ),
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=PROJECT_ROOT / "outputs" / "metrics" / "toolcall_tca_metrics.json",
        help="Summary metrics JSON output path.",
    )
    parser.add_argument(
        "--predictions-path",
        type=Path,
        default=None,
        help="Optional JSONL path for per-record TCA predictions.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=0,
        help="Number of records sampled for TCA. 0 means all records.",
    )
    parser.add_argument("--seed", type=int, default=20260630)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--include-generated-text", action="store_true")
    parser.add_argument("--no-4bit", action="store_true", help="Disable 4-bit loading.")
    parser.add_argument("--bf16", action="store_true", help="Load/generate with bf16.")
    parser.add_argument("--fp16", action="store_true", help="Load/generate with fp16.")
    parser.add_argument(
        "--disable-thinking",
        dest="enable_thinking",
        action="store_false",
        help="Render Qwen chat templates with enable_thinking=False.",
    )
    parser.set_defaults(enable_thinking=True)
    return parser.parse_args()


def percent(numerator: int, denominator: int) -> float:
    return 100.0 * numerator / denominator if denominator else 0.0


def select_indices(total: int, sample_size: int, seed: int) -> list[int]:
    if sample_size <= 0 or sample_size >= total:
        return list(range(total))
    rng = random.Random(seed)
    return sorted(rng.sample(range(total), sample_size))


def node_for_tool_sequence(tool_names: list[str]) -> str:
    return role_for_tool_names(tool_names)


def load_training_metadata(adapter_path: Path | None) -> dict[str, Any] | None:
    if adapter_path is None:
        return None
    adapter_path = adapter_path.expanduser()
    candidates = [
        adapter_path / "training_metadata.json",
        adapter_path.parent / "training_metadata.json",
    ]
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if not candidate.exists():
            continue
        payload = json.loads(candidate.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = dict(payload)
            payload["metadata_path"] = str(candidate)
            return payload
    return None


def coerce_tool_calls_from_json(payload: Any) -> list[dict[str, Any]] | None:
    if isinstance(payload, dict) and isinstance(payload.get("tool_calls"), list):
        return payload["tool_calls"]
    if isinstance(payload, dict) and (
        isinstance(payload.get("function"), dict) or isinstance(payload.get("name"), str)
    ):
        return [payload]
    if isinstance(payload, list):
        return payload
    return None


def iter_json_objects(text: str) -> list[Any]:
    decoder = json.JSONDecoder()
    payloads = []
    start = 0
    while start < len(text):
        match = re.search(r"[\{\[]", text[start:])
        if match is None:
            break
        object_start = start + match.start()
        try:
            payload, object_end = decoder.raw_decode(text[object_start:])
        except json.JSONDecodeError:
            start = object_start + 1
            continue
        payloads.append(payload)
        start = object_start + object_end
    return payloads


def tool_names_from_calls(calls: list[dict[str, Any]]) -> list[str]:
    return [call["function"]["name"] for call in calls]


def tool_calls_from_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    assistant = record["messages"][-1]
    raw_calls = assistant.get("tool_calls")
    if not raw_calls:
        return []
    return normalize_tool_calls(raw_calls)


def canonical_tool_calls(calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "name": call["function"]["name"],
            "arguments": call["function"].get("arguments", {}),
        }
        for call in calls
    ]


def parse_parameter_value(raw_value: str) -> Any:
    text = raw_value.strip()
    if not text:
        return ""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def parse_qwen_tool_calls(text: str) -> tuple[list[dict[str, Any]], bool]:
    raw_calls: list[dict[str, Any]] = []
    tool_blocks = re.findall(r"<tool_call>\s*(.*?)\s*</tool_call>", text, flags=re.S)
    if not tool_blocks:
        return [], False

    for block in tool_blocks:
        function_match = re.search(
            r"<function=([^>\n]+)>\s*(.*?)\s*</function>",
            block,
            flags=re.S,
        )
        if function_match is None:
            return [], False
        name = function_match.group(1).strip()
        body = function_match.group(2)
        arguments: dict[str, Any] = {}
        for parameter_name, parameter_value in re.findall(
            r"<parameter=([^>\n]+)>\s*(.*?)\s*</parameter>",
            body,
            flags=re.S,
        ):
            arguments[parameter_name.strip()] = parse_parameter_value(parameter_value)
        raw_calls.append(
            {
                "type": "function",
                "function": {
                    "name": name,
                    "arguments": arguments,
                },
            }
        )

    try:
        return normalize_tool_calls(raw_calls), True
    except ValueError:
        return [], False


def parse_json_fallback_tool_calls(text: str) -> tuple[list[dict[str, Any]], bool]:
    stripped = text.strip()
    if not stripped:
        return [], False

    raw_calls: list[dict[str, Any]] = []
    block_matches = re.findall(r"<tool_call>\s*(.*?)\s*</tool_call>", stripped, flags=re.S)
    candidates = block_matches if block_matches else [stripped]

    for candidate in candidates:
        payloads: list[Any] = []
        try:
            payloads.append(json.loads(candidate))
        except json.JSONDecodeError:
            payloads.extend(iter_json_objects(candidate))

        for payload in payloads:
            maybe_calls = coerce_tool_calls_from_json(payload)
            if maybe_calls is not None:
                raw_calls.extend(maybe_calls)

    if not raw_calls:
        return [], False

    try:
        normalized = normalize_tool_calls(raw_calls)
    except ValueError:
        return [], False
    return normalized, True


def tool_schema_map(tool_specs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for spec in tool_specs:
        function = spec.get("function", {})
        name = function.get("name")
        if isinstance(name, str):
            schemas[name] = function.get("parameters", {}) or {}
    return schemas


def validate_tool_call_schema(
    calls: list[dict[str, Any]],
    schemas: dict[str, dict[str, Any]],
) -> bool:
    for call in calls:
        function = call.get("function", {})
        name = function.get("name")
        arguments = function.get("arguments", {})
        if not isinstance(name, str) or name not in schemas:
            return False
        if not isinstance(arguments, dict):
            return False
        try:
            validate(instance=arguments, schema=schemas[name])
        except ValidationError:
            return False
    return True


def first_parameter_device(model: torch.nn.Module) -> torch.device:
    try:
        return next(model.parameters()).device
    except StopIteration:
        return torch.device("cpu")


def load_model_and_processor(args: argparse.Namespace) -> tuple[Any, torch.nn.Module]:
    if args.bf16 and args.fp16:
        raise ValueError("Use only one of --bf16 or --fp16.")

    processor = AutoProcessor.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        use_fast=True,
    )
    if not hasattr(processor, "tokenizer"):
        raise ValueError("The loaded processor does not expose a tokenizer.")
    if processor.tokenizer.pad_token_id is None:
        processor.tokenizer.pad_token = processor.tokenizer.eos_token

    dtype = torch.bfloat16 if args.bf16 else torch.float16
    quantization_config = None
    if not args.no_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )

    base_model = AutoModelForImageTextToText.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        device_map="auto",
        quantization_config=quantization_config,
        dtype=dtype,
    )
    if args.adapter_path is None:
        model = base_model
    else:
        model = PeftModel.from_pretrained(
            base_model,
            str(args.adapter_path.expanduser()),
            is_trainable=False,
        )
    model.eval()
    return processor, model


def evaluate_tca(args: argparse.Namespace) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    records = [normalize_record(record) for record in load_records(args.data_path)]
    selected_indices = select_indices(len(records), args.sample_size, args.seed)
    processor, model = load_model_and_processor(args)
    tokenizer = processor.tokenizer
    device = first_parameter_device(model)
    tool_specs = load_tool_specs()
    schemas = tool_schema_map(tool_specs)

    buckets = {name: TcaBucket() for name in NODE_ORDER}
    predictions: list[dict[str, Any]] = []

    with torch.inference_mode():
        for index in selected_indices:
            record = records[index]
            gold_calls = tool_calls_from_record(record)
            gold_names = tool_names_from_calls(gold_calls)
            node = node_for_tool_sequence(gold_names)
            prompt_text = render_chat(
                processor,
                record["messages"][:-1],
                add_generation_prompt=True,
                tools=tool_specs,
                enable_thinking=args.enable_thinking,
            )
            inputs = tokenizer(
                prompt_text,
                return_tensors="pt",
                add_special_tokens=False,
            )
            inputs = {key: value.to(device) for key, value in inputs.items()}
            generated = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
            new_tokens = generated[0, inputs["input_ids"].shape[1] :]
            decoded = tokenizer.decode(new_tokens, skip_special_tokens=True)
            pred_calls, tool_parse_valid = parse_qwen_tool_calls(decoded)
            json_calls, json_fallback_valid = parse_json_fallback_tool_calls(decoded)
            if not gold_calls and not pred_calls:
                tool_parse_valid = True
            schema_valid = validate_tool_call_schema(pred_calls, schemas)
            pred_names = tool_names_from_calls(pred_calls)

            buckets["overall"].add(
                gold_calls=gold_calls,
                pred_calls=pred_calls,
                tool_parse_valid=tool_parse_valid,
                json_fallback_valid=json_fallback_valid,
                schema_valid=schema_valid,
            )
            buckets[node].add(
                gold_calls=gold_calls,
                pred_calls=pred_calls,
                tool_parse_valid=tool_parse_valid,
                json_fallback_valid=json_fallback_valid,
                schema_valid=schema_valid,
            )

            prediction = {
                "record_index": index,
                "node": node,
                "gold_tool_names": gold_names,
                "pred_tool_names": pred_names,
                "json_fallback_tool_names": tool_names_from_calls(json_calls),
                "tool_parse_valid": tool_parse_valid,
                "tool_schema_valid": schema_valid,
                "tool_json_fallback_valid": json_fallback_valid,
                "TCA_first": (
                    bool(gold_names)
                    and bool(pred_names)
                    and pred_names[0] == gold_names[0]
                ),
                "TCA_all_exact": pred_names == gold_names,
                "argument_exact": canonical_tool_calls(pred_calls) == canonical_tool_calls(gold_calls),
            }
            if args.include_generated_text:
                prediction["generated_text"] = decoded
            predictions.append(prediction)

    metrics: dict[str, Any] = {
        "data_path": str(args.data_path),
        "model_name_or_path": args.model_name_or_path,
        "adapter_path": str(args.adapter_path) if args.adapter_path is not None else None,
        "record_count": len(records),
        "evaluated_records": len(selected_indices),
        "sample_size": args.sample_size,
        "seed": args.seed,
        "max_new_tokens": args.max_new_tokens,
        "node_rule": {
            "plan": sorted(PLAN_TOOLS),
            "termination": sorted(TERMINATION_TOOLS),
            "correction": "all other non-empty tool sequences",
        },
    }
    training_metadata = load_training_metadata(args.adapter_path)
    if training_metadata is not None:
        metrics["training_metadata"] = training_metadata
    for node in NODE_ORDER:
        metrics[node] = buckets[node].to_metrics(node)
    return metrics, predictions


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_predictions(path: Path, predictions: list[dict[str, Any]]) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for prediction in predictions:
            handle.write(json.dumps(prediction, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    metrics, predictions = evaluate_tca(args)
    write_json(args.output_path, metrics)
    if args.predictions_path is not None:
        write_predictions(args.predictions_path, predictions)
        print(f"[tca] predictions={args.predictions_path.expanduser()}")
    print(json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True))
    print(f"[tca] metrics={args.output_path.expanduser()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
