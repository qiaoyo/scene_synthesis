from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNS_ROOT = PROJECT_ROOT / "outputs" / "runs"
DEFAULT_OUTPUT_JSON = PROJECT_ROOT / "outputs" / "metrics" / "direct_metrics.json"
DEFAULT_OUTPUT_MD = PROJECT_ROOT / "outputs" / "metrics" / "direct_metrics.md"
EPSILON = 1e-9


@dataclass
class RunMetrics:
    run_id: str
    command: str
    sr_ok: bool
    saved_usd: bool
    usd_path: Optional[str]
    final_observation_ok: bool
    collision_free: Optional[bool]
    stable: Optional[bool]
    valid_support_count: int
    declared_support_count: int
    support_accuracy: Optional[float]
    steps: int
    action_steps: int
    tool_calls: int
    errors: List[str] = field(default_factory=list)


@dataclass
class BatchMetrics:
    runs_root: str
    run_count: int
    metrics: Dict[str, Optional[float]]
    counts: Dict[str, int]
    quality_score_available: Optional[float]
    weights: Dict[str, float]
    run_metrics: List[RunMetrics]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute directly implementable metrics from run record.json files."
    )
    parser.add_argument(
        "--runs-root",
        type=Path,
        default=DEFAULT_RUNS_ROOT,
        help="Directory containing outputs/runs/<run_id>/record.json files.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=DEFAULT_OUTPUT_JSON,
        help="Path to write aggregate metrics JSON.",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help="Path to write a compact aggregate Markdown report.",
    )
    parser.add_argument(
        "--include-run-details",
        action="store_true",
        help="Include per-run metric details in the JSON output.",
    )
    parser.add_argument(
        "--strict-unknown",
        action="store_true",
        help=(
            "Treat unknown collision/stability observations as failures. "
            "By default, CFR and PSR are computed only over observed boolean values."
        ),
    )
    return parser.parse_args()


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_record_paths(runs_root: Path) -> Iterable[Path]:
    yield from sorted(runs_root.expanduser().glob("*/record.json"))


