"""momozi-3A-GamegenBench 主 runner。

三维评分：
  B (Behavior)  = 末轮行为通过率 · (1 − 0.2·regression_rate)   # 0.55
  S (Structure) = 静态检查加权通过率                          # 0.20
  P (Presentation) = rubric judge（claude/codex/adapter）      # 0.25

行为回归 = 某例行为上一轮通过而本轮失败 → regressions 计数计入 regression_rate。

用法:
  python3 -m momozi.run <task.yaml> --agent <profile> [--rounds R1,R2] [--out res.json]
产物约定: agent 必须把全部产物写到 <workspace>/product/
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from .task import Task
from .adapters import build_adapter, load_profiles
from .mock_adapter import MockAdapter
from .verifiers import StaticChecker, BehaviorSuite
from .judge import run_rubric_judge  # 延迟导入避免缺 judge CLI 时崩

ROOT = Path(__file__).resolve().parent.parent
PROFILES_PATH = ROOT / "profiles.yaml"
WORKSPACE_ROOT = ROOT / "workspaces"
RUNS_ROOT = ROOT / "runs"

WEIGHTS = {"behavior": 0.55, "structure": 0.20, "presentation": 0.25}
# 家族 → 参考实现目录别名（新建家族时可复用既有参考实现）
FAMILY_REF_ALIAS = {"physics_breakout": "tg1"}


_GC_PLACEHOLDER = """<!doctype html>
<html><head><meta charset="utf-8"><title>gc mock placeholder</title>
<script type="importmap">{"imports":{"three":"https://unpkg.com/three@0.169.0/build/three.module.js"}}</script></head>
<body><canvas id="c"></canvas>
<script type="module">
import * as THREE from 'three';
import { createGame, advance } from './game_logic.js';
const g = createGame({});
function loop(){ advance(g, {}, 1/60); requestAnimationFrame(loop); }
loop();
</script></body></html>
"""


def _prepare_workspace(task: Task, agent: str, stamp: str) -> Path:
    """init workspace: 清空 product/, 落 tests 套件 + _prompt.md。"""
    work = WORKSPACE_ROOT / stamp / task.id / agent
    prod = work / "product"
    prod.mkdir(parents=True, exist_ok=True)

    base = task.path.parent
    # 复制 task 目录下所有文件（yaml/tests/题目提示材料）到 workspace 根
    for item in base.iterdir():
        if item.is_file():
            shutil.copy(item, work / item.name)
        elif item.is_dir():
            shutil.copytree(item, work / item.name, dirs_exist_ok=True)
    # 任务自带 tests/ → workspace 根 + product
    suite_name = Path(task.behavior.get("script", "beh_behavior.mjs")).name
    for sub in ("tests",):
        if (work / sub).exists():
            for p in (work / sub).iterdir():
                shutil.copy(p, work / p.name)
                shutil.copy(p, prod / p.name)
    # 公共套件（bench/tests/*.mjs）也要进 product —— behavior 永远可执行
    pub_suite_dir = ROOT / "bench" / "tests"
    if pub_suite_dir.exists():
        for p in pub_suite_dir.glob("*.mjs"):
            shutil.copy(p, prod / p.name)
            shutil.copy(p, work / p.name)
    keep_l1 = {suite_name}
    for p in list(prod.iterdir()):
        if p.name not in keep_l1 and p.suffix not in {".mjs"}:
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            else:
                p.unlink()
    # 清 workspace 根的题目自带残留
    keep_top = {"_prompt.md", "product", "tests"}
    for p in list(work.iterdir()):
        if p.name not in keep_top and not p.name.startswith("."):
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            else:
                p.unlink()
    return work


def _task_public_suite(task: Task) -> Path:
    """任务自带专项套件路径（放 bench/tasks/<id>/tests/）。"""
    script = task.behavior.get("script", "beh_behavior.mjs")
    cand = task.path.parent / script
    return cand


def _run_gc_path(task, work, prod, agent, skip_judge, judge_agent, stamp):
    """gc 路径：adapter 一次性生成，然后 BUILD gate → judge → GC 公式。"""
    adapter = _build(task, agent)
    # 把 prompt 落盘然后让 adapter 生成（无多轮，是为 gc 单轮命题）
    prompt_text = task.rounds[0].spec if task.rounds else ""
    (work / "_prompt.md").write_text(prompt_text, encoding="utf-8")
    # gc 题联调：mock adapter 不产物，我们用 _GC_PLACEHOLDER 手动补齐纯净 HTML 壳
    if agent == "mock":
        (prod / "index.html").write_text(_GC_PLACEHOLDER, encoding="utf-8")
        (prod / "game_logic.js").write_text(
            "export function createGame(){return {bricks:[],lives:3,score:0,state:'playing'};}\n"
            "export function advance(g,a,dt){return g;}\n", encoding="utf-8")
    gen = adapter.generate(work, prompt_text, 0)
    if not skip_judge:
        from .run_gc import run_gc_task as _gc
        res = _gc(task, work, adapter, prod, judge_agent or "claude")
    else:
        # skip_judge 也要跑 BUILD gate 拿个便宜分
        from .run_gc import run_gc_task as _gc
        res = _gc(task, work, adapter, prod, "mock")
    return {
        "benchmark": "momozi-3A-GamegenBench",
        "version": "0.1.0",
        "task": task.id,
        "title": task.title,
        "family": task.family,
        "difficulty": task.difficulty,
        "engine": task.engine,
        "agent": adapter.name,
        "timestamp": stamp,
        "scores": {"gc_formula": res.get("status_score"),
                   "dimensions": res.get("judge", {}).get("dimensions")},
        "build_gate": res.get("build_gate", {}),
        "gen_ok": bool(gen.get("ok")),
        "workspace": str(work),
    }


def _build(task: Task, agent: str) -> object:
    if agent == "mock":
        # 参考实现：任务声明为准；否则按题族_参考目录别名推
        rel = task.reference_dir or f"bench/references/{task.family}"
        ref = ROOT / rel
        if not ref.exists():
            ref = ROOT / "bench" / "references" / FAMILY_REF_ALIAS.get(task.family, task.family)
        return MockAdapter(ref)
    return build_adapter(agent, load_profiles(PROFILES_PATH))


def run_task(task_path: str, agent: str = "mock", out_path: str = None,
             rounds_filter=None, skip_judge: bool = False, judge_agent: str = None):
    task = Task.load(Path(task_path))
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    work = _prepare_workspace(task, agent, stamp)
    prod = work / "product"

    # gc-* 题：HTML 静态合规 BUILD gate × GC 公式(0.15M+0.35D+0.15V+0.35A)
    # 工厂参数化题不计入排行榜，移到 tasks_synthetic 单独维护
    if task.id.startswith("gc_"):
        if agent == "mock":
            (prod / "index.html").write_text(_GC_PLACEHOLDER, encoding="utf-8")
            (prod / "game_logic.js").write_text(
                "export function createGame(){return {bricks:[],lives:3,score:0,state:'playing'};}\n"
                "export function advance(g,a,dt){return g;}\n", encoding="utf-8")
        res = _run_gc_path(task, work, prod, agent, skip_judge, judge_agent, stamp)
        if out_path:
            Path(out_path).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return res

    # prompt 逐轮
    prompt_specs = list(task.rounds)
    if rounds_filter:
        names = set(rounds_filter)
        prompt_specs = [p for p in prompt_specs if p.name in names]

    adapter = _build(task, agent)
    static = StaticChecker(task.static)
    req = task.artifact_requirements()
    suite_path = task.behavior.get("script", "beh_behavior.mjs") if task.behavior else "beh_behavior.mjs"
    suite = BehaviorSuite(prod, suite_path,
                          timeout=task.behavior.get("timeout", 60)) if task.behavior else None

    rounds_log = []
    prev_pass = set()
    for idx, spec in enumerate(prompt_specs):
        prompt_path = work / "_prompt.md"
        prompt_path.write_text(spec.spec, encoding="utf-8")
        t0 = time.time()
        gen = adapter.generate(work, spec.name, idx)
        dur = round(time.time() - t0, 1)

        s_res = static.run(prod, req)
        b_res = suite.run() if suite else []
        ok_ids = {r["id"] for r in b_res if r["ok"]}
        regressions = sorted(prev_pass - ok_ids)
        next_pass = sorted(ok_ids - prev_pass)
        b_all = len(b_res)
        b_ok = len([r for r in b_res if r["ok"]])
        b_rate = b_ok / b_all if b_all else 1.0

        rounds_log.append({
            "round": spec.name,
            "ok_prompt": bool(gen.get("ok")),
            "duration_s": dur,
            "gen_stderr": (gen.get("stderr", "") or "")[:600],
            "static": s_res,
            "static_pass_rate": (sum(x["weight"] for x in s_res if x["ok"] is True) /
                                 max(1e-9, sum(x["weight"] for x in s_res))) if s_res else 1.0,
            "behavior": b_res,
            "behavior_pass_rate": b_rate,
            "regressions": regressions,
            "newly_passing": next_pass,
        })
        prev_pass = ok_ids

    final = rounds_log[-1] if rounds_log else {}
    b_total = len(final.get("behavior", []))
    b_pass = len([r for r in final.get("behavior", []) if r["ok"]])
    b_rate_final = b_pass / b_total if b_total else 0.0
    regressions_total = sum(len(r["regressions"]) for r in rounds_log)
    regression_rate = min(1.0, regressions_total / b_pass) if b_pass else 1.0
    B = round(b_rate_final * (1 - 0.2 * min(1.0, regression_rate)), 4)

    s_items = final.get("static", [])
    S = (round(sum(x["weight"] for x in s_items if x["ok"] is True) /
               max(1e-9, sum(x["weight"] for x in s_items)), 4)) if s_items else 1.0

    # rubric judge（对本轮末产物一次性打分）
    judge = None
    if not skip_judge and judge_agent and task.rubric:
        try:
            judge = run_rubric_judge(task, prod, judge_agent)
        except Exception as e:  # judge 拉闸不致命
            judge = {"error": str(e)}
    if judge and "scores" in judge:
        # GameXpert 式四维（completeness/richness/player_exp/visual，各 0-5）
        dims = {k: round(float(v), 2) for k, v in judge["scores"].items()}
        P = round(sum(dims.values()) / (5.0 * len(dims)), 4) if dims else None
    else:
        dims = None
        P = None

    total = B * WEIGHTS["behavior"] + S * WEIGHTS["structure"] if P is None else \
        B * WEIGHTS["behavior"] + S * WEIGHTS["structure"] + P * WEIGHTS["presentation"]

    result = {
        "benchmark": "momozi-3A-GamegenBench",
        "version": "0.1.0",
        "task": task.id,
        "title": task.title,
        "family": task.family,
        "difficulty": task.difficulty,
        "engine": task.engine,
        "agent": adapter.name,
        "timestamp": stamp,
        "scores": {
            "B": B, "S": S, "P": P,
            "total": round(total, 4),
            "weights": WEIGHTS,
            "dimensions": dims,        # 四维原始分(0-5)
            "judge_raw": judge.get("raw") if judge else None,
            "judge_details": judge.get("details") if judge else None,
        },
        "behavior_pass_rate_final": b_rate_final,
        "regression_rate": regression_rate,
        "regressions_total": regressions_total,
        "rounds": rounds_log,
        "workspace": str(work),
    }
    RUNS_DIR = RUNS_ROOT / stamp
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    out = Path(out_path) if out_path else RUNS_DIR / f"{task.id}.{agent}.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "rounds"}, ensure_ascii=False, indent=2))
    for r in rounds_log:
        print(f"[{r['round']}] static={r['static_pass_rate']:.2f} "
              f"beh={r['behavior_pass_rate']:.2f} reg={r['regressions']}", file=sys.stderr)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(prog="momozi.run")
    ap.add_argument("task")
    ap.add_argument("--agent", default="mock")
    ap.add_argument("--out", default=None)
    ap.add_argument("--rounds", default=None, help="comma-separated round names")
    ap.add_argument("--skip-judge", action="store_true")
    ap.add_argument("--judge-agent", default=None,
                    help="rubric judge 用的 adapter profile（建议 claude / codex）")
    args = ap.parse_args(argv)
    run_task(args.task, args.agent, args.out,
             rounds_filter=args.rounds.split(",") if args.rounds else None,
             skip_judge=args.skip_judge, judge_agent=args.judge_agent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
