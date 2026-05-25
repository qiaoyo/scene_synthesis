"""
Subprocess bridge to the Isaac Sim worker.

The scene_synthesis runtime may not run inside the SimKit/Isaac Python
environment. This bridge keeps Isaac imports in a separate process and
communicates through a small JSON protocol.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Dict
import select
import threading
import uuid

class IsaacBridgeError(RuntimeError):
    """Raised when the Isaac worker cannot complete a request."""


def _scene_to_dict(scene: Any) -> Dict[str, Any]:
    if hasattr(scene, "to_dict"):
        return scene.to_dict()
    if isinstance(scene, dict):
        return scene
    raise TypeError(f"Unsupported scene payload type: {type(scene)!r}")


def _last_json_object(stdout: str) -> Dict[str, Any]:
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    for line in reversed(lines):
        if not line.startswith("{"):
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            return payload
    raise IsaacBridgeError(f"Isaac worker did not return JSON. stdout={stdout[-1000:]!r}")


def run_isaac_operation(
    *,
    config: Any,
    operation: str,
    scene: Any,
    options: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """Run one Isaac operation in the configured worker process."""
    #worker_path = Path(getattr(config, "isaac_worker_path", "") or "")
    worker_path = Path("/home/simple/joey/scene_synthesis/scene_layout_react/physics/worker.py")
    #worker_path = Path("/home/simple/joey/scene_synthesis/scene_layout_react/physics/worker1.py")
    if not worker_path:
        worker_path = Path(__file__).with_name("worker.py")
    worker_path = worker_path.expanduser()

    isaac_python = Path(
        getattr(config, "isaac_python", "/home/simple/isaac_env/bin/python3")
    ).expanduser()
    
    if not worker_path.exists():
        raise IsaacBridgeError(f"Isaac worker script not found at {worker_path}")
    if not isaac_python.exists():
        raise IsaacBridgeError(f"Isaac Python executable not found at {isaac_python}")
    timeout_sec = float(getattr(config, "isaac_worker_timeout_sec", 120))
    
    operation_options = dict(options or {})
    temp_dir = Path(
        operation_options.get(
            "temp_dir",
            getattr(config, "isaac_temp_dir", "/tmp/scene_synthesis_isaac"),
        )
    )
    collision_approximation = getattr(
        config,
        "isaac_collision_approximation",
        "convexhull",
    )
    simulation_config = getattr(config, "isaac_simulation", {"headless": True})

    request = {
        "operation": operation,
        "scene": _scene_to_dict(scene),
        "options": operation_options,
        "temp_dir": str(temp_dir),
        "simulation_config": simulation_config,
        "collision_approximation": collision_approximation,
        "keep_stage": bool(
            getattr(config, "isaac_keep_stage", False)
            or operation_options.get("keep_stage", False)
            or operation_options.get("keep_temp_stage", False)
        ),
    }

    try:
        completed = subprocess.run(
            [str(isaac_python), str(worker_path)],
            input=json.dumps(request, ensure_ascii=False),
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )

    except subprocess.TimeoutExpired as exc:
        raise IsaacBridgeError(
            f"Isaac worker timed out after {timeout_sec}s"
        ) from exc
    except OSError as exc:
        raise IsaacBridgeError(
            f"Isaac worker could not be started: {exc}"
        ) from exc

    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        detail = stderr or stdout or "<no output>"
        raise IsaacBridgeError(
            f"Isaac worker failed with exit code {completed.returncode}: {detail}"
        )

    return _last_json_object(completed.stdout)


def run_isaac_physics_feedback(config: Any, scene: Any) -> Dict[str, Any]:
    """Return Observation.physics-shaped data from simulate_step."""
    try:
        payload = run_isaac_operation(
            config=config,
            operation="simulate_step",
            scene=scene,
            options={"duration": getattr(config, "physics_sim_duration", 2.0)},
        )
    except IsaacBridgeError as exc:
        return {
            "stable": False,
            "fallen_assets": [],
            "contacts": [],
            "warnings": [],
            "backend": "isaacsim",
            "error": str(exc),
        }

    if not payload.get("ok", False):
        return {
            "stable": False,
            "fallen_assets": payload.get("fallen_assets", []),
            "contacts": payload.get("contacts", []),
            "warnings": payload.get("warnings", []),
            "backend": "isaacsim",
            "error": payload.get("error") or "; ".join(payload.get("errors", [])),
        }

    return {
        "stable": bool(payload.get("stable", False)),
        "fallen_assets": payload.get("fallen_assets", []),
        "contacts": payload.get("contacts", []),
        "warnings": payload.get("warnings", []),
        "backend": payload.get("backend", "isaacsim"),
    }

__all__ = [
    "IsaacBridgeError",
    "run_isaac_operation",
    "run_isaac_physics_feedback",
]
