"""set_support — 登记 child 由 parent 支撑。

按 ``方案/优化.md`` 优化方向 4：当前实现「LLM 决定 + 规则验证」中的「写入」步。
LLM 调用本工具登记关系，工具内部用几何检查给出 ``geometry_ok`` 标志，但
*不* 自动回滚——是否回滚由 ReAct 主循环根据观测结果决定。
"""
from __future__ import annotations

from typing import Any

from ..data_models import Instance
from ..validators import check_support_geometry
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class SetSupportTool(Tool):
    name = "set_support"
    description = "登记 child 实例由 parent 实例支撑（仅维护逻辑关系，会同时给出几何检查结果）。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "child_id": {"type": "string", "description": "child 实例 id"},
            "parent_id": {"type": "string", "description": "parent 实例 id"},
        },
        required=["child_id", "parent_id"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        child_id = str(kwargs["child_id"])
        parent_id = str(kwargs["parent_id"])
        child = context.scene.get(child_id)
        parent = context.scene.get(parent_id)
        context.scene.set_support(child_id, parent_id)
        geo = check_support_geometry(child, parent)
        return ToolResult(ok=True, data={
            "child": child_id,
            "parent": parent_id,
            "geometry_ok": geo["ok"],
            "geometry": geo,
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        parent_id = "__tool_test_support_parent"
        child_id = "__tool_test_support_child"
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
        if context.scene.get(child_id).parent_instance_id != parent_id:
            return ToolResult(ok=False, error="set_support run_test did not register parent")
        context.scene.delete(child_id)
        context.scene.delete(parent_id)
        return ToolResult(ok=True, data={"tested": self.name})
