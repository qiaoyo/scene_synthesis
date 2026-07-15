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
    compute_tool_weights_by_role,
    compute_role_weights,
    count_tools_by_role,
    role_for_tool_names,
    tokenize_record,
    weighted_loss_average,
)


class LoraLossModeTests(unittest.TestCase):
    def test_role_for_tool_names_matches_tca_buckets(self) -> None:
        self.assertEqual(role_for_tool_names([]), "final")
        self.assertEqual(role_for_tool_names(["retrieve_asset"]), "plan")
        self.assertEqual(role_for_tool_names(["place_instance"]), "plan")
        self.assertEqual(role_for_tool_names(["save_scene_usd"]), "termination")
        self.assertEqual(role_for_tool_names(["check_support"]), "correction")

    def test_loss_weight_vectors_cover_four_modes(self) -> None:
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

        for legacy_mode, expected_name_weight in (
            ("plain", 1.0),
            ("toolcall", 3.0),
            ("role_aware", 6.0),
        ):
            legacy_weights, _ = build_loss_weight_vectors(
                **kwargs,
                loss_mode=legacy_mode,
                role_weight=2.0,
                tool_name_weights={"save_scene_usd": 10.0},
            )
            self.assertEqual(legacy_weights[name_start], expected_name_weight)

        combined_weights, combined_denominator = build_loss_weight_vectors(
            **kwargs,
            loss_mode="tool_role_aware",
            role_weight=2.0,
            tool_name_weights={"save_scene_usd": 1.5},
        )
        self.assertEqual(combined_weights[name_start], 9.0)
        self.assertEqual(combined_denominator[name_start], 4.5)

    def test_combined_mode_applies_distinct_tool_name_weights(self) -> None:
        prompt = "prompt "
        target = (
            "<tool_call><function=check_support></function></tool_call>"
            "<tool_call><function=simulate_step></function></tool_call>"
        )
        full_text = prompt + target
        spans = [(index, index + 1) for index in range(len(full_text))]
        loss_weights, denominator_weights = build_loss_weight_vectors(
            full_text=full_text,
            prompt_text=prompt,
            token_count=len(full_text),
            token_spans=spans,
            prompt_len=len(prompt),
            tool_names=["check_support", "simulate_step"],
            tca_loss_weight=3.0,
            loss_mode="tool_role_aware",
            role_weight=2.0,
            tool_name_weights={
                "check_support": 0.5,
                "simulate_step": 1.5,
            },
        )
        check_start = full_text.index("check_support")
        simulate_start = full_text.index("simulate_step")
        self.assertEqual(loss_weights[check_start], 3.0)
        self.assertEqual(denominator_weights[check_start], 1.5)
        self.assertEqual(loss_weights[simulate_start], 9.0)
        self.assertEqual(denominator_weights[simulate_start], 4.5)
        self.assertEqual(loss_weights[len(prompt)], 2.0)
        self.assertEqual(denominator_weights[len(prompt)], 1.0)

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

    def test_tool_counts_include_repeated_calls_within_role(self) -> None:
        def record(*tool_names: str) -> dict[str, object]:
            return {
                "messages": [
                    {"role": "user", "content": "next"},
                    {
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [
                            {
                                "type": "function",
                                "function": {
                                    "name": tool_name,
                                    "arguments": {},
                                },
                            }
                            for tool_name in tool_names
                        ],
                    },
                ]
            }

        counts = count_tools_by_role(
            [
                record("place_instance", "place_instance"),
                record("retrieve_asset"),
                record("check_support"),
            ]
        )
        self.assertEqual(counts["plan"]["place_instance"], 2)
        self.assertEqual(counts["plan"]["retrieve_asset"], 1)
        self.assertEqual(counts["correction"]["check_support"], 1)
        self.assertEqual(counts["termination"], {})

    def test_tool_weights_normalize_each_role_call_weighted_mean(self) -> None:
        counts = {
            "plan": {"place_instance": 4, "retrieve_asset": 1},
            "correction": {"check_support": 8, "simulate_step": 2},
            "termination": {"save_scene_usd": 3},
            "final": {},
        }
        weights = compute_tool_weights_by_role(
            counts,
            alpha=0.5,
            normalize=True,
        )
        for role, role_counts in counts.items():
            if not role_counts:
                self.assertEqual(weights[role], {})
                continue
            total = sum(role_counts.values())
            weighted_mean = sum(
                weights[role][tool_name] * count
                for tool_name, count in role_counts.items()
            ) / total
            self.assertAlmostEqual(weighted_mean, 1.0)
        self.assertGreater(
            weights["plan"]["retrieve_asset"],
            weights["plan"]["place_instance"],
        )
        self.assertGreater(
            weights["correction"]["simulate_step"],
            weights["correction"]["check_support"],
        )
        self.assertEqual(weights["termination"]["save_scene_usd"], 1.0)

    def test_combined_mode_applies_role_weight_to_eos(self) -> None:
        class FakeTokenizer:
            eos_token_id = 999

            def __call__(
                self,
                text: str,
                *,
                add_special_tokens: bool,
                return_offsets_mapping: bool = False,
            ) -> dict[str, object]:
                encoded: dict[str, object] = {
                    "input_ids": list(range(len(text))),
                }
                if return_offsets_mapping:
                    encoded["offset_mapping"] = [
                        (index, index + 1)
                        for index in range(len(text))
                    ]
                return encoded

        class FakeProcessor:
            tokenizer = FakeTokenizer()

            def apply_chat_template(
                self,
                messages: list[dict[str, object]],
                *,
                tokenize: bool,
                add_generation_prompt: bool,
                tools: list[dict[str, object]] | None,
                enable_thinking: bool,
            ) -> str:
                if add_generation_prompt:
                    return "prompt "
                return "prompt <tool_call><function=save_scene_usd></function></tool_call>"

        record = {
            "messages": [
                {"role": "user", "content": "save"},
                {
                    "role": "assistant",
                    "content": "",
                    "tool_calls": [
                        {
                            "type": "function",
                            "function": {
                                "name": "save_scene_usd",
                                "arguments": {},
                            },
                        }
                    ],
                },
            ]
        }
        tokenized = tokenize_record(
            record,
            FakeProcessor(),
            max_length=512,
            tca_loss_weight=3.0,
            loss_mode="tool_role_aware",
            role_weight=2.0,
            tool_name_weights={"save_scene_usd": 1.5},
        )
        self.assertEqual(tokenized["loss_weights"][-1], 2.0)
        self.assertEqual(tokenized["normalizer_weights"][-1], 1.0)


if __name__ == "__main__":
    unittest.main()
