"""
Subprocess bridge to the Isaac Sim worker.

The scene_synthesis runtime may not run inside the SimKit/Isaac Python
environment. This bridge keeps Isaac imports in a separate process and
communicates through a small JSON protocol.
"""

from __future__ import annotations

import json
import queue
import subprocess
import threading
import time
from pathlib import Path
from typing import Any, Dict

class IsaacBridgeError(RuntimeError):
    """Raised when the Isaac worker cannot complete a request."""


_PERSISTENT_CLIENTS: Dict[tuple[str, str, str], "IsaacWorkerClient"] = {}
_PERSISTENT_CLIENTS_LOCK = threading.Lock()


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


def _worker_paths(config: Any) -> tuple[Path, Path]:
    configured_worker_path = getattr(config, "isaac_worker_path", None)
    if configured_worker_path:
        worker_path = Path(configured_worker_path)
    else:
        worker_path = Path(__file__).with_name("worker.py")
    worker_path = worker_path.expanduser()

    isaac_python = Path(
        getattr(config, "isaac_python", "/home/simple/isaac_env/bin/python3")
    ).expanduser()
    
    if not worker_path.exists():
        raise IsaacBridgeError(f"Isaac worker script not found at {worker_path}")
    if not isaac_python.exists():
        raise IsaacBridgeError(f"Isaac Python executable not found at {isaac_python}")

    return worker_path, isaac_python


