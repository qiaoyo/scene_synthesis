from __future__ import annotations

from typing import Any, Dict, List

from .data_models import SUPPORT_TYPE_SURFACE, SceneState
from .physics.isaac_bridge import IsaacBridgeError, run_isaac_operation


def _payload_error(payload: Dict[str, Any]) -> str:
    return payload.get("error") or "; ".join(payload.get("errors", [])) or "unknown Isaac error"


def observe_scene_with_isaac(config: Any, state: SceneState) -> Dict[str, Any]:
    errors: List[str] = []
    warnings: List[str] = []

    validation = {
        "backend": "isaacsim",
        "authoritative": False,
        "collision_free": None,
        "collision_count": None,
    }
    support_state = {
        "backend": "isaacsim",
        "authoritative": False,
        "checked_relation_count": 0,
        "valid_relation_count": 0,
        "invalid_relations": [],
    }
    physics_feedback = {
        "backend": "isaacsim",
        "authoritative": False,
        "stable": None,
        "fallen_assets": [],
    }

    try:
        payload = run_isaac_operation(
            config=config,
            operation="check_collision",
            scene=state,
            options={"include_suggestions": False},
        )
        warnings.extend(payload.get("warnings", []))
        if payload.get("ok"):
            collisions = payload.get("collisions", []) or []
            validation.update({
                "authoritative": True,
                "collision_free": payload.get("collision_free"),
                "collision_count": len(collisions),
            })
            if collisions:
                validation["collisions"] = collisions

        else:
            errors.append(f"check_collision: {_payload_error(payload)}")
    except IsaacBridgeError as exc:
        errors.append(f"check_collision: {exc}")

    for parent_id, children in state.support_children.items():
        if parent_id not in state.instances:
            continue

        for child_id in children:
            if child_id not in state.instances:
                continue

            support_state["checked_relation_count"] += 1
            support_type = state.support_relation_types.get(child_id, SUPPORT_TYPE_SURFACE)

            try:
                payload = run_isaac_operation(
                    config=config,
                    operation="check_support",
                    scene=state,
                    options={
                        "child_id": child_id,
                        "parent_id": parent_id,
                        "support_type": support_type,
                        "include_suggestions": False,
                    },
                )
                warnings.extend(payload.get("warnings", []))
            except IsaacBridgeError as exc:
                errors.append(f"check_support({child_id}, {parent_id}): {exc}")
                support_state["invalid_relations"].append({
                    "source": "isaacsim",
                    "child": child_id,
                    "parent": parent_id,
                    "support_type": support_type,
                    "issue": "isaac_check_failed",
                    "error": str(exc),
                })
                continue

            if not payload.get("ok"):
                err = _payload_error(payload)
                errors.append(f"check_support({child_id}, {parent_id}): {err}")
                support_state["invalid_relations"].append({
                    "source": "isaacsim",
                    "child": child_id,
                    "parent": parent_id,
                    "support_type": support_type,
                    "issue": "isaac_check_failed",
                    "error": err,
                })
                continue

            support = payload.get("support", {}) or {}
            if support.get("supported"):
                support_state["valid_relation_count"] += 1
            else:
                support_state["invalid_relations"].append({
                    "source": "isaacsim",
                    "child": support.get("child", child_id),
                    "parent": support.get("parent", parent_id),
                    "support_type": support.get("support_type", support_type),
                    "issue": "not_supported",
                    "issues": support.get("issues", []),
                })
    try:
        payload = run_isaac_operation(
            config=config,
            operation="simulate_step",
            scene=state,
            options={"duration": getattr(config, "physics_sim_duration", 2.0),},
        )
        warnings.extend(payload.get("warnings", []))
        if payload.get("ok"):
            stable = payload.get("stable")
            fallen_assets = payload.get("fallen_assets", []) or []

            physics_feedback.update({
                "authoritative": True,
                "stable": stable,
                "fallen_assets": fallen_assets,
            })
        else:
            errors.append(f"simulate_step: {_payload_error(payload)}")
    except IsaacBridgeError as exc:
        errors.append(f"simulate_step: {exc}")

    return {
        "ok": (
            not errors
            and validation["collision_free"] is True
            and not support_state["invalid_relations"]
            and physics_feedback["stable"] is True
        ),
        "validation": validation,
        "support_state": support_state,
        "physics_feedback": physics_feedback,
        "warnings": warnings,
        "error": "; ".join(errors) if errors else None,
    }
