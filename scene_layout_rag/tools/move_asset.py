"""move_asset — 平移已有实例。"""
from __future__ import annotations

from typing import Any, List

from ..data_models import Instance
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class MoveAssetTool(Tool):
    name = "move_asset"
    description = "把场景中已存在的实例平移到 new_position。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "instance_id": {"type": "string", "description": "目标实例 id"},
            "new_position": {
                "type": "array",
                "items": {"type": "number"},
                "minItems": 3,
                "maxItems": 3,
                "description": "[x, y, z]，米",
            },
        },
        required=["instance_id", "new_position"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        iid = str(kwargs["instance_id"])
        new_pos = kwargs["new_position"]
        if not isinstance(new_pos, (list, tuple)) or len(new_pos) != 3:
            return ToolResult(ok=False, error="new_position 必须是长度为 3 的列表")
        new_pos = [float(v) for v in new_pos]
        old = list(context.scene.get(iid).position)
        context.scene.move(iid, new_pos)
        return ToolResult(ok=True, data={
            "instance_id": iid,
            "old_position": old,
            "new_position": new_pos,
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        instance_id = "__tool_test_move_asset"
        if instance_id not in context.scene.state.instances:
            context.scene.add_instance(Instance(
                instance_id=instance_id,
                asset_type="Box",
                asset_doc_id="box-doc",
                usd_path="/assets/box.usdz",
                position=[0.0, 0.0, 0.5],
                bbox_size=[1.0, 1.0, 1.0],
            ))
        result = self(context, instance_id=instance_id, new_position=[1.0, 2.0, 0.5])
        if not result.ok:
            return result
        moved = context.scene.get(instance_id)
        if moved.position != [1.0, 2.0, 0.5]:
            return ToolResult(ok=False, error="move_asset run_test did not update position")
        context.scene.delete(instance_id)
        return ToolResult(ok=True, data={"tested": self.name})
