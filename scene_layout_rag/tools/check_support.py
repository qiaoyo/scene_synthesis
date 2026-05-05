"""check_support — 几何上验证某条支撑关系是否成立（不修改场景）。"""
from __future__ import annotations

from typing import Any

from ..data_models import Instance
from ..validators import check_support_geometry, evaluate_support_state
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class CheckSupportTool(Tool):
    name = "check_support"
    description = "检查支撑关系：可指定 child/parent 单独验证；不传则评估当前所有 set_support 关系。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "child_id": {"type": "string", "description": "child 实例 id"},
            "parent_id": {"type": "string", "description": "parent 实例 id（与 child_id 同时给出）"},
        },
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        child_id = kwargs.get("child_id")
        parent_id = kwargs.get("parent_id")
        if child_id and parent_id:
            child = context.scene.get(child_id)
            parent = context.scene.get(parent_id)
            geo = check_support_geometry(child, parent)
            return ToolResult(ok=True, data={
                "child": child_id,
                "parent": parent_id,
                **geo,
            })
        if child_id or parent_id:
            return ToolResult(ok=False, error="child_id 与 parent_id 必须同时给出，或都不给。")
        return ToolResult(ok=True, data=evaluate_support_state(context.scene.state))

    def run_test(self, context: ToolContext) -> ToolResult:
        parent_id = "__tool_test_check_support_parent"
        child_id = "__tool_test_check_support_child"
        for instance_id in (child_id, parent_id):
            if instance_id in context.scene.state.instances:
                context.scene.delete(instance_id)
        context.scene.add_instance(Instance(
            instance_id=parent_id,
            asset_type="Workbench",
            asset_doc_id="workbench-doc",
            usd_path="/assets/workbench.usdz",
            position=[0.0, 0.0, 0.5],
            bbox_size=[2.0, 2.0, 1.0],
        ))
        context.scene.add_instance(Instance(
            instance_id=child_id,
            asset_type="Box",
            asset_doc_id="box-doc",
            usd_path="/assets/box.usdz",
            position=[0.0, 0.0, 1.5],
            bbox_size=[1.0, 1.0, 1.0],
        ))
        result = self(context, child_id=child_id, parent_id=parent_id)
        if not result.ok:
            return result
        if result.data.get("ok") is not True:
            return ToolResult(ok=False, error="check_support run_test expected valid support")
        context.scene.delete(child_id)
        context.scene.delete(parent_id)
        return ToolResult(ok=True, data={"tested": self.name})
