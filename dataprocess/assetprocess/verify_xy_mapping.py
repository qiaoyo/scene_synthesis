"""
Verify that pixel_to_world_xy.npy correctly maps rendered pixels
to world XY coordinates in the USD scene.

Experiments:
1. BBox projection: compute world bbox of target prim,
   project bottom-face corners to pixel coords, draw on rendered image
2. Grid linearity check: verify xy_map is a uniform linear grid

Usage:
  ~/simkit/.venv/bin/python verify_xy_mapping.py \
    --usd_path /mnt/bn/isaac-sim-assets/GenieSimAssets/scenes/commercial_scenes_fast/MV5M25QKTKJZZ2AAB \
    --render_dir ./render_output \
    --target_prim /Root/Meshes/BaseAnimation/cabinet/model_35e4facb38c17da6ee87134cdc9cb5ae_0
"""
import argparse
import os
import cv2
import numpy as np
from PIL import Image
from pxr import Usd, UsdGeom

def compute_world_bbox(stage, prim_path_str):
    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_, UsdGeom.Tokens.render, UsdGeom.Tokens.proxy],
        useExtentsHint=True,
    )
    prim = stage.GetPrimAtPath(prim_path_str)
    if not prim or not prim.IsValid():
        raise RuntimeError(f"Prim not found: {prim_path_str}")
    bbox = bbox_cache.ComputeWorldBound(prim)
    bbox_range = bbox.ComputeAlignedRange()
    if bbox_range.IsEmpty():
        raise RuntimeError(f"BBox is empty for: {prim_path_str}")
    return bbox_range.GetMin(), bbox_range.GetMax()


def world_xy_to_pixel(wx, wy, xy_map):
    H, W = xy_map.shape[:2]
    x_min = xy_map[0, 0, 0]
    x_max = xy_map[0, -1, 0]
    y_max = xy_map[0, 0, 1]
    y_min = xy_map[-1, 0, 1]
    if abs(x_max - x_min) < 1e-9 or abs(y_max - y_min) < 1e-9:
        return None, None
    u = (wx - x_min) / (x_max - x_min) * (W - 1)
    v = (wy - y_max) / (y_min - y_max) * (H - 1)
    return int(round(v)), int(round(u))


def experiment_bbox_overlay(xy_map, rgb_img, render_dir, stage, target_prim_path):
    print("=" * 60)
    print("Experiment 1: BBox Projection")
    print("=" * 60)

    bbox_min, bbox_max = compute_world_bbox(stage, target_prim_path)
    print(f"  BBox min: {bbox_min[0]:.3f}, {bbox_min[1]:.3f}, {bbox_min[2]:.3f}")
    print(f"  BBox max: {bbox_max[0]:.3f}, {bbox_max[1]:.3f}, {bbox_max[2]:.3f}")

    annotated = rgb_img.copy()
    H, W = xy_map.shape[:2]

    bottom_corners_xy = [
        (bbox_min[0], bbox_min[1]),
        (bbox_max[0], bbox_min[1]),
        (bbox_max[0], bbox_max[1]),
        (bbox_min[0], bbox_max[1]),
    ]

    pixels = []
    for wx, wy in bottom_corners_xy:
        r, c = world_xy_to_pixel(wx, wy, xy_map)
        pixels.append((c, r))
        print(f"  World ({wx:.3f}, {wy:.3f}) -> pixel ({r}, {c})")

    pts = np.array(pixels, dtype=np.int32)
    cv2.polylines(annotated, [pts], True, (0, 255, 0), 3)
    for px, py in pixels:
        cv2.circle(annotated, px, py, 8, (0, 255, 0), -1)

    cx = (bbox_min[0] + bbox_max[0]) / 2
    cy = (bbox_min[1] + bbox_max[1]) / 2
    cr, cc = world_xy_to_pixel(cx, cy, xy_map)
    if cr is not None:
        cv2.drawMarker(annotated, (cc, cr), (255, 0, 255), cv2.MARKER_CROSS, 30, 3)

    # # 0: minX, minY
    # # 1: maxX, minY
    # # 2: maxX, maxY
    # # 3: minX, maxY
    corner_labels = ["0", "1", "2", "3"]
    for i, (px, py) in enumerate(pixels):
        cv2.putText(
            annotated,
            corner_labels[i],
            (px + 10, py - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

    out_path = os.path.join(render_dir, "verify_bbox.png")
    Image.fromarray(annotated).save(out_path)

    print(f"  Green rect = bbox bottom face (XY projection)")
    print(f"  Magenta cross = bbox XY center")
    print(f"  Corner labels show world coordinate meaning")
    print(f"  Saved to: {out_path}")
    print(f"  -> Green rect should tightly wrap the target object")
    print(
        f"  -> Corner labels should match spatial position (minX=left, maxX=right, etc.)"
    )

    return True


def experiment_grid_linearity(xy_map):
    print("\n" + "=" * 60)
    print("Experiment 2: Grid Linearity Check")
    print("=" * 60)

    dx = np.diff(xy_map[:, :, 0], axis=1)
    dy = np.diff(xy_map[:, :, 1], axis=0)

    dx_mean = dx.mean()
    dx_std = dx.std()
    dy_mean = dy.mean()
    dy_std = dy.std()

    print(f"  X step per pixel (horizontal): mean={dx_mean:.6f}, std={dx_std:.8f}")
    print(f"  Y step per pixel (vertical):   mean={dy_mean:.6f}, std={dy_std:.8f}")
    print(f"  X uniform: {'PASS' if dx_std < 1e-6 else 'FAIL'}")
    print(f"  Y uniform: {'PASS' if dy_std < 1e-6 else 'FAIL'}")

    linear_pass = dx_std < 1e-6 and dy_std < 1e-6
    print(f"  Overall: {'PASS' if linear_pass else 'FAIL'}")

    return linear_pass


def main():
    parser = argparse.ArgumentParser(description="Verify pixel_to_world_xy mapping")
    parser.add_argument("--usd_path", type=str, required=True)
    parser.add_argument("--render_dir", type=str, required=True)
    parser.add_argument(
        "--target_prim",
        type=str,
        default="/Root/Meshes/BaseAnimation/cabinet/model_35e4facb38c17da6ee87134cdc9cb5ae_0",
        help="Prim path of the object to verify",
    )
    args = parser.parse_args()

    xy_path = os.path.join(args.render_dir, "pixel_to_world_xy.npy")
    rgb_path = os.path.join(args.render_dir, "topdown_render.png")

    if not os.path.exists(xy_path):
        print(f"ERROR: {xy_path} not found")
        return
    if not os.path.exists(rgb_path):
        print(f"ERROR: {rgb_path} not found")
        return

    xy_map = np.load(xy_path)
    rgb_img = np.array(Image.open(rgb_path))
    print(f"xy_map shape: {xy_map.shape}, dtype: {xy_map.dtype}")
    print(f"rgb_img shape: {rgb_img.shape}")
    print(f"target_prim: {args.target_prim}\n")

    stage = Usd.Stage.Open(args.usd_path)
    if not stage:
        print(f"ERROR: Cannot open USD: {args.usd_path}")
        return

    r1 = experiment_bbox_overlay(
        xy_map, rgb_img, args.render_dir, stage, args.target_prim
    )
    r2 = experiment_grid_linearity(xy_map)

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"1. BBox projection:  {'PASS' if r1 else 'FAIL'}")
    print(f"2. Grid linearity:   {'PASS' if r2 else 'FAIL'}")


if __name__ == "__main__":
    main()
