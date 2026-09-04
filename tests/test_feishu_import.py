import json
import unittest
from pathlib import Path

import yaml


class FeishuImportTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_manifest_and_task_pairs(self):
        manifest = json.loads(
            (self.ROOT / "bench" / "sources" / "feishu_game_prompts.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(manifest["concept_count"], 220)
        self.assertEqual(manifest["sheet_counts"], {"直接1": 100, "直接生成": 120})

        task_dirs = sorted((self.ROOT / "bench" / "tasks").glob("mz_feishu-*"))
        self.assertEqual(len(task_dirs), 440)
        bases = {}
        for task_dir in task_dirs:
            yaml_path = next(task_dir.glob("*.task.yaml"))
            raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
            self.assertIn(raw["language"], {"en", "zh"})
            self.assertEqual(raw["id"], task_dir.name)
            self.assertEqual(raw["base_task_id"], task_dir.name.rsplit("-", 1)[0])
            prompt = (task_dir / "prompt.md").read_text(encoding="utf-8").strip()
            self.assertEqual(raw["rounds"][0]["spec"].strip(), prompt)
            self.assertIn("Vibe Gaming", prompt)
            self.assertIn("game_logic.js", prompt)
            bases.setdefault(raw["base_task_id"], set()).add(raw["language"])
        self.assertEqual(len(bases), 220)
        self.assertTrue(all(languages == {"en", "zh"} for languages in bases.values()))


if __name__ == "__main__":
    unittest.main()
