"""Physics integration boundary.

当前默认走 ``validators.run_static_simulation`` 做 AABB / 几何近似。后续接入
IsaacSim 时只需实现 ``isaac_bridge.IsaacBridge`` 并在 ``Observer`` 里替换
``physics_callable``，其它代码不需要改。
"""
from .isaac_bridge import IsaacBridge  # noqa: F401
