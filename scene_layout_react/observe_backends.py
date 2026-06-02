from __future__ import annotations

from typing import Any, Dict, List

from .data_models import SceneState
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
        "collisions": [],
        "suggested_move": None,
        "suggested_moves": [],
        "suggested_final_positions": {},
    }
    support_state = {
        "backend": "isaacsim",
        "authoritative": False,
        "valid_relations": [],
        "invalid_relations": [],
    }
    physics_feedback = {
        "backend": "isaacsim",
        "authoritative": False,
        "stable": None,
        "fallen_assets": [],
        "contacts": [],
        "final_positions": {},
    }

    try:
        payload = run_isaac_operation(
            config=config,
            operation="check_collision",
            scene=state,
        )
        warnings.extend(payload.get("warnings", []))
        if payload.get("ok"):
            validation.update({
                "authoritative": True,
                "collision_free": payload.get("collision_free"),
                "collisions": payload.get("collisions", []),
                "suggested_final_positions": payload.get("suggested_final_positions", {}),
            })
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

            try:
                payload = run_isaac_operation(
                    config=config,
                    operation="check_support",
                    scene=state,
                    options={"child_id": child_id, "parent_id": parent_id},
                )
                warnings.extend(payload.get("warnings", []))
            except IsaacBridgeError as exc:
                errors.append(f"check_support({child_id}, {parent_id}): {exc}")
                support_state["invalid_relations"].append({
                    "child": child_id,
                    "parent": parent_id,
                    "issue": "isaac_check_failed",
                    "error": str(exc),
                })
                continue

            if not payload.get("ok"):
                err = _payload_error(payload)
                errors.append(f"check_support({child_id}, {parent_id}): {err}")
                support_state["invalid_relations"].append({
                    "child": child_id,
                    "parent": parent_id,
                    "issue": "isaac_check_failed",
                    "error": err,
                    "suggested_move": payload.get("suggested_move"),
                })
                continue

            support_state["authoritative"] = True
            relation = {
                "child": child_id,
                "parent": parent_id,
                "contacts": payload.get("contacts", []),
                "z_gap": payload.get("z_gap"),
                "xy_coverage": payload.get("xy_coverage"),
            }

            if payload.get("supported"):
                support_state["valid_relations"].append(relation)
            else:
                relation["issue"] = "not_supported"
                relation["issues"] = payload.get("issues", [])
                relation["suggested_move"] = payload.get("suggested_move")
                support_state["invalid_relations"].append(relation)
    try:
        payload = run_isaac_operation(
            config=config,
            operation="simulate_step",
            scene=state,
            options={"duration": getattr(config, "physics_sim_duration", 2.0)},
        )
        warnings.extend(payload.get("warnings", []))
        if payload.get("ok"):
            physics_feedback.update({
                "authoritative": True,
                "stable": payload.get("stable"),
                "fallen_assets": payload.get("fallen_assets", []),
                "contacts": payload.get("contacts", []),
                "final_positions": payload.get("final_positions", {}),
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
