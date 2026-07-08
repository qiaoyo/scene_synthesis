from __future__ import annotations

import sys
import unittest
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LORA_SCRIPT_DIR = PROJECT_ROOT / "scripts" / "lora"
if str(LORA_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(LORA_SCRIPT_DIR))

from train_qwen35_multimodal_toolcall_lora import (  # noqa: E402
    build_loss_weight_vectors,
    compute_role_weights,
    role_for_tool_names,
    weighted_loss_average,
)


class LoraLossModeTests(unittest.TestCase):
    def test_role_for_tool_names_matches_tca_buckets(self) -> None:
        self.assertEqual(role_for_tool_names([]), "final")
        self.assertEqual(role_for_tool_names(["retrieve_asset"]), "plan")
        self.assertEqual(role_for_tool_names(["place_instance"]), "plan")
        self.assertEqual(role_for_tool_names(["save_scene_usd"]), "termination")
        self.assertEqual(role_for_tool_names(["check_support"]), "correction")

    def test_loss_weight_vectors_cover_three_modes(self) -> None:
        prompt = "prompt "
        target = "<tool_call><function=save_scene_usd></function></tool_call>"
        full_text = prompt + target
        spans = [(index, index + 1) for index in range(len(full_text))]
        kwargs = {
            "full_text": full_text,
            "prompt_text": prompt,
            "token_count": len(full_text),
            "token_spans": spans,
            "prompt_len": len(prompt),
            "tool_names": ["save_scene_usd"],
            "tca_loss_weight": 3.0,
        }
        name_start = full_text.index("save_scene_usd")

        plain_weights, plain_denominator = build_loss_weight_vectors(
            **kwargs,
            loss_mode="plain",
            role_weight=2.0,
        )
        self.assertEqual(max(plain_weights), 1.0)
        self.assertEqual(max(plain_denominator), 1.0)

        tool_weights, tool_denominator = build_loss_weight_vectors(
            **kwargs,
            loss_mode="toolcall",
            role_weight=2.0,
        )
        self.assertEqual(tool_weights[name_start], 3.0)
        self.assertEqual(tool_denominator[name_start], 3.0)

        role_weights, role_denominator = build_loss_weight_vectors(
            **kwargs,
            loss_mode="role_aware",
            role_weight=2.0,
        )
        self.assertEqual(role_weights[name_start], 6.0)
        self.assertEqual(role_denominator[name_start], 3.0)

    def test_role_weights_normalize_train_set_mean(self) -> None:
        counts = {
            "plan": 2,
            "correction": 8,
            "termination": 1,
            "final": 0,
        }
        weights = compute_role_weights(counts, alpha=1.0, normalize=True)
        weighted_mean = sum(
            weights[role] * count
            for role, count in counts.items()
        ) / sum(counts.values())
        self.assertAlmostEqual(weighted_mean, 1.0)
        self.assertGreater(weights["termination"], weights["plan"])
        self.assertGreater(weights["plan"], weights["correction"])

    def test_role_weight_is_not_canceled_in_single_item_batch(self) -> None:
        loss = weighted_loss_average(
            torch.tensor([2.0]),
            torch.tensor([3.0]),
            torch.tensor([1.0]),
        )
        self.assertEqual(float(loss), 6.0)


if __name__ == "__main__":
    unittest.main()
