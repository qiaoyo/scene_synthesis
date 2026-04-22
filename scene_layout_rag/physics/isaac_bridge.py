"""Isaac Sim bridge -- manages the SimulationApp lifecycle and USD stage.

IMPORTANT: Isaac Sim's SimulationApp must be created BEFORE any ``pxr``
imports.  This module handles that ordering internally.  Do NOT import
``pxr`` at the top of this file.
"""
from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple


class IsaacBridge:
    """Wraps Isaac Sim 5.1 for physics simulation inside the ReAct loop.

    Typical usage::

        bridge = IsaacBridge(headless=True, gpu_id=0)
        bridge.load_scene(scene_state)
        bridge.step(n_steps=120)       # 2 seconds at 60 Hz
        poses = bridge.get_all_poses()
        bridge.shutdown()
    """

    _instance: Optional["IsaacBridge"] = None

    def __init__(self, headless: bool = True, gpu_id: int = 0):
        os.environ.setdefault("CUDA_VISIBLE_DEVICES", str(gpu_id))

        # ── 1. Create SimulationApp (singleton) ──
        from isaacsim.simulation_app import SimulationApp
        self.app = SimulationApp({"headless": headless})

        # ── 2. NOW import pxr / omni (safe after app creation) ──
        import omni.usd
        from pxr import Gf, Sdf, Usd, UsdGeom, UsdPhysics, PhysxSchema
        from isaacsim.core.api import World
        from isaacsim.core.utils.stage import add_reference_to_stage

        self._omni_usd = omni.usd
        self._Usd = Usd
        self._UsdGeom = UsdGeom
        self._UsdPhysics = UsdPhysics
        self._PhysxSchema = PhysxSchema
        self._Gf = Gf
        self._Sdf = Sdf
        self._add_reference_to_stage = add_reference_to_stage

        # ── 3. Create World (physics context) ──
        self.world = World(
            physics_dt=1.0 / 60.0,
            rendering_dt=1.0 / 60.0,
            stage_units_in_meters=1.0,
        )
        self.stage = self._omni_usd.get_context().get_stage()

        # Set Z-up axis
        UsdGeom.SetStageUpAxis(self.stage, UsdGeom.Tokens.z)

        # Ensure a physics scene exists
        physics_scene_path = "/physicsScene"
        if not self.stage.GetPrimAtPath(physics_scene_path).IsValid():
            scene_prim = UsdPhysics.Scene.Define(self.stage, physics_scene_path)
            scene_prim.CreateGravityDirectionAttr().Set(Gf.Vec3f(0, 0, -1))
            scene_prim.CreateGravityMagnitudeAttr().Set(9.81)

        # Add ground plane
        self._add_ground_plane()

        self._prim_paths: Dict[str, str] = {}
        self._world_reset = False

        IsaacBridge._instance = self

    # ------------------------------------------------------------------
    # Scene loading
    # ------------------------------------------------------------------

    def load_scene(self, scene_state: Any) -> None:
        """Sync a :class:`SceneState` into the Isaac Sim stage."""
        Gf = self._Gf
        UsdGeom = self._UsdGeom
        UsdPhysics = self._UsdPhysics

        # Clear previous assets (keep ground plane and physics scene)
        world_prim = self.stage.GetPrimAtPath("/World")
        if world_prim.IsValid():
            for child in world_prim.GetChildren():
                path_str = str(child.GetPath())
                if path_str not in ("/World/GroundPlane",):
                    self.stage.RemovePrim(child.GetPath())

        self._prim_paths.clear()

        for asset in scene_state.assets.values():
            prim_path = f"/World/{asset.instance_id}"
            self._prim_paths[asset.instance_id] = prim_path

            # Add USD reference
            self._add_reference_to_stage(
                usd_path=asset.usd_path,
                prim_path=prim_path,
            )

            prim = self.stage.GetPrimAtPath(prim_path)
            if not prim.IsValid():
                continue

            # Apply physics APIs
            if not prim.HasAPI(UsdPhysics.RigidBodyAPI):
                UsdPhysics.RigidBodyAPI.Apply(prim)
            if not prim.HasAPI(UsdPhysics.CollisionAPI):
                UsdPhysics.CollisionAPI.Apply(prim)
            if not prim.HasAPI(UsdPhysics.MassAPI):
                mass_api = UsdPhysics.MassAPI.Apply(prim)
                mass_api.CreateMassAttr(10.0)

            # Set transform
            xform = UsdGeom.Xformable(prim)
            xform.ClearXformOpOrder()

            # Handle up-axis alignment (reuse pattern from scene.py)
            temp_stage = self._Usd.Stage.Open(asset.usd_path)
            up_axis = UsdGeom.GetStageUpAxis(temp_stage)
            align_euler = (0.0, 0.0, 0.0)
            if up_axis == UsdGeom.Tokens.y:
                align_euler = (90.0, 0.0, 0.0)
            elif up_axis == UsdGeom.Tokens.x:
                align_euler = (0.0, -90.0, 0.0)

            # Compose alignment + user rotation → quaternion
            align_rot = Gf.Rotation(Gf.Vec3d(1, 0, 0), align_euler[0])
            align_rot = align_rot * Gf.Rotation(Gf.Vec3d(0, 1, 0), align_euler[1])
            align_rot = align_rot * Gf.Rotation(Gf.Vec3d(0, 0, 1), align_euler[2])

            user_rot = Gf.Rotation(Gf.Vec3d(1, 0, 0), asset.rotation[0])
            user_rot = user_rot * Gf.Rotation(Gf.Vec3d(0, 1, 0), asset.rotation[1])
            user_rot = user_rot * Gf.Rotation(Gf.Vec3d(0, 0, 1), asset.rotation[2])

            final_quat = user_rot.GetQuat() * align_rot.GetQuat()

            translate_op = xform.AddTranslateOp()
            translate_op.Set(Gf.Vec3d(*asset.position))

            scale_op = xform.AddScaleOp()
            scale_op.Set(Gf.Vec3f(0.01, 0.01, 0.01))

            orient_op = xform.AddOrientOp()
            orient_op.Set(Gf.Quatf(
                final_quat.GetReal(),
                Gf.Vec3f(*final_quat.GetImaginary()),
            ))

        self._world_reset = False

    # ------------------------------------------------------------------
    # Simulation
    # ------------------------------------------------------------------

    def step(self, n_steps: int = 60) -> None:
        """Advance the physics simulation by *n_steps* frames."""
        if not self._world_reset:
            self.world.reset()
            self._world_reset = True
        for _ in range(n_steps):
            self.world.step(render=False)

    # ------------------------------------------------------------------
    # Pose queries
    # ------------------------------------------------------------------

    def get_all_poses(self) -> Dict[str, Tuple[tuple, tuple]]:
        """Return ``{instance_id: (position, orientation)}`` for all loaded prims."""
        from isaacsim.core.prims import SingleXFormPrim
        poses: Dict[str, Tuple[tuple, tuple]] = {}
        for instance_id, prim_path in self._prim_paths.items():
            try:
                xform = SingleXFormPrim(prim_path=prim_path)
                xform.initialize()
                pos, orient = xform.get_world_pose()
                poses[instance_id] = (tuple(pos), tuple(orient))
            except Exception:
                poses[instance_id] = ((0, 0, 0), (1, 0, 0, 0))
        return poses

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def shutdown(self) -> None:
        if self.app is not None:
            self.app.close()
            self.app = None

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _add_ground_plane(self) -> None:
        """Add an invisible ground plane at z=0 for physics support."""
        UsdGeom = self._UsdGeom
        UsdPhysics = self._UsdPhysics
        Gf = self._Gf

        plane_path = "/World/GroundPlane"
        if self.stage.GetPrimAtPath(plane_path).IsValid():
            return

        plane_prim = UsdGeom.Xform.Define(self.stage, plane_path)
        cube = UsdGeom.Cube.Define(self.stage, f"{plane_path}/Collision")
        cube.CreateSizeAttr(1.0)

        xform = UsdGeom.Xformable(cube.GetPrim())
        xform.AddTranslateOp().Set(Gf.Vec3d(0, 0, -0.5))
        xform.AddScaleOp().Set(Gf.Vec3f(100, 100, 1.0))

        UsdPhysics.CollisionAPI.Apply(cube.GetPrim())


__all__ = ["IsaacBridge"]
