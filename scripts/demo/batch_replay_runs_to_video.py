from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[1]
DEFAULT_RUNS_ROOT = ROOT / "outputs" / "runs"
DEFAULT_OUTPUT_DIR = ROOT / "outputs" / "demo_videos"
DEFAULT_ISAAC_PYTHON = Path("/home/simple/isaac_env/bin/python")
REPLAY_SCRIPT = SCRIPT_DIR / "replay_run_to_video.py"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from replay_run_to_video import _load_json, _summarize


@dataclass
class RunInfo:
    run_dir: Path
    output_path: Path
    log_path: Path
    record_path: Path
    stage_path: Path
    final_instances: int
    place_actions: int
    move_actions: int


def _default_python() -> Path:
    if DEFAULT_ISAAC_PYTHON.exists():
        return DEFAULT_ISAAC_PYTHON
    return Path(sys.executable)


def _normalize_run_dir(path: Path) -> Path:
    candidate = path.expanduser().resolve()
    if candidate.is_file() and candidate.name == "record.json":
        return candidate.parent
    return candidate


def _read_run_list(path: Path) -> List[Path]:
    run_dirs: List[Path] = []
    for raw_line in path.expanduser().read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line:
            run_dirs.append(Path(line))
    return run_dirs


def _find_run_dirs(args: argparse.Namespace) -> List[Path]:
    paths: List[Path] = list(args.run_dirs)

    for list_path in args.run_list:
        paths.extend(_read_run_list(list_path))

    runs_root = args.runs_root
    if runs_root is None and not paths:
        runs_root = DEFAULT_RUNS_ROOT

    if runs_root is not None:
        root = runs_root.expanduser().resolve()
        matches = root.rglob(args.glob) if args.recursive else root.glob(args.glob)
        for match in matches:
            if match.is_file() and match.name == "record.json":
                paths.append(match.parent)
            elif match.is_dir() and (match / "record.json").exists():
                paths.append(match)

    unique: List[Path] = []
    seen = set()
    for path in paths:
        run_dir = _normalize_run_dir(path)
        key = str(run_dir)
        if key not in seen:
            unique.append(run_dir)
            seen.add(key)
    return unique


def _inspect_run(run_dir: Path, output_dir: Path, output_in_run_dir: bool) -> RunInfo:
    record_path = run_dir / "record.json"
    if not record_path.exists():
        raise FileNotFoundError(f"record.json not found: {record_path}")

    record = _load_json(record_path)
    summary = _summarize(record, run_dir)
    actions = summary["actions"]
    place_count = sum(1 for action in actions if action.kind == "place_instance")
    move_count = sum(1 for action in actions if action.kind == "move_asset")
    target_dir = run_dir if output_in_run_dir else output_dir
    output_path = target_dir / f"{run_dir.name}_replay.mp4"
    log_path = target_dir / f"{run_dir.name}_render.log"

    return RunInfo(
        run_dir=run_dir,
        output_path=output_path,
        log_path=log_path,
        record_path=summary["record_path"],
        stage_path=summary["stage_path"],
        final_instances=len(summary["final_instances"]),
        place_actions=place_count,
        move_actions=move_count,
    )


def _append_option(command: List[str], flag: str, value: Any) -> None:
    command.extend([flag, str(value)])


def _build_command(info: RunInfo, args: argparse.Namespace) -> List[str]:
    command = [
        str(args.python.expanduser()),
        str(REPLAY_SCRIPT),
        str(info.run_dir),
        "--render",
        "--output",
        str(info.output_path),
    ]
    if args.headless:
        command.append("--headless")

    for flag, value in [
        ("--fps", args.fps),
        ("--width", args.width),
        ("--height", args.height),
        ("--action-frames", args.action_frames),
        ("--hold-frames", args.hold_frames),
        ("--initial-hold-frames", args.initial_hold_frames),
        ("--final-hold-frames", args.final_hold_frames),
        ("--hidden-distance", args.hidden_distance),
        ("--spawn-height-scale", args.spawn_height_scale),
        ("--spawn-height-min", args.spawn_height_min),
        ("--render-preset", args.render_preset),
        ("--spp", args.spp),
        ("--bitrate", args.bitrate),
    ]:
        _append_option(command, flag, value)

    return command


