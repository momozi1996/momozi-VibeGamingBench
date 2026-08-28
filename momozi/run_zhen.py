"""MZ browser-game runner extension: BUILD gate plus weighted rubric scoring.
在 run_task 循环前调用 build_gate() 决定该 run 是否值得继续。
MZ 分支只走 build -> rubric，不走旧式多轮回归评分。
"""
from __future__ import annotations

import re
from pathlib import Path


def _weighted_judge_score(task, scores: dict) -> float:
    weighted = 0.0
    total_weight = 0.0
    for dimension in task.rubric:
        dimension_id = dimension.get("id")
        if dimension_id not in scores:
            continue
        weight = float(dimension.get("weight", 0))
        maximum = float(dimension.get("max", 5)) or 5.0
        value = max(0.0, min(maximum, float(scores[dimension_id])))
        weighted += weight * (value / maximum)
        total_weight += weight
    return weighted / total_weight if total_weight else 0.0




def build_gate_product(prod: Path) -> dict:
    """Run the static HTML gate against a product directory.

    门控内容:
      - product/index.html 存在
      - product/game_logic.js 存在
      - HTML 不引用除 three.js 之外的运行时外链(fetch/XHR/other CDN)
      - HTML 有 <canvas> 或 WebGL 引用迹象
    """
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


def build_gate(work: Path, cmd_override: str = None, timeout: int = 30) -> dict:
    """Compatibility wrapper accepting a workspace containing product/."""
    return build_gate_product(work / "product")


def run_mz_task(task, work, adapter, prod, judge_agent):
    """Run the MZ BUILD gate and weighted four-dimension rubric."""
    gate = build_gate(work)
    judge = None
    if not gate["ok"]:
        judge = {"ok": False, "error": "build gate failed", "detail": gate.get("detail", "")}
    elif (judge_agent or "claude") == "mock":
        # mock 模式：跳过真 judge，直接给 0；由调用方决定是否用 gate 分
        judge = {"ok": True, "dimensions": {"completeness": 0, "richness": 0, "player_exp": 0, "visual": 0},
                 "rubric_score": 0.0}
    else:
        try:
            judge = run_rubric_judge_adapter(task, prod, judge_agent or "claude")
            if "scores" in judge:
                judge["dimensions"] = judge["scores"]
                judge["rubric_score"] = _weighted_judge_score(
                    task, judge["scores"]
                )
        except Exception as e:
            judge = {"error": str(e)}
    score = judge.get("rubric_score", 0.0) if isinstance(judge, dict) else 0.0
    return {
        "engine": task.engine,
        "build_gate": gate,
        "judge": judge,
        "rubric_score": round(score * (1.0 if gate["ok"] else 0.0), 4),
    }

def run_rubric_judge_adapter(task, artifact_dir, profile="claude"):
    """Delegate to judge.py's generic rubric runner."""
    from .judge import run_rubric_judge
    return run_rubric_judge(task, artifact_dir, profile)
