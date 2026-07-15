from __future__ import annotations

import unittest

from dataprocess.bbox_coordinates import normalize_bbox_to_z_up_meters


class NormalizeBBoxToZUpMetersTests(unittest.TestCase):
    def assertPointAlmostEqual(self, actual, expected) -> None:
        self.assertEqual(len(actual), len(expected))
        for actual_value, expected_value in zip(actual, expected):
            self.assertAlmostEqual(actual_value, expected_value, places=12)

    def test_z_up_only_scales_to_meters(self) -> None:
        bbox_min, bbox_max = normalize_bbox_to_z_up_meters(
            ((-60.0, -40.0, 0.0), (60.0, 40.0, 20.0)),
            source_up_axis="Z",
            meters_per_unit=0.01,
        )

        self.assertPointAlmostEqual(bbox_min, (-0.6, -0.4, 0.0))
        self.assertPointAlmostEqual(bbox_max, (0.6, 0.4, 0.2))

    def test_y_up_rack_matches_runtime_z_up_bbox(self) -> None:
        bbox_min, bbox_max = normalize_bbox_to_z_up_meters(
            (
                (-149.9865871322951, -150.00058448935663, -36.43336965695829),
                (149.98658713239936, 149.99939182849224, 36.49280755889972),
            ),
            source_up_axis="Y",
            meters_per_unit=0.01,
        )

        self.assertPointAlmostEqual(
            bbox_min,
            (-1.499865871322951, -0.3649280755889972, -1.5000058448935663),
        )
        self.assertPointAlmostEqual(
            bbox_max,
            (1.4998658713239936, 0.3643336965695829, 1.4999939182849225),
        )

    def test_x_up_is_rotated_into_target_z(self) -> None:
        bbox_min, bbox_max = normalize_bbox_to_z_up_meters(
            ((1.0, 2.0, 3.0), (4.0, 5.0, 6.0)),
            source_up_axis="X",
            meters_per_unit=1.0,
        )

        self.assertEqual(bbox_min, (-6.0, 2.0, 1.0))
        self.assertEqual(bbox_max, (-3.0, 5.0, 4.0))

    def test_rejects_invalid_axis_scale_and_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported source up axis"):
            normalize_bbox_to_z_up_meters(((0, 0, 0), (1, 1, 1)), "Q", 1.0)

        with self.assertRaisesRegex(ValueError, "finite and positive"):
            normalize_bbox_to_z_up_meters(((0, 0, 0), (1, 1, 1)), "Z", 0.0)

        with self.assertRaisesRegex(ValueError, "min exceeds max"):
            normalize_bbox_to_z_up_meters(((2, 0, 0), (1, 1, 1)), "Z", 1.0)


if __name__ == "__main__":
    unittest.main()
