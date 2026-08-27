"""评审侧复评：解压 submission tar.gz 到临时 product/，重跑 B/S 校验，
与 submissions/*.json 的 scores 比对，不一致按验算值出榜。
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path

from momozi.run import _prepare_workspace  # noqa
from momozi.task import Task
from momozi.verifiers import StaticChecker, BehaviorSuite


def _run_verification(task: Task, product_dir: Path):
    static = StaticChecker(task.static)
    req = task.artifact_requirements()
    s_items = static.run(product_dir, req)
    suite = BehaviorSuite(product_dir, task.behavior.get("script", "beh_behavior.mjs"))
    b_items = suite.run()
    b_total = len(b_items)
    b_ok = len([r for r in b_items if r["ok"]])
    return {
        "static": s_items,
        "static_pass_rate": (sum(x["weight"] for x in s_items if x["ok"] is True) /
                             max(1e-9, sum(x["weight"] for x in s_items))) if s_items else 1.0,
        "behavior": b_items,
        "behavior_pass_rate": b_ok / b_total if b_total else 0.0,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(prog="momozi verify")
    ap.add_argument("json_path")
    ap.add_argument("archive")
    args = ap.parse_args(argv)
    sub = Path(args.json_path)
    claim = json.loads(sub.read_text(encoding="utf-8"))
    task = Task.load(Path(claim["task_path"])) if claim.get("task_path") else None
    if task is None:
        # fallback：默认任务目录
        task = Task.load(Path("bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml"))

    tmp = Path(tempfile.mkdtemp(prefix="momozi-verify-"))
    with tarfile.open(args.archive) as tf:
        tf.extractall(tmp)
    # tar 里结构可能是 product/ 或平铺
    candidate = tmp / "product"
    if not candidate.exists():
        candidate = tmp if (tmp / "game_logic.js").exists() else tmp
    result = _run_verification(task, candidate)
    recomputed = round(0.55 * result["behavior_pass_rate"]
                       + 0.20 * result["static_pass_rate"], 4)
    claim_total = claim.get("scores", {}).get("total")
    match = claim_total is not None and abs(claim_total - recomputed) <= 0.01
    print(json.dumps({
        "claimed_total": claim_total,
        "recomputed_total": recomputed,
        "verified": match,
        "behavior_pass_rate": result["behavior_pass_rate"],
        "static_pass_rate": result["static_pass_rate"],
    }, ensure_ascii=False, indent=2))
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if match else 1


if __name__ == "__main__":
    sys.exit(main())
