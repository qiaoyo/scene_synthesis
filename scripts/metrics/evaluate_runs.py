from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNS_ROOT = PROJECT_ROOT / "outputs" / "runs"
DEFAULT_TASKS_JSON = PROJECT_ROOT / "docs" / "industrial_small_area_english_instructions.json"
DEFAULT_OUTPUT_JSON = PROJECT_ROOT / "outputs" / "metrics" / "direct_metrics.json"
DEFAULT_OUTPUT_MD = PROJECT_ROOT / "outputs" / "metrics" / "direct_metrics.md"
EPSILON = 1e-9


@dataclass
class TaskAnnotation:
    task_id: str
    command_en: str
    command_zh: str
    asset_types: List[str]
    support_relations: List[tuple[str, str]]


@dataclass
class RunMetrics:
    run_id: str
    task_id: Optional[str]
    task_index: Optional[int]
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
    asset_coverage: Optional[float]
    required_asset_count: int
    covered_asset_count: int
    required_asset_counts: Dict[str, int]
    placed_asset_counts: Dict[str, int]
    missing_assets: Dict[str, int]
    extra_assets: Dict[str, int]
    relation_satisfaction: Optional[float]
    required_support_relation_count: int
    satisfied_support_relation_count: int
    required_support_relation_counts: Dict[str, int]
    satisfied_support_relation_counts: Dict[str, int]
    missing_support_relations: Dict[str, int]
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
    quality_score_full: Optional[float]
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
        "--tasks-json",
        type=Path,
        default=DEFAULT_TASKS_JSON,
        help="Task annotation JSON file with asset_types and support_relations.",
    )
    parser.add_argument(
        "--batch-manifest",
        type=Path,
        default=None,
        help="Optional batch_manifest.jsonl mapping run_id to task_id.",
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


def read_json_any(path: Path) -> Any:
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


def normalize_type(value: Any) -> str:
    text = str(value or "").strip()
    aliases = {
        "Part": "IndustrialPart",
        "Robot": "IndustrialRobot",
        "Industrialrobot": "IndustrialRobot",
    }
    return aliases.get(text, text)


def relation_key(child_type: str, parent_type: str) -> str:
    return f"{normalize_type(child_type)} supported_by {normalize_type(parent_type)}"


def parse_support_relation(text: str) -> Optional[tuple[str, str]]:
    quoted = re.findall(r"`([^`]+)`", text)
    if len(quoted) >= 2:
        return normalize_type(quoted[0]), normalize_type(quoted[1])
    match = re.search(
        r"([A-Za-z]+)\s+supported\s+by\s+([A-Za-z]+)",
        text,
        flags=re.IGNORECASE,
    )
    if match:
        return normalize_type(match.group(1)), normalize_type(match.group(2))
    return None


def load_task_annotations(
    path: Optional[Path],
) -> tuple[dict[str, TaskAnnotation], dict[str, TaskAnnotation]]:
    if path is None:
        return {}, {}
    expanded = path.expanduser()
    if not expanded.exists():
        return {}, {}
    payload = read_json_any(expanded)
    if not isinstance(payload, list):
        raise ValueError(f"Expected top-level JSON list in {expanded}")

    by_id: dict[str, TaskAnnotation] = {}
    by_command: dict[str, TaskAnnotation] = {}
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            continue
        task_id = str(item.get("id") or index)
        relations: list[tuple[str, str]] = []
        for raw_relation in item.get("support_relations") or []:
            parsed = parse_support_relation(str(raw_relation))
            if parsed is not None:
                relations.append(parsed)
        annotation = TaskAnnotation(
            task_id=task_id,
            command_en=str(item.get("instruction_en") or "").strip(),
            command_zh=str(item.get("instruction_zh") or "").strip(),
            asset_types=[normalize_type(value) for value in item.get("asset_types") or []],
            support_relations=relations,
        )
        by_id[task_id] = annotation
        if annotation.command_en:
            by_command[annotation.command_en] = annotation
        if annotation.command_zh:
            by_command[annotation.command_zh] = annotation
    return by_id, by_command


def load_batch_manifest(path: Optional[Path]) -> list[dict[str, Any]]:
    if path is None:
        return []
    expanded = path.expanduser()
    if not expanded.exists():
        return []
    records: list[dict[str, Any]] = []
    for line in expanded.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        payload = json.loads(line)
        if isinstance(payload, dict):
            records.append(payload)
    return records


def manifest_by_run_id(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_run_id: dict[str, dict[str, Any]] = {}
    for record in records:
        run_id = record.get("run_id")
        if isinstance(run_id, str) and run_id:
            by_run_id[run_id] = record
    return by_run_id


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


def final_instances(observation: Optional[Dict[str, Any]]) -> dict[str, dict[str, Any]]:
    if observation is None:
        return {}
    current_state = observation.get("current_state") or {}
    instances = current_state.get("instances") or {}
    if not isinstance(instances, dict):
        return {}
    return {
        str(instance_id): payload
        for instance_id, payload in instances.items()
        if isinstance(payload, dict)
    }


def placed_asset_counts(observation: Optional[Dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for instance in final_instances(observation).values():
        asset_type = normalize_type(instance.get("asset_type"))
        if asset_type:
            counts[asset_type] += 1
    return counts


def invalid_support_pairs(observation: Optional[Dict[str, Any]]) -> set[tuple[str, str]]:
    if observation is None:
        return set()
    support_state = observation.get("support_state") or {}
    invalid_relations = support_state.get("invalid_relations") or []
    pairs: set[tuple[str, str]] = set()
    if not isinstance(invalid_relations, list):
        return pairs
    for relation in invalid_relations:
        if not isinstance(relation, dict):
            continue
        child = relation.get("child")
        parent = relation.get("parent")
        if isinstance(child, str) and isinstance(parent, str):
            pairs.add((child, parent))
    return pairs


def valid_support_relation_counts(observation: Optional[Dict[str, Any]]) -> Counter[str]:
    if observation is None:
        return Counter()
    instances = final_instances(observation)
    invalid_pairs = invalid_support_pairs(observation)
    current_state = observation.get("current_state") or {}
    support_children = current_state.get("support_children") or {}
    counts: Counter[str] = Counter()
    if not isinstance(support_children, dict):
        return counts
    for parent_id, children in support_children.items():
        if not isinstance(parent_id, str) or not isinstance(children, list):
            continue
        parent = instances.get(parent_id)
        if parent is None:
            continue
        parent_type = normalize_type(parent.get("asset_type"))
        for child_id in children:
            if not isinstance(child_id, str):
                continue
            if (child_id, parent_id) in invalid_pairs:
                continue
            child = instances.get(child_id)
            if child is None:
                continue
            child_type = normalize_type(child.get("asset_type"))
            if child_type and parent_type:
                counts[relation_key(child_type, parent_type)] += 1
    return counts


def counter_to_dict(counter: Counter[str]) -> Dict[str, int]:
    return {key: int(value) for key, value in sorted(counter.items())}


def asset_coverage(annotation: Optional[TaskAnnotation], observation: Optional[Dict[str, Any]]) -> dict[str, Any]:
    if annotation is None or not annotation.asset_types:
        return {
            "score": None,
            "required_count": 0,
            "covered_count": 0,
            "required_counts": {},
            "placed_counts": counter_to_dict(placed_asset_counts(observation)),
            "missing": {},
            "extra": {},
        }
    required = Counter(annotation.asset_types)
    placed = placed_asset_counts(observation)
    covered = Counter(
        {asset_type: min(required[asset_type], placed.get(asset_type, 0)) for asset_type in required}
    )
    missing = Counter(
        {
            asset_type: required[asset_type] - placed.get(asset_type, 0)
            for asset_type in required
            if placed.get(asset_type, 0) < required[asset_type]
        }
    )
    extra = Counter(
        {
            asset_type: placed[asset_type] - required.get(asset_type, 0)
            for asset_type in placed
            if placed[asset_type] > required.get(asset_type, 0)
        }
    )
    required_count = sum(required.values())
    covered_count = sum(covered.values())
    return {
        "score": covered_count / max(required_count, EPSILON),
        "required_count": int(required_count),
        "covered_count": int(covered_count),
        "required_counts": counter_to_dict(required),
        "placed_counts": counter_to_dict(placed),
        "missing": counter_to_dict(missing),
        "extra": counter_to_dict(extra),
    }


def relation_satisfaction(
    annotation: Optional[TaskAnnotation],
    observation: Optional[Dict[str, Any]],
) -> dict[str, Any]:
    if annotation is None or not annotation.support_relations:
        return {
            "score": None,
            "required_count": 0,
            "satisfied_count": 0,
            "required_counts": {},
            "satisfied_counts": {},
            "missing": {},
        }
    required = Counter(
        relation_key(child_type, parent_type)
        for child_type, parent_type in annotation.support_relations
    )
    valid = valid_support_relation_counts(observation)
    satisfied = Counter(
        {key: min(required[key], valid.get(key, 0)) for key in required}
    )
    missing = Counter(
        {
            key: required[key] - valid.get(key, 0)
            for key in required
            if valid.get(key, 0) < required[key]
        }
    )
    required_count = sum(required.values())
    satisfied_count = sum(satisfied.values())
    return {
        "score": satisfied_count / max(required_count, EPSILON),
        "required_count": int(required_count),
        "satisfied_count": int(satisfied_count),
        "required_counts": counter_to_dict(required),
        "satisfied_counts": counter_to_dict(satisfied),
        "missing": counter_to_dict(missing),
    }


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


def compute_run_metrics(
    record: Dict[str, Any],
    annotation: Optional[TaskAnnotation] = None,
    manifest_record: Optional[dict[str, Any]] = None,
) -> RunMetrics:
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

    asset = asset_coverage(annotation, observation)
    relation = relation_satisfaction(annotation, observation)
    task_index = None
    if manifest_record is not None and isinstance(manifest_record.get("task_index"), int):
        task_index = int(manifest_record["task_index"])
    elif manifest_record is not None and isinstance(manifest_record.get("index"), int):
        task_index = int(manifest_record["index"])

    return RunMetrics(
        run_id=str(record.get("run_id") or ""),
        task_id=annotation.task_id if annotation else None,
        task_index=task_index,
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
        asset_coverage=asset["score"],
        required_asset_count=asset["required_count"],
        covered_asset_count=asset["covered_count"],
        required_asset_counts=asset["required_counts"],
        placed_asset_counts=asset["placed_counts"],
        missing_assets=asset["missing"],
        extra_assets=asset["extra"],
        relation_satisfaction=relation["score"],
        required_support_relation_count=relation["required_count"],
        satisfied_support_relation_count=relation["satisfied_count"],
        required_support_relation_counts=relation["required_counts"],
        satisfied_support_relation_counts=relation["satisfied_counts"],
        missing_support_relations=relation["missing"],
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


def coverage_rate(run_metrics: List[RunMetrics]) -> Optional[float]:
    required = sum(item.required_asset_count for item in run_metrics)
    if required <= 0:
        return None
    covered = sum(item.covered_asset_count for item in run_metrics)
    return min(covered / max(required, EPSILON), 1.0)


def relation_rate(run_metrics: List[RunMetrics]) -> Optional[float]:
    required = sum(item.required_support_relation_count for item in run_metrics)
    if required <= 0:
        return None
    satisfied = sum(item.satisfied_support_relation_count for item in run_metrics)
    return min(satisfied / max(required, EPSILON), 1.0)


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


def quality_score_full(
    metrics: Dict[str, Optional[float]],
    weights: Dict[str, float],
) -> Optional[float]:
    required = ("SR", "CFR", "PSR", "SVR", "ACR", "RSR", "AS", "S_max")
    if any(metrics.get(name) is None for name in required):
        return None
    step_penalty = metrics["AS"] / max(metrics["S_max"] or 1.0, EPSILON)
    return (
        weights["alpha"] * metrics["SR"]
        + weights["beta"] * metrics["CFR"]
        + weights["gamma"] * metrics["PSR"]
        + weights["delta"] * metrics["SVR"]
        + weights["eta"] * metrics["ACR"]
        + weights["lambda"] * metrics["RSR"]
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
        "ACR": coverage_rate(run_metrics),
        "RSR": relation_rate(run_metrics),
        "TCA": None,
        "TPS": None,
        "PE": None,
        "RE": None,
    }
    annotated_runs = sum(
        1
        for item in run_metrics
        if item.required_asset_count > 0 or item.required_support_relation_count > 0
    )
    counts = {
        "run_count": len(run_metrics),
        "annotated_runs": annotated_runs,
        "sr_ok_runs": sum(1 for item in run_metrics if item.sr_ok),
        "saved_usd_runs": sum(1 for item in run_metrics if item.saved_usd),
        "final_observation_ok_runs": sum(1 for item in run_metrics if item.final_observation_ok),
        "collision_observed_runs": sum(1 for item in run_metrics if item.collision_free is not None),
        "collision_free_runs": sum(1 for item in run_metrics if item.collision_free is True),
        "stability_observed_runs": sum(1 for item in run_metrics if item.stable is not None),
        "stable_runs": sum(1 for item in run_metrics if item.stable is True),
        "declared_support_total": sum(item.declared_support_count for item in run_metrics),
        "valid_support_total": sum(item.valid_support_count for item in run_metrics),
        "required_asset_total": sum(item.required_asset_count for item in run_metrics),
        "covered_asset_total": sum(item.covered_asset_count for item in run_metrics),
        "required_support_relation_total": sum(
            item.required_support_relation_count for item in run_metrics
        ),
        "satisfied_support_relation_total": sum(
            item.satisfied_support_relation_count for item in run_metrics
        ),
        "runs_with_errors": sum(1 for item in run_metrics if item.errors),
    }
    full_score = (
        quality_score_full(metrics, weights)
        if run_metrics and annotated_runs == len(run_metrics)
        else None
    )
    return BatchMetrics(
        runs_root=str(runs_root.expanduser()),
        run_count=len(run_metrics),
        metrics=metrics,
        counts=counts,
        quality_score_available=quality_score_available(metrics, weights),
        quality_score_full=full_score,
        weights=weights,
        run_metrics=run_metrics,
    )


def annotation_for_record(
    record: Dict[str, Any],
    record_path: Path,
    annotations_by_id: dict[str, TaskAnnotation],
    annotations_by_command: dict[str, TaskAnnotation],
    manifest_records_by_run_id: dict[str, dict[str, Any]],
) -> tuple[Optional[TaskAnnotation], Optional[dict[str, Any]]]:
    run_id = str(record.get("run_id") or record_path.parent.name)
    manifest_record = manifest_records_by_run_id.get(run_id)
    if manifest_record is not None:
        task_id = manifest_record.get("task_id")
        if isinstance(task_id, str) and task_id in annotations_by_id:
            return annotations_by_id[task_id], manifest_record
    command = str(record.get("command") or "").strip()
    return annotations_by_command.get(command), manifest_record


def failed_manifest_run_metrics(
    manifest_record: dict[str, Any],
    annotation: Optional[TaskAnnotation],
) -> RunMetrics:
    asset = asset_coverage(annotation, None)
    relation = relation_satisfaction(annotation, None)
    run_id = str(
        manifest_record.get("run_id")
        or f"missing_record_{manifest_record.get('task_id', manifest_record.get('task_index', 'unknown'))}"
    )
    task_index = None
    if isinstance(manifest_record.get("task_index"), int):
        task_index = int(manifest_record["task_index"])
    elif isinstance(manifest_record.get("index"), int):
        task_index = int(manifest_record["index"])
    return RunMetrics(
        run_id=run_id,
        task_id=annotation.task_id if annotation else str(manifest_record.get("task_id") or ""),
        task_index=task_index,
        command=str(manifest_record.get("command") or ""),
        sr_ok=False,
        saved_usd=False,
        usd_path=None,
        final_observation_ok=False,
        collision_free=None,
        stable=None,
        valid_support_count=0,
        declared_support_count=0,
        support_accuracy=None,
        asset_coverage=asset["score"],
        required_asset_count=asset["required_count"],
        covered_asset_count=asset["covered_count"],
        required_asset_counts=asset["required_counts"],
        placed_asset_counts=asset["placed_counts"],
        missing_assets=asset["missing"],
        extra_assets=asset["extra"],
        relation_satisfaction=relation["score"],
        required_support_relation_count=relation["required_count"],
        satisfied_support_relation_count=relation["satisfied_count"],
        required_support_relation_counts=relation["required_counts"],
        satisfied_support_relation_counts=relation["satisfied_counts"],
        missing_support_relations=relation["missing"],
        steps=0,
        action_steps=0,
        tool_calls=0,
        errors=["record.json not found for batch manifest entry"],
    )


def load_run_metrics(
    runs_root: Path,
    annotations_by_id: dict[str, TaskAnnotation],
    annotations_by_command: dict[str, TaskAnnotation],
    manifest_records: list[dict[str, Any]],
) -> List[RunMetrics]:
    run_metrics: List[RunMetrics] = []
    manifest_records_by_run_id = manifest_by_run_id(manifest_records)
    seen_run_ids: set[str] = set()
    for record_path in iter_record_paths(runs_root):
        try:
            record = read_json(record_path)
            annotation, manifest_record = annotation_for_record(
                record,
                record_path,
                annotations_by_id,
                annotations_by_command,
                manifest_records_by_run_id,
            )
            run_id = str(record.get("run_id") or record_path.parent.name)
            seen_run_ids.add(run_id)
            run_metrics.append(compute_run_metrics(record, annotation, manifest_record))
        except Exception as exc:
            run_metrics.append(
                RunMetrics(
                    run_id=record_path.parent.name,
                    task_id=None,
                    task_index=None,
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
                    asset_coverage=None,
                    required_asset_count=0,
                    covered_asset_count=0,
                    required_asset_counts={},
                    placed_asset_counts={},
                    missing_assets={},
                    extra_assets={},
                    relation_satisfaction=None,
                    required_support_relation_count=0,
                    satisfied_support_relation_count=0,
                    required_support_relation_counts={},
                    satisfied_support_relation_counts={},
                    missing_support_relations={},
                    steps=0,
                    action_steps=0,
                    tool_calls=0,
                    errors=[f"failed to read record: {exc}"],
                )
            )
    for manifest_record in manifest_records:
        run_id = manifest_record.get("run_id")
        if isinstance(run_id, str) and run_id in seen_run_ids:
            continue
        record_path = manifest_record.get("record_path")
        if isinstance(record_path, str):
            expanded_record_path = Path(record_path).expanduser()
            if expanded_record_path.exists():
                try:
                    record = read_json(expanded_record_path)
                    task_id = manifest_record.get("task_id")
                    annotation = (
                        annotations_by_id.get(str(task_id))
                        if task_id is not None
                        else None
                    )
                    record_run_id = str(record.get("run_id") or expanded_record_path.parent.name)
                    seen_run_ids.add(record_run_id)
                    run_metrics.append(compute_run_metrics(record, annotation, manifest_record))
                    continue
                except Exception as exc:
                    failed = failed_manifest_run_metrics(manifest_record, None)
                    failed.errors.append(f"failed to read manifest record_path: {exc}")
                    run_metrics.append(failed)
                    continue
        task_id = manifest_record.get("task_id")
        annotation = annotations_by_id.get(str(task_id)) if task_id is not None else None
        run_metrics.append(failed_manifest_run_metrics(manifest_record, annotation))
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
        f"- Full QS: `{format_number(batch.quality_score_full)}`",
        "",
        "| Metric | Value | Implementation |",
        "| --- | ---: | --- |",
        f"| SR | {format_percent(metrics.get('SR'))} | save_scene_usd success + USD exists + final observation ok |",
        f"| CFR | {format_percent(metrics.get('CFR'))} | final observation validation.collision_free |",
        f"| PSR | {format_percent(metrics.get('PSR'))} | final observation physics_feedback.stable |",
        f"| SVR | {format_percent(metrics.get('SVR'))} | valid support relations / declared support relations |",
        f"| ACR | {format_percent(metrics.get('ACR'))} | required asset count coverage from task annotations |",
        f"| RSR | {format_percent(metrics.get('RSR'))} | required support relation satisfaction from task annotations |",
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
    annotations_by_id, annotations_by_command = load_task_annotations(args.tasks_json)
    manifest_records = load_batch_manifest(args.batch_manifest)
    run_metrics = load_run_metrics(
        runs_root,
        annotations_by_id,
        annotations_by_command,
        manifest_records,
    )
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
    print(f"[metrics] ACR={format_percent(batch.metrics.get('ACR'))}")
    print(f"[metrics] RSR={format_percent(batch.metrics.get('RSR'))}")
    print(f"[metrics] AS={format_number(batch.metrics.get('AS'))}")
    print(f"[metrics] ATC={format_number(batch.metrics.get('ATC'))}")
    print(f"[metrics] json={args.output_json.expanduser()}")
    print(f"[metrics] markdown={args.output_md.expanduser()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
