from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TASKS_JSON = PROJECT_ROOT / "docs" / "industrial_small_area_english_instructions.json"
DEFAULT_BATCH_ROOT = PROJECT_ROOT / "outputs" / "batches"
RUN_INFERENCE_PATH = PROJECT_ROOT / "scripts" / "run_inference.py"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_batch_id() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


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
        "--batch-root",
        type=Path,
        default=DEFAULT_BATCH_ROOT,
        help="Root directory where outputs/batches/<batch_id> is created.",
    )
    parser.add_argument(
        "--batch-id",
        type=str,
        default=None,
        help="Optional batch id. Defaults to a timestamp.",
    )
    parser.add_argument(
        "--summary-path",
        type=Path,
        default=None,
        help="Optional legacy JSONL mirror path. The primary manifest is under the batch directory.",
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
        tasks.append(
            {
                "index": index,
                "task_id": str(item.get("id") or index),
                "title_en": str(item.get("title_en") or ""),
                "title_zh": str(item.get("title_zh") or ""),
                "asset_types": list(item.get("asset_types") or []),
                "support_relations": list(item.get("support_relations") or []),
                "command": command.strip(),
            }
        )
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


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def batch_summary(
    *,
    batch_id: str,
    batch_dir: Path,
    tasks_json: Path,
    language: str,
    selected: list[dict[str, Any]],
    results: list[dict[str, Any]],
) -> dict[str, Any]:
    ok_count = sum(1 for item in results if item.get("ok") is True)
    return {
        "batch_id": batch_id,
        "batch_dir": str(batch_dir),
        "tasks_json": str(tasks_json.expanduser()),
        "language": language,
        "selected_count": len(selected),
        "completed_count": len(results),
        "ok_count": ok_count,
        "failed_count": len(results) - ok_count,
        "started_at": results[0]["started_at"] if results else None,
        "finished_at": now_iso(),
    }


def run_task(task: dict[str, Any], batch_dir: Path, run_no: int) -> dict[str, Any]:
    command = task["command"]
    started_at = now_iso()
    start = time.perf_counter()
    task_label = f"{task['index']:03d}_{task['task_id']}"
    stdout_log = batch_dir / "logs" / f"{task_label}_stdout.log"
    stderr_log = batch_dir / "logs" / f"{task_label}_stderr.log"
    result_json = batch_dir / "run_results" / f"{task_label}_result.json"
    env = os.environ.copy()
    env["SCENE_SYNTHESIS_OUTPUT_DIR"] = str(batch_dir)
    completed = subprocess.run(
        [
            sys.executable,
            str(RUN_INFERENCE_PATH),
            "--command",
            command,
            "--result-json",
            str(result_json),
        ],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        env=env,
        text=True,
    )
    elapsed_sec = round(time.perf_counter() - start, 3)
    stdout_log.parent.mkdir(parents=True, exist_ok=True)
    stdout_log.write_text(completed.stdout or "", encoding="utf-8")
    stderr_log.parent.mkdir(parents=True, exist_ok=True)
    stderr_log.write_text(completed.stderr or "", encoding="utf-8")

    result_payload: dict[str, Any] = {}
    if result_json.exists():
        try:
            loaded = json.loads(result_json.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                result_payload = loaded
        except json.JSONDecodeError:
            result_payload = {"result_json_error": "invalid JSON"}

    return {
        "run_no": run_no,
        "index": task["index"],
        "task_index": task["index"],
        "task_id": task["task_id"],
        "title_en": task["title_en"],
        "title_zh": task["title_zh"],
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "started_at": started_at,
        "elapsed_sec": elapsed_sec,
        "language": task["language"],
        "command": command,
        "asset_types": task["asset_types"],
        "support_relations": task["support_relations"],
        "run_id": result_payload.get("run_id"),
        "run_dir": result_payload.get("run_dir"),
        "record_path": result_payload.get("record_path"),
        "final_scene_path": result_payload.get("final_scene_path"),
        "stdout_log": str(stdout_log),
        "stderr_log": str(stderr_log),
        "result_json": str(result_json),
    }


def main() -> int:
    args = parse_args()
    tasks = load_tasks(args.tasks_json, args.language)
    selected = select_tasks(tasks, args.start_index, args.limit)
    for task in selected:
        task["language"] = args.language

    batch_id = args.batch_id or new_batch_id()
    batch_dir = args.batch_root.expanduser() / batch_id
    manifest_path = batch_dir / "batch_manifest.jsonl"
    summary_path = args.summary_path.expanduser() if args.summary_path else None

    if args.skip_completed:
        done = completed_indices(manifest_path)
        selected = [task for task in selected if task["index"] not in done]

    print(
        f"[batch_run] loaded={len(tasks)} selected={len(selected)} "
        f"language={args.language} dry_run={args.dry_run} batch_dir={batch_dir}"
    )

    if args.dry_run:
        for task in selected:
            print(
                f"[batch_run][dry-run] index={task['index']} "
                f"task_id={task['task_id']} title={task['title_en']} "
                f"command={task['command']}"
            )
        return 0

    batch_dir.mkdir(parents=True, exist_ok=True)
    (batch_dir / "logs").mkdir(exist_ok=True)
    (batch_dir / "run_results").mkdir(exist_ok=True)
    write_json(batch_dir / "tasks.json", selected)
    results: list[dict[str, Any]] = []

    for run_no, task in enumerate(selected, 1):
        print(
            f"[batch_run] running {run_no}/{len(selected)} "
            f"index={task['index']} task_id={task['task_id']}"
        )
        result = run_task(task, batch_dir, run_no)
        results.append(result)
        append_summary(manifest_path, result)
        if summary_path is not None:
            append_summary(summary_path, result)
        status = "ok" if result["ok"] else "failed"
        print(
            f"[batch_run] {status} index={result['index']} "
            f"returncode={result['returncode']} elapsed={result['elapsed_sec']}s"
        )
        write_json(
            batch_dir / "batch_summary.json",
            batch_summary(
                batch_id=batch_id,
                batch_dir=batch_dir,
                tasks_json=args.tasks_json,
                language=args.language,
                selected=selected,
                results=results,
            ),
        )
        if not result["ok"] and not args.continue_on_error:
            return int(result["returncode"] or 1)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# python scripts/batch_run_inference_from_tasks.py \
#   --tasks-json docs/industrial_small_area_english_instructions.json \
#   --language en \
#   --continue-on-error \
#   --skip-completed
