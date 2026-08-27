"""gc 专属 runner 扩展：BUILD gate 前置 + GC 公式打分。
在 run_task 循环前调用 build_gate() 决定该 run 是否值得继续。
gc 分支只走 build → rubric(gc_formula)，不走 suite/regression。
"""
from __future__ import annotations

import json
import subprocess
import shutil
from pathlib import Path

from .judge_gc import run_gc_rubric_judge


def build_gate(work: Path, cmd_override: str = None, timeout: int = 60) -> dict:
    """跑 BUILD 门控：原 BMK build_check.cmd = `godot --headless --path <dir> --quit-after 5`。"""
    cmd_tokens = (cmd_override or "godot --headless --path <GAME> --quit-after 5").split()
    # 替换 <GAME> → product 目录
    cmd = [c.replace("<GAME>", str(work / "product")) for c in cmd_tokens]
    try:
        proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=timeout)
        return {
            "ok": proc.returncode == 0 and "SCRIPT ERROR" not in proc.stdout.upper() and "ERROR:" not in proc.stderr.upper(),
            "returncode": proc.returncode,
            "stdout": proc.stdout[-600:],
            "stderr": proc.stderr[-600:],
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "returncode": -1, "stderr": "timeout"}
    except FileNotFoundError:
        return {"ok": False, "returncode": -2, "stderr": "godot not installed"}


def run_gc_task(task, work, adapter, prod, judge_agent):
    """gc 单轮测: BUILD gate -> rubric -> gc 公式。返回的 shape 与 run_task 里 B/S/P 对齐。"""
    gate = build_gate(work)
    judge = None
    if not gate["ok"]:
        judge = {"ok": False, "error": "build gate failed", "stderr": gate["stderr"]}
    else:
        try:
            judge = run_gc_rubric_judge(task, prod, judge_agent or "claude")
        except Exception as e:
            judge = {"error": str(e)}
    gc = (judge.get("gc_formula_score") if isinstance(judge, dict) else None) or 0.0
    return {
        "engine": task.engine,
        "build_gate": gate,
        "judge": judge,
        "status_score": round(gc * (1.0 if gate["ok"] else 0.0), 4),
    }
