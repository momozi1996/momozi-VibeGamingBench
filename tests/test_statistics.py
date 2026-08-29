import unittest

from momozi.statistics import (
    aggregate_results,
    bootstrap_ci,
    paired_delta_ci,
    rank_stability,
)


def row(task, base, language, family, score):
    return {
        "task_id": task,
        "base_task_id": base,
        "language": language,
        "family": family,
        "scores": {"final": score},
    }


class StatisticsTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            row("a-en", "a", "en", "action", 80),
            row("a-zh", "a", "zh", "action", 60),
            row("b-en", "b", "en", "strategy", 40),
            row("b-zh", "b", "zh", "strategy", 50),
        ]

    def test_balances_pairs_before_families(self):
        result = aggregate_results(self.rows)
        self.assertEqual(result["micro_score"], 57.5)
        self.assertEqual(result["concept_balanced_score"], 57.5)
        self.assertEqual(result["family_balanced_score"], 57.5)
        self.assertEqual(result["language_gap"], 5.0)

    def test_bootstrap_is_deterministic_and_paired(self):
        first = bootstrap_ci(self.rows, iterations=100, seed=7)
        second = bootstrap_ci(self.rows, iterations=100, seed=7)
        self.assertEqual(first, second)
        self.assertEqual(first["sampling_unit"], "base_task_id")

    def test_delta_and_rank_stability(self):
        better = [
            {**item, "scores": {"final": item["scores"]["final"] + 10}}
            for item in self.rows
        ]
        delta = paired_delta_ci(better, self.rows, iterations=50, seed=3)
        self.assertEqual(delta["delta"], 10.0)
        stability = rank_stability(
            {"better": better, "baseline": self.rows},
            iterations=50,
            seed=3,
        )
        self.assertEqual(stability["better"]["p_rank_1"], 1.0)


if __name__ == "__main__":
    unittest.main()
