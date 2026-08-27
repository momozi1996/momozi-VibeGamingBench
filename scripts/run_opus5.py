"""Opus5 实跑 BMK: 用 momozi runner + claude profile (headless -p + acceptEdits)。
用法: python3 scripts/run_opus5.py --task bench/tasks/mz_sports-fishing-tournament/mz_sports-fishing-tournament.task.yaml [--out runs/<ts>.json]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_claude_once(prompt_path: Path, workdir: Path, timeout: int = 900) -> dict:
    """用 headless claude -p + allow-edit 造产品。"""
    argv = [
        "claude", "-p", str(prompt_path),
        "--permission-mode", "acceptEdits",
        "--allowedTools", "Edit,Write,Bash",
    ]
    t0 = time.time()
    try:
        res = subprocess.run(argv, cwd=workdir, capture_output=True, text=True, timeout=timeout)
        return {"ok": res.returncode == 0, "rc": res.returncode,
                "stdout": res.stdout[-3000:], "stderr": res.stderr[-1500:],
                "duration_s": round(time.time() - t0, 1)}
    except subprocess.TimeoutExpired as e:
        return {"ok": False, "rc": -1, "stdout": "", "stderr": f"timeout after {timeout}s — {e}", "duration_s": timeout}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args()

    task_yaml = Path(args.task).resolve()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    work = Path("/tmp/mz_run") / stamp
    work.mkdir(parents=True, exist_ok=True)
    (work / "product").mkdir(exist_ok=True)

    # 拷 prompt
    task_dir = task_yaml.parent
    prompt_md = task_dir / "prompt.md"
    (work / "_prompt.md").write_bytes(prompt_md.read_bytes())

    # 让 adapter 产物进 product/
    cwd_run = work
    gen = run_claude_once(work / "_prompt.md", cwd_run, args.timeout)
    # 列出产物
    product = work / "product"
    got = sorted(p.name for p in product.iterdir()) if product.exists() else []
    print(f"[run] agent=claude rc={gen['rc']} dur={gen['duration_s']}s files={got}")
    if gen['stderr']:
        print(f"[stderr] {gen['stderr'][:400]}")
    # 输出摘要到 json
    summary = {
        "task": task_yaml.stem,
        "timestamp": stamp,
        "workspace": str(work),
        "agent": "claude (opus5)",
        "generate": gen,
        "product_files": got,
    }
    out = Path(args.out) if args.out else Path(ROOT) / "runs" / f"opus5_{stamp}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[out] {out}")


if __name__ == "__main__":
    main()
