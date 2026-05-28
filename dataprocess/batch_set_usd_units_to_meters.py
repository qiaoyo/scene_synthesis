import argparse
import os
import shutil
import sys
import zipfile
from pathlib import Path


USD_EXTENSIONS = {".usd", ".usda", ".usdc", ".usdz"}
TARGET_METERS_PER_UNIT = 1.0


def iter_usd_files(input_dir, recursive):
    pattern = "**/*" if recursive else "*"
    for path in sorted(input_dir.glob(pattern)):
        if path.is_file() and path.suffix.lower() in USD_EXTENSIONS:
            yield path


def write_single_layer_usdz(input_file, output_file, archive_name):
    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.write(input_file, arcname=archive_name)


def scale_stage(stage, scale_factor):
    from pxr import Gf, Usd, UsdGeom, Vt

    for prim in stage.Traverse():
        if prim.IsA(UsdGeom.PointBased):
            point_based = UsdGeom.PointBased(prim)
            points_attr = point_based.GetPointsAttr()
            points = points_attr.Get(Usd.TimeCode.Default())
            if points:
                scaled_points = Vt.Vec3fArray(
                    [Gf.Vec3f(point[0] * scale_factor, point[1] * scale_factor, point[2] * scale_factor) for point in points]
                )
                points_attr.Set(scaled_points, Usd.TimeCode.Default())
                extent = UsdGeom.PointBased.ComputeExtent(scaled_points)
                point_based.GetExtentAttr().Set(extent, Usd.TimeCode.Default())

        if prim.IsA(UsdGeom.Xformable):
            xformable = UsdGeom.Xformable(prim)
            for op in xformable.GetOrderedXformOps():
                op_name = op.GetOpName()
                if not op_name.startswith("xformOp:translate"):
                    continue
                value = op.Get(Usd.TimeCode.Default())
                if value is not None:
                    op.Set(Gf.Vec3d(value) * scale_factor, Usd.TimeCode.Default())


def save_stage(stage, output_path):
    from pxr import Sdf, UsdUtils

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.suffix.lower() != ".usdz":
        stage.Export(str(output_path))
        return

    temp_usdc = output_path.with_name(f".temp_{output_path.stem}.usdc")
    try:
        stage.Export(str(temp_usdc))
        try:
            success = UsdUtils.CreateNewUsdzPackage(
                Sdf.AssetPath(str(temp_usdc)),
                str(output_path),
            )
            if not success:
                raise RuntimeError(f"Failed to create usdz: {output_path}")
        except Exception as exc:
            print(f"  Full package failed, writing single-layer usdz: {exc}")
            write_single_layer_usdz(temp_usdc, output_path, f"{output_path.stem}.usdc")
    finally:
        if temp_usdc.exists():
            os.remove(temp_usdc)


def process_usd_file(input_path, output_path, scale_geometry):
    from pxr import Usd, UsdGeom

    print(f"Processing: {input_path}")
    stage = Usd.Stage.Open(str(input_path))
    if not stage:
        print(f"  Failed to open stage: {input_path}", file=sys.stderr)
        return False

    old_meters_per_unit = float(UsdGeom.GetStageMetersPerUnit(stage))
    print(f"  metersPerUnit: {old_meters_per_unit} -> {TARGET_METERS_PER_UNIT}")

    if scale_geometry and old_meters_per_unit != TARGET_METERS_PER_UNIT:
        scale_factor = old_meters_per_unit / TARGET_METERS_PER_UNIT
        print(f"  Scaling authored geometry/translates by: {scale_factor}")
        scale_stage(stage, scale_factor)

    UsdGeom.SetStageMetersPerUnit(stage, TARGET_METERS_PER_UNIT)
    save_stage(stage, output_path)
    print(f"  Saved: {output_path}")
    return True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch set USD stage units to meters."
    )
    parser.add_argument("input_dir", help="Folder containing USD files.")
    parser.add_argument("output_dir", help="Folder where converted USD files are saved.")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Process USD files in subfolders and preserve relative paths.",
    )
    parser.add_argument(
        "--scale-geometry",
        action="store_true",
        help="Scale authored points and translate ops so world size stays unchanged.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow output_dir to be the same as input_dir and overwrite files.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not input_dir.is_dir():
        print(f"Input folder does not exist: {input_dir}", file=sys.stderr)
        return 1

    if input_dir == output_dir and not args.overwrite:
        print("Refusing to overwrite input files. Use --overwrite if intended.", file=sys.stderr)
        return 1

    usd_files = list(iter_usd_files(input_dir, args.recursive))
    if not usd_files:
        print(f"No USD files found in: {input_dir}")
        return 1

    print(f"Found {len(usd_files)} USD files.")
    success_count = 0
    for input_path in usd_files:
        relative_path = input_path.relative_to(input_dir)
        output_path = output_dir / relative_path
        if input_path == output_path:
            backup_path = input_path.with_suffix(input_path.suffix + ".bak")
            shutil.copy2(input_path, backup_path)
            print(f"  Backup: {backup_path}")
        if process_usd_file(input_path, output_path, args.scale_geometry):
            success_count += 1

    failed_count = len(usd_files) - success_count
    print(f"Done. success={success_count}, failed={failed_count}")
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
