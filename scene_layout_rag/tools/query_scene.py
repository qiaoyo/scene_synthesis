"""query_scene — 查询当前场景状态。

按 ``方案/优化.md`` 重新定义为：行动前的「就绪检查」工具，返回 LLM 决策需要的
精确数据，包括实例列表、bbox、支撑关系、空闲空间统计等。
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..data_models import Instance
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class QuerySceneTool(Tool):
    name = "query_scene"
    description = "返回当前场景的精确状态，供 LLM 在决策前读取（实例尺寸、位置、支撑关系等）。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "instance_id": {"type": "string", "description": "若指定，只返回这一个实例的详情"},
            "asset_type": {"type": "string", "description": "若指定，只返回该类别的实例"},
        },
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        instances: List[Dict[str, Any]] = []
        target_id: Optional[str] = kwargs.get("instance_id")
        asset_type: Optional[str] = kwargs.get("asset_type")
        for inst in context.scene.state.instances.values():
            if target_id and inst.instance_id != target_id:
                continue
            if asset_type and inst.asset_type != asset_type:
                continue
            bbox_min, bbox_max = inst.aabb()
            instances.append({
                "instance_id": inst.instance_id,
                "asset_type": inst.asset_type,
                "asset_doc_id": inst.asset_doc_id,
                "position": inst.position,
                "rotation_deg": inst.rotation_deg,
                "bbox_size": inst.bbox_size,
                "bbox_min": bbox_min,
                "bbox_max": bbox_max,
                "parent_instance_id": inst.parent_instance_id,
            })
        if target_id and not instances:
            return ToolResult(ok=False, error=f"未找到实例: {target_id}")
        return ToolResult(ok=True, data={
            "instances": instances,
            "support_children": dict(context.scene.state.support_children),
            "instance_count": len(context.scene.state.instances),
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        instance_id = "__tool_test_query_scene"
        if instance_id not in context.scene.state.instances:
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
        if not result.data.get("instances"):
            return ToolResult(ok=False, error="query_scene run_test returned no instance")
        context.scene.delete(instance_id)
        return ToolResult(ok=True, data={"tested": self.name})
