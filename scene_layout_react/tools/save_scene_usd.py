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


def export_scene_to_usd_with_worker(
    scene: Any,
    output_path: str | Path,
    config: Any,
    include_physics: bool = False,
) -> Dict[str, Any]:
    output_path = Path(output_path).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = run_isaac_operation(
        config=config,
        operation="save_scene_usd",
        scene=scene.to_dict(),
        options={
            "output_path": str(output_path),
            "include_physics": include_physics,
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
                    "include_physics": {
                        "type": "boolean",
                        "description": "If true, author rigid body and collision APIs before exporting.",
                    },
                },
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        include_physics: bool = False,
    ) -> ToolResult:
        output_path = _default_output_path(context)

        data = export_scene_to_usd_with_worker(
            context.scene.state,
            output_path,
            context.config,
            include_physics=include_physics,
        )
        return ToolResult(ok=True, data=data)
