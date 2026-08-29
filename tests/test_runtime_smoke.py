import importlib.util
import tempfile
import unittest
from pathlib import Path

from momozi.runtime_smoke import RuntimeConfig, run_runtime_smoke


PLAYWRIGHT_AVAILABLE = importlib.util.find_spec("playwright") is not None


@unittest.skipUnless(
    PLAYWRIGHT_AVAILABLE,
    "Playwright is not installed; browser integration runs in CI after browser setup.",
)
class RuntimeSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = Path(__file__).parent / "fixtures" / "minimal_game"

    def test_fixture_loads_and_screenshots(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run_runtime_smoke(
                self.fixture,
                Path(directory),
                RuntimeConfig(stabilization_ms=100, input_probe=True),
            )
            if result.get("failure_code") == "D_RUNTIME_UNAVAILABLE":
                self.skipTest(result["failure_details"])
            self.assertEqual(result["status"], "pass", result)
            self.assertEqual(result["viewport"], {"width": 1280, "height": 720})
            self.assertEqual(len(result["screenshots"]), 1)
            self.assertTrue(Path(result["screenshots"][0]["path"]).is_file())

    def test_console_errors_are_fatal(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "game"
            fixture.mkdir()
            for source in self.fixture.iterdir():
                (fixture / source.name).write_text(
                    source.read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
            with (fixture / "index.html").open("a", encoding="utf-8") as handle:
                handle.write("<script>console.error('fixture failure')</script>")
            result = run_runtime_smoke(
                fixture,
                Path(directory) / "evidence",
                RuntimeConfig(stabilization_ms=50, input_probe=False),
            )
            if result.get("failure_code") == "D_RUNTIME_UNAVAILABLE":
                self.skipTest(result["failure_details"])
            self.assertEqual(result["failure_code"], "D_RUNTIME_FATAL", result)
            self.assertGreater(result["fatal_console_errors"], 0)

    def test_timeout_is_structured(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "game"
            fixture.mkdir()
            (fixture / "index.html").write_text(
                "<script>while (true) {}</script>",
                encoding="utf-8",
            )
            result = run_runtime_smoke(
                fixture,
                Path(directory) / "evidence",
                RuntimeConfig(
                    navigation_timeout_ms=300,
                    stabilization_ms=10,
                    input_probe=False,
                ),
            )
            if result.get("failure_code") == "D_RUNTIME_UNAVAILABLE":
                self.skipTest(result["failure_details"])
            self.assertIn(
                result["failure_code"],
                {"D_TIMEOUT", "D_RUNTIME_FATAL"},
                result,
            )


if __name__ == "__main__":
    unittest.main()
