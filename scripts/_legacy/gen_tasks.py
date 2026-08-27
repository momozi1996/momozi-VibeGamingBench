"""题目工厂 v1：把 N 道题一次性生成到 bench/tasks/。
每道 task dir 含一份 *_task.yaml + 从 bench/tests 复制的家族行为套件。
题面用家族模板 + 参数化数值，两轮（R1 基础 / R2 增量）。

生成: python3 scripts/gen_tasks.py --count 1000 --out bench/tasks
校验: python3 scripts/validate_pool.py
"""
from __future__ import annotations

import argparse
import random
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "bench"
REF_DIR = BENCH / "references"
SRC_TESTS = BENCH / "tests"

FAMILIES = {
    "physics_breakout": {
        "suite": "beh_breakout.mjs",
        "kwargs": ["cols", "rows", "paddle_half_w", "ball_speed"],
        "title": "3D 打砖块",
        "r1_extra": "拍宽 {paddle_half_w}，球速 {ball_speed}。",
        "r2_extra": "新增 3 层砖块硬度（hp 1/2/3），破 6 块落补速道具。",
    },
    "runner_dodge": {
        "suite": "beh_runner.mjs",
        "kwargs": ["lanes", "gravity", "jump_v", "speed"],
        "title": "跑酷躲避",
        "r1_extra": "{lanes} 条跑道，重力 {gravity}，跳跃初速 {jump_v}，滚动速度 {speed}。",
        "r2_extra": "加二段跳 + 减速道具；保持 R1 的跑酷手感不破。",
    },
    "turn_combat": {
        "suite": "beh_combat.mjs",
        "kwargs": ["n_units", "base_atk", "base_hp"],
        "title": "回合制战斗",
        "r1_extra": "{n_units} 个单位，攻击力 {base_atk}，血量 {base_hp}。",
        "r2_extra": "加 skill 冷却 + 状态回合；保持 R1 的老 behavior 不回潮。",
    },
    "economy_market": {
        "suite": "beh_market.mjs",
        "kwargs": ["items_n", "start_cash"],
        "title": "市场模拟",
        "r1_extra": "{items_n} 个物品，初始资金 {start_cash}。",
        "r2_extra": "加多轮供需调价与库存上限；R1 的买卖行为不回退。",
    },
}


def _pick_rng(i: int, stride: int) -> random.Random:
    return random.Random(i * 2654435761 % (2**32))


def _params(fam: str, i: int) -> dict:
    r = _pick_rng(i, 1).random  # 单轮 rng 就够（避免跨函数耦合）
    if fam == "physics_breakout":
        return dict(cols=4 + int(r() * 7), rows=2 + int(r() * 3),
                    paddle_half_w=round(1.6 + r() * 1.2, 2),
                    ball_speed=round(4 + r() * 3, 2))
    if fam == "runner_dodge":
        return dict(lanes=2 + int(r() * 3), gravity=round(14 + r() * 8, 2),
                    jump_v=round(7 + r() * 3, 2), speed=round(5 + r() * 4, 2))
    if fam == "turn_combat":
        return dict(n_units=4 + int(r() * 4), base_atk=2 + int(r() * 4),
                    base_hp=8 + int(r() * 8))
    if fam == "economy_market":
        return dict(items_n=4 + int(r() * 6), start_cash=500 + int(r() * 1500))
    raise SystemExit(f"unknown family {fam}")


_STATIC_BREAKOUT = """\
static:
  - kind: required_file
    role: entry
    path: index.html
    weight: 1.0
  - kind: required_file
    role: logic
    path: game_logic.js
    weight: 1.0
  - kind: contains
    path: index.html
    pattern: "THREE"
    weight: 0.5
  - kind: contains
    path: index.html
    pattern: "game_logic.js"
    weight: 0.5
  - kind: line_budget
    path: game_logic.js
    max_lines: 220
    weight: 0.5
"""
_STATIC_LOGIC = """\
static:
  - kind: required_file
    role: entry
    path: index.html
    weight: 1.0
  - kind: required_file
    role: logic
    path: game_logic.js
    weight: 1.0
  - kind: contains
    path: index.html
    pattern: "game_logic.js"
    weight: 1.0
  - kind: line_budget
    path: game_logic.js
    max_lines: 220
    weight: 1.0
"""
_TAIL = """\
behavior:
  script: __SUITE__
  timeout: 60
rubric:
  - id: completeness
    weight: 0.30
    max: 5
  - id: richness
    weight: 0.25
    max: 5
  - id: player_exp
    weight: 0.25
    max: 5
  - id: visual
    weight: 0.20
    max: 5
reference_dir: __REF__
"""


def render_yaml(fam: str, meta: dict, tid: str, params: dict) -> str:
    fam_def = FAMILIES[fam]
    r1 = ("# Round 1：基础可玩「{title}」\n"
          "交付：index.html + game_logic.js（单目录，纯前端 three.js，可离线打开）。\n"
          "逻辑层必须导出 createGame(opts) 与 advance(game, input, dt)。\n"
          "本轮参数：{extra}\n"
          "宏观要求：可玩、可暂停、可重开。").format(
        title=fam_def["title"], extra=fam_def["r1_extra"].format(**params))
    r2 = ("# Round 2：在此产物基础上做增量\n"
          "目标：{extra}\n"
          "**必须**保证 R1 的行为不破（beh_{suite} 的断言仍全过）。").format(
        extra=fam_def["r2_extra"].format(**params),
        suite=Path(fam_def["suite"]).stem.removeprefix("beh_"))
    return "\n".join([
        f"id: {tid}",
        f"title: {fam_def['title']} #{meta['idx']:04d}（参数化种子）",
        f"family: {fam}",
        "difficulty: easy",
        "rounds:",
        "  - name: R1",
        "    spec: |",
        *[f"      {line}" for line in r1.strip().splitlines()],
        "  - name: R2",
        "    spec: |",
        *[f"      {line}" for line in r2.strip().splitlines()],
        (_STATIC_BREAKOUT if fam == "physics_breakout" else _STATIC_LOGIC)
        + _TAIL.replace("__SUITE__", fam_def["suite"]).replace("__REF__", f"bench/references/{fam}"),
    ])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1000)
    ap.add_argument("--out", default="bench/tasks")
    ap.add_argument("--prune", action="store_true")
    args = ap.parse_args(argv)

    out_dir = Path(args.out)
    if args.prune and out_dir.exists():
        for p in sorted(out_dir.glob("t*")):
            if p.is_dir():
                shutil.rmtree(p)
    out_dir.mkdir(parents=True, exist_ok=True)

    fam_keys = list(FAMILIES)
    per = args.count // len(fam_keys)
    total = 0
    for fi, fam in enumerate(fam_keys):
        for i in range(per):
            idx = fi * 1000 + i
            tid = f"t{idx:04d}_{fam}"
            p = out_dir / tid
            p.mkdir(parents=True, exist_ok=True)
            params = _params(fam, idx)
            y = render_yaml(fam, {"idx": idx}, tid, params)
            (p / f"{tid}.task.yaml").write_text(y, encoding="utf-8")
            suite = Path(FAMILIES[fam]["suite"]).name
            if (SRC_TESTS / suite).exists():
                shutil.copy(SRC_TESTS / suite, p / suite)
            total += 1
    print(f"generated {total} tasks under {out_dir}")


if __name__ == "__main__":
    main()
