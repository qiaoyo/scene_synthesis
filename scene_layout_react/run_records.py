from __future__ import annotations

import json
import platform
import subprocess
import time
import uuid
from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_run_id() -> str:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{stamp}_{uuid.uuid4().hex[:8]}"

def jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return jsonable(value.to_dict())
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(v) for v in value]
    return str(value)


def git_revision() -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            timeout=2,
        )
    except Exception:
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def config_snapshot(config: Any) -> Dict[str, Any]:
    snapshot = jsonable(config)
    if not isinstance(snapshot, dict):
        snapshot = jsonable(getattr(config, "__dict__", {}))

    for key in list(snapshot.keys()):
        lowered = key.lower()
        if "key" in lowered or "token" in lowered or "secret" in lowered:
            snapshot[key] = "<redacted>"

    return snapshot


def perf_ms(start: float) -> float:
    return round((time.perf_counter() - start) * 1000.0, 3)


@dataclass
class ToolRecord:
    name: str
    arguments: Dict[str, Any]
    ok: bool
    elapsed_ms: float
    result: Dict[str, Any]


@dataclass
class StepRecord:
    step: int
    started_at: str
    elapsed_ms: Optional[float] = None
    strategy: Optional[Dict[str, Any]] = None
    decision: Optional[Dict[str, Any]] = None
    tools: List[ToolRecord] = field(default_factory=list)
    observation: Optional[Dict[str, Any]] = None
    reflection: Optional[Dict[str, Any]] = None
    scene_snapshot_path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return jsonable({
            "step": self.step,
            "started_at": self.started_at,
            "elapsed_ms": self.elapsed_ms,
            "strategy": self.strategy,
            "decision": self.decision,
            "tools": self.tools,
            "observation": self.observation,
            "reflection": self.reflection,
            "scene_snapshot_path": self.scene_snapshot_path,
        })


@dataclass
class RunRecord:
    run_id: str
    command: str
    started_at: str
    ok: Optional[bool] = None
    elapsed_ms: Optional[float] = None
    response: Optional[str] = None
    error: Optional[str] = None
    version: Dict[str, Any] = field(default_factory=dict)
    config: Dict[str, Any] = field(default_factory=dict)
    steps: List[StepRecord] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return jsonable({
            "run_id": self.run_id,
            "command": self.command,
            "started_at": self.started_at,
            "ok": self.ok,
            "elapsed_ms": self.elapsed_ms,
            "response": self.response,
            "error": self.error,
            "version": self.version,
            "config": self.config,
            "steps": self.steps,
        })


