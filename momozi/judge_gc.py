"""GameCraft-derived rubric judge。

结构对齐原始 GameCraft-Bench 评测：
- SYSTEM:  "You are a strict but fair video-game evaluator..." (0/0.5/1 分段)
- USER:    "Evaluate the recording against each of the following requirements." + M/D/V/A 全条目
- 输入:    录屏/截图帧 (multimodal)；无录屏时退化为 index.html + 静态截图
- 输出:    {"scores": {"M1": x, ...}, "rationales": {...}}

GC 重打分公式 (score_formula)：
    score = BUILD · (0.15·mean(M) + 0.35·mean(D) + 0.15·mean(V) + 0.35·mean(A))
被 momozi 记为 B 维（外加 S 静态合规）；P 维另走 4 维归一 (completeness/.../richness/...).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .task import Task
from .adapters import build_adapter, load_profiles

SYSTEM_PROMPT = """You are a strict but fair video-game evaluator. Given a short playthrough recording of a Godot 2D game, decide how clearly each listed requirement is demonstrated. Score every requirement on a 0.0 to 1.0 scale where 0.0 = not demonstrated at all (or contradicted), 0.5 = partially demonstrated / ambiguous, and 1.0 = clearly and unambiguously demonstrated by what is visible in the recording. Reply with strict JSON only, no prose, no markdown, no code fences."""


def _render_user_prompt(requirements: list[dict]) -> str:
    lines = ["Evaluate the recording against each of the following requirements.",
             "", "Requirements:"]
    for r in requirements:
        lines.append(f"- {r['id']}: {r['description']}")
    out = "\n".join(lines)
    out += "\n\nReturn JSON in exactly this shape (no extra keys, no markdown):\n"
    ids = ", ".join(f'"{r["id"]}": <0..1>' for r in requirements)
    scores_obj = "{" + ids + "}"
    rats_obj = "{" + ", ".join(f'"{r["id"]}": "<one short sentence>"' for r in requirements) + "}"
    out += '{\n  "scores": ' + scores_obj + ',\n  "rationales": ' + rats_obj + '\n}\n'
    return out


def run_gc_rubric_judge(task: Task, artifact_dir: Path, profile: str = "claude") -> dict:
    """调用 adapter，传入原 BMK 风格的 SYSTEM+USER。artifact_dir 里要有 demo_outputs/*.mp4。"""
    mapping = json.loads((Path(task.path).parent / "rubric.mapping.json").read_text(encoding="utf-8"))
    # 汇总所有维度的 requirement (M*/D*/V*/A*)
    all_ids = []
    for k in ("completeness", "richness", "player_exp", "visual"):
        all_ids += mapping.get(k, [])
    # 从 rubric.original.json 里取逐条描述
    original = json.loads((Path(task.path).parent / "rubric.original.json").read_text(encoding="utf-8"))
    reqs = {r["id"]: r for r in original.get("requirements", [])}
    ordered_reqs = [reqs[i] for i in all_ids if i in reqs]
    sys_p = SYSTEM_PROMPT
    user_p = _render_user_prompt(ordered_reqs)

    # 拼成多模态 prompt：首段文本 + 视频/截图附件引用（adapter 端处理）
    prompt = sys_p + "\n\n" + user_p
    # 把 artifact 里没有的 demo 转成 screenshot-only（降级）
    demos = list((artifact_dir / "demo_outputs").glob("*.mp4")) if (artifact_dir / "demo_outputs").exists() else []

    adapter = build_adapter(profile, load_profiles(Path(__file__).resolve().parent.parent / "profiles.yaml"))
    payload = prompt + ("\n\n[demo video attached: %s]" % demos[0].name if demos else
                        "\n\n[No video — fall back to stitched screenshots of index.html running state]")
    res = adapter.generate(artifact_dir.parent, payload, 0)
    raw = res.get("stdout", "") or ""

    m = re.search(r"\{[\s\S]*\}", raw)
    if not m:
        return {"error": "no_json", "stdout": raw[:800]}
    try:
        parsed = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        return {"error": f"bad_json: {e}", "stdout": raw[:800]}

    scores = parsed.get("scores", {}) or {}
    rationales = parsed.get("rationales", {}) or {}

    # 按 GC 公式聚合（mo...实际分）
    _M = [scores.get(i) for i in mapping.get("completeness", []) if scores.get(i) is not None]
    _D = [scores.get(i) for i in mapping.get("richness", []) if scores.get(i) is not None]
    _V = [scores.get(i) for i in mapping.get("player_exp", []) if scores.get(i) is not None]
    _A = [scores.get(i) for i in mapping.get("visual", []) if scores.get(i) is not None]
    mean = lambda xs: sum(xs) / len(xs) if xs else 0.0
    gc_score = 0.15 * mean(_M) + 0.35 * mean(_D) + 0.15 * mean(_V) + 0.35 * mean(_A)

    return {
        "raw": raw[:1500],
        "scores": scores,
        "rationales": rationales,
        "dimensions": {"completeness": mean(_M), "richness": mean(_D),
                        "player_exp": mean(_V), "visual": mean(_A)},
        "gc_formula_score": round(gc_score, 4),
    }
