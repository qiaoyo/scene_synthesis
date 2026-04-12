from __future__ import annotations
from typing import Iterable
from core.simple_base import USDProcessingContext, USDProcessor
from pxr import Gf, Usd, UsdGeom, Vt, UsdPhysics, Sdf
from utils.utils_prim_info import decompose_matrix_to_trs, decompose_matrix_to_tos


class FlattenXform2MeshJoint(USDProcessor):
    """Flatten Xform prim transforms onto descendant meshes by baking them into point data."""
    def __init__(self, flatten_scale: bool = True) -> None:
        super().__init__(
            name="FlattenXform2MeshJoint",
            description="bake Xform translate/rotate (and optionally scale) into mesh vertices",
        )
        self.flatten_scale = flatten_scale

    def process(self, context: USDProcessingContext) -> bool:
        stage = context.stage

        xform_prims: list[Usd.Prim] = [
            prim
            for prim in stage.Traverse()
            if prim.IsA(UsdGeom.Xform) and not prim.IsPseudoRoot() and not prim.IsInstance()
        ]
        joint_prims: list[Usd.Prim] = [
            prim
            for prim in stage.Traverse()
            if prim.IsA(UsdPhysics.Joint) and not prim.IsPseudoRoot() and not prim.IsInstance()
        ]

        # Process deepest Xforms first so child transforms are baked before parents.
        xform_prims.sort(key=lambda prim: prim.GetPath().pathElementCount, reverse=True)

        for xform_prim in xform_prims:
            self._flatten_xform2mesh(xform_prim)

        root_path = Sdf.Path("/Root/Instance")
        if not xform_prim.GetPath() == root_path:
            self._reset_xform_ops(xform_prim, UsdGeom.Xformable(xform_prim))

        root_prim = stage.GetPrimAtPath(Sdf.Path("/Root/Instance"))
        # self._flatten_xform2joint(stage, root_prim, joint_prims)
        # self._reset_xform_ops(root_prim, UsdGeom.Xformable(root_prim))

        return True

    def _flatten_xform2mesh(self, xform_prim: Usd.Prim) -> None:
        xformable = UsdGeom.Xformable(xform_prim)
        local_matrix = self._get_local_matrix(xformable)

        translation, rotation, scale = decompose_matrix_to_trs(local_matrix)
        matrix_to_apply = (
            local_matrix
            if self.flatten_scale
            else self._remove_scale_from_matrix(local_matrix, scale)
        )

        for mesh_prim in self._iter_descendant_meshes(xform_prim):
            self._apply_transform_to_mesh(mesh_prim, matrix_to_apply)
            # break

        root_path = Sdf.Path("/Root/Instance")
        if not xform_prim.GetPath() == root_path:
            self._reset_xform_ops(xform_prim, xformable, scale)

    def _flatten_xform2joint(self, stage: Usd.Stage, xform_prim: Usd.Prim, joint_prims: list[Usd.Prim]) -> None:
        if not xform_prim.IsA(UsdGeom.Xform) or not xform_prim.IsValid():
            raise ValueError(f"xform_prim {xform_prim.GetPath()} is not a valid Xform prim")

        xform_path = xform_prim.GetPath()
        xform_matrix = self._get_world_matrix(UsdGeom.Xformable(xform_prim))

        for joint_prim in joint_prims:
            joint_path = joint_prim.GetPath()
            joint_str = str(joint_path)
            if not joint_str or not joint_str.startswith(str(xform_path)):
                raise ValueError(f"joint_prim {joint_prim.GetPath()} is not a valid joint prim")

            joint = UsdPhysics.Joint(joint_prim)
            rel_0 = joint.GetBody0Rel().GetTargets()[0]
            rel_1 = joint.GetBody1Rel().GetTargets()[0]
            rel_0_prim = stage.GetPrimAtPath(rel_0)
            rel_1_prim = stage.GetPrimAtPath(rel_1)

            world_transform_0 = self._get_world_matrix(UsdGeom.Xformable(rel_0_prim))
            world_transform_1 = self._get_world_matrix(UsdGeom.Xformable(rel_1_prim))

            local_pos_0 = joint.GetLocalPos0Attr().Get(Usd.TimeCode.Default())
            local_pos_1 = joint.GetLocalPos1Attr().Get(Usd.TimeCode.Default())
            local_rot_0 = joint.GetLocalRot0Attr().Get(Usd.TimeCode.Default())
            local_rot_1 = joint.GetLocalRot1Attr().Get(Usd.TimeCode.Default())
            # print(f"local_rot_0: {local_rot_0}, local_rot_1: {local_rot_1}")

            local_frame_0 = Gf.Matrix4d(1)
            local_frame_0.SetRotate(local_rot_0)
            local_frame_0.SetTranslateOnly(Gf.Vec3d(local_pos_0))
            world_frame_0 = local_frame_0 * world_transform_0  # Gf.Matrix4d
            # print(f"world_frame_0: {world_frame_0}\n \nlocal_frame_0: {local_frame_0} \n \nworld_transform_0: {world_transform_0}")

            translation_0, orientation_0, world_scale_0 = decompose_matrix_to_tos(world_frame_0)
            # print(f"translation_0: {translation_0}, rotation_0: {orientation_0}, world_scale_0: {world_scale_0}")

            local_frame_1 = Gf.Matrix4d(1)
            local_frame_1.SetRotate(local_rot_1)
            local_frame_1.SetTranslateOnly(Gf.Vec3d(local_pos_1))
            world_frame_1 = local_frame_1 * world_transform_1  # Gf.Matrix4d

            translation_1, orientation_1, world_scale_1 = decompose_matrix_to_tos(world_frame_1)
            # print(f"translation_1: {translation_1}, rotation_1: {orientation_1}, world_scale_1: {world_scale_1}")

            joint.GetLocalPos0Attr().Set(translation_0, Usd.TimeCode.Default())
            joint.GetLocalPos1Attr().Set(translation_1, Usd.TimeCode.Default())
            joint.GetLocalRot0Attr().Set(orientation_0, Usd.TimeCode.Default())
            joint.GetLocalRot1Attr().Set(orientation_1, Usd.TimeCode.Default())
            # joint local pos 0/1: Gf.Vec3d(point3f defined in usd prim but getattr returns Gf.Vec3d). Gf.Quatf
        return

    def _iter_descendant_meshes(self, prim: Usd.Prim) -> Iterable[Usd.Prim]:
        for descendant in Usd.PrimRange(prim):
            if descendant == prim:
                continue
            if descendant.IsInstance():
                continue
            if descendant.IsA(UsdGeom.Mesh):
                yield descendant

    def _apply_transform_to_mesh(self, mesh_prim: Usd.Prim, matrix: Gf.Matrix4d) -> None:
        mesh = UsdGeom.Mesh(mesh_prim)
        points_attr = mesh.GetPointsAttr()
        if not points_attr:
            return

        mesh_xformable = UsdGeom.Xformable(mesh_prim)
        mesh_local_matrix = self._get_local_matrix(mesh_xformable)
        _, _, mesh_scale = decompose_matrix_to_trs(mesh_local_matrix)

        if any(abs(component) < 1e-8 for component in mesh_scale):
            # Degenerate scale makes inversion unstable; fall back to parent matrix only.
            combined_matrix = matrix
        else:
            mesh_local_inverse = mesh_local_matrix.GetInverse()
            combined_matrix = matrix * mesh_local_matrix

        points = points_attr.Get(Usd.TimeCode.Default())
        if not points:
            return

        transformed_points = [
            Gf.Vec3f(combined_matrix.Transform(Gf.Vec3d(point)))
            for point in points
        ]
        transformed_array = Vt.Vec3fArray(transformed_points)
        points_attr.Set(transformed_array, Usd.TimeCode.Default())

        # print(f"✅successfully apply transform to mesh {mesh_prim.GetPath()}")
        point_based = UsdGeom.PointBased(mesh_prim)
        if point_based:
            extent = UsdGeom.PointBased.ComputeExtent(transformed_array)
            point_based.GetExtentAttr().Set(extent, Usd.TimeCode.Default())
            # print(f"✅successfully set extent for mesh {mesh_prim.GetPath()}")

        # After baking points, reset the mesh's own transform ops to identity.
        self._write_identity_ops(mesh_prim, mesh_xformable)

    def _reset_xform_ops(
        self,
        prim: Usd.Prim,
        xformable: UsdGeom.Xformable,
        original_scale: Gf.Vec3f | None = None,
    ) -> None:
        self._clear_existing_ops(prim, xformable)

        translate_op = xformable.AddTranslateOp()
        rotate_op = xformable.AddRotateXYZOp()
        scale_op = xformable.AddScaleOp()

        translate_op.Set(Gf.Vec3d(0.0), Usd.TimeCode.Default())
        rotate_op.Set(Gf.Vec3f(0.0), Usd.TimeCode.Default())

        if self.flatten_scale or original_scale is None:
            scale_value = Gf.Vec3f(1.0)
        else:
            scale_value = original_scale
        scale_op.Set(scale_value, Usd.TimeCode.Default())

    def _write_identity_ops(self, prim: Usd.Prim, xformable: UsdGeom.Xformable) -> None:
        self._reset_xform_ops(prim, xformable, Gf.Vec3f(1.0))

    def _get_local_matrix(self, xformable: UsdGeom.Xformable) -> Gf.Matrix4d:
        result = xformable.GetLocalTransformation(Usd.TimeCode.Default())
        if isinstance(result, tuple):
            return result[0]
        return result

    def _get_world_matrix(self, xformable: UsdGeom.Xformable) -> Gf.Matrix4d:
        if not xformable or not xformable.GetPrim().IsValid():
            raise ValueError("Invalid xformable provided for world matrix computation")

        xform_cache = UsdGeom.XformCache(Usd.TimeCode.Default())
        return xform_cache.GetLocalToWorldTransform(xformable.GetPrim())

    def _remove_scale_from_matrix(self, matrix: Gf.Matrix4d, scale: Gf.Vec3f) -> Gf.Matrix4d:
        scale_vec = Gf.Vec3d(scale)
        if any(abs(component) < 1e-8 for component in scale_vec):
            return matrix

        scale_matrix = Gf.Matrix4d(1.0)
        scale_matrix.SetScale(scale_vec)
        scale_inverse = scale_matrix.GetInverse()
        return matrix * scale_inverse

    def _is_identity_matrix(self, matrix: Gf.Matrix4d) -> bool:
        return Gf.IsClose(matrix, Gf.Matrix4d(1.0), 1e-8)

    def _clear_existing_ops(self, prim: Usd.Prim, xformable: UsdGeom.Xformable) -> None:
        xform_op_order = prim.GetAttribute("xformOpOrder")
        if not xform_op_order.Get():
            return
        for xform_op in xform_op_order.Get():
            prim.RemoveProperty(xform_op)

        xform_op_transform = prim.GetAttribute("xformOp:transform")
        if xform_op_transform.Get():
            prim.RemoveProperty("xformOp:transform")
        xformable.ClearXformOpOrder()