class RunRecorder:
    def __init__(self, output_dir: Path, run_id: str):
        self.run_id = run_id
        self.run_dir = Path(output_dir) / "runs" / run_id
        self.snapshot_dir = self.run_dir / "snapshots"
        self.events_path = self.run_dir / "events.jsonl"
        self.record_path = self.run_dir / "record.json"
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)
        self.tools_path = self.run_dir / "tools.json"
        self._tool_steps: List[Dict[str, Any]] = []
        

    def event(self, event_type: str, payload: Dict[str, Any]) -> None:
        event = {
            "type": event_type,
            "timestamp": now_iso(),
            "payload": jsonable(payload),
        }
        with self.events_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    def save_scene(self, step: int, scene: Dict[str, Any]) -> str:
        path = self.snapshot_dir / f"step_{step:03d}_scene.json"
        path.write_text(
            json.dumps(jsonable(scene), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return str(path)

    def save_record(self, record: RunRecord) -> None:
        self.record_path.write_text(
            json.dumps(record.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        
    def save_step_tool(
        self,
        step: int,
        tool_index: int,
        tool_record: ToolRecord,
        action_record: Dict[str, Any],
    ) -> None:
        step_entry = None

        for item in self._tool_steps:
            if item["step"] == step:
                step_entry = item
                break

        if step_entry is None:
            step_entry = {
                "step": step,
                "tools": [],
            }
            self._tool_steps.append(step_entry)

        step_entry["tools"].append({
            "tool_index": tool_index,
            "timestamp": now_iso(),
            "tool": tool_record,
            "action_summary": action_record,
        })

        payload = {
            "run_id": self.run_id,
            "steps": self._tool_steps,
        }

        self.tools_path.write_text(
            json.dumps(jsonable(payload), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        

def runtime_version() -> Dict[str, Any]:
    return {
        "git_revision": git_revision(),
        "python": platform.python_version(),
    }
    
    
def _compact_tool_args(tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name == "retrieve_asset":
        return {
            "query": args.get("query"),
            "expected_asset_type": args.get("expected_asset_type"),
            "top_k": args.get("top_k"),
        }

    if tool_name in {"place_instance", "move_asset"}:
        return dict(args)

    if tool_name == "set_support":
        return {
            "child_id": args.get("child_id"),
            "parent_id": args.get("parent_id"),
        }

    if tool_name == "check_collision":
        return {
            "instance_id_a": args.get("instance_id_a"),
            "instance_id_b": args.get("instance_id_b"),
        }

    if tool_name == "check_support":
        return {
            "child_id": args.get("child_id"),
            "parent_id": args.get("parent_id"),
        }

    if tool_name == "simulate_step":
        return {
            "duration": args.get("duration"),
            "update_scene": args.get("update_scene"),
        }

    if tool_name == "save_scene_usd":
        return {
            "keep_temp_stage": args.get("keep_temp_stage"),
        }

    return dict(args)


def _compact_tool_result(tool_name: str, result: ToolResult) -> Dict[str, Any]:
    data = result.data or {}

    if tool_name == "retrieve_asset":
        results = data.get("results", []) or []
        return {
            "count": data.get("count", len(results)),
            "asset_type": data.get("asset_type"),
            "top_doc_ids": [item.get("doc_id") for item in results[:3]],
        }

    if tool_name == "place_instance":
        return {
            "instance_id": data.get("instance_id"),
            "asset_type": data.get("asset_type"),
            "position": data.get("position"),
            "bbox_size": data.get("bbox_size"),
        }

    if tool_name == "set_support":
        return {
            "child": data.get("child"),
            "parent": data.get("parent"),
            "registered": data.get("registered"),
            "validation_performed": data.get("validation_performed"),
        }

    if tool_name == "check_collision":
        collisions = data.get("collisions", []) or []
        first = collisions[0] if collisions else {}
        return {
            "collision_free": data.get("collision_free"),
            "collision_count": len(collisions),
            "first_collision": {
                "a": first.get("a"),
                "b": first.get("b"),
                "overlap": first.get("overlap"),
                "suggested_move": first.get("suggested_move"),
            } if first else None,
            "suggested_move": data.get("suggested_move"),
            "suggested_moves": data.get("suggested_moves", [])[:3],
        }

    if tool_name == "check_support":
        return {
            "supported": data.get("supported"),
            "child": data.get("child"),
            "parent": data.get("parent"),
            "issues": data.get("issues", []),
            "z_gap": data.get("z_gap"),
            "xy_coverage": data.get("xy_coverage"),
            "suggested_move": data.get("suggested_move"),
        }

    if tool_name == "move_asset":
        return {
            "instance_id": data.get("instance_id"),
            "old_position": data.get("old_position"),
            "new_position": data.get("new_position"),
        }

    if tool_name == "simulate_step":
        return {
            "stable": data.get("stable"),
            "fallen_assets": data.get("fallen_assets", []),
        }

    if tool_name == "save_scene_usd":
        return {
            "saved": result.ok,
            "usd_path": data.get("usd_path"),
            "exported_count": data.get("exported_count"),
            "instance_count": data.get("instance_count"),
        }

    return data

def _make_action_record(
    step_idx: int,
    tool_name: str,
    tool_args: Dict[str, Any],
    result: ToolResult,
) -> Dict[str, Any]:
    return {
        "step": step_idx,
        "name": tool_name,
        "arguments": _compact_tool_args(tool_name, tool_args),
        "ok": result.ok,
        "error": result.error,
        "summary": _compact_tool_result(tool_name, result),
    }

def _recent_action_records(history: List[AgentStep], limit: int = 3) -> List[Dict[str, Any]]:
    records = []
    for step in history[-limit:]:
        if step.action_records:
            records.append({
                "step": step.step,
                "actions": step.action_records,
            })
    return records
