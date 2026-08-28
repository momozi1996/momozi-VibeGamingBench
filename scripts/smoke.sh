#!/bin/bash
# Current repository smoke checks.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== syntax =="
python3 -m py_compile momozi/*.py scripts/*.py
for script in bench/tests/*.mjs; do node --check "$script"; done

echo "== task metadata =="
python3 scripts/split_bilingual_tasks.py
python3 scripts/generate_task_distribution.py --check
python3 scripts/add_22_expansion_tasks.py
python3 scripts/add_summerengine_tasks.py
python3 scripts/add_three_source_tasks.py

echo "== mock runner/build gate =="
result="$(mktemp)"
python3 -m momozi run \
  bench/tasks/mz_sports-fishing-tournament-en/mz_sports-fishing-tournament-en.task.yaml \
  --agent mock --skip-judge --out "$result" >/dev/null
python3 - "$result" <<'PY'
import json
import sys

result = json.load(open(sys.argv[1], encoding="utf-8"))
assert result["benchmark"] == "momozi-VibeGamingBench", result
assert result["version"] == "0.4.0", result
assert result["build_gate"]["ok"] is True, result
print("mock runner/build gate OK")
PY
rm -f "$result"

echo "== automatic evaluation protocol =="
auto_tmp="$(mktemp -d)"
python3 scripts/auto_evaluate.py \
  --task mz_sports-fishing-tournament-en \
  --agent mock \
  --mock-judge \
  --run-id smoke \
  --output-root "$auto_tmp/runs" \
  --leaderboard-out "$auto_tmp/leaderboard.json" \
  --leaderboard-md-out "$auto_tmp/LEADERBOARD.md" >/dev/null
python3 - "$auto_tmp" <<'PY'
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
result = json.loads(
    (root / "runs" / "smoke" / "mz_sports-fishing-tournament-en.json").read_text()
)
assert result["evaluation_protocol"] == "auto-v1", result
assert result["build_gate"]["ok"] is True, result
assert result["contract"]["pass_rate"] == 1.0, result
assert result["scores"]["overall_score"] == 60.0, result
assert result["leaderboard_eligible"] is False, result
leaderboard = json.loads((root / "leaderboard.json").read_text())
assert leaderboard["leaderboard"] == [], leaderboard
print("automatic evaluation protocol OK")
PY
rm -rf "$auto_tmp"

echo "== imports =="
python3 -c "import momozi.auto_eval, momozi.run, momozi.judge, momozi.leaderboard, momozi.verify; print('python imports ok')"
