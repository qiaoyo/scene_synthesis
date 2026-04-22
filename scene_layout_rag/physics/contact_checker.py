"""Contact sensor management for Isaac Sim physics feedback."""
from __future__ import annotations

from typing import Any, Dict, List

from .isaac_bridge import IsaacBridge


class ContactChecker:
    """Creates contact sensors on loaded prims and reads contact data.

    Requires an active :class:`IsaacBridge` with a loaded scene.
    Uses ``isaacsim.sensors.physics.ContactSensor`` (Isaac Sim 5.1 API).
    """

    def __init__(self, bridge: IsaacBridge):
        self.bridge = bridge
        self._sensors: Dict[str, Any] = {}

    def setup_sensors(self) -> None:
        """Attach a ``ContactSensor`` to every physics-enabled prim."""
        from isaacsim.sensors.physics import ContactSensor
        from pxr import UsdPhysics

        stage = self.bridge.stage
        for instance_id, prim_path in self.bridge._prim_paths.items():
            prim = stage.GetPrimAtPath(prim_path)
            if not prim.IsValid():
                continue
            if not prim.HasAPI(UsdPhysics.CollisionAPI):
                continue

            sensor_path = f"{prim_path}/contact_sensor"
            try:
                sensor = ContactSensor(
                    prim_path=sensor_path,
                    name=f"{instance_id}_sensor",
                    min_threshold=0,
                    max_threshold=100000,
                )
                sensor.initialize()
                self._sensors[instance_id] = sensor
            except Exception as exc:
                print(f"[ContactChecker] Failed to create sensor for {instance_id}: {exc}")

    def get_contacts(self) -> List[Dict[str, Any]]:
        """Read current contact data from all sensors."""
        contacts: List[Dict[str, Any]] = []
        for instance_id, sensor in self._sensors.items():
            try:
                frame = sensor.get_current_frame()
                if frame.get("in_contact", False):
                    contacts.append({
                        "instance_id": instance_id,
                        "in_contact": True,
                        "force": float(frame.get("force", 0)),
                        "number_of_contacts": int(frame.get("number_of_contacts", 0)),
                    })
            except Exception:
                pass
        return contacts


__all__ = ["ContactChecker"]
