#!/bin/bash
# 一键生成/刷新展示站（site/index.html 的数据层）
# 用法: scripts/gen_site.sh
set -e
cd "$(dirname "$0")/.."
ROOT=$(pwd)

# 0. 目标数据目录
mkdir -p site/data

# 1. 更新 leaderboard
python3 -m momozi leaderboard --out site/data/leaderboard.json

# 2. 收集可玩游戏（参考实现 + 每个 run 的 product）
python3 - "$ROOT" <<'PYEOF'
import json, os, shutil, sys
from pathlib import Path
root = Path(sys.argv[1])
play = root / "site" / "play"
play.mkdir(parents=True, exist_ok=True)

items = []
# 参考实现
for ref in sorted((root / "bench" / "references").glob("*/index.html")):
    tid = ref.parent.name
    dst = play / f"{tid}_reference.html"
    shutil.copy(ref, dst)
    items.append({"id": f"{tid}_reference", "kind": "reference", "task": tid,
                  "url": dst.relative_to(root / "site").as_posix()})

# 每个 run 里 agent 的交卷
for rj in sorted((root / "runs").rglob("*.json")):
    try:
        d = json.loads(rj.read_text())
    except Exception:
        continue
    if "scores" not in d:
        continue
    base = rj.parent / "product"
    entry = base / "index.html"
    if entry.exists():
        key = f"{d['task']}_{d['agent']}"
        dst = play / f"{key}.html"
        shutil.copy(entry, dst)
        items.append({"id": key, "kind": "run", "task": d["task"], "agent": d["agent"],
                      "url": dst.relative_to(root / "site").as_posix(),
                      "scores": d["scores"],
                      "regression_rate": d.get("regression_rate"),
                      "behavior_pass_rate_final": d.get("behavior_pass_rate_final")})

json.dump(items, open(root / "site" / "data" / "playables.json", "w"),
          ensure_ascii=False, indent=2)
print(f"collected {len(items)} playable artifacts")
PYEOF

echo "site data regenerated under site/data/"
