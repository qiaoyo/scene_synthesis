import unittest

from scene_layout_rag.data_models import AssetDocument
from scene_layout_rag.template_layout import SelectedAsset, TemplateLayoutPlanner


class TemplateLayoutPlannerTests(unittest.TestCase):
    def test_normalizes_and_places(self):
        anchors = [
            AssetDocument(
                doc_id="a1",
                content="",
                metadata={
                    "md_kind": "referenced_xform",
                    "prim_path": "/World/Conveyor_Belt",
                    "payload": "../assets/Conveyor_Belt/Conveyor_Belt.usdc",
                    "bbox_world": {"center": [100.0, 0.0, 0.0], "size": [1.0, 1.0, 1.0]},
                },
            ),
            AssetDocument(
                doc_id="a2",
                content="",
                metadata={
                    "md_kind": "referenced_xform",
                    "prim_path": "/World/Workbench_2",
                    "payload": "../assets/Workbench_2/Workbench_2.usdc",
                    "bbox_world": {"center": [0.0, 50.0, 0.0], "size": [1.0, 1.0, 1.0]},
                },
            ),
        ]
        assets = [
            SelectedAsset(asset_id="Conveyor", usd_path="/x/Conveyor_Belt.usdc", scale=[1.0, 1.0, 1.0]),
            SelectedAsset(asset_id="Workbench", usd_path="/x/Workbench_2.usdc", scale=[0.01, 0.01, 0.01]),
        ]
        planner = TemplateLayoutPlanner(target_radius_xy=8.0)
        elements = planner.plan(assets, anchors)
        self.assertEqual(len(elements), 2)
        for e in elements:
            self.assertLessEqual(abs(e.transform["x"]), 8.0 + 1e-6)
            self.assertLessEqual(abs(e.transform["y"]), 8.0 + 1e-6)


if __name__ == "__main__":
    unittest.main()

