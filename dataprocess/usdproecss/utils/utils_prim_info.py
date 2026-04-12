import math
from pxr import Gf, Sdf, Usd, UsdGeom


def get_xform_matrix(xform_prim: Usd.Prim):
    """获取Xform节点的变换矩阵"""
    xform = UsdGeom.Xform(xform_prim)
    xform_api = UsdGeom.XformCommonAPI(xform_prim)
    translate, rot, scale, pivot, rot_order = xform_api.GetXformVectors(Usd.TimeCode.Default())
    # print(translate, rot, scale, pivot, rot_order)
    transform = UsdGeom.Xformable(xform_prim).GetLocalTransformation()
    return transform

def accumulate_parent_transforms(prim: Usd.Prim, depth: int = 0):
    """计算当前prim到depth层Xform的累积变换矩阵"""
    current_prim = prim.GetParent()
    total_matrix = Gf.Matrix4d(1.0)  # 初始化为单位矩阵
    # print(prim, current_prim)
    cnt = 0
    while cnt < depth and not current_prim.IsPseudoRoot():
        xform_matrix = get_xform_matrix(current_prim)
        total_matrix = xform_matrix * total_matrix
        current_prim = current_prim.GetParent()
        cnt += 1
    return total_matrix


def decompose_matrix_to_trs(matrix: Gf.Matrix4d) -> tuple[Gf.Vec3d, Gf.Vec3f, Gf.Vec3f]:
    # Gf.Matrix4d.Factor() provides a robust decomposition.
    # It returns: (scaleOrientation, scale, rotation, translation, perspective)
    (ok, scale_orientation_quat, scale, rotation_matrix_decomposed, translation, projection) = matrix.Factor()
    rotation_quat_decomposed = rotation_matrix_decomposed.ExtractRotation()
    euler_angles_rad = rotation_quat_decomposed.Decompose(Gf.Vec3d.XAxis(), Gf.Vec3d.YAxis(), Gf.Vec3d.ZAxis())
    euler_angles_deg = [math.degrees(angle) for angle in euler_angles_rad]
    return Gf.Vec3d(translation), Gf.Vec3f(euler_angles_deg), Gf.Vec3f(scale)


def decompose_matrix_to_tos(matrix: Gf.Matrix4d) -> tuple[Gf.Vec3d, Gf.Quatd, Gf.Vec3f]:
    """decompose the matrix to translation, orientation, scale"""
    (ok, scale_orientation_quat, scale, rotation_matrix_decomposed, translation, projection) = matrix.Factor()
    rotation_quat = rotation_matrix_decomposed.ExtractRotationQuat()
    return Gf.Vec3d(translation), Gf.Quatf(rotation_quat), Gf.Vec3f(scale)

def merge_transform_to_current_prim(current_prim: Usd.Prim, depth: int = 0):
    """将上层K级Xform合并到current所在的Xform节点，并重置上层变换"""
    # 计算所有上层Xform的累积变换
    parent_matrix = accumulate_parent_transforms(current_prim, depth)
    # 如果上层没有变换，直接返回
    if parent_matrix == Gf.Matrix4d(1.0):
        print(f"⚠️ {current_prim.GetPath()} 上层无变换，无需处理")
        return

    # 获取current所在Xform当前的变换
    current_matrix = get_xform_matrix(current_prim)
    # 合并变换（上层累积变换 × 当前变换）
    new_matrix = parent_matrix * current_matrix

    # 将合并后的矩阵应用到current所在的Xform
    (translation, rotationzyx, scale) = decompose_matrix_to_trs(new_matrix)
    (translation, orientation, scale) = decompose_matrix_to_tos(new_matrix)
    xform_api_current = UsdGeom.Xformable(current_prim)
    xform_api_current.ClearXformOpOrder()

    if current_prim.IsA(UsdGeom.Mesh):
        transform_op = xform_api_current.AddTransformOp(UsdGeom.XformOp.PrecisionDouble, "transform")
        transform_op.Set(new_matrix, Usd.TimeCode.Default())
    elif current_prim.IsA(UsdGeom.Xform):
        translate_op = xform_api_current.AddTranslateOp()
        rotatezyx_op = xform_api_current.AddRotateZYXOp()
        orient_op = xform_api_current.AddOrientOp()
        scale_op = xform_api_current.AddScaleOp()
        translate_op.Set(translation, Usd.TimeCode.Default())
        # rotatezyx_op.Set(rotationzyx, Usd.TimeCode.Default())
        orient_op.Set(orientation, Usd.TimeCode.Default())
        scale_op.Set(scale, Usd.TimeCode.Default())

    # xform_api_current.SetTranslate(translation, Usd.TimeCode.Default())
    # xform_api_current.SetRotate(rotationzyx, UsdGeom.XformCommonAPI.RotationOrderZYX, Usd.TimeCode.Default())
    # xform_api_current.SetScale(Gf.Vec3f(scale), Usd.TimeCode.Default())

    # xformable = UsdGeom.Xformable(current_prim)
    # xform_op = xformable.AddTransformOp(UsdGeom.XformOp.PrecisionDouble, "transform")
    # xform_op.Set(new_matrix, Usd.TimeCode.Default())

    print(f"✅ 已合并变换到 {current_prim.GetPath()}")

    # 重置所有上层Xform为单位矩阵（无变换）
    parent_cnt = 0
    current_parent = current_prim.GetParent()
    while current_parent and not current_parent.IsPseudoRoot() and parent_cnt < depth:
        xformable = UsdGeom.Xformable(current_parent)
        xformable.ClearXformOpOrder()
        # current_parent.GetAttribute("xformOpOrder").Get()
        if current_parent.IsA(UsdGeom.Mesh):
            current_parent_transform = UsdGeom.Xformable(current_parent).AddTransformOp(UsdGeom.XformOp.PrecisionDouble, "trans")
            current_parent_transform.Set(Gf.Matrix4d(1.0), Usd.TimeCode.Default())
        elif current_parent.IsA(UsdGeom.Xform):
            translate_op = xformable.AddTranslateOp()
            rotatezyx_op = xformable.AddRotateZYXOp()
            scale_op = xformable.AddScaleOp()
            translate_op.Set(Gf.Vec3d(0, 0, 0), Usd.TimeCode.Default())
            rotatezyx_op.Set(Gf.Vec3f(0, 0, 0), Usd.TimeCode.Default())
            scale_op.Set(Gf.Vec3f(1, 1, 1), Usd.TimeCode.Default())
        parent_cnt += 1
        # translation, rotationzyx, scale = decompose_matrix_to_trs(new_matrix)
        prim_type = current_parent.GetTypeName()
        # print(f"Prim类型：{prim_type}") # 正常应为 "Xform"
        # xform_op_order = current_prim.GetAttribute("xformOpOrder")
        # for op in xform_op_order.Get():
        #   current_prim.RemoveProperty(op)
        # print(current_prim.GetAttribute("xformOpOrder").Get())
        # xform_api_current = UsdGeom.XformCommonAPI(current_prim)
        # xform_api_current.SetTranslate(Gf.Vec3d(0,0,0), Usd.TimeCode.Default())
        # xform_api_current.SetRotate(Gf.Vec3f(0,0,0), UsdGeom.XformCommonAPI.RotationOrderZYX, Usd.TimeCode.Default())
        # xform_api_current.SetScale(Gf.Vec3f(1, 1, 1), Usd.TimeCode.Default())
        print(f"✅ 已重置上层Xform {current_parent.GetPath()}")
        current_parent = current_parent.GetParent()
