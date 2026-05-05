"""simulate_step — 运行一步（近似）物理仿真。

默认走 ``validators.run_static_simulation``。当 ``physics_enabled`` 且
extras 中带 ``isaac_bridge`` 时，转发给 IsaacSim。
"""
from __future__ import annotations

from typing import Any

from ..data_models import Instance
from ..validators import run_static_simulation
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class SimulateStepTool(Tool):
    name = "simulate_step"
    description = "执行一步物理近似（默认 AABB / 静态稳定性；启用 IsaacSim 时改用真实物理）。"
    schema = make_openai_tool_schema(
        name,
        description,
        {"duration": {"type": "number", "description": "仿真时长（秒），默认 1.0"}},
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        duration = float(kwargs.get("duration", 1.0))
        bridge = context.extras.get("isaac_bridge") if context.physics_enabled else None
        if bridge is not None:
            try:
                result = bridge.simulate(context.scene.state, duration=duration)
                return ToolResult(ok=True, data={"backend": "isaac", **result})
            except NotImplementedError:
                pass  # 回退静态
        result = run_static_simulation(context.scene.state)
        return ToolResult(ok=True, data={"backend": "static", "duration": duration, **result})

    def run_test(self, context: ToolContext) -> ToolResult:
        parent_id = "__tool_test_sim_parent"
        child_id = "__tool_test_sim_child"
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
        context.scene.set_support(child_id, parent_id)
        result = self(context, duration=0.1)
        if not result.ok:
            return result
        if result.data.get("stable") is not True:
            return ToolResult(ok=False, error="simulate_step run_test expected stable scene")
        context.scene.delete(child_id)
        context.scene.delete(parent_id)
        return ToolResult(ok=True, data={"tested": self.name})
