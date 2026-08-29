"""Run every task through the mock runner and BUILD gate.

This checks task/runner compatibility. It does not claim that a real model has
implemented each game or that the subjective rubric has been calibrated.

用法: python3 scripts/validate_pool.py --only-mz [--tasks N] [--workers 8]
输出: bench/POOL_AUDIT.md + runs/pool_audit/pool_audit_<ts>.json
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "bench"
AUDIT_DIR = ROOT / "runs" / "pool_audit"

# 强制用环境干净的 Python 跑子进程。
INTERPRETER = sys.executable
if "momo-T2V-skill" in INTERPRETER or "site-packages" in INTERPRETER:
    for cand in ("/usr/bin/python3", "/usr/local/bin/python3"):
        if Path(cand).exists():
            INTERPRETER = cand
            break
else:
    try:
        import yaml  # noqa
    except ImportError:
        INTERPRETER = "/usr/bin/python3"


def _run_one(task_yaml: str, idx: int) -> dict:
    """单题 mock 跑一次。子进程跑，避免互相污染（每 worker 独立 out 文件）。"""
    handle = tempfile.NamedTemporaryFile(
        prefix=f"momozi-audit-{idx}-", suffix=".json", delete=False
    )
    out_path = Path(handle.name)
    handle.close()
    try:
        out = subprocess.run(
            [
                INTERPRETER,
                "-m",
                "momozi",
                "run",
                task_yaml,
                "--agent",
                "mock",
                "--skip-judge",
                "--out",
                str(out_path),
            ],
            capture_output=True, text=True, cwd=ROOT, timeout=180,
        )
        if out.returncode != 0:
            return {
                "task": Path(task_yaml).stem,
                "family": "?",
                "ok": False,
                "error": (out.stderr or out.stdout)[-500:],
            }
        res = json.loads(out_path.read_text(encoding="utf-8"))
        s = res.get("scores") or {}
        # 两套兼容路径：
        # - 当前 mz_* 浏览器题 -> HTML BUILD gate 通过
        # - 旧式多轮题 -> B=S=1.0 且零回归
        tid = res.get("task") or ""
        if tid.startswith("mz_"):
            gate = res.get("build_gate", {}) or {}
            ok_mz = bool(gate.get("ok"))
            return {
                "task": tid, "family": res.get("family"),
                "language": res.get("language"),
                "ok": ok_mz, "build_gate_ok": ok_mz,
            }
        b_ok = s.get("B") == 1.0
        s_ok = s.get("S") == 1.0
        reg_ok = res.get("regression_rate", 1.0) == 0.0
        return {
            "task": tid, "family": res.get("family"),
            "language": res.get("language"),
            "ok": b_ok and s_ok and reg_ok,
            "B": s.get("B"), "S": s.get("S"),
            "regression_rate": res.get("regression_rate"),
        }
    except Exception as e:
        return {"task": Path(task_yaml).stem, "family": "?", "ok": False, "error": str(e)[:200]}
    finally:
        out_path.unlink(missing_ok=True)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", type=int, default=None, help="按排序取前 N 条")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument(
        "--include-legacy",
        action="store_true",
        help="include non-mz legacy tasks if any are present",
    )
    ap.add_argument(
        "--only-mz",
        dest="only_mz",
        action="store_true",
        help="run only the current mz browser-game pool",
    )
    args = ap.parse_args(argv)

    all_tasks = sorted(glob.glob(str(BENCH / "tasks" / "*" / "*.task.yaml")))
    if args.only_mz:
        tasks = [t for t in all_tasks if Path(t).parent.name.startswith("mz_")]
    elif args.include_legacy:
        tasks = all_tasks
    else:
        tasks = [t for t in all_tasks if Path(t).parent.name.startswith("mz_")]
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
    per_lang_total = Counter(r.get("language") or "unspecified" for r in results)
    per_lang_bad = Counter(r.get("language") or "unspecified" for r in bad)

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    (AUDIT_DIR / f"pool_audit_{stamp}.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))

    lines = ["# Pool Audit - Runner 与 BUILD Gate 兼容性门禁",
             "",
             "> mock adapter 只验证题目元数据、runner 和静态 BUILD gate 可以完整执行，",
             "> 不代表真实模型已完成题目，也不替代 rubric 校准或浏览器交互测试。",
             "",
             f"总题数：**{len(results)}**  通过：**{len(results)-len(bad)}**  失败：{len(bad)}",
             ""]
    lines.append("| 家族 | 通过 / 总数 |")
    lines.append("|---|---|")
    for fam in sorted(per_fam_total):
        lines.append(f"| {fam} | {per_fam_total[fam]-per_fam_bad[fam]} / {per_fam_total[fam]} |")
    lines += ["", "| 语言 | 通过 / 总数 |", "|---|---|"]
    for language in sorted(per_lang_total):
        lines.append(
            f"| {language} | "
            f"{per_lang_total[language]-per_lang_bad[language]} / {per_lang_total[language]} |"
        )
    if bad:
        lines += ["", "## 失败样例（前 20）"]
        for r in bad[:20]:
            tail = r.get("error") or "B=%s S=%s" % (r.get("B"), r.get("S"))
            lines.append("- `%s` — %s" % (r.get("task"), tail))
    (BENCH / "POOL_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n结果：{len(results)-len(bad)} / {len(results)} 通过")
    print(f"报告：{BENCH/'POOL_AUDIT.md'}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
