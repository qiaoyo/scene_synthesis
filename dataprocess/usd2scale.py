import argparse
import os
from pathlib import Path
import sys


def ensure_usd_python_path():
    repo_root = Path("/home/simple/isaacsim")
    candidates = sorted(repo_root.glob("extscache/omni.usd.libs-*"))
    for candidate in reversed(candidates):
        candidate_str = str(candidate)
        bin_path = str(candidate / "bin")
        env = os.environ.copy()

        if env.get("_USD2SCALE_BOOTSTRAPPED") != "1":
            env["_USD2SCALE_BOOTSTRAPPED"] = "1"
            env["PYTHONPATH"] = (
                candidate_str
                if not env.get("PYTHONPATH")
                else f"{candidate_str}:{env['PYTHONPATH']}"
            )
            env["LD_LIBRARY_PATH"] = (
                bin_path
                if not env.get("LD_LIBRARY_PATH")
                else f"{bin_path}:{env['LD_LIBRARY_PATH']}"
            )
            os.execvpe(sys.executable, [sys.executable, *sys.argv], env)

        if candidate_str not in sys.path:
            sys.path.insert(0, candidate_str)
        return

    raise ModuleNotFoundError(
        "Unable to locate Isaac Sim USD Python bindings (pxr). "
        "Expected under /home/simple/isaacsim/extscache/omni.usd.libs-*"
    )


ensure_usd_python_path()

from pxr import Gf, Usd, UsdGeom


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Open a USD, multiply its local scale, and save it as a new USD."
    )
    parser.add_argument("--input", required=True, help="Source USD path.")
    parser.add_argument("--output", required=True, help="Output USD path.")
    parser.add_argument(
        "--scale",
        type=float,
        required=True,
        help="Uniform scale factor. Example: 0.5 shrinks the asset by half.",
    )
    parser.add_argument(
        "--prim-path",
        help="Optional prim path to scale. Defaults to defaultPrim, then the first active root prim.",
    )
    return parser


def resolve_target_prim(stage: Usd.Stage, prim_path: str | None) -> Usd.Prim:
    if prim_path:
        prim = stage.GetPrimAtPath(prim_path)
        if not prim or not prim.IsValid():
            raise ValueError(f"Prim not found: {prim_path}")
        return prim

    default_prim = stage.GetDefaultPrim()
    if default_prim and default_prim.IsValid():
        return default_prim

    for child in stage.GetPseudoRoot().GetChildren():
        if child.IsActive() and child.IsDefined():
            return child

    raise ValueError("No active root prim found in the stage.")


def extract_local_trs(prim: Usd.Prim):
    xformable = UsdGeom.Xformable(prim)
    if not xformable:
        raise ValueError(f"Prim is not Xformable: {prim.GetPath()}")

    pose = xformable.GetLocalTransformation()
    translate = pose.ExtractTranslation()
    orient = pose.ExtractRotationQuat()
    scale = Gf.Vec3d(
        Gf.Vec3d(pose[0][0], pose[0][1], pose[0][2]).GetLength(),
        Gf.Vec3d(pose[1][0], pose[1][1], pose[1][2]).GetLength(),
        Gf.Vec3d(pose[2][0], pose[2][1], pose[2][2]).GetLength(),
    )
    return translate, orient, scale


def clear_existing_xform_ops(prim: Usd.Prim):
    xform_op_order = prim.GetAttribute("xformOpOrder")
    if xform_op_order.IsValid():
        op_names = xform_op_order.Get() or []
        for op_name in op_names:
            prim.RemoveProperty(str(op_name))
        prim.RemoveProperty("xformOpOrder")

    for prop in prim.GetProperties():
        prop_name = prop.GetName()
        if prop_name.startswith("xformOp:"):
            prim.RemoveProperty(prop_name)


def set_local_trs(prim: Usd.Prim, translate, orient, scale):
    xform = UsdGeom.Xformable(prim)
    if not xform:
        raise ValueError(f"Prim is not Xformable: {prim.GetPath()}")

    clear_existing_xform_ops(prim)

    translate_op = xform.AddTranslateOp(precision=UsdGeom.XformOp.PrecisionDouble)
    orient_op = xform.AddOrientOp(precision=UsdGeom.XformOp.PrecisionFloat)
    scale_op = xform.AddScaleOp(precision=UsdGeom.XformOp.PrecisionDouble)

    orient_f = Gf.Quatf(float(orient.GetReal()), Gf.Vec3f(*orient.GetImaginary()))

    translate_op.Set(translate)
    orient_op.Set(orient_f)
    scale_op.Set(scale)


def scale_usd(input_usd: str, output_usd: str, scale_factor: float, prim_path: str | None):
    if scale_factor <= 0:
        raise ValueError(f"Scale must be > 0, got {scale_factor}")

    stage = Usd.Stage.Open(input_usd)
    if stage is None:
        raise RuntimeError(f"Failed to open USD stage: {input_usd}")

    target_prim = resolve_target_prim(stage, prim_path)
    translate, orient, current_scale = extract_local_trs(target_prim)
    scaled = Gf.Vec3d(
        current_scale[0] * scale_factor,
        current_scale[1] * scale_factor,
        current_scale[2] * scale_factor,
    )

    set_local_trs(target_prim, translate, orient, scaled)

    output_path = Path(output_usd)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not stage.Export(str(output_path)):
        raise RuntimeError(f"Failed to export USD stage to: {output_path}")

    print(f"Target prim: {target_prim.GetPath()}", flush=True)
    print(f"Original scale: {current_scale}", flush=True)
    print(f"Scaled to: {scaled}", flush=True)
    print(f"Saved scaled USD to: {output_path}", flush=True)


def main():
    args = build_parser().parse_args()
    scale_usd(args.input, args.output, args.scale, args.prim_path)


if __name__ == "__main__":
    main()
