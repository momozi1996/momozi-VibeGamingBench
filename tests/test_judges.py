import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from momozi.auto_eval import DeepSeekJudge, _aggregate_judgements
from momozi.judge_errors import JudgeFailure
from momozi.task import Task


class JudgeTests(unittest.TestCase):
    def test_code_judge_uses_median_aggregation(self):
        def judgement(score):
            return {
                "dimensions": {
                    key: {
                        "score": score,
                        "reason": f"reason {score}",
                        "evidence": [f"evidence {score}"],
                        "missing": [],
                    }
                    for key in ("completeness", "richness", "player_exp", "visual")
                },
                "fatal_issues": [],
                "confidence": 0.8,
            }

        result = _aggregate_judgements(
            [judgement(1), judgement(5), judgement(3)]
        )
        self.assertEqual(result["dimensions"]["visual"]["score"], 3.0)

    def test_malformed_code_response_preserves_raw_content(self):
        task_path = Path("bench/tasks/mz_puzzle-circuit-wizard-en") / (
            "mz_puzzle-circuit-wizard-en.task.yaml"
        )
        task = Task.load(task_path)
        with tempfile.TemporaryDirectory() as directory:
            product = Path(directory)
            (product / "index.html").write_text("<canvas></canvas>", encoding="utf-8")
            (product / "game_logic.js").write_text("", encoding="utf-8")

            class Response:
                def __enter__(self):
                    return self

                def __exit__(self, *args):
                    return False

                def read(self):
                    return json.dumps(
                        {
                            "choices": [
                                {"message": {"content": "RAW JUDGE OUTPUT"}}
                            ]
                        }
                    ).encode()

            judge = DeepSeekJudge(
                "test-key",
                base_url="https://example.test",
                retries=0,
                samples=1,
            )
            with patch(
                "momozi.auto_eval.urllib.request.urlopen",
                return_value=Response(),
            ):
                with self.assertRaises(JudgeFailure) as raised:
                    judge.evaluate(task, product)
            details = raised.exception.details
            self.assertTrue(details)
            self.assertIn("RAW JUDGE OUTPUT", details[0]["detail"])


if __name__ == "__main__":
    unittest.main()