def _build_request(
    *,
    config: Any,
    operation: str,
    scene: Any,
    options: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
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

    return {
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


def _run_isaac_operation_once(
    *,
    config: Any,
    request: Dict[str, Any],
) -> Dict[str, Any]:
    worker_path, isaac_python = _worker_paths(config)
    timeout_sec = float(getattr(config, "isaac_worker_timeout_sec", 120))

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


class IsaacWorkerClient:
    def __init__(self, config: Any) -> None:
        self.config = config
        self.worker_path, self.isaac_python = _worker_paths(config)
        self.timeout_sec = float(getattr(config, "isaac_worker_timeout_sec", 120))
        self.restart_after = int(getattr(config, "isaac_worker_restart_after", 100))
        self._lock = threading.Lock()
        self._process: subprocess.Popen[str] | None = None
        self._stdout_queue: queue.Queue[str] | None = None
        self._reader_thread: threading.Thread | None = None
        self._request_count = 0

    def start(self) -> None:
        if self._process is not None and self._process.poll() is None:
            return

        try:
            process = subprocess.Popen(
                [str(self.isaac_python), str(self.worker_path), "--serve"],
                stdin=subprocess.PIPE, #发送请求
                stdout=subprocess.PIPE, #接收响应
                stderr=subprocess.STDOUT, #错误日志
                text=True,
                bufsize=1,
            )
        except OSError as exc:
            raise IsaacBridgeError(
                f"Isaac persistent worker could not be started: {exc}"
            ) from exc

        if process.stdout is None:
            process.kill()
            raise IsaacBridgeError("Isaac worker persistent stdout is not available")

        self._stdout_queue = queue.Queue()
        self._reader_thread = threading.Thread(
            target=self._drain_stdout,
            args=(process.stdout, self._stdout_queue),
            daemon=True,
        )
        self._reader_thread.start()
        self._process = process
        self._request_count = 0

    def stop(self) -> None:
        process = self._process
        self._process = None
        if process is None:
            return

        try:
            if process.poll() is None and process.stdin is not None:
                process.stdin.write(json.dumps({"operation": "__shutdown__"}) + "\n")
                process.stdin.flush()
                process.wait(timeout=min(self.timeout_sec, 5.0))
        except Exception:
            process.kill()
            process.wait(timeout=5)

    def request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        with self._lock:
            if self.restart_after > 0 and self._request_count >= self.restart_after:
                self.stop()

            return self._request_locked(request, allow_restart=True)

    def _request_locked(
        self,
        request: Dict[str, Any],
        *,
        allow_restart: bool,
    ) -> Dict[str, Any]:
        self.start()
        process = self._process
        if process is None or process.stdin is None or process.stdout is None:
            raise IsaacBridgeError("Isaac worker persistent process is not available")
        if process.poll() is not None:
            if not allow_restart:
                raise IsaacBridgeError("Isaac worker persistent process exited")
            self.stop()
            return self._request_locked(request, allow_restart=False)

        try:
            process.stdin.write(json.dumps(request, ensure_ascii=False) + "\n")
            process.stdin.flush()
            payload = self._read_payload(process)
        except IsaacBridgeError:
            if not allow_restart:
                raise
            self.stop()
            return self._request_locked(request, allow_restart=False)
        except Exception as exc:
            if not allow_restart:
                raise IsaacBridgeError(f"Isaac persistent worker communication failed: {exc}") from exc
            self.stop()
            return self._request_locked(request, allow_restart=False)

        self._request_count += 1
        return payload

    def _read_payload(self, process: subprocess.Popen[str]) -> Dict[str, Any]:
        if self._stdout_queue is None:
            raise IsaacBridgeError("Isaac worker persistent stdout is not available")

        deadline = time.monotonic() + self.timeout_sec
        recent_lines: list[str] = []

        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                detail = "\n".join(recent_lines)[-1000:] or "<no output>"
                raise IsaacBridgeError(
                    f"Isaac persistent worker timed out after {self.timeout_sec}s: {detail}"
                )

            try:
                line = self._stdout_queue.get(timeout=min(remaining, 0.2))
            except queue.Empty:
                if process.poll() is not None:
                    detail = "\n".join(recent_lines)[-1000:] or "<no output>"
                    raise IsaacBridgeError(
                        "Isaac persistent worker exited before returning JSON: "
                        f"{detail}"
                    ) from None
                continue

            if not line:
                if process.poll() is not None:
                    detail = "\n".join(recent_lines)[-1000:] or "<no output>"
                    raise IsaacBridgeError(
                        "Isaac persistent worker exited before returning JSON: "
                        f"{detail}"
                    )
                continue

            last_line = line.strip()
            if last_line:
                recent_lines.append(last_line)
                recent_lines = recent_lines[-20:]

            if not last_line.startswith("{"):
                continue

            try:
                payload = json.loads(last_line)
            except json.JSONDecodeError:
                continue

            if isinstance(payload, dict):
                return payload

            raise IsaacBridgeError(
                f"Isaac persistent worker returned non-object JSON: {payload!r}"
            )

    @staticmethod
    def _drain_stdout(stdout: Any, output_queue: queue.Queue[str]) -> None:
        while True:
            try:
                line = stdout.readline()
            except Exception:
                return
            if not line:
                return
            output_queue.put(line)


def _persistent_client(config: Any) -> IsaacWorkerClient:
    worker_path, isaac_python = _worker_paths(config)
    simulation_config = json.dumps(
        getattr(config, "isaac_simulation", {"headless": True}),
        sort_keys=True,
        default=str,
    )
    key = (str(isaac_python), str(worker_path), simulation_config)
    with _PERSISTENT_CLIENTS_LOCK:
        client = _PERSISTENT_CLIENTS.get(key)
        if client is None:
            client = IsaacWorkerClient(config)
            _PERSISTENT_CLIENTS[key] = client
        return client


def run_isaac_operation(
    *,
    config: Any,
    operation: str,
    scene: Any,
    options: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """Run one Isaac operation in the configured worker process."""
    request = _build_request(
        config=config,
        operation=operation,
        scene=scene,
        options=options,
    )

    if bool(getattr(config, "isaac_worker_persistent", False)):
        return _persistent_client(config).request(request)

    return _run_isaac_operation_once(config=config, request=request)

__all__ = [
    "IsaacBridgeError",
    "run_isaac_operation",
]