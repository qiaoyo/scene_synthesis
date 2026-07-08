from __future__ import annotations

import unittest

from scene_layout_react.data_models import (
    SUPPORT_TYPE_CONTAINER_INNER,
    SUPPORT_TYPE_SURFACE,
    Instance,
    SceneState,
)
from scene_layout_react.physics.container_inner_support import (
    run_container_inner_support_check,
)
from scene_layout_react.physics.physx_contact_checks import is_valid_support_contact
from scene_layout_react.scene_state import SceneStateManager


class TypedSupportStateTests(unittest.TestCase):
    def test_old_scene_defaults_support_type_to_surface(self) -> None:
        state = SceneState.from_dict({
            "instances": {
                "Box.a": {
                    "instance_id": "Box.a",
                    "asset_type": "Box",
                    "asset_doc_id": "box-doc",
                    "usd_path": "box.usd",
                },
                "Part.a": {
                    "instance_id": "Part.a",
                    "asset_type": "IndustrialPart",
                    "asset_doc_id": "part-doc",
                    "usd_path": "part.usd",
                    "parent_instance_id": "Box.a",
                },
            },
            "support_children": {"Box.a": ["Part.a"]},
        })

        self.assertEqual(
            state.support_relation_types,
            {"Part.a": SUPPORT_TYPE_SURFACE},
        )

    def test_container_inner_serializes_and_clears(self) -> None:
        manager = _scene_manager()
        manager.set_support(
            "Part.a",
            "Box.a",
            support_type=SUPPORT_TYPE_CONTAINER_INNER,
        )

        payload = manager.to_dict()
        self.assertEqual(
            payload["support_relation_types"]["Part.a"],
            SUPPORT_TYPE_CONTAINER_INNER,
        )

        roundtrip = SceneStateManager.from_dict(payload)
        self.assertEqual(
            roundtrip.state.support_relation_types["Part.a"],
            SUPPORT_TYPE_CONTAINER_INNER,
        )

        roundtrip.clear_support("Part.a")
        self.assertNotIn("Part.a", roundtrip.state.support_relation_types)

    def test_delete_cleans_child_support_type(self) -> None:
        manager = _scene_manager()
        manager.set_support(
            "Part.a",
            "Box.a",
            support_type=SUPPORT_TYPE_CONTAINER_INNER,
        )

        manager.delete("Box.a")

        self.assertNotIn("Part.a", manager.state.support_relation_types)
        self.assertIsNone(manager.state.instances["Part.a"].parent_instance_id)


class ContainerInnerSupportTests(unittest.TestCase):
    def test_open_box_inner_bottom_passes(self) -> None:
        support = run_container_inner_support_check(
            scene=_scene_payload(),
            bboxes=_valid_bboxes(),
            child_id="Part.a",
            parent_id="Box.a",
        )

        self.assertTrue(support["supported"], support)
        self.assertEqual(support["support_backend"], "container_inner_bbox")

    def test_outside_xy_fails(self) -> None:
        bboxes = _valid_bboxes()
        bboxes["Part.a"] = {
            "min": [0.0, 0.20, 0.01],
            "max": [0.15, 0.35, 0.20],
        }

        support = run_container_inner_support_check(
            scene=_scene_payload(),
            bboxes=bboxes,
            child_id="Part.a",
            parent_id="Box.a",
        )

        self.assertFalse(support["supported"], support)

    def test_above_rim_fails(self) -> None:
        bboxes = _valid_bboxes()
        bboxes["Part.a"] = {
            "min": [0.20, 0.20, 0.01],
            "max": [0.35, 0.35, 1.20],
        }

        support = run_container_inner_support_check(
            scene=_scene_payload(),
            bboxes=bboxes,
            child_id="Part.a",
            parent_id="Box.a",
        )

        self.assertFalse(support["supported"], support)

    def test_container_inner_contact_counts_as_support(self) -> None:
        self.assertTrue(
            is_valid_support_contact(
                _scene_payload(),
                _valid_bboxes(),
                "Part.a",
                "Box.a",
            )
        )


def _scene_manager() -> SceneStateManager:
    manager = SceneStateManager()
    manager.add_instance(
        Instance(
            "Box.a",
            "Box",
            "box-doc",
            "box.usd",
            tags={"Colsure": "Open"},
            description="open plastic storage bin",
        )
    )
    manager.add_instance(
        Instance(
            "Part.a",
            "IndustrialPart",
            "part-doc",
            "part.usd",
        )
    )
    return manager


def _scene_payload() -> dict:
    manager = _scene_manager()
    manager.set_support(
        "Part.a",
        "Box.a",
        support_type=SUPPORT_TYPE_CONTAINER_INNER,
    )
    return manager.to_dict()


def _valid_bboxes() -> dict:
    return {
        "Box.a": {"min": [0.0, 0.0, 0.0], "max": [1.0, 1.0, 1.0]},
        "Part.a": {"min": [0.20, 0.20, 0.01], "max": [0.35, 0.35, 0.20]},
    }


if __name__ == "__main__":
    unittest.main()
