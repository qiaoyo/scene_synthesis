"""High-level physics validation -- orchestrates IsaacBridge + ContactChecker."""
from __future__ import annotations

import math
from typing import Any, Dict, List, Tuple

from .isaac_bridge import IsaacBridge
from .contact_checker import ContactChecker


# Displacement threshold: if an asset moves more than this (metres)
# during simulation it is classified as *fallen / unstable*.
_DISPLACEMENT_THRESHOLD = 0.1


class PhysicsValidator:
    """Run a short physics simulation and report stability / contacts.

    Creates an :class:`IsaacBridge` on first use (or reuses the
    singleton). This keeps the heavy SimulationApp alive across
    multiple validation calls.

    Returns a dict compatible with the ``physics_feedback`` slot
    in the observer's observation report.
    """

    def __init__(self, headless: bool = True, gpu_id: int = 0):
        self._headless = headless
        self._gpu_id = gpu_id
        self._bridge: IsaacBridge | None = None

    def _get_bridge(self) -> IsaacBridge:
        if self._bridge is None:
            if IsaacBridge._instance is not None:
                self._bridge = IsaacBridge._instance
            else:
                self._bridge = IsaacBridge(
                    headless=self._headless,
                    gpu_id=self._gpu_id,
                )
        return self._bridge

    def validate(
        self,
        scene_state: Any,
        duration: float = 2.0,
    ) -> Dict[str, Any]:
        """Load *scene_state*, simulate for *duration* seconds, and report.

        Returns::

            {
                "physics_available": True,
                "stable": bool,
                "stable_assets": [str, ...],
                "fallen_assets": [str, ...],
                "contacts": [...],
                "warnings": [str, ...],
            }
        """
        bridge = self._get_bridge()
        bridge.load_scene(scene_state)

        # Snapshot initial positions
        initial_poses = bridge.get_all_poses()

        # Set up contact sensors
        checker = ContactChecker(bridge)
        checker.setup_sensors()

        # Run simulation
        n_steps = max(1, int(duration * 60))
        bridge.step(n_steps=n_steps)

        # Read final state
        final_poses = bridge.get_all_poses()
        contacts = checker.get_contacts()

        # Classify stability
        stable_assets: List[str] = []
        fallen_assets: List[str] = []
        warnings: List[str] = []

        for instance_id in initial_poses:
            init_pos = initial_poses[instance_id][0]
            final_pos = final_poses.get(instance_id, ((0, 0, 0), (1, 0, 0, 0)))[0]
            displacement = math.sqrt(sum(
                (final_pos[i] - init_pos[i]) ** 2 for i in range(3)
            ))
            if displacement > _DISPLACEMENT_THRESHOLD:
                fallen_assets.append(instance_id)
                warnings.append(
                    f"{instance_id} 位移 {displacement:.3f}m (阈值 {_DISPLACEMENT_THRESHOLD}m)，"
                    f"判定为不稳定"
                )
            else:
                stable_assets.append(instance_id)

        return {
            "physics_available": True,
            "stable": len(fallen_assets) == 0,
            "stable_assets": stable_assets,
            "fallen_assets": fallen_assets,
            "contacts": contacts,
            "warnings": warnings,
        }


__all__ = ["PhysicsValidator"]
