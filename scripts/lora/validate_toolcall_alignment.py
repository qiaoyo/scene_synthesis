from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from transformers import AutoProcessor

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LORA_SCRIPT_DIR = PROJECT_ROOT / "scripts" / "lora"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(LORA_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(LORA_SCRIPT_DIR))

from train_qwen35_multimodal_toolcall_lora import (  # noqa: E402
    load_records,
    load_tool_specs,
    normalize_record,
    normalize_tool_calls,
    render_chat,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that LoRA SFT records render with the same Qwen tool-call "
            "template used by the agent serving path."
        )
    )
    parser.add_argument(
        "--model-name-or-path",
        type=str,
        required=True,
        help="Qwen3.5 model path or Hugging Face model id used for its processor/template.",
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        action="append",
        required=True,
        help="Training/eval JSON or JSONL path. Pass multiple times to validate several files.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=20,
        help="Number of records to validate per data path. 0 means all records.",
    )
    parser.add_argument(
        "--disable-thinking",
        dest="enable_thinking",
        action="store_false",
        help="Render Qwen chat templates with enable_thinking=False.",
    )
    parser.set_defaults(enable_thinking=True)
    return parser.parse_args()


def tool_schema_map(tool_specs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for spec in tool_specs:
        function = spec.get("function", {})
        name = function.get("name")
        if isinstance(name, str):
            schemas[name] = function.get("parameters", {}) or {}
    return schemas


def validate_gold_calls(
    calls: list[dict[str, Any]],
    schemas: dict[str, dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    for call in calls:
        function = call["function"]
        name = function["name"]
        arguments = function.get("arguments", {})
        schema = schemas.get(name)
        if schema is None:
            errors.append(f"unknown tool {name}")
            continue
        try:
            validate(instance=arguments, schema=schema)
        except ValidationError as exc:
            errors.append(f"{name}: {exc.message}")
    return errors


def validate_record(
    *,
    processor: Any,
    record: dict[str, Any],
    tools: list[dict[str, Any]],
    schemas: dict[str, dict[str, Any]],
    enable_thinking: bool,
) -> list[str]:
    errors: list[str] = []
    normalized = normalize_record(record)
    messages = normalized["messages"]
    assistant = messages[-1]
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
        errors.append("full_text does not start with prompt_text")

    raw_calls = assistant.get("tool_calls")
    if raw_calls:
        calls = normalize_tool_calls(raw_calls)
        target_text = full_text[len(prompt_text) :]
        if "<tool_call>" not in target_text:
            errors.append("assistant target does not contain <tool_call>")
        for call in calls:
            name = call["function"]["name"]
            if f"<function={name}>" not in target_text:
                errors.append(f"assistant target missing <function={name}>")
        errors.extend(validate_gold_calls(calls, schemas))
    return errors


def main() -> int:
    args = parse_args()
    processor = AutoProcessor.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        use_fast=True,
    )
    tool_specs = load_tool_specs()
    schemas = tool_schema_map(tool_specs)
    failures: list[dict[str, Any]] = []
    checked = 0

    for data_path in args.data_path:
        records = load_records(data_path)
        if args.sample_size > 0:
            records = records[: args.sample_size]
        for index, record in enumerate(records):
            checked += 1
            try:
                errors = validate_record(
                    processor=processor,
                    record=record,
                    tools=tool_specs,
                    schemas=schemas,
                    enable_thinking=args.enable_thinking,
                )
            except Exception as exc:
                errors = [f"{exc.__class__.__name__}: {exc}"]
            if errors:
                failures.append(
                    {
                        "data_path": str(data_path),
                        "record_index": index,
                        "errors": errors,
                    }
                )

    summary = {
        "checked": checked,
        "failed": len(failures),
        "failures": failures[:20],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
