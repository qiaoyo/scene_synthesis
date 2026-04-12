#!/usr/bin/env /home/simple/robot/bin/python
import os
# 设置 GPU 设备
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# 启动 Isaac Sim
from isaacsim.simulation_app import SimulationApp
simulation_app = SimulationApp({"headless": True})
import pandas as pd
from pathlib import Path
from typing import Tuple

from pxr import Usd, UsdGeom, Gf


def _range_to_bbox(range3d: Gf.Range3d) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    mn = range3d.GetMin()
    mx = range3d.GetMax()
    return (float(mn[0]), float(mn[1]), float(mn[2])), (
        float(mx[0]), float(mx[1]), float(mx[2])
    )


def get_bbox(usd_path: Path):
    stage = Usd.Stage.Open(str(usd_path))
    if not stage:
        raise RuntimeError(f"Failed to open USD stage: {usd_path}")

    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_],
        useExtentsHint=True,
    )

    default_prim = stage.GetDefaultPrim()
    if not default_prim or not default_prim.IsValid():
        raise RuntimeError(f"USD stage has no valid default prim: {usd_path}")

    imageable = UsdGeom.Imageable(default_prim)
    if not imageable:
        raise RuntimeError(f"Default prim is not imageable: {default_prim.GetPath()}")

    rng = bbox_cache.ComputeWorldBound(default_prim).ComputeAlignedRange()
    if rng.IsEmpty():
        raise RuntimeError(f"Default prim bbox is empty: {default_prim.GetPath()}")

    return _range_to_bbox(rng)

def process_csv(csv_file: Path):
    print(f"\n📄 Processing CSV: {csv_file}")

    df = pd.read_csv(csv_file)

    if "Path" not in df.columns:
        print(f"⚠️ CSV {csv_file} does not contain 'Path' column, skipped.")
        return

    bbox_min_list = []
    bbox_max_list = []
    
    for usd_path in df["Path"]:
        # 1. 过滤 NaN 或空值
        if pd.isna(usd_path):
            bbox_min_list.append(None)
            bbox_max_list.append(None)
            continue

        # 2. 强制转换为字符串
        usd_path = str(usd_path).strip()

        # 3. 空字符串也跳过
        if usd_path == "":
            bbox_min_list.append(None)
            bbox_max_list.append(None)
            continue

        # 4. 转换为 Path
        usd_path = Path(usd_path)

        if not usd_path.exists():
            print(f"⚠️ File not found: {usd_path}")
            bbox_min_list.append(None)
            bbox_max_list.append(None)
            continue

        try:
            mn, mx = get_bbox(usd_path)
            bbox_min_list.append(mn)
            bbox_max_list.append(mx)
            print(f"✓ {usd_path} → {mn}  {mx}")
        except Exception as e:
            print(f"❌ Error processing {usd_path}: {e}")
            bbox_min_list.append(None)
            bbox_max_list.append(None)


    df["bbox_min"] = bbox_min_list
    df["bbox_max"] = bbox_max_list

    output_file = csv_file.with_name(csv_file.stem + "_with_bbox.csv")
    df.to_csv(output_file, index=False)
    print(f"✔️ Saved: {output_file}")


def process_all_csv(folder: Path):
    csv_files = list(folder.glob("*.csv"))
    if not csv_files:
        print("❌ No CSV files found in folder.")
        return

    print(f"📂 Found {len(csv_files)} CSV files in {folder}")

    for csv_file in csv_files:
        process_csv(csv_file)


if __name__ == "__main__":
    folder_path = Path("/home/simple/Desktop/Scene-Knowledge/csv/1")  # 修改为你的文件夹路径
    process_all_csv(folder_path)

