"""Physics simulation integration (optional -- requires Isaac Sim 5.1)."""
from __future__ import annotations

ISAAC_AVAILABLE: bool = False

try:
    # Guard: only set True if the simulation app can be imported.
    # The actual SimulationApp is NOT created here -- that happens
    # inside IsaacBridge.__init__() because it must be a singleton
    # and requires specific GPU/headless settings.
    from isaacsim.simulation_app import SimulationApp as _SimApp  # noqa: F401
    ISAAC_AVAILABLE = True
except ImportError:
    pass

# Lazy imports -- avoid importing pxr at module level
if ISAAC_AVAILABLE:
    from .physics_validator import PhysicsValidator
else:
    PhysicsValidator = None  # type: ignore[assignment,misc]

__all__ = ["ISAAC_AVAILABLE", "PhysicsValidator"]
