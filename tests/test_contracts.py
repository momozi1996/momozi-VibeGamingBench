import json
import tempfile
import unittest
from pathlib import Path

from momozi.run_zhen import build_gate_product
from momozi.verifiers import BehaviorSuite


class ContractTests(unittest.TestCase):
    def test_classic_script_behavior_contract(self):
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as directory:
            root = Path(directory)
            (root / "game_logic.js").write_text(
                """(function (root) {
  function createGame() { return { score: 0 }; }
  function advance(game) { return game; }
  root.GameLogic = { createGame, advance };
}(typeof window !== "undefined" ? window : globalThis));
""",
                encoding="utf-8",
            )
            suite_path = root / "beh_html.mjs"
            suite_path.write_text(
                Path("bench/tests/beh_html.mjs").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            result = BehaviorSuite(
                root,
                "beh_html.mjs",
                artifact_dir=root,
                script_path=suite_path,
            ).run()
            self.assertTrue(result, result)
            self.assertTrue(all(item["ok"] for item in result), result)

    def test_data_uri_assets_are_not_heavy_external_refs(self):
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as directory:
            product = Path(directory)
            (product / "index.html").write_text(
                '<canvas></canvas><img src="data:image/png;base64,AAAA">',
                encoding="utf-8",
            )
            (product / "game_logic.js").write_text(
                "window.GameLogic = {createGame(){return {}},advance(g){return g}};",
                encoding="utf-8",
            )
            result = build_gate_product(product)
            self.assertTrue(result["checks"]["no_external_heavy_refs"], result)
            self.assertTrue(result["ok"], result)

    def test_static_evaluator_accepts_relative_product_path(self):
        from momozi.static_eval import StaticEvaluator
        from momozi.task import Task

        task = Task.load(
            Path("bench/tasks/mz_feishu-structured-001-en")
            / "mz_feishu-structured-001-en.task.yaml"
        )
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as directory:
            root = Path(directory)
            product = root / "product"
            product.mkdir()
            (product / "index.html").write_text(
                "<canvas></canvas><script src='./game_logic.js'></script>",
                encoding="utf-8",
            )
            (product / "game_logic.js").write_text(
                "(function(root){function createGame(){return {};}"
                "function advance(g){return g;}root.GameLogic={createGame,advance};"
                "})(typeof window!=='undefined'?window:globalThis);",
                encoding="utf-8",
            )
            result = StaticEvaluator().evaluate(task, product.relative_to(Path.cwd()))
            self.assertTrue(result["build"]["ok"], result)
            self.assertEqual(result["contract"]["pass_rate"], 1.0, result)


if __name__ == "__main__":
    unittest.main()
