from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUNS_ROOT = PROJECT_ROOT / "outputs" / "runs"
DEFAULT_OUTPUT_JSONL = PROJECT_ROOT / "data" / "lora" / "planner_toolcall_sft.jsonl"
DEFAULT_OUTPUT_JSON = PROJECT_ROOT / "data" / "lora" / "planner_toolcall_sft_preview.json"
ALLOWED_TOOL_NAMES = {
    "delete_asset",
    "move_asset",
    "place_instance",
    "replace_instance",
    "retrieve_asset",
    "retrieve_scene_template",
    "set_support",
    "check_collision",
    "check_support",
    "simulate_step",
    "save_scene_usd",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert outputs/runs/*/planner_steps.jsonl records into "
            "LoRA/SFT tool-call training samples."
        )
    )
    parser.add_argument(
        "--runs-root",
        type=Path,
        default=DEFAULT_RUNS_ROOT,
        help="Directory containing per-run subdirectories.",
    )
    parser.add_argument(
        "--output-jsonl",
        type=Path,
        default=DEFAULT_OUTPUT_JSONL,
        help="Training JSONL output path.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=DEFAULT_OUTPUT_JSON,
        help="Pretty JSON preview output path.",
    )
    parser.add_argument(
        "--successful-runs-only",
        action="store_true",
        help="Only convert runs whose record.json has ok=true.",
    )
    parser.add_argument(
        "--include-final",
        action="store_true",
        help="Also convert final_response records into assistant content samples.",
    )
    parser.add_argument(
        "--max-records",
        type=int,
        default=None,
        help="Maximum number of samples to write.",
    )
    parser.add_argument(
        "--allow-unknown-tools",
        action="store_true",
        help="Keep tool-call samples whose tool names are not in the project tool registry.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def iter_planner_files(runs_root: Path) -> Iterable[Path]:
    yield from sorted(runs_root.expanduser().glob("*/planner_steps.jsonl"))


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
        if not isinstance(payload, dict):
            raise ValueError(f"Expected object at {path}:{line_no}")
        yield payload


def to_openai_tool_calls(calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    converted = []
    for call in calls:
        name = call.get("name")
        if not isinstance(name, str) or not name:
            raise ValueError(f"Invalid tool call name: {call}")
        arguments = call.get("arguments", {})
        converted.append(
            {
                "type": "function",
                "function": {
                    "name": name,
                    "arguments": json.dumps(
                        arguments,
                        ensure_ascii=False,
                        separators=(",", ":"),
                    ),
                },
            }
        )
    return converted


def build_tool_sample(
    row: Dict[str, Any],
    source_path: Path,
    run_record: Optional[Dict[str, Any]],
    allow_unknown_tools: bool,
) -> Optional[Dict[str, Any]]:
    messages = row.get("messages")
    tool_calls = row.get("tool_calls") or []
    if not isinstance(messages, list) or len(messages) < 2:
        return None
    if not isinstance(tool_calls, list) or not tool_calls:
        return None
    if row.get("error"):
        return None
    if not allow_unknown_tools:
        for call in tool_calls:
            if call.get("name") not in ALLOWED_TOOL_NAMES:
                return None

    assistant_tool_calls = to_openai_tool_calls(tool_calls)
    sample = {
        "messages": [
            *messages,
            {
                "role": "assistant",
                "tool_calls": assistant_tool_calls,
            },
        ],
        "expected_output": {
            "tool_calls": assistant_tool_calls,
        },
        "metadata": {
            "source_path": str(source_path),
            "run_id": row.get("run_id"),
            "step": row.get("step"),
            "timestamp": row.get("timestamp"),
            "command": row.get("command"),
            "run_ok": run_record.get("ok") if run_record else None,
            "run_error": run_record.get("error") if run_record else None,
        },
    }
    return sample


def build_final_sample(
    row: Dict[str, Any],
    source_path: Path,
    run_record: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    messages = row.get("messages")
    final_response = row.get("final_response")
    if not isinstance(messages, list) or len(messages) < 2:
        return None
    if not isinstance(final_response, str) or not final_response:
        return None
    if row.get("error"):
        return None

    return {
        "messages": [
            *messages,
            {
                "role": "assistant",
                "content": final_response,
            },
        ],
        "metadata": {
            "source_path": str(source_path),
            "run_id": row.get("run_id"),
            "step": row.get("step"),
            "timestamp": row.get("timestamp"),
            "command": row.get("command"),
            "run_ok": run_record.get("ok") if run_record else None,
            "run_error": run_record.get("error") if run_record else None,
        },
    }


def convert_records(args: argparse.Namespace) -> List[Dict[str, Any]]:
    samples: List[Dict[str, Any]] = []
    for planner_path in iter_planner_files(args.runs_root):
        run_dir = planner_path.parent
        run_record = load_json(run_dir / "record.json")
        if args.successful_runs_only and (not run_record or run_record.get("ok") is not True):
            continue

        for row in read_jsonl(planner_path):
            sample = build_tool_sample(
                row,
                planner_path,
                run_record,
                allow_unknown_tools=args.allow_unknown_tools,
            )
            if sample is None and args.include_final:
                sample = build_final_sample(row, planner_path, run_record)
            if sample is None:
                continue
            samples.append(sample)
            if args.max_records is not None and len(samples) >= args.max_records:
                return samples
    return samples


def write_outputs(
    samples: List[Dict[str, Any]],
    output_jsonl: Path,
    output_json: Path,
) -> None:
    output_jsonl = output_jsonl.expanduser()
    output_json = output_json.expanduser()
    output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    output_json.parent.mkdir(parents=True, exist_ok=True)

    with output_jsonl.open("w", encoding="utf-8") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")

    output_json.write_text(
        json.dumps(samples, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    samples = convert_records(args)
    write_outputs(samples, args.output_jsonl, args.output_json)
    print(f"[convert_lora] samples={len(samples)}")
    print(f"[convert_lora] jsonl={args.output_jsonl}")
    print(f"[convert_lora] json={args.output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# 默认命令
# cd /home/simple/joey/scene_synthesis
# source ~/isaac_env/bin/activate
# python dataprocess/convert_planner_steps_to_lora.py
# 只转换成功的
# python dataprocess/convert_planner_steps_to_lora.py --successful-runs-only