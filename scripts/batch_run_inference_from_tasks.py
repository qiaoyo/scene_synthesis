from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TASKS_JSON = PROJECT_ROOT / "data" / "lora" / "industrial_scene_tasks_200.json"
DEFAULT_SUMMARY_PATH = PROJECT_ROOT / "outputs" / "batch_inference_runs.jsonl"
RUN_INFERENCE_PATH = PROJECT_ROOT / "scripts" / "run_inference.py"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run scripts/run_inference.py for bilingual task instructions."
    )
    parser.add_argument(
        "--tasks-json",
        type=Path,
        default=DEFAULT_TASKS_JSON,
        help="JSON file containing task records with instruction_en/instruction_zh.",
    )
    parser.add_argument(
        "--language",
        choices=["en", "zh"],
        default="en",
        help="Instruction language to use as the run_inference --command value.",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=0,
        help="Zero-based task index to start from.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of tasks to run after start-index.",
    )
    parser.add_argument(
        "--summary-path",
        type=Path,
        default=DEFAULT_SUMMARY_PATH,
        help="JSONL manifest path for per-task execution results.",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Keep running remaining tasks if one task fails.",
    )
    parser.add_argument(
        "--skip-completed",
        action="store_true",
        help="Skip task indices that already have ok=true in summary-path.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print selected commands without executing run_inference.py.",
    )
    return parser.parse_args()


def load_tasks(path: Path, language: str) -> list[dict[str, Any]]:
    payload = json.loads(path.expanduser().read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected top-level JSON list in {path}")

    instruction_key = f"instruction_{language}"
    tasks: list[dict[str, Any]] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f"Task {index} must be an object.")
        command = item.get(instruction_key)
        if not isinstance(command, str) or not command.strip():
            raise ValueError(f"Task {index} is missing non-empty {instruction_key}.")
        tasks.append({"index": index, "command": command.strip()})
    return tasks


def completed_indices(summary_path: Path) -> set[int]:
    if not summary_path.exists():
        return set()

    completed: set[int] = set()
    for line_no, line in enumerate(summary_path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            print(
                f"[batch_run] ignoring invalid summary line {line_no}: {summary_path}",
                file=sys.stderr,
            )
            continue
        if record.get("ok") is True and isinstance(record.get("index"), int):
            completed.add(record["index"])
    return completed


def select_tasks(
    tasks: list[dict[str, Any]],
    start_index: int,
    limit: int | None,
) -> list[dict[str, Any]]:
    if start_index < 0:
        raise ValueError("--start-index must be >= 0")
    selected = [task for task in tasks if task["index"] >= start_index]
    if limit is not None:
        if limit < 0:
            raise ValueError("--limit must be >= 0")
        selected = selected[:limit]
    return selected


def append_summary(summary_path: Path, record: dict[str, Any]) -> None:
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
        handle.write("\n")


def run_task(task: dict[str, Any]) -> dict[str, Any]:
    command = task["command"]
    started_at = now_iso()
    start = time.perf_counter()
    completed = subprocess.run(
        [
            sys.executable,
            str(RUN_INFERENCE_PATH),
            "--command",
            command,
        ],
        cwd=str(PROJECT_ROOT),
        text=True,
    )
    elapsed_sec = round(time.perf_counter() - start, 3)
    return {
        "index": task["index"],
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "started_at": started_at,
        "elapsed_sec": elapsed_sec,
        "language": task["language"],
        "command": command,
    }


def main() -> int:
    args = parse_args()
    tasks = load_tasks(args.tasks_json, args.language)
    selected = select_tasks(tasks, args.start_index, args.limit)
    for task in selected:
        task["language"] = args.language

    if args.skip_completed:
        done = completed_indices(args.summary_path)
        selected = [task for task in selected if task["index"] not in done]

    print(
        f"[batch_run] loaded={len(tasks)} selected={len(selected)} "
        f"language={args.language} dry_run={args.dry_run}"
    )

    if args.dry_run:
        for task in selected:
            print(
                f"[batch_run][dry-run] index={task['index']} "
                f"command={task['command']}"
            )
        return 0

    for run_no, task in enumerate(selected, 1):
        print(
            f"[batch_run] running {run_no}/{len(selected)} "
            f"index={task['index']}"
        )
        result = run_task(task)
        append_summary(args.summary_path, result)
        status = "ok" if result["ok"] else "failed"
        print(
            f"[batch_run] {status} index={result['index']} "
            f"returncode={result['returncode']} elapsed={result['elapsed_sec']}s"
        )
        if not result["ok"] and not args.continue_on_error:
            return int(result["returncode"] or 1)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# python scripts/batch_run_inference_from_tasks.py \
#   --tasks-json data/lora/industrial_scene_tasks_200.json \
#   --language en \
#   --continue-on-error \
#   --skip-completed
