"""Rubric judge: 调用 adapter profile（默认 claude/codex）对产出的 index.html 打 0-5。
盲评协议：assessor 只看到 index.html + 需求描述，看不到 agent 名/模型。
"""
from __future__ import annotations

import json
import re
import subprocess
import tempfile
from pathlib import Path

from .task import Task
from .adapters import build_adapter, load_profiles

SCORING_TEMPLATE = """\
# Rubric Judge — 盲评
你是一名专业 3A 游戏评审官。请阅读以下「需求说明书」与「agent 产物代码」，给出 0-5 分。
- 0 = 不可玩/完全没满足
- 3 = 达到需求
- 5 = 超出需求（优秀手感/视觉/创意）

### 需求摘要
{spec}

### 产物 index.html（节选关键片段：点列关键实现）
{artifact}

### 评分维度（每维 0-5，给分理由在 detail 中）
{rubrics}

### 输出格式（严格 JSON 数组）
[ {{"id": "dim_id", "score": N, "detail": "..."}} ]
"""


def _artifact_digest(artifact_dir: Path, max_chars: int = 12000) -> str:
    entry = artifact_dir / "index.html"
    if not entry.exists():
        entry = next(artifact_dir.glob("*.html"), None)
    if not entry:
        return "(no html artifact)"
    text = entry.read_text(encoding="utf-8", errors="ignore")
    if len(text) > max_chars:
        text = text[:max_chars] + "\n... [truncated]"
    return text


def run_rubric_judge(task: Task, artifact_dir: Path, profile: str = "claude"):
    rubric_lines = "\n".join(
        f"- {r['id']}: {r.get('name', r['id'])} (权重 {r.get('weight', 0.25)}) — "
        f"评分锚点：{r.get('rubric', '见需求')}"
        for r in task.rubric
    )
    spec = task.rounds[-1].spec
    prompt = SCORING_TEMPLATE.format(
        spec=spec,
        artifact=_artifact_digest(artifact_dir),
        rubrics=rubric_lines,
    )
    adapter = build_adapter(profile, load_profiles(Path(__file__).resolve().parent.parent / "profiles.yaml"))
    res = adapter.generate(artifact_dir.parent, prompt, 0)
    raw = res.get("stdout", "") or ""
    # 提取 stdout 中的 JSON 数组
    m = re.search(r"\[[\s\S]*\]", raw)
    if not m:
        return {"error": "no json from judge", "stdout": raw[:600]}
    try:
        arr = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        return {"error": f"bad json: {e}", "stdout": raw[:600]}
    scores = {x["id"]: float(x["score"]) for x in arr if isinstance(x, dict) and "id" in x}
    details = {x["id"]: x.get("detail", "") for x in arr if isinstance(x, dict)}
    return {"raw": raw[:2000], "scores": scores, "details": details}
