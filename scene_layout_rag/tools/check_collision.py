"""check_collision — 主动检测碰撞。

默认走 AABB；将来接 IsaacSim 时只需让 ``ToolContext.physics_enabled=True`` 并
通过 ``context.extras['isaac_bridge']`` 注入 ``IsaacBridge`` 实例。
"""
from __future__ import annotations

from typing import Any, Dict, List

from ..data_models import Instance
from ..validators import aabb_collisions, aabb_overlap
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class CheckCollisionTool(Tool):
    name = "check_collision"
    description = "检测当前场景的所有 AABB 碰撞；可选地只检查某一对实例。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "instance_id_a": {"type": "string", "description": "若与 instance_id_b 同时给出，只比较这两个"},
            "instance_id_b": {"type": "string", "description": "见上"},
        },
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        a_id = kwargs.get("instance_id_a")
        b_id = kwargs.get("instance_id_b")
        bridge = context.extras.get("isaac_bridge") if context.physics_enabled else None
        if bridge is not None:
            # 留出真实物理通道
            try:
                contacts = bridge.query_contacts(context.scene.state)
                return ToolResult(ok=True, data={"backend": "isaac", **contacts})
            except NotImplementedError:
                pass  # 退回 AABB

        if a_id and b_id:
            a = context.scene.get(a_id)
            b = context.scene.get(b_id)
            a_min, a_max = a.aabb()
            b_min, b_max = b.aabb()
            collision = aabb_overlap(a_min, a_max, b_min, b_max)
            return ToolResult(ok=True, data={
                "backend": "aabb",
                "pair": [a_id, b_id],
                "collision": bool(collision),
            })

        collisions: List[Dict[str, Any]] = aabb_collisions(context.scene.state)
        return ToolResult(ok=True, data={
            "backend": "aabb",
            "collisions": collisions,
            "ok": len(collisions) == 0,
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        a_id = "__tool_test_collision_a"
        b_id = "__tool_test_collision_b"
        for instance_id in (a_id, b_id):
            if instance_id in context.scene.state.instances:
                context.scene.delete(instance_id)
        context.scene.add_instance(Instance(
            instance_id=a_id,
            asset_type="Box",
            asset_doc_id="box-doc",
            usd_path="/assets/box.usdz",
            position=[0.0, 0.0, 0.5],
            bbox_size=[1.0, 1.0, 1.0],
        ))
        context.scene.add_instance(Instance(
            instance_id=b_id,
            asset_type="Box",
            asset_doc_id="box-doc",
            usd_path="/assets/box.usdz",
            position=[0.0, 0.0, 0.5],
            bbox_size=[1.0, 1.0, 1.0],
        ))
        result = self(context, instance_id_a=a_id, instance_id_b=b_id)
        if not result.ok:
            return result
        if result.data.get("collision") is not True:
            return ToolResult(ok=False, error="check_collision run_test expected collision")
        context.scene.delete(a_id)
        context.scene.delete(b_id)
        return ToolResult(ok=True, data={"tested": self.name})