def last_observation(record: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    for step in reversed(record.get("steps", []) or []):
        observation = step.get("observation")
        if isinstance(observation, dict):
            return observation
    return None


def bool_or_none(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    return None


def count_declared_support(observation: Optional[Dict[str, Any]]) -> int:
    if observation is None:
        return 0
    current_state = observation.get("current_state") or {}
    support_children = current_state.get("support_children") or {}
    if not isinstance(support_children, dict):
        return 0
    return sum(
        len(children)
        for children in support_children.values()
        if isinstance(children, list)
    )


def count_valid_support(observation: Optional[Dict[str, Any]]) -> int:
    if observation is None:
        return 0
    support_state = observation.get("support_state") or {}
    try:
        return int(support_state.get("valid_relation_count") or 0)
    except (TypeError, ValueError):
        return 0


def find_successful_save(record: Dict[str, Any]) -> tuple[bool, Optional[str], List[str]]:
    errors: List[str] = []
    for step in reversed(record.get("steps", []) or []):
        for tool in reversed(step.get("tools", []) or []):
            if tool.get("name") != "save_scene_usd":
                continue
            if tool.get("ok") is not True:
                return False, None, ["latest save_scene_usd tool was not ok"]

            result = tool.get("result") or {}
            data = result.get("data") or {}
            usd_path = data.get("usd_path")
            if result.get("ok") is False or data.get("ok") is False or data.get("save") is False:
                return False, str(usd_path) if usd_path else None, [
                    "latest save_scene_usd result did not report success"
                ]
            if not usd_path:
                return False, None, ["latest save_scene_usd result has no usd_path"]

            path = Path(str(usd_path)).expanduser()
            if not path.exists():
                return False, str(path), [f"saved USD path does not exist: {path}"]
            return True, str(path), errors

    return False, None, ["save_scene_usd was not called"]


def count_tool_calls(record: Dict[str, Any]) -> int:
    return sum(len(step.get("tools", []) or []) for step in record.get("steps", []) or [])


def count_action_steps(record: Dict[str, Any]) -> int:
    return sum(1 for step in record.get("steps", []) or [] if step.get("tools"))


def compute_run_metrics(record: Dict[str, Any]) -> RunMetrics:
    observation = last_observation(record)
    validation = observation.get("validation") if observation else {}
    physics_feedback = observation.get("physics_feedback") if observation else {}

    saved_usd, usd_path, errors = find_successful_save(record)
    final_observation_ok = bool(observation and observation.get("ok") is True)
    collision_free = bool_or_none((validation or {}).get("collision_free"))
    stable = bool_or_none((physics_feedback or {}).get("stable"))

    declared_support = count_declared_support(observation)
    valid_support = count_valid_support(observation)
    support_accuracy = (
        min(valid_support / max(declared_support, EPSILON), 1.0)
        if declared_support > 0
        else None
    )

    if observation is None:
        errors.append("no final observation found")
    elif not final_observation_ok:
        errors.append("final observation is not ok")

    return RunMetrics(
        run_id=str(record.get("run_id") or ""),
        command=str(record.get("command") or ""),
        sr_ok=bool(saved_usd and final_observation_ok),
        saved_usd=saved_usd,
        usd_path=usd_path,
        final_observation_ok=final_observation_ok,
        collision_free=collision_free,
        stable=stable,
        valid_support_count=valid_support,
        declared_support_count=declared_support,
        support_accuracy=support_accuracy,
        steps=len(record.get("steps", []) or []),
        action_steps=count_action_steps(record),
        tool_calls=count_tool_calls(record),
        errors=errors,
    )


def rate(values: List[bool]) -> Optional[float]:
    if not values:
        return None
    return sum(1 for value in values if value) / len(values)


def average(values: List[float]) -> Optional[float]:
    if not values:
        return None
    return sum(values) / len(values)


def observed_bool_values(
    run_metrics: List[RunMetrics],
    attr: str,
    strict_unknown: bool,
) -> List[bool]:
    values: List[bool] = []
    for item in run_metrics:
        value = getattr(item, attr)
        if isinstance(value, bool):
            values.append(value)
        elif strict_unknown:
            values.append(False)
    return values


def support_rate(run_metrics: List[RunMetrics]) -> Optional[float]:
    declared = sum(item.declared_support_count for item in run_metrics)
    if declared <= 0:
        return None
    valid = sum(item.valid_support_count for item in run_metrics)
    return min(valid / max(declared, EPSILON), 1.0)


def quality_score_available(
    metrics: Dict[str, Optional[float]],
    weights: Dict[str, float],
) -> Optional[float]:
    required = ("SR", "CFR", "PSR", "SVR", "AS", "S_max")
    if any(metrics.get(name) is None for name in required):
        return None
    step_penalty = metrics["AS"] / max(metrics["S_max"] or 1.0, EPSILON)
    return (
        weights["alpha"] * metrics["SR"]
        + weights["beta"] * metrics["CFR"]
        + weights["gamma"] * metrics["PSR"]
        + weights["delta"] * metrics["SVR"]
        - weights["mu"] * step_penalty
    )


def compute_batch_metrics(
    runs_root: Path,
    run_metrics: List[RunMetrics],
    strict_unknown: bool,
) -> BatchMetrics:
    steps = [float(item.steps) for item in run_metrics]
    action_steps = [float(item.action_steps) for item in run_metrics]
    tool_calls = [float(item.tool_calls) for item in run_metrics]
    weights = {
        "alpha": 0.25,
        "beta": 0.20,
        "gamma": 0.15,
        "delta": 0.15,
        "eta": 0.15,
        "lambda": 0.10,
        "mu": 0.05,
    }
    metrics: Dict[str, Optional[float]] = {
        "SR": rate([item.sr_ok for item in run_metrics]),
        "CFR": rate(observed_bool_values(run_metrics, "collision_free", strict_unknown)),
        "PSR": rate(observed_bool_values(run_metrics, "stable", strict_unknown)),
        "SVR": support_rate(run_metrics),
        "AS": average(steps),
        "AAS": average(action_steps),
        "ATC": average(tool_calls),
        "S_max": max(steps) if steps else None,
        "ACR": None,
        "RSR": None,
        "TCA": None,
        "TPS": None,
        "PE": None,
        "RE": None,
    }
    counts = {
        "run_count": len(run_metrics),
        "sr_ok_runs": sum(1 for item in run_metrics if item.sr_ok),
        "saved_usd_runs": sum(1 for item in run_metrics if item.saved_usd),
        "final_observation_ok_runs": sum(1 for item in run_metrics if item.final_observation_ok),
        "collision_observed_runs": sum(1 for item in run_metrics if item.collision_free is not None),
        "collision_free_runs": sum(1 for item in run_metrics if item.collision_free is True),
        "stability_observed_runs": sum(1 for item in run_metrics if item.stable is not None),
        "stable_runs": sum(1 for item in run_metrics if item.stable is True),
        "declared_support_total": sum(item.declared_support_count for item in run_metrics),
        "valid_support_total": sum(item.valid_support_count for item in run_metrics),
        "runs_with_errors": sum(1 for item in run_metrics if item.errors),
    }
    return BatchMetrics(
        runs_root=str(runs_root.expanduser()),
        run_count=len(run_metrics),
        metrics=metrics,
        counts=counts,
        quality_score_available=quality_score_available(metrics, weights),
        weights=weights,
        run_metrics=run_metrics,
    )


def load_run_metrics(runs_root: Path) -> List[RunMetrics]:
    run_metrics: List[RunMetrics] = []
    for record_path in iter_record_paths(runs_root):
        try:
            record = read_json(record_path)
            run_metrics.append(compute_run_metrics(record))
        except Exception as exc:
            run_metrics.append(
                RunMetrics(
                    run_id=record_path.parent.name,
                    command="",
                    sr_ok=False,
                    saved_usd=False,
                    usd_path=None,
                    final_observation_ok=False,
                    collision_free=None,
                    stable=None,
                    valid_support_count=0,
                    declared_support_count=0,
                    support_accuracy=None,
                    steps=0,
                    action_steps=0,
                    tool_calls=0,
                    errors=[f"failed to read record: {exc}"],
                )
            )
    return run_metrics


def format_percent(value: Optional[float]) -> str:
    if value is None:
        return "N/A"
    return f"{value * 100.0:.2f}%"


def format_number(value: Optional[float]) -> str:
    if value is None:
        return "N/A"
    return f"{value:.4f}"


def write_json(path: Path, batch: BatchMetrics, include_run_details: bool) -> None:
    payload = asdict(batch)
    if not include_run_details:
        payload.pop("run_metrics", None)
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_markdown(path: Path, batch: BatchMetrics) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    metrics = batch.metrics
    lines = [
        "# Direct Metrics Report",
        "",
        f"- Runs root: `{batch.runs_root}`",
        f"- Run count: `{batch.run_count}`",
        f"- Available-subset QS: `{format_number(batch.quality_score_available)}`",
        "",
        "| Metric | Value | Implementation |",
        "| --- | ---: | --- |",
        f"| SR | {format_percent(metrics.get('SR'))} | save_scene_usd success + USD exists + final observation ok |",
        f"| CFR | {format_percent(metrics.get('CFR'))} | final observation validation.collision_free |",
        f"| PSR | {format_percent(metrics.get('PSR'))} | final observation physics_feedback.stable |",
        f"| SVR | {format_percent(metrics.get('SVR'))} | valid support relations / declared support relations |",
        f"| AS | {format_number(metrics.get('AS'))} | average len(record.steps) |",
        f"| AAS | {format_number(metrics.get('AAS'))} | average steps containing tool calls |",
        f"| ATC | {format_number(metrics.get('ATC'))} | average tool records per run |",
        "",
        "## Counts",
        "",
        "| Count | Value |",
        "| --- | ---: |",
    ]
    for key, value in batch.counts.items():
        lines.append(f"| {key} | {value} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    runs_root = args.runs_root.expanduser()
    run_metrics = load_run_metrics(runs_root)
    batch = compute_batch_metrics(
        runs_root=runs_root,
        run_metrics=run_metrics,
        strict_unknown=bool(args.strict_unknown),
    )
    write_json(args.output_json, batch, include_run_details=bool(args.include_run_details))
    write_markdown(args.output_md, batch)

    print(f"[metrics] runs={batch.run_count}")
    print(f"[metrics] SR={format_percent(batch.metrics.get('SR'))}")
    print(f"[metrics] CFR={format_percent(batch.metrics.get('CFR'))}")
    print(f"[metrics] PSR={format_percent(batch.metrics.get('PSR'))}")
    print(f"[metrics] SVR={format_percent(batch.metrics.get('SVR'))}")
    print(f"[metrics] AS={format_number(batch.metrics.get('AS'))}")
    print(f"[metrics] ATC={format_number(batch.metrics.get('ATC'))}")
    print(f"[metrics] json={args.output_json.expanduser()}")
    print(f"[metrics] markdown={args.output_md.expanduser()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
