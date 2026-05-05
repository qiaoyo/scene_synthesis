"""IsaacSim 接入抽象（占位）。

按 ``方案/优化.md`` 的「优化方向 5：引入仿真」要求，``check_collision``、
``check_support``、``simulate_step`` 都应当能够替换为 IsaacSim 的真实物理。
但本阶段（``AgentConfig.physics_enabled = False``）默认不接入。

接入步骤（备忘）：
1. 实现 ``IsaacBridge`` 子类，覆盖 ``simulate``、``query_contacts``。
2. 在 ``Observer.__init__`` 中传入实例，替换默认的 ``run_static_simulation``。
3. 工具 ``check_collision`` / ``check_support`` 可以选择优先调用 bridge。
"""
from __future__ import annotations

from typing import Any, Dict

from ..data_models import SceneState


class IsaacBridge:
    """IsaacSim 接口契约。当前默认实现直接抛 NotImplementedError。"""

    def simulate(self, state: SceneState, duration: float) -> Dict[str, Any]:
        raise NotImplementedError("IsaacBridge.simulate 尚未实现，请安装 isaacsim 后接入。")

    def query_contacts(self, state: SceneState) -> Dict[str, Any]:
        raise NotImplementedError("IsaacBridge.query_contacts 尚未实现。")


__all__ = ["IsaacBridge"]
