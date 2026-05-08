#!/usr/bin/env python
from pathlib import Path
from typing import Dict, Optional, Tuple

# 1. 启动 Isaac Sim (必须在导入 pxr 之前)
from isaacsim.simulation_app import SimulationApp
simulation_app = SimulationApp({"headless": True})

from pxr import Usd, UsdGeom, Gf


_UNIT_NAME_BY_METERS_PER_UNIT = {
    1.0: "m",
    0.1: "dm",
    0.01: "cm",
    0.001: "mm",
    0.0254: "in",
    0.3048: "ft",
}


def _range_to_bbox(range3d: Gf.Range3d) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """内部辅助函数：将 Gf.Range3d 转换为 Python 元组"""
    mn = range3d.GetMin()
    mx = range3d.GetMax()
    return (float(mn[0]), float(mn[1]), float(mn[2])), (
        float(mx[0]), float(mx[1]), float(mx[2])
    )


def _infer_unit_name(meters_per_unit: float, tolerance: float = 1e-9) -> str:
    """将 metersPerUnit 转成人类可读的单位名。"""
    for candidate, unit_name in _UNIT_NAME_BY_METERS_PER_UNIT.items():
        if abs(meters_per_unit - candidate) <= tolerance:
            return unit_name
    return f"unknown({meters_per_unit} m/unit)"


def _scale_bbox(
    bbox: Tuple[Tuple[float, float, float], Tuple[float, float, float]],
    scale: float,
) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """按比例缩放 bbox。"""
    bbox_min, bbox_max = bbox
    scaled_min = tuple(float(value * scale) for value in bbox_min)
    scaled_max = tuple(float(value * scale) for value in bbox_max)
    return scaled_min, scaled_max


def _get_stage_unit_info(stage: Usd.Stage) -> Dict[str, Optional[object]]:
    """
    读取 stage 的长度单位信息。

    metersPerUnit 表示“1 个 stage 单位 = 多少米”。
    例如:
    - 1.0   -> 米
    - 0.01  -> 厘米
    - 0.001 -> 毫米
    """
    meters_per_unit = float(UsdGeom.GetStageMetersPerUnit(stage))

    authored = None
    if hasattr(UsdGeom, "StageHasAuthoredMetersPerUnit"):
        authored = bool(UsdGeom.StageHasAuthoredMetersPerUnit(stage))

    return {
        "meters_per_unit": meters_per_unit,
        "unit_name": _infer_unit_name(meters_per_unit),
        "authored_meters_per_unit": authored,
    }


def get_single_object_bbox(usd_file_path: str) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """
    读取单个 USD 文件并输出其包围盒 (BBox)。
    
    Args:
        usd_file_path: USD 文件的绝对路径或相对路径字符串。
        
    Returns:
        一个包含两个元组的元组: ((min_x, min_y, min_z), (max_x, max_y, max_z))
        
    Raises:
        RuntimeError: 各种读取失败的情况。
    """
    usd_path = Path(usd_file_path)
    
    if not usd_path.exists():
        raise FileNotFoundError(f"文件不存在: {usd_path}")

    # 打开 USD Stage
    stage = Usd.Stage.Open(str(usd_path))
    if not stage:
        raise RuntimeError(f"无法打开 USD Stage: {usd_path}")

    # 初始化包围盒缓存
    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_],
        useExtentsHint=True,
    )

    # 获取默认 Prim (通常是根节点)
    default_prim = stage.GetDefaultPrim()
    if not default_prim or not default_prim.IsValid():
        # 尝试获取 Root Layer 的第一个 Prim (备选方案)
        root_prims = stage.GetPseudoRoot().GetChildren()
        if not root_prims:
             raise RuntimeError(f"USD Stage 中没有找到有效的 Prim: {usd_path}")
        default_prim = root_prims[0]

    # 计算世界坐标下的包围盒
    rng = bbox_cache.ComputeWorldBound(default_prim).ComputeAlignedRange()
    
    if rng.IsEmpty():
        raise RuntimeError(f"计算出的包围盒为空: {default_prim.GetPath()}")

    return _range_to_bbox(rng)


def get_single_object_bbox_with_unit(usd_file_path: str) -> Dict[str, object]:
    """
    读取单个 USD 的 bbox，并同时返回单位信息。

    Returns:
        {
            "bbox_min": 原始 stage 单位下的最小点,
            "bbox_max": 原始 stage 单位下的最大点,
            "bbox_min_meters": 换算到米后的最小点,
            "bbox_max_meters": 换算到米后的最大点,
            "meters_per_unit": stage 的 metersPerUnit,
            "unit_name": 识别出的单位名,
            "authored_meters_per_unit": 是否显式写过单位元数据(若 API 不支持则为 None),
        }
    """
    usd_path = Path(usd_file_path)

    if not usd_path.exists():
        raise FileNotFoundError(f"文件不存在: {usd_path}")

    stage = Usd.Stage.Open(str(usd_path))
    if not stage:
        raise RuntimeError(f"无法打开 USD Stage: {usd_path}")

    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_],
        useExtentsHint=True,
    )

    default_prim = stage.GetDefaultPrim()
    if not default_prim or not default_prim.IsValid():
        root_prims = stage.GetPseudoRoot().GetChildren()
        if not root_prims:
            raise RuntimeError(f"USD Stage 中没有找到有效的 Prim: {usd_path}")
        default_prim = root_prims[0]

    rng = bbox_cache.ComputeWorldBound(default_prim).ComputeAlignedRange()
    if rng.IsEmpty():
        raise RuntimeError(f"计算出的包围盒为空: {default_prim.GetPath()}")

    bbox_min, bbox_max = _range_to_bbox(rng)
    unit_info = _get_stage_unit_info(stage)
    bbox_min_meters, bbox_max_meters = _scale_bbox(
        (bbox_min, bbox_max),
        unit_info["meters_per_unit"],
    )

    return {
        "bbox_min": bbox_min,
        "bbox_max": bbox_max,
        "bbox_min_meters": bbox_min_meters,
        "bbox_max_meters": bbox_max_meters,
        **unit_info,
    }


# ---------------- 调用示例 ----------------
if __name__ == "__main__":
    # 在这里修改为你的 USD 文件路径
    target_file = "/media/simple/another_Documents/isaacsim_assets/device_data/usdz/AGV/model_AGV_1.usdz" 
    
    try:
        bbox_info = get_single_object_bbox_with_unit(target_file)
        print("-" * 30)
        print(f"成功读取: {target_file}")
        print(
            "Stage 单位: "
            f"{bbox_info['unit_name']} "
            f"(metersPerUnit={bbox_info['meters_per_unit']}, "
            f"authored={bbox_info['authored_meters_per_unit']})"
        )
        print(f"包围盒最小值 (Min, stage unit): {bbox_info['bbox_min']}")
        print(f"包围盒最大值 (Max, stage unit): {bbox_info['bbox_max']}")
        print(f"包围盒最小值 (Min, meters): {bbox_info['bbox_min_meters']}")
        print(f"包围盒最大值 (Max, meters): {bbox_info['bbox_max_meters']}")
        print("-" * 30)
    except Exception as e:
        print(f"❌ 发生错误: {e}")
    finally:
        # 关闭应用
        simulation_app.close()
