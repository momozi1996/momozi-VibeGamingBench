"""gc 专属 runner 扩展：BUILD gate 前置 + GC 公式打分。
在 run_task 循环前调用 build_gate() 决定该 run 是否值得继续。
mz 分支只走 build → rubric(zhen_formula)，不走 suite/regression。
"""
from __future__ import annotations

import json
import subprocess
import shutil
import re
from pathlib import Path




def build_gate(work: Path, cmd_override: str = None, timeout: int = 30) -> dict:
    """HTML 硬门控：无 CLI, 只做静态合规。
    门控内容:
      - product/index.html 存在
      - product/game_logic.js 存在
      - HTML 不引用除 three.js 之外的运行时外链(fetch/XHR/other CDN)
      - HTML 有 <canvas> 或 WebGL 引用迹象
    """
    prod = work / "product"
    html_files = list(prod.glob("index.html")) + list(prod.glob("*.html"))
    js_files = list(prod.glob("game_logic.js"))
    checks = {
        "index_html_present": len(html_files) > 0,
        "game_logic_present": len(js_files) > 0,
        "canvas_or_webgl": False,
        "no_external_heavy_refs": True,
    }
    reasons = []
    if html_files:
        txt = html_files[0].read_text(encoding="utf-8", errors="ignore")
        if "<canvas" in txt or "WebGLRenderer" in txt or "getContext(" in txt:
            checks["canvas_or_webgl"] = True
        else:
            reasons.append("no <canvas>/WebGL signal")
        # 外链(不允许 three.js CDN 之外): fetch/XMLHttpRequest/img的http
        heavy = re.findall(r"(?:fetch\(|XMLHttpRequest|src=\"http[^\"]*\.(?:png|jpg|mp3|wav|mp4)\")", txt)
        if heavy:
            checks["no_external_heavy_refs"] = False
            reasons.append(f"external runtime refs: {heavy[:3]}")
    else:
        reasons.append("index.html missing")
    ok = all(checks.values())
    return {
        "ok": ok,
        "checks": checks,
        "reasons": reasons,
        "detail": "HTML static gates pass" if ok else "; ".join(reasons),
    }


def run_gamebench_task(task, work, adapter, prod, judge_agent):
    """gc 单轮测: BUILD gate -> rubric -> gc 公式。返回的 shape 与 run_task 里 B/S/P 对齐。"""
    gate = build_gate(work)
    judge = None
    if not gate["ok"]:
        judge = {"ok": False, "error": "build gate failed", "detail": gate.get("detail", "")}
    elif (judge_agent or "claude") == "mock":
        # mock 模式：跳过真 judge，直接给 0；由调用方决定是否用 gate 分
        judge = {"ok": True, "dimensions": {"completeness": 0, "richness": 0, "player_exp": 0, "visual": 0},
                 "zhen_formula_score": 0.0}
    else:
        try:
            judge = run_zon_rubric_judge(task, prod, judge_agent or "claude")
        except Exception as e:
            judge = {"error": str(e)}
    gc = (judge.get("zhen_formula_score") if isinstance(judge, dict) else None) or 0.0
    return {
        "engine": task.engine,
        "build_gate": gate,
        "judge": judge,
        "status_score": round(gc * (1.0 if gate["ok"] else 0.0), 4),
    }

def run_zon_rubric_judge(task, artifact_dir, profile="claude"):
    """Delegate to judge.py's generic rubric runner (keeps name stable for GC/MZ callers)."""
    from .judge import run_rubric_judge
    return run_rubric_judge(task, artifact_dir, profile)
