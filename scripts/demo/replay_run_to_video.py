from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_RUN_DIR = Path("/home/simple/joey/scene_synthesis/outputs/runs/20260525_063013_aaf35f06")


def _safe_name(value: str) -> str:
    chars = [ch if (ch.isalnum() or ch in {"-", "_"}) else "_" for ch in value.strip()]
    safe = "".join(chars).strip("_")
    return safe or "instance"


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _lerp(a: List[float], b: List[float], t: float) -> List[float]:
    return [float(a[i]) + (float(b[i]) - float(a[i])) * t for i in range(3)]


def _smoothstep(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def _clone_state(state: Dict[str, List[float]]) -> Dict[str, List[float]]:
    return {key: [float(v) for v in value] for key, value in state.items()}


def _scene_instances_from_step(step: Dict[str, Any]) -> Dict[str, Any]:
    observation = step.get("observation") or {}
    current_state = observation.get("current_state") or {}
    instances = current_state.get("instances") or {}
    return instances if isinstance(instances, dict) else {}


def _find_final_instances(record: Dict[str, Any]) -> Dict[str, Any]:
    for step in reversed(record.get("steps", [])):
        instances = _scene_instances_from_step(step)
        if instances:
            return instances
    return {}


def _find_prim_paths(record: Dict[str, Any], run_dir: Path) -> Dict[str, str]:
    for step in reversed(record.get("steps", [])):
        for tool in step.get("tools", []):
            if tool.get("name") != "save_scene_usd":
                continue
            result = tool.get("result") or {}
            data = result.get("data") or {}
            prim_paths = data.get("prim_paths") or {}
            if isinstance(prim_paths, dict) and prim_paths:
                return {str(k): str(v) for k, v in prim_paths.items()}

    final_instances = _find_final_instances(record)
    return {
        instance_id: f"/World/Instances/{_safe_name(instance_id)}"
        for instance_id in final_instances.keys()
    }


def _find_stage_path(record: Dict[str, Any], run_dir: Path) -> Path:
    saved_scene = run_dir / "saved_scene.usd"
    if saved_scene.exists():
        return saved_scene

    for step in reversed(record.get("steps", [])):
        for tool in step.get("tools", []):
            if tool.get("name") != "save_scene_usd":
                continue
            result = tool.get("result") or {}
            data = result.get("data") or {}
            stage_path = data.get("stage_path") or data.get("usd_path")
            if stage_path:
                candidate = Path(str(stage_path))
                if candidate.exists():
                    return candidate

    raise FileNotFoundError("could not find saved_scene.usd or save_scene_usd stage_path")


@dataclass
class ReplayAction:
    kind: str
    step: int
    instance_id: str
    start: List[float]
    end: List[float]
    bbox_size: List[float]


def _collect_actions(record: Dict[str, Any], final_instances: Dict[str, Any]) -> List[ReplayAction]:
    actions: List[ReplayAction] = []
    for step in record.get("steps", []):
        step_index = int(step.get("step", 0))
        for tool in step.get("tools", []):
            name = tool.get("name")
            result = tool.get("result") or {}
            data = result.get("data") or {}
            arguments = tool.get("arguments") or {}

            if name == "place_instance":
                instance_id = str(data.get("instance_id") or data.get("base_instance_id") or "")
                position = data.get("position") or []
                bbox_size = data.get("bbox_size") or [1.0, 1.0, 1.0]
                if instance_id and len(position) == 3:
                    actions.append(
                        ReplayAction(
                            kind="place_instance",
                            step=step_index,
                            instance_id=instance_id,
                            start=[float(position[0]), float(position[1]), float(position[2])],
                            end=[float(position[0]), float(position[1]), float(position[2])],
                            bbox_size=[float(v) for v in bbox_size[:3]],
                        )
                    )
                continue

            if name == "move_asset":
                instance_id = str(arguments.get("instance_id") or data.get("instance_id") or "")
                start = data.get("old_position") or arguments.get("old_position") or []
                end = data.get("new_position") or arguments.get("new_position") or []
                bbox_size = final_instances.get(instance_id, {}).get("bbox_size") or [1.0, 1.0, 1.0]
                if instance_id and len(start) == 3 and len(end) == 3:
                    actions.append(
                        ReplayAction(
                            kind="move_asset",
                            step=step_index,
                            instance_id=instance_id,
                            start=[float(start[0]), float(start[1]), float(start[2])],
                            end=[float(end[0]), float(end[1]), float(end[2])],
                            bbox_size=[float(v) for v in bbox_size[:3]],
                        )
                    )
                continue

    return actions


def _build_frame_states(
    actions: List[ReplayAction],
    final_instances: Dict[str, Any],
    *,
    action_frames: int,
    hold_frames: int,
    initial_hold_frames: int,
    final_hold_frames: int,
    hidden_distance: float,
    spawn_height_scale: float,
    spawn_height_min: float,
) -> List[Dict[str, List[float]]]:
    instance_ids = sorted(final_instances.keys())
    state: Dict[str, List[float]] = {}
    for index, instance_id in enumerate(instance_ids):
        state[instance_id] = [
            hidden_distance + index * 8.0,
            hidden_distance + index * 4.0,
            hidden_distance + index * 2.0,
        ]

    frames: List[Dict[str, List[float]]] = []

    def add_hold(count: int) -> None:
        for _ in range(max(0, count)):
            frames.append(_clone_state(state))

    def add_transition(instance_id: str, start: List[float], end: List[float]) -> None:
        steps = max(2, action_frames)
        for idx in range(steps):
            t = 0.0 if steps == 1 else idx / float(steps - 1)
            state[instance_id] = _lerp(start, end, _smoothstep(t))
            frames.append(_clone_state(state))

    add_hold(initial_hold_frames)

    for action in actions:
        instance_id = action.instance_id
        bbox_size = action.bbox_size or [1.0, 1.0, 1.0]

        if action.kind == "place_instance":
            target = [float(v) for v in action.end]
            spawn_height = max(spawn_height_min, float(bbox_size[2]) * spawn_height_scale)
            spawn = [target[0], target[1], target[2] + spawn_height]
            state[instance_id] = spawn
            add_transition(instance_id, spawn, target)
            state[instance_id] = target
            add_hold(hold_frames)
            continue

        if action.kind == "move_asset":
            start = [float(v) for v in action.start]
            end = [float(v) for v in action.end]
            state[instance_id] = start
            add_transition(instance_id, start, end)
            state[instance_id] = end
            add_hold(hold_frames)
            continue

    add_hold(final_hold_frames)
    return frames


def _summarize(record: Dict[str, Any], run_dir: Path) -> Dict[str, Any]:
    final_instances = _find_final_instances(record)
    actions = _collect_actions(record, final_instances)
    prim_paths = _find_prim_paths(record, run_dir)
    stage_path = _find_stage_path(record, run_dir)

    place_steps: Dict[int, List[str]] = {}
    move_steps: Dict[int, List[str]] = {}
    for action in actions:
        if action.kind == "place_instance":
            place_steps.setdefault(action.step, []).append(action.instance_id)
        elif action.kind == "move_asset":
            move_steps.setdefault(action.step, []).append(action.instance_id)

    first_appearance: Dict[str, int] = {}
    for action in actions:
        if action.kind == "place_instance" and action.instance_id not in first_appearance:
            first_appearance[action.instance_id] = action.step

    return {
        "record_path": run_dir / "record.json",
        "events_path": run_dir / "events.jsonl",
        "tools_path": run_dir / "tools.json",
        "snapshots": sorted((run_dir / "snapshots").glob("step_*_scene.json")),
        "stage_path": stage_path,
        "actions": actions,
        "place_steps": place_steps,
        "move_steps": move_steps,
        "first_appearance": first_appearance,
        "prim_paths": prim_paths,
        "final_instances": final_instances,
    }


def _scene_center_and_radius(final_instances: Dict[str, Any]) -> tuple[List[float], float]:
    if not final_instances:
        return [0.0, 0.0, 0.0], 4.0

    mins = [float("inf"), float("inf"), float("inf")]
    maxs = [float("-inf"), float("-inf"), float("-inf")]
    for inst in final_instances.values():
        position = [float(v) for v in (inst.get("position") or [0.0, 0.0, 0.0])[:3]]
        size = [float(v) for v in (inst.get("bbox_size") or [1.0, 1.0, 1.0])[:3]]
        for axis in range(3):
            half = size[axis] / 2.0
            mins[axis] = min(mins[axis], position[axis] - half)
            maxs[axis] = max(maxs[axis], position[axis] + half)

    center = [(mins[axis] + maxs[axis]) / 2.0 for axis in range(3)]
    radius = max(maxs[axis] - mins[axis] for axis in range(3))
    return center, max(radius, 2.0)


def _print_summary(summary: Dict[str, Any]) -> None:
    actions: List[ReplayAction] = summary["actions"]
    final_instances: Dict[str, Any] = summary["final_instances"]
    place_count = sum(1 for action in actions if action.kind == "place_instance")
    move_count = sum(1 for action in actions if action.kind == "move_asset")

    print(f"record: {summary['record_path']}")
    print(f"stage: {summary['stage_path']}")
    print(f"snapshots: {len(summary['snapshots'])}")
    print(f"final_instances: {len(final_instances)}")
    print(f"place_actions: {place_count}")
    print(f"move_actions: {move_count}")
    print("best_log: record.json")
    print(
        "why: it already carries step order, tool inputs/outputs, "
        "scene snapshots, and the final saved USD path."
    )
    print("first_appearance:")
    for instance_id, step in sorted(summary["first_appearance"].items(), key=lambda item: item[1]):
        print(f"  step {step}: {instance_id}")


def _log(message: str) -> None:
    print(f"[replay_video] {message}", flush=True)


def _ensure_extension(app: Any, name: str) -> None:
    ext_manager = app.get_extension_manager()
    ext_manager.set_extension_enabled_immediate(name, True)


def _stage_pending_loads(ctx: Any) -> int:
    try:
        status = ctx.get_stage_loading_status()
    except Exception:
        return 0
    if not isinstance(status, (list, tuple)) or len(status) < 3:
        return 0
    try:
        return int(status[2])
    except Exception:
        return 0


def _set_prim_position(stage: Any, prim_path: str, position: List[float]) -> None:
    from pxr import Gf, UsdGeom

    prim = stage.GetPrimAtPath(prim_path)
    if not prim or not prim.IsValid():
        return

    xformable = UsdGeom.Xformable(prim)
    translate_op = None
    for op in xformable.GetOrderedXformOps():
        try:
            if op.GetOpType() == UsdGeom.XformOp.TypeTranslate:
                translate_op = op
                break
        except Exception:
            continue

    if translate_op is None:
        translate_op = xformable.AddTranslateOp(precision=UsdGeom.XformOp.PrecisionDouble)

    translate_op.Set(Gf.Vec3d(float(position[0]), float(position[1]), float(position[2])))


class ReplayTimeline:
    def __init__(self, stage: Any, prim_paths: Dict[str, str], frames: List[Dict[str, List[float]]]):
        self._stage = stage
        self._prim_paths = prim_paths
        self._frames = frames
        self._index = 0

    def prime(self) -> None:
        if not self._frames:
            return
        self.apply(self._frames[0])

    def apply(self, frame: Dict[str, List[float]]) -> None:
        for instance_id, position in frame.items():
            prim_path = self._prim_paths.get(instance_id)
            if prim_path:
                _set_prim_position(self._stage, prim_path, position)

    def forward_one_frame(self, dt: float) -> bool:
        next_index = self._index + 1
        if next_index >= len(self._frames):
            return False
        self._index = next_index
        self.apply(self._frames[self._index])
        return True


def _run_render(summary: Dict[str, Any], args: argparse.Namespace) -> List[str]:
    _log("starting Isaac SimulationApp")
    if "isaac_env" not in sys.executable:
        _log(f"warning: current Python does not look like isaac_env: {sys.executable}")

    from isaacsim import SimulationApp

    app = SimulationApp({"headless": bool(args.headless)})
    outputs: List[str] = []
    try:
        import omni.kit.app
        import omni.kit.viewport.utility as viewport_utility
        import omni.usd
        from omni.kit.viewport.utility.camera_state import ViewportCameraState
        from pxr import Gf

        _log("enabling viewport capture extensions")
        for ext in [
            "omni.kit.capture.viewport",
            "omni.kit.window.movie_capture",
            "omni.videoencoding",
            "omni.kit.viewport.utility",
        ]:
            try:
                _ensure_extension(omni.kit.app.get_app(), ext)
                _log(f"enabled extension: {ext}")
            except Exception as exc:
                _log(f"warning: could not enable extension {ext}: {exc}")

        for _ in range(8):
            app.update()

        from omni.kit.capture.viewport import (
            CaptureExtension,
            CaptureMovieType,
            CaptureOptions,
            CaptureRangeType,
            CaptureRenderPreset,
        )

        ctx = omni.usd.get_context()
        _log(f"opening stage: {summary['stage_path']}")
        ctx.open_stage(str(summary["stage_path"]))
        for _ in range(10):
            app.update()
        for _ in range(600):
            if _stage_pending_loads(ctx) <= 0:
                break
            app.update()

        stage = ctx.get_stage()
        if stage is None:
            raise RuntimeError(f"failed to open stage: {summary['stage_path']}")
        _log("stage opened")

        viewport = viewport_utility.get_active_viewport()
        if viewport is None:
            raise RuntimeError("no active viewport available")

        prim_paths = summary["prim_paths"]
        center, radius = _scene_center_and_radius(summary["final_instances"])
        distance = radius * 2.4
        camera_state = ViewportCameraState(viewport=viewport)
        camera_state.set_position_world(
            Gf.Vec3d(center[0] + distance, center[1] - distance, center[2] + distance * 0.75),
            True,
        )
        camera_state.set_target_world(Gf.Vec3d(center[0], center[1], center[2]), True)
        for _ in range(5):
            app.update()
        _log("camera framed")

        final_instances = summary["final_instances"]
        actions = summary["actions"]
        frames = _build_frame_states(
            actions,
            final_instances,
            action_frames=int(args.action_frames),
            hold_frames=int(args.hold_frames),
            initial_hold_frames=int(args.initial_hold_frames),
            final_hold_frames=int(args.final_hold_frames),
            hidden_distance=float(args.hidden_distance),
            spawn_height_scale=float(args.spawn_height_scale),
            spawn_height_min=float(args.spawn_height_min),
        )
        if not frames:
            raise RuntimeError("no animation frames were generated")
        _log(f"generated {len(frames)} replay frames")

        replay = ReplayTimeline(stage, prim_paths, frames)
        replay.prime()
        for _ in range(2):
            app.update()

        output_path = Path(args.output).expanduser()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        capture = CaptureExtension.get_instance()
        if capture is None:
            raise RuntimeError("capture extension is unavailable")

        _log(f"configuring capture: {output_path}")
        options = CaptureOptions()
        options.camera = viewport.camera_path.pathString
        options.output_folder = str(output_path.parent)
        options.file_name = output_path.stem
        options.file_type = ".mp4"
        options.movie_type = CaptureMovieType.SEQUENCE
        options.range_type = CaptureRangeType.FRAMES
        options.start_frame = 1
        options.end_frame = len(frames)
        options.capture_every_nth_frames = 1
        options.fps = int(args.fps)
        options.overwrite_existing_frames = True
        options.render_preset = getattr(CaptureRenderPreset, args.render_preset)
        options.res_width = int(args.width)
        options.res_height = int(args.height)
        options.path_trace_spp = int(args.spp)
        options.spp_per_iteration = int(args.spp)
        options.animation_fps = int(args.fps)
        options.mp4_encoding_bitrate = int(args.bitrate)
        capture.options = options
        capture.forward_one_frame_fn = replay.forward_one_frame

        _log("starting viewport capture")
        if not capture.start():
            raise RuntimeError("capture could not be started")

        update_count = 0
        while not capture.done:
            app.update()
            update_count += 1
            if update_count % 120 == 0:
                _log("capture still running")

        outputs = capture.get_outputs()
        _log(f"capture finished with {len(outputs)} output(s)")
        return outputs
    finally:
        _log("closing Isaac SimulationApp")
        try:
            app.close()
        except Exception:
            pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replay one run directory into an Isaac Sim video.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "run_dir",
        type=Path,
        nargs="?",
        default=DEFAULT_RUN_DIR,
        help="Run directory containing record.json and snapshots/",
    )
    parser.add_argument("--output", type=Path, default=None, help="Output mp4 path")
    parser.add_argument("--render", action="store_true", help="Render the replay with Isaac Sim")
    parser.add_argument("--headless", action="store_true", help="Start Isaac Sim headless")
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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    record_path = run_dir / "record.json"
    if not record_path.exists():
        raise FileNotFoundError(f"record.json not found: {record_path}")

    record = _load_json(record_path)
    summary = _summarize(record, run_dir)

    if args.output is None:
        args.output = run_dir / f"{run_dir.name}_replay.mp4"

    _print_summary(summary)
    if not args.render:
        print(f"dry_run_output: {args.output}")
        return 0

    outputs = _run_render(summary, args)
    print("render_outputs:")
    for path in outputs:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
