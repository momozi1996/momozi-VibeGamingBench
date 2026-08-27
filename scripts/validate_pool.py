"""校验题池：遍历 bench/tasks/*/*.task.yaml，用 mock adapter 跑一遍，
确保每题在参考实现下 B=1.0、S=1.0、regression=0（即"可靠题目+可靠判分"的门禁）。

用法: python3 scripts/validate_pool.py [--tasks N] [--workers 8]
输出: bench/POOL_AUDIT.md + runs/pool_audit_<ts>.json
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import os
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "bench"
AUDIT_DIR = ROOT / "runs" / "pool_audit"


def _run_one(task_yaml: str, idx: int) -> dict:
    """单题 mock 跑一次。子进程跑，避免互相污染（每 worker 独立 out 文件）。"""
    out_path = f"/tmp/audit_one_{idx}.json"
    try:
        out = subprocess.run(
            [sys.executable, "-m", "momozi", "run", task_yaml, "--agent", "mock", "--out", out_path],
            capture_output=True, text=True, cwd=ROOT, timeout=180,
        )
        res = json.load(open(out_path))
        s = res["scores"]
        return {
            "task": res["task"],
            "family": res["family"],
            "ok": s["B"] == 1.0 and s["S"] >= 0.999 and res["regression_rate"] == 0.0,
            "B": s["B"], "S": s["S"], "total": s["total"],
            "regression_rate": res["regression_rate"],
        }
    except Exception as e:
        return {"task": Path(task_yaml).stem, "family": "?", "ok": False, "error": str(e)[:200]}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", type=int, default=None, help="按排序取前 N 条")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--include-gc", action="store_true",
                    help="连带 gamecraft 题一起跑（需要本机有 Godot 4 + 原 BMK 资产，默认关）")
    ap.add_argument("--only-gc", action="store_true", help="只跑 gamecraft 题")
    args = ap.parse_args(argv)

    all_tasks = sorted(glob.glob(str(BENCH / "tasks" / "*" / "*.task.yaml")))
    if args.only_gc:
        tasks = [t for t in all_tasks if "/gc_" in t]
    elif args.include_gc:
        tasks = all_tasks
    else:
        tasks = [t for t in all_tasks if "/gc_" not in t]
    if args.tasks:
        tasks = tasks[: args.tasks]
    print(f"auditing {len(tasks)} tasks with {args.workers} workers")

    results = []
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, r in enumerate(ex.map(lambda t: _run_one(t[1], t[0]), enumerate(tasks)), 1):
            results.append(r)
            if i % 100 == 0:
                bad = sum(1 for x in results if not x["ok"])
                print(f"  [{i}/{len(tasks)}] bad={bad} elapsed={time.time()-t0:.0f}s")

    bad = [r for r in results if not r["ok"]]
    per_fam_total = Counter(r.get("family", "?") for r in results)
    per_fam_bad = Counter(r.get("family", "?") for r in bad)

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    (AUDIT_DIR / f"pool_audit_{stamp}.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))

    lines = ["# Pool Audit — 题池可靠性门禁（mock adapter 通过=题目可信）",
             "",
             f"总题数：**{len(results)}**  通过：**{len(results)-len(bad)}**  失败：{len(bad)}",
             ""]
    lines.append("| 家族 | 通过 / 总数 |")
    lines.append("|---|---|")
    for fam in sorted(per_fam_total):
        lines.append(f"| {fam} | {per_fam_total[fam]-per_fam_bad[fam]} / {per_fam_total[fam]} |")
    if bad:
        lines += ["", "## 失败样例（前 20）"]
        for r in bad[:20]:
            tail = r.get("error") or "B=%s S=%s" % (r.get("B"), r.get("S"))
            lines.append("- `%s` — %s" % (r.get("task"), tail))
    (BENCH / "POOL_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\n结果：{len(results)-len(bad)} / {len(results)} 通过")
    print(f"报告：{BENCH/'POOL_AUDIT.md'}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