def _run_command(command: List[str], log_path: Path, label: str) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log_file:
        log_file.write(f"$ {shlex.join(command)}\n")
        log_file.flush()
        process = subprocess.Popen(
            command,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        if process.stdout is not None:
            for line in process.stdout:
                print(f"[{label}] {line}", end="", flush=True)
                log_file.write(line)
        return process.wait()


def _result_dict(info: RunInfo, status: str, returncode: int | None) -> Dict[str, Any]:
    return {
        "run_dir": str(info.run_dir),
        "output_path": str(info.output_path),
        "log_path": str(info.log_path),
        "record_path": str(info.record_path),
        "stage_path": str(info.stage_path),
        "final_instances": info.final_instances,
        "place_actions": info.place_actions,
        "move_actions": info.move_actions,
        "status": status,
        "returncode": returncode,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch replay run directories into Isaac Sim videos.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("run_dirs", nargs="*", type=Path, help="Run directories or record.json files")
    parser.add_argument("--run-list", action="append", type=Path, default=[], help="Text file with one run_dir per line")
    parser.add_argument("--runs-root", type=Path, default=None, help="Directory to scan for run directories")
    parser.add_argument("--glob", default="*/record.json", help="Glob used with --runs-root")
    parser.add_argument("--recursive", action="store_true", help="Use recursive search under --runs-root")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for videos and logs")
    parser.add_argument("--output-in-run-dir", action="store_true", help="Save each video and log into its own run_dir")
    parser.add_argument(
        "--collect-to-output-dir",
        dest="output_in_run_dir",
        action="store_false",
        help="Save all videos and logs into --output-dir instead",
    )
    parser.add_argument("--python", type=Path, default=_default_python(), help="Python executable with Isaac Sim available")
    parser.add_argument("--dry-run", action="store_true", help="Inspect runs and print commands without rendering")
    parser.add_argument("--skip-existing", action="store_true", help="Skip runs whose output mp4 already exists")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop after the first failed render")
    parser.add_argument("--headless", action="store_true", help="Pass --headless to the single-run renderer")
    parser.add_argument("--fps", type=int, default=30, help="Capture FPS")
    parser.add_argument("--width", type=int, default=1920, help="Capture width")
    parser.add_argument("--height", type=int, default=1080, help="Capture height")
    parser.add_argument("--action-frames", type=int, default=12, help="Frames per place/move action")
    parser.add_argument("--hold-frames", type=int, default=3, help="Hold frames after each action")
    parser.add_argument("--initial-hold-frames", type=int, default=8, help="Frames to hold the initial hidden state")
    parser.add_argument("--final-hold-frames", type=int, default=20, help="Frames to hold the final state")
    parser.add_argument("--hidden-distance", type=float, default=1000.0, help="Off-screen hidden distance")
    parser.add_argument("--spawn-height-scale", type=float, default=1.2, help="Spawn height multiplier")
    parser.add_argument("--spawn-height-min", type=float, default=0.6, help="Minimum spawn height above target")
    parser.add_argument(
        "--render-preset",
        choices=["PATH_TRACE", "RAY_TRACE", "IRAY", "REAL_TIME_PATHTRACING"],
        default="PATH_TRACE",
        help="Capture render preset",
    )
    parser.add_argument("--spp", type=int, default=1, help="Path tracing samples per pixel")
    parser.add_argument("--bitrate", type=int, default=16_777_216, help="MP4 encoding bitrate")
    parser.set_defaults(output_in_run_dir=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dirs = _find_run_dirs(args)
    if not run_dirs:
        print("No run directories found. Pass run_dirs, --run-list, or --runs-root.", file=sys.stderr)
        return 2

    output_dir = args.output_dir.expanduser().resolve()
    if not args.output_in_run_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    results: List[Dict[str, Any]] = []
    failures = 0
    print(f"batch_runs: {len(run_dirs)}")
    print(f"output_mode: {'run_dir' if args.output_in_run_dir else 'output_dir'}")
    print(f"output_dir: {output_dir}")
    print(f"python: {args.python.expanduser()}")

    for index, run_dir in enumerate(run_dirs, start=1):
        label = f"{index:03d}_{run_dir.name}"
        try:
            info = _inspect_run(run_dir, output_dir, bool(args.output_in_run_dir))
        except Exception as exc:
            failures += 1
            print(f"[{label}] inspect failed: {exc}", flush=True)
            results.append(
                {
                    "run_dir": str(run_dir),
                    "status": "inspect_failed",
                    "error": str(exc),
                    "returncode": None,
                }
            )
            if args.stop_on_error:
                break
            continue

        print(
            f"[{label}] instances={info.final_instances} "
            f"place={info.place_actions} move={info.move_actions} output={info.output_path}",
            flush=True,
        )

        if args.skip_existing and info.output_path.exists() and info.output_path.stat().st_size > 0:
            print(f"[{label}] skipped existing output", flush=True)
            results.append(_result_dict(info, "skipped_existing", 0))
            continue

        command = _build_command(info, args)
        if args.dry_run:
            print(f"[{label}] command: {shlex.join(command)}", flush=True)
            results.append(_result_dict(info, "dry_run", None))
            continue

        returncode = _run_command(command, info.log_path, label)
        if returncode == 0:
            results.append(_result_dict(info, "rendered", returncode))
        else:
            failures += 1
            results.append(_result_dict(info, "failed", returncode))
            print(f"[{label}] failed with returncode={returncode}", flush=True)
            if args.stop_on_error:
                break

    if args.output_in_run_dir:
        manifest_dir = args.runs_root.expanduser().resolve() if args.runs_root else DEFAULT_RUNS_ROOT
    else:
        manifest_dir = output_dir
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / "batch_manifest.json"
    manifest_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"manifest: {manifest_path}")
    print(f"completed: {len(results)}")
    print(f"failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
