import unittest

from momozi.protocol import (
    AGENT_EVALUATION_PROTOCOL,
    BENCHMARK_RELEASE,
    SCHEMA_VERSION,
    result_schema_errors,
    validate_result_schema,
)


class SchemaTests(unittest.TestCase):
    def result(self):
        return {
            "schema_version": SCHEMA_VERSION,
            "benchmark_release": BENCHMARK_RELEASE,
            "evaluation_protocol": AGENT_EVALUATION_PROTOCOL,
            "task_id": "fixture-en",
            "base_task_id": "fixture",
            "language": "en",
            "agent": {"name": "test", "model": "test", "harness": "test"},
            "static": {},
            "dynamic": {},
            "visual": {},
            "scores": {"final": 42.0},
            "failure_details": [],
        }

    def test_valid_result(self):
        result = self.result()
        self.assertEqual(result_schema_errors(result), [])
        self.assertIs(validate_result_schema(result), result)

    def test_invalid_score(self):
        result = self.result()
        result["scores"]["final"] = 120
        self.assertTrue(result_schema_errors(result))

    def test_runtime_alias_is_accepted(self):
        result = self.result()
        result.pop("dynamic")
        result["runtime"] = {"status": "pass"}
        self.assertEqual(result_schema_errors(result), [])


if __name__ == "__main__":
    unittest.main()
