from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from ..physics.isaac_bridge import run_isaac_operation
from .base import Tool, ToolContext, ToolResult, register_tool


def _default_output_path(context: ToolContext) -> Path:
    run_dir = context.extras.get("run_dir") if isinstance(context.extras, dict) else None
    if run_dir:
        return Path(run_dir).expanduser() / "saved_scene.usd"

    config_output_dir = getattr(context.config, "output_dir", None)
    if config_output_dir:
        return Path(config_output_dir).expanduser() / "save_usd" / "saved_scene.usd"

    return Path("/home/simple/joey/scene_synthesis/outputs/save_usd/saved_scene.usd")


def _scene_to_dict(scene: Any) -> Dict[str, Any]:
    if hasattr(scene, "to_dict"):
        return scene.to_dict()
    if isinstance(scene, dict):
        return scene
    raise TypeError(f"unsupported scene type: {type(scene)!r}")


def export_scene_to_usd_with_worker(
    scene: Any,
    output_path: str | Path,
    config: Any,
    keep_temp_stage: bool = False,
) -> Dict[str, Any]:
    output_path = Path(output_path).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = run_isaac_operation(
        config=config,
        operation="save_scene_usd",
        scene=_scene_to_dict(scene),
        options={
            "output_path": str(output_path),
            "temp_dir": str(output_path.parent),
            "keep_temp_stage": keep_temp_stage,
        },
    )
    if not payload.get("ok", False):
        error = payload.get("error") or "; ".join(payload.get("errors", []))
        raise RuntimeError(error or "Isaac save_scene_usd operation failed")
    return payload


@register_tool
class SaveSceneUsdTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "save_scene_usd",
            "description": "Export the current scene state to a persistent USD file using the worker stage builder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keep_temp_stage": {
                        "type": "boolean",
                        "description": "Keep the intermediate worker-generated USD file for debugging.",
                    },
                },
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        keep_temp_stage: bool = False,
    ) -> ToolResult:
        output_path = _default_output_path(context)

        data = export_scene_to_usd_with_worker(
            context.scene.state,
            output_path,
            context.config,
            keep_temp_stage=keep_temp_stage,
        )
        return ToolResult(ok=True, data=data)
