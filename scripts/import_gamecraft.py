"""把 gamecraft_queries/prompts+grading 转换成 momozi-3A-GamegenBench 原生任务。

原 BMK 是 Godot 工程任务（14 个族、140 题、hidden grading JSON）。
本转换把每题落成 momozi 任务目录：

  bench/tasks/gc_<name>/gc_<name>.task.yaml
  bench/tasks/gc_<name>/prompt.md              # 原命题（等同"玩家视角"spec）
  bench/tasks/gc_<name>/rubric.mapping.json    # 原 rubric 到 momozi 4 维的映射

原 rubric 结构：
  {
    "score_formula": "...",
    "build_check":  {"BUILD": ...},
    "categories":   [{"name": "Core Mechanics", "items": ["M1", ...]}, ...],
    "requirements": [{"id": "M1", "agg": "max", "description": "..."}]
  }

映射规则（评分维度 geno-compat）：
  M* (Core Mechanics)      → completeness (权重 0.30)
  D* (Content Depth)       → richness    (权重 0.25)
  V* (Functional Visuals)  → player_exp  (权重 0.25)
  A* (Presentation & Art)  → visual      (权重 0.20)
  BUILD（godot 门控）       → 硬性 gate，不通过按 P=0 处理

用法: python3 scripts/import_gamecraft.py [--limit N]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path("/Users/jyxc-dz-0100378/AAAtest/gamecraft_queries")
PROMPT_DIR = SRC / "prompts"
GRADE_DIR = SRC / "grading"
OUT_DIR = ROOT / "bench" / "tasks"

# idx → 题族，来自 INDEX.md 的表格；本地静态写下来，避免依赖外部索引变更
# （140 条里每条的题族关键词与 bundle 内的 name 前缀一一对应是稳定的）
def family_of(name: str) -> str:
    for fam in ("cardgame", "horror", "idle", "openworld", "platformer",
                "puzzle", "racing", "rhythm", "roguelike", "shooter",
                "simulation", "sports", "strategy", "tycoon", "visualnovel"):
        if name.startswith(fam + "-") or name == fam:
            return fam
    return "other"


def build_yaml(name: str, title: str, family: str, rubric_ids: dict) -> str:
    """rubric_ids: {"completeness": [...], "richness": [...], ...}"""
    def ids(prefix):
        return rubric_ids.get(prefix, [])
    return "\n".join([
        f'id: gc_{name}',
        f'title: "{title}"',
        f'family: {family}',
        'difficulty: expert',
        'engine: godot',
        'rounds:',
        '  - name: R1',
        '    spec: |',
        *[f'      {ln}' for ln in _prompt_body(name).splitlines()],
        'static:',
        '  - kind: required_file',
        '    role: entry',
        '    path: project.godot',
        '    weight: 1.0',
        '  - kind: required_file',
        '    path: demo_outputs',
        '    weight: 1.0',
        'behavior:',
        '  script: beh_build.mjs',
        '  timeout: 300',
        'rubric:',
        '  - id: completeness',
        '    weight: 0.30',
        '    max: 5',
        '    anchors: ' + json.dumps(ids("completeness"), ensure_ascii=False),
        '  - id: richness',
        '    weight: 0.25',
        '    max: 5',
        '    anchors: ' + json.dumps(ids("richness"), ensure_ascii=False),
        '  - id: player_exp',
        '    weight: 0.25',
        '    max: 5',
        '    anchors: ' + json.dumps(ids("player_exp"), ensure_ascii=False),
        '  - id: visual',
        '    weight: 0.20',
        '    max: 5',
        '    anchors: ' + json.dumps(ids("visual"), ensure_ascii=False),
        '',
    ])


_probe_cache: dict[str, str] = {}


def _prompt_body(name: str) -> str:
    if name in _probe_cache:
        return _probe_cache[name]
    p = PROMPT_DIR / f"{name}.md"
    body = p.read_text(encoding="utf-8").strip() if p.exists() else "(原命题未找到)"
    _probe_cache[name] = body
    return body


def import_bundle(limit: int | None = None) -> dict:
    grds = sorted(GRADE_DIR.glob("*.json"))
    if limit:
        grds = grds[:limit]
    imported, skipped = [], []
    for gpath in grds:
        name = gpath.stem
        try:
            g = json.loads(gpath.read_text(encoding="utf-8"))
        except Exception as e:
            skipped.append((name, f"rubric parse: {e}"))
            continue
        prompt_md = PROMPT_DIR / f"{name}.md"
        if not prompt_md.exists():
            skipped.append((name, "no prompt"))
            continue
        fam = family_of(name)
        reqs = g.get("requirements", [])
        rubric_ids = {
            "completeness": [r["id"] for r in reqs if r["id"].startswith("M") and r["id"][1:].isdigit()],
            "richness":    [r["id"] for r in reqs if r["id"].startswith("D") and r["id"][1:].isdigit()],
            "player_exp":  [r["id"] for r in reqs if r["id"].startswith("V") and r["id"][1:].isdigit()],
            "visual":      [r["id"] for r in reqs if r["id"].startswith("A") and r["id"][1:].isdigit()],
        }
        title = name.replace("-", " ")
        out = OUT_DIR / f"gc_{name}"
        out.mkdir(parents=True, exist_ok=True)
        (out / f"gc_{name}.task.yaml").write_text(build_yaml(name, title, fam, rubric_ids), encoding="utf-8")
        (out / "prompt.md").write_text(_prompt_body(name), encoding="utf-8")
        (out / "rubric.original.json").write_text(gpath.read_text(encoding="utf-8"), encoding="utf-8")
        (out / "rubric.mapping.json").write_text(json.dumps(rubric_ids, ensure_ascii=False, indent=2), encoding="utf-8")
        imported.append({"name": name, "family": fam, "n_reqs": len(reqs)})
    return {"imported": imported, "skipped": skipped}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--summary", default=str(ROOT / "bench" / "GAMECRAFT_IMPORT.json"))
    args = ap.parse_args(argv)

    res = import_bundle(args.limit)
    Path(args.summary).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"imported {len(res['imported'])} tasks, skipped {len(res['skipped'])}")
    if res["skipped"]:
        print("skipped:", res["skipped"][:5])


if __name__ == "__main__":
    main()
