#!/usr/bin/env /home/simple/robot/bin/python

import os
import json
from collections import defaultdict

# 设置 GPU 设备
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# 启动 Isaac Sim
from isaacsim.simulation_app import SimulationApp
simulation_app = SimulationApp({"headless": False})

# 导入 USD 和 Isaac Sim 模块
import omni.usd
from pxr import Usd, UsdGeom, Gf
from isaacsim.core.utils.stage import add_reference_to_stage

# 添加参考并设置变换
def add_reference_with_transform(stage, prim_path, usd_path, position=(0, 0, 0), scale=(0.01, 0.01, 0.01), rotation=None):
    from pxr import UsdGeom, Gf

    # 打开参考文件，获取其 Up Axis
    temp_stage = Usd.Stage.Open(usd_path)
    up_axis = UsdGeom.GetStageUpAxis(temp_stage)

    # 自动对齐旋转（欧拉角，单位为度）
    align_euler = (0, 0, 0)
    if up_axis == UsdGeom.Tokens.y:
        align_euler = (90, 0, 0)
    elif up_axis == UsdGeom.Tokens.x:
        align_euler = (0, -90, 0)

    # 用户指定旋转（欧拉角，单位为度）
    user_euler = rotation if rotation else (0, 0, 0)

    # 构造对齐旋转的四元数
    align_rot = Gf.Rotation(Gf.Vec3d(1, 0, 0), align_euler[0])
    align_rot = align_rot * Gf.Rotation(Gf.Vec3d(0, 1, 0), align_euler[1])
    align_rot = align_rot * Gf.Rotation(Gf.Vec3d(0, 0, 1), align_euler[2])
    align_quat = align_rot.GetQuat()

    # 构造用户旋转的四元数
    user_rot = Gf.Rotation(Gf.Vec3d(1, 0, 0), user_euler[0])
    user_rot = user_rot * Gf.Rotation(Gf.Vec3d(0, 1, 0), user_euler[1])
    user_rot = user_rot * Gf.Rotation(Gf.Vec3d(0, 0, 1), user_euler[2])
    user_quat = user_rot.GetQuat()

    # 合并旋转（先对齐，再应用用户旋转）
    final_quat = user_quat * align_quat

    # 添加引用
    add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)

    # 设置变换
    prim = stage.GetPrimAtPath(prim_path)
    xform = UsdGeom.Xformable(prim)
    def get_or_add(op_type):
        for op in xform.GetOrderedXformOps():
            if op.GetOpType() == op_type:
                return op
        return xform.AddXformOp(op_type)
    get_or_add(UsdGeom.XformOp.TypeTranslate).Set(Gf.Vec3f(*position))
    get_or_add(UsdGeom.XformOp.TypeScale).Set(Gf.Vec3f(*scale))
    orient_op = get_or_add(UsdGeom.XformOp.TypeOrient)
    attr = orient_op.GetAttr()
    type_name = attr.GetTypeName()
    if type_name == "quatf":
        quatf = Gf.Quatf(
            final_quat.GetReal(),
            Gf.Vec3f(*final_quat.GetImaginary())
        )
        orient_op.Set(quatf)
    elif type_name == "quatd":
        orient_op.Set(final_quat)
    else:
        raise RuntimeError(f"Unsupported orient type: {type_name}")

# 加载 JSON 并添加资产
def load_layout_from_json(json_path):
    stage = omni.usd.get_context().get_stage()

    with open(json_path, "r", encoding="utf-8") as f:
        layout = json.load(f)

    # 用于生成唯一 prim_path 的计数器
    id_counter = defaultdict(int)

    for item in layout:
        asset_id = item.get("asset_id", "Asset")
        usd_path = item["usd_path"]
        position = item.get("position", [0, 0, 0])
        rotation = item.get("rotation", [0, 0, 0])

        # 生成唯一 prim_path
        id_counter[asset_id] += 1
        prim_path = f"/World/{asset_id}_{id_counter[asset_id]}"

        print(f"添加 {asset_id} → {prim_path}")
        add_reference_with_transform(stage, prim_path, usd_path, position, scale, rotation)

# === 执行 ===
if __name__ == "__main__":

    # 加载布局 JSON
    load_layout_from_json("/home/simple/joey/scene_synthesis/scripts/scene.json")
    print("✅ 所有资产已加载完成！")
    # ===== 启动仿真循环（仅用于查看场景）=====
    try:
        while simulation_app.is_running():
            simulation_app.update()
    finally:
        simulation_app.close()
