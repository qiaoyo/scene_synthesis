#!/usr/bin/env /home/simple/robot/bin/python
import argparse
import csv
import os
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

# 启动 Isaac Sim 之前设置环境变量。
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "1")

from isaacsim.simulation_app import SimulationApp

simulation_app = SimulationApp({"headless": True})

from pxr import Gf, Usd, UsdGeom


PATH_COLUMN_CANDIDATES = ("Path", "Scene_path", "USD_Path", "usd_path", "path")


def _range_to_bbox(
    range3d: Gf.Range3d,
) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    mn = range3d.GetMin()
    mx = range3d.GetMax()
    return (
        float(mn[0]),
        float(mn[1]),
        float(mn[2]),
    ), (
        float(mx[0]),
        float(mx[1]),
        float(mx[2]),
    )


def _scale_bbox(
    bbox: Tuple[Tuple[float, float, float], Tuple[float, float, float]],
    scale: float,
) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    bbox_min, bbox_max = bbox
    scaled_min = tuple(float(value * scale) for value in bbox_min)
    scaled_max = tuple(float(value * scale) for value in bbox_max)
    return scaled_min, scaled_max


def _find_path_column(header: Sequence[str]) -> Optional[str]:
    for column in PATH_COLUMN_CANDIDATES:
        if column in header:
            return column

    for column in header:
        if "path" in str(column).lower():
            return column

    return None


def _get_default_prim(stage: Usd.Stage, usd_path: Path) -> Usd.Prim:
    default_prim = stage.GetDefaultPrim()
    if default_prim and default_prim.IsValid():
        return default_prim

    root_prims = stage.GetPseudoRoot().GetChildren()
    if root_prims:
        return root_prims[0]

    raise RuntimeError(f"USD Stage 中没有找到有效的 Prim: {usd_path}")


def get_bbox_in_meters(
    usd_path: Path,
) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    stage = Usd.Stage.Open(str(usd_path))
    if not stage:
        raise RuntimeError(f"无法打开 USD Stage: {usd_path}")

    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_],
        useExtentsHint=True,
    )

    default_prim = _get_default_prim(stage, usd_path)
    rng = bbox_cache.ComputeWorldBound(default_prim).ComputeAlignedRange()
    if rng.IsEmpty():
        raise RuntimeError(f"计算出的包围盒为空: {default_prim.GetPath()}")

    bbox = _range_to_bbox(rng)
    meters_per_unit = float(UsdGeom.GetStageMetersPerUnit(stage))
    return _scale_bbox(bbox, meters_per_unit)


def _normalize_usd_path(raw_path: object, csv_file: Path) -> Optional[Path]:
    if raw_path is None:
        return None

    text = str(raw_path).strip()
    if not text or text.lower() in {"nan", "none", "null"}:
        return None

    path = Path(text)
    if not path.is_absolute():
        path = (csv_file.parent / path).resolve()

    return path


def process_csv(csv_file: Path, output_suffix: str) -> Optional[Path]:
    print(f"\nProcessing CSV: {csv_file}")
    with csv_file.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))

    if not rows:
        print("  Skipped: 空 CSV 文件。")
        return None

    header = rows[0]
    data_rows = rows[1:]

    path_column = _find_path_column(header)
    if not path_column:
        print(f"  Skipped: 未找到路径列，现有列为 {list(header)}")
        return None

    path_column_index = header.index(path_column)

    output_rows = []

    for index, row in enumerate(data_rows, start=1):
        normalized_row = list(row)
        if len(normalized_row) < len(header):
            normalized_row.extend([""] * (len(header) - len(normalized_row)))

        raw_path = normalized_row[path_column_index] if path_column_index < len(normalized_row) else ""
        usd_path = _normalize_usd_path(raw_path, csv_file)
        if usd_path is None:
            normalized_row.extend(["", ""])
            output_rows.append(normalized_row)
            print(f"  [{index}] Empty path, skipped.")
            continue

        if not usd_path.exists():
            normalized_row.extend(["", ""])
            output_rows.append(normalized_row)
            print(f"  [{index}] File not found: {usd_path}")
            continue

        try:
            bbox_min_meters, bbox_max_meters = get_bbox_in_meters(usd_path)
            normalized_row.extend([str(bbox_min_meters), str(bbox_max_meters)])
            output_rows.append(normalized_row)
            print(f"  [{index}] OK: {usd_path}")
        except Exception as exc:
            normalized_row.extend(["", ""])
            output_rows.append(normalized_row)
            print(f"  [{index}] Error: {usd_path} -> {exc}")

    output_file = csv_file.with_name(f"{csv_file.stem}{output_suffix}.csv")
    output_header = list(header) + ["bbox_min_meters", "bbox_max_meters"]
    with output_file.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(output_header)
        writer.writerows(output_rows)

    print(f"Saved: {output_file}")
    return output_file


def _expand_inputs(inputs: Sequence[str]) -> List[Path]:
    csv_files: List[Path] = []

    for raw_input in inputs:
        path = Path(raw_input).expanduser()
        if path.is_dir():
            csv_files.extend(sorted(path.glob("*.csv")))
        elif path.suffix.lower() == ".csv":
            csv_files.append(path)
        else:
            print(f"Skipped non-csv input: {path}")

    unique_files = []
    seen = set()
    for csv_file in csv_files:
        resolved = csv_file.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_files.append(resolved)

    return unique_files


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="读取一个或多个 CSV，计算其中 USD 路径对应的米制 bbox，并追加到结果 CSV 末尾两列。",
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="CSV 文件路径，或包含 CSV 的目录路径。",
    )
    parser.add_argument(
        "--output-suffix",
        default="_with_bbox_meters",
        help="输出文件后缀，默认: _with_bbox_meters",
    )
    args = parser.parse_args(argv)

    csv_files = _expand_inputs(args.inputs)
    if not csv_files:
        print("No CSV files found.")
        return 1

    print(f"Found {len(csv_files)} CSV file(s).")

    for csv_file in csv_files:
        process_csv(csv_file, args.output_suffix)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    finally:
        simulation_app.close()
