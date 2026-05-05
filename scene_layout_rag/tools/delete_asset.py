"""delete_asset — 从场景里删除一个实例。"""
from __future__ import annotations

from typing import Any

from ..data_models import Instance
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class DeleteAssetTool(Tool):
    name = "delete_asset"
    description = "删除场景中已存在的实例；该实例支撑的子项会被解绑（不连带删除）。"
    schema = make_openai_tool_schema(
        name,
        description,
        {"instance_id": {"type": "string", "description": "目标实例 id"}},
        required=["instance_id"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        iid = str(kwargs["instance_id"])
        # 先记录被解绑的 children
        unparented = list(context.scene.state.support_children.get(iid, []))
        context.scene.delete(iid)
        return ToolResult(ok=True, data={
            "instance_id": iid,
            "unparented_children": unparented,
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        instance_id = "__tool_test_delete_asset"
        if instance_id in context.scene.state.instances:
            context.scene.delete(instance_id)
        context.scene.add_instance(Instance(
            instance_id=instance_id,
            asset_type="Box",
            asset_doc_id="box-doc",
            usd_path="/assets/box.usdz",
            position=[0.0, 0.0, 0.5],
            bbox_size=[1.0, 1.0, 1.0],
        ))
        result = self(context, instance_id=instance_id)
        if not result.ok:
            return result
        if instance_id in context.scene.state.instances:
            return ToolResult(ok=False, error="delete_asset run_test did not remove instance")
        return ToolResult(ok=True, data={"tested": self.name})
