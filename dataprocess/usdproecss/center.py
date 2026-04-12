from __future__ import annotations
from typing import List, Tuple
from core.simple_base import USDProcessingContext, USDProcessor
from pxr import Gf, Usd, UsdGeom, UsdPhysics, Vt


class CenterChecker(USDProcessor):
    """move the asset so its meshes are centered around the origin."""
    def __init__(self) -> None:
        super().__init__(name="CenterChecker", description="recenter all meshes to their combined midpoint")

    def process(self, context: USDProcessingContext) -> bool:
        stage = context.stage
        time = Usd.TimeCode.Default()

        mesh_prims = [prim for prim in stage.Traverse() if prim.IsA(UsdGeom.Mesh) and not prim.IsInstance()]
        print(f"[CenterChecker] found {len(mesh_prims)} mesh prims")
        if not mesh_prims:
            return True

        mesh_data: List[Tuple[Usd.Prim, Vt.Vec3fArray, Gf.Matrix4d]] = []
        world_bounds = Gf.Range3d()

        for mesh_primin in mesh_prims:
            mesh = UsdGeom.Mesh(mesh_primin)
            points_attr = mesh.GetPointsAttr()
            if not points_attr:
                continue

            points = points_attr.Get(time)
            if not points or len(points) == 0:
                continue

            xformable = UsdGeom.Xformable(mesh_primin)
            local_to_world = xformable.ComputeLocalToWorldTransform(time)
            local_range = Gf.Range3d()
            for point in points:
                world_point = local_to_world.Transform(Gf.Vec3d(point))
                local_range.UnionWith(world_point)
            if local_range.IsEmpty():
                continue

            world_bounds.UnionWith(local_range)
            mesh_data.append((mesh_primin, points, local_to_world))

        print(f"[CenterChecker] mesh_data:{len(mesh_data)}")
        if world_bounds.IsEmpty():
            return True

        center = world_bounds.GetMidpoint()
        print(f"[CenterChecker] computed center at {center}")
        self._recenter_joint_local_positions(stage, center, time)
        for mesh_primin, original_points, local_to_world in mesh_data:
            self._recenter_mesh(mesh_primin, original_points, local_to_world, center, time)
        return True

    def _recenter_mesh(
        self,
        prim: Usd.Prim,
        points: Vt.Vec3fArray,
        local_to_world: Gf.Matrix4d,
        center: Gf.Vec3d,
        time: Usd.TimeCode,
    ) -> None:
        mesh = UsdGeom.Mesh(prim)
        world_to_local = local_to_world.GetInverse()
        delta_local = world_to_local.TransformDir(center)
        new_points = [
            Gf.Vec3f(Gf.Vec3d(point) - delta_local)
            for point in points
        ]
        new_points_array = Vt.Vec3fArray(new_points)
        mesh.GetPointsAttr().Set(new_points_array, time)

        point_based = UsdGeom.PointBased(prim)
        if point_based:
            extent = UsdGeom.PointBased.ComputeExtent(new_points_array)
            point_based.GetExtentAttr().Set(extent, time)

    def _recenter_joint_local_positions(
        self,
        stage: Usd.Stage,
        center: Gf.Vec3d,
        time: Usd.TimeCode,
    ) -> None:
        joint_prims = [
            prim
            for prim in stage.Traverse()
            if prim.IsA(UsdPhysics.Joint) and not prim.IsInstance()
        ]
        if not joint_prims:
            return
        for joint_primin in joint_prims:
            joint = UsdPhysics.Joint(joint_primin)
            self._offset_joint_anchor(stage, joint, center, time, anchor_index=0)
            self._offset_joint_anchor(stage, joint, center, time, anchor_index=1)

    def _offset_joint_anchor(
        self,
        stage: Usd.Stage,
        joint: UsdPhysics.Joint,
        center: Gf.Vec3d,
        time: Usd.TimeCode,
        anchor_index: int,
    ) -> None:
        if anchor_index == 0:
            rel = joint.GetBody0Rel()
            pos_attr = joint.GetLocalPos0Attr()
        else:
            rel = joint.GetBody1Rel()
            pos_attr = joint.GetLocalPos1Attr()

        if not rel or not pos_attr or not pos_attr.HasAuthoredValue():
            return
        targets = rel.GetTargets()
        if not targets:
            return
        body_primin = stage.GetPrimAtPath(targets[0])
        if not body_primin or not body_primin.IsValid():
            return

        xformable = UsdGeom.Xformable(body_primin)
        if not xformable or not xformable.GetPrim().IsValid():
            return

        local_to_world = xformable.ComputeLocalToWorldTransform(time)
        world_to_local = local_to_world.GetInverse()
        delta_local = world_to_local.TransformDir(center)
        current_pos = pos_attr.Get(time)
        if current_pos is None:
            return

        # print(f"center: {center}, current_pos: {current_pos}, delta_local: {delta_local}")
        updated_pos = Gf.Vec3f(Gf.Vec3d(current_pos) - delta_local)
        pos_attr.Set(updated_pos, time)
