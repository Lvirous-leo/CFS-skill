import sys
import unittest
from decimal import Decimal
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from top10_aggregation import aggregate_top_n, full_data_hhi


class TopTenAggregationTests(unittest.TestCase):
    def test_ten_rows_are_all_displayed_without_other(self):
        rows = [{"name": "项目%02d" % i, "amount": Decimal(i)} for i in range(1, 11)]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            sort_key=lambda row: (-row["amount"], row["name"]),
        )

        self.assertEqual(len(result["display_rows"]), 10)
        self.assertEqual(result["other_count"], 0)
        self.assertFalse(any(row["name"].startswith("其他") for row in result["display_rows"]))

    def test_eleven_rows_become_top_ten_plus_other(self):
        rows = [{"name": "项目%02d" % i, "amount": Decimal(i)} for i in range(1, 12)]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            sort_key=lambda row: (-row["amount"], row["name"]),
        )

        self.assertEqual(len(result["display_rows"]), 11)
        self.assertEqual(result["display_rows"][-1]["name"], "其他（1项）")
        self.assertEqual(result["display_rows"][-1]["amount"], Decimal("1"))
        self.assertEqual(result["full_totals"]["amount"], Decimal("66"))

    def test_other_weighted_rate_is_recalculated_from_raw_rows(self):
        rows = [
            {"name": "项目%02d" % i, "amount": Decimal("100"), "rate": Decimal(i)}
            for i in range(1, 13)
        ]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            weighted_fields={"rate": ("rate", "amount")},
            sort_key=lambda row: (-row["rate"], row["name"]),
        )

        self.assertEqual(result["display_rows"][-1]["rate"], Decimal("1.5"))

    def test_hhi_uses_full_rows_not_aggregated_other(self):
        rows = [{"name": str(i), "amount": Decimal("10")} for i in range(11)]

        expected = Decimal(1) / Decimal(11)
        self.assertLess(abs(full_data_hhi(rows, "amount") - expected), Decimal("1e-26"))

    def test_overdue_records_sort_before_larger_non_overdue_records(self):
        rows = [
            {"name": "正常大额", "overdue": False, "amount": Decimal("1000")},
            {"name": "逾期小额", "overdue": True, "amount": Decimal("1")},
        ]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            sort_key=lambda row: (not row["overdue"], -row["amount"], row["name"]),
            limit=1,
        )

        self.assertEqual(result["display_rows"][0]["name"], "逾期小额")
        self.assertEqual(result["display_rows"][-1]["name"], "其他（1项）")

    def test_sorting_is_stable_for_equal_amounts(self):
        rows = [
            {"name": "B", "amount": Decimal("10")},
            {"name": "A", "amount": Decimal("10")},
            {"name": "C", "amount": Decimal("10")},
        ]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            sort_key=lambda row: (-row["amount"], row["name"]),
        )

        self.assertEqual([row["name"] for row in result["display_rows"]], ["A", "B", "C"])

    def test_zero_weight_returns_unavailable_weighted_metric(self):
        rows = [
            {"name": "A", "amount": Decimal("0"), "rate": Decimal("3")},
            {"name": "B", "amount": Decimal("0"), "rate": Decimal("4")},
        ]

        result = aggregate_top_n(
            rows,
            label_field="name",
            additive_fields=("amount",),
            weighted_fields={"rate": ("rate", "amount")},
            sort_key=lambda row: row["name"],
            limit=1,
        )

        self.assertIsNone(result["display_rows"][-1]["rate"])


if __name__ == "__main__":
    unittest.main()
