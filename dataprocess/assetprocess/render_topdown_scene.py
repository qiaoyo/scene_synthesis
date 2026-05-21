"""
Top-down orthographic render of a USD scene in Isaac Sim 5.14.
Automatically computes scene bounding box from /Root/Meshes/,
positions an orthographic camera above the scene center,
and outputs both an RGB image and a per-pixel world XY mapping.

Usage:
~/simkit/.venv/bin/python render_topdown_scene.py \
    --usd_path /path/to/scene.usd \
    --output_dir ./output \
    --max_resolution 4096
"""
import argparse
import os

import numpy as np
from isaacsim import SimulationApp

parser = argparse.ArgumentParser(description="Top-down orthographic render of USD scene")
parser.add_argument(
    "--usd_path",
    type=str,
    required=True,
    help="Path to the USD scene file",
)
parser.add_argument(
    "--output_dir",
    type=str,
    default="./render_output",
    help="Output directory",
)
parser.add_argument(
    "--max_resolution",
    type=int,
    default=4096,
    help="Max resolution of the longer edge (pixels). Shorter edge is derived from bbox aspect ratio.",
)
parser.add_argument(
    "--scene_prim_path",
    type=str,
    default="/Root/Meshes",
    help="Prim path for scene bounding box",
)
parser.add_argument(
    "--padding",
    type=float,
    default=0.0,
    help="Padding around scene bounds (meters)",
)
parser.add_argument(
    "--cam_z_offset",
    type=float,
    default=5.0,
    help="Camera height offset above scene top (meters)",
)
parser.add_argument(
    "--renderer",
    type=str,
    default="RayTracing",
    choices=["PathTracing", "Iray", "rtx"],
    help="Renderer type",
)
args, remaining = parser.parse_known_args()

sim_app = SimulationApp({"headless": True, "renderer": args.renderer})

import isaacsim.core.utils.numpy.rotations as rot_utils
import omni.usd
from isaacsim.core.api import World
from isaacsim.sensors.camera import Camera
from PIL import Image
from pxr import Usd, UsdGeom


def compute_scene_bbox(stage, prim_path_str):
    bbox_cache = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_, UsdGeom.Tokens.render, UsdGeom.Tokens.proxy],
        useExtentsHint=True,
    )
    prim = stage.GetPrimAtPath(prim_path_str)
    if not prim or not prim.IsValid():
        prim = stage.GetDefaultPrim()
    if not prim or not prim.IsValid():
        prim = stage.GetPseudoRoot()
    bbox = bbox_cache.ComputeWorldBound(prim)
    bbox_range = bbox.ComputeAlignedRange()
    if bbox_range.IsEmpty():
        raise RuntimeError(f"Bounding box is empty for prim: {prim_path_str}")
    min_pt = bbox_range.GetMin()
    max_pt = bbox_range.GetMax()
    return np.array([min_pt[0], min_pt[1], min_pt[2]]), np.array(
        [max_pt[0], max_pt[1], max_pt[2]]
    )


omni.usd.get_context().open_stage(args.usd_path)
stage = omni.usd.get_context().get_stage()

scene_min, scene_max = compute_scene_bbox(stage, args.scene_prim_path)
scene_center = (scene_min + scene_max) / 2.0
scene_size = scene_max - scene_min

print(f"Scene bounds min: {scene_min}")
print(f"Scene bounds max: {scene_max}")
print(f"Scene center: {scene_center}")
print(f"Scene size: {scene_size}")

ortho_width = scene_size[0] + 2 * args.padding
ortho_height = scene_size[1] + 2 * args.padding

cam_x = scene_center[0]
cam_y = scene_center[1]
cam_z = scene_max[2] + args.cam_z_offset

aspect = ortho_width / ortho_height
if aspect >= 1.0:
    IMG_W = args.max_resolution
    IMG_H = max(1, round(args.max_resolution / aspect))
else:
    IMG_H = args.max_resolution
    IMG_W = max(1, round(args.max_resolution * aspect))

world = World(stage_units_in_meters=1.0)
camera = Camera(
    prim_path="/TopDownCam",
    position=np.array([cam_x, cam_y, cam_z]),
    orientation=rot_utils.euler_angles_to_quats(np.array([0, 90, -90]), degrees=True),
    frequency=30,
    resolution=(IMG_W, IMG_H),
)

world.play()
camera.initialize()

camera.set_projection_mode("orthographic")
camera.set_horizontal_aperture(ortho_width)
camera.set_vertical_aperture(ortho_height)
camera.set_clipping_range(0.05, 1.0e5)

for _ in range(10):
    world.step(render=True)

frame = camera.get_rgba()
rgb = frame[:, :, :3]

cam_prim = camera.prim
xformable = UsdGeom.Xformable(cam_prim)
world_xform = xformable.ComputeLocalToWorldTransform(Usd.TimeCode.Default())

cam_right = np.array([world_xform[0][0], world_xform[1][0], world_xform[2][0]])
cam_up = np.array([world_xform[0][1], world_xform[1][1], world_xform[2][1]])

print(
    f"Camera right axis (world): ({cam_right[0]:.4f}, {cam_right[1]:.4f}, {cam_right[2]:.4f})"
)
print(f"Camera up axis (world):    ({cam_up[0]:.4f}, {cam_up[1]:.4f}, {cam_up[2]:.4f})")

cam_pos = np.array([cam_x, cam_y, cam_z])

u = np.arange(IMG_W)
v = np.arange(IMG_H)
uu, vv = np.meshgrid(u, v)

du = (uu - IMG_W / 2.0) / IMG_W * ortho_width
dv = (IMG_H / 2.0 - vv) / IMG_H * ortho_height

world_x = cam_pos[0] + du * cam_right[0] + dv * cam_up[0]
world_y = cam_pos[1] + du * cam_right[1] + dv * cam_up[1]

xy_map = np.stack([world_x, world_y], axis=-1).astype(np.float32)

os.makedirs(args.output_dir, exist_ok=True)
rgb_path = os.path.join(args.output_dir, "topdown_render.png")
xy_path = os.path.join(args.output_dir, "pixel_to_world_xy.npy")

Image.fromarray(rgb).save(rgb_path)
np.save(xy_path, xy_map)

print(f"\nRendered: {IMG_W}x{IMG_H}")
print(f"Aspect ratio (W/H): {aspect:.4f}")
print(f"Ortho coverage: {ortho_width:.2f} x {ortho_height:.2f} meters")
print(f"Camera position: ({cam_x:.2f}, {cam_y:.2f}, {cam_z:.2f})")
print(f"RGB saved to: {rgb_path}")
print(f"XY map saved to: {xy_path}")
print(f"Pixel (0,0) -> world XY: ({xy_map[0, 0, 0]:.3f}, {xy_map[0, 0, 1]:.3f})")
print(
    f"Pixel center -> world XY: ({xy_map[IMG_H // 2, IMG_W // 2, 0]:.3f}, {xy_map[IMG_H // 2, IMG_W // 2, 1]:.3f})"
)

world.stop()
omni.usd.get_context().close_stage()
sim_app.close()