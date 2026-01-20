import unittest

from scene_layout_rag.react_agent import SceneLayoutReActAgent


class _DummyRag:
    pass


class ReActAgentTests(unittest.TestCase):
    def test_detect_scene_type_keywords(self):
        agent = SceneLayoutReActAgent(_DummyRag())
        self.assertEqual(agent._tool_detect_scene_type("在仓库里放置货架和托盘"), "warehouse")
        self.assertEqual(agent._tool_detect_scene_type("装配线增加工位和工业机器人"), "assembly")
        self.assertEqual(agent._tool_detect_scene_type("分拣中心增加传送带和扫码台"), "sorting")


if __name__ == "__main__":
    unittest.main()

