"""Rubric judge: 调用 adapter profile（默认 claude/codex）对产出的 index.html 打 0-5。
盲评协议：assessor 只看到 index.html + 需求描述，看不到 agent 名/模型。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .task import Task
from .adapters import build_adapter, load_profiles

SCORING_TEMPLATE = """\
# Rubric Judge — 盲评
你是一名专业的游戏评审。请阅读「需求说明书」与「agent 产物代码」，按下列四维各给 0-5 分。
- 0 = 不可用/完全没满足
- 3 = 达到需求（达标）
- 5 = 优秀（超出预期）

重要：评分只看代码 + 需求，不要考虑 agent 是谁、模型是什么。

### 需求摘要（R1+R2 全部要求）
{spec}

### 产物 index.html（节选关键实现片段）
{artifact}

### 评分维度与锚点（严格遵守锚点范围）
{rubrics}

### 输出格式（严格 JSON 数组，含 detail 说明理由）
[ {{"id": "completeness", "score": N, "detail": "..."}}, {{"id": "richness", "score": N, "detail": "..."}}, {{"id": "player_exp", "score": N, "detail": "..."}}, {{"id": "visual", "score": N, "detail": "..."}} ]
"""


def _artifact_digest(artifact_dir: Path, max_chars: int = 24000) -> str:
    paths = [artifact_dir / "index.html", artifact_dir / "game_logic.js"]
    available = [path for path in paths if path.exists()]
    if not available:
        return "(no index.html or game_logic.js artifact)"
    per_file = max(2000, max_chars // len(available))
    sections = []
    for path in available:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if len(text) > per_file:
            text = text[:per_file] + "\n... [truncated]"
        sections.append(f"## {path.name}\n{text}")
    return "\n\n".join(sections)


def _rubric_text(task: Task) -> str:
    original_path = task.path.parent / "rubric.original.json"
    mapping_path = task.path.parent / "rubric.mapping.json"
    if not original_path.exists() or not mapping_path.exists():
        return "\n".join(
            f"- {item['id']}: {item.get('rubric', 'See the task specification.')}"
            for item in task.rubric
        )

    original = json.loads(original_path.read_text(encoding="utf-8"))
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    requirements = {
        item["id"]: item.get("description", "")
        for item in original.get("requirements", [])
        if item.get("id")
    }
    sections = []
    for dimension in task.rubric:
        dimension_id = dimension["id"]
        sections.append(
            f"### {dimension_id} (weight {dimension.get('weight', 0):.2f})"
        )
        for anchor_id in mapping.get(dimension_id, dimension.get("anchors", [])):
            sections.append(f"- {anchor_id}: {requirements.get(anchor_id, 'Missing anchor')}")
    return "\n".join(sections)


def _extract_json_array(text: str) -> list | None:
    candidates = []
    stripped = text.strip()
    if stripped:
        candidates.append(stripped)
    candidates.extend(
        match.group(1).strip()
        for match in re.finditer(r"```(?:json)?\s*([\s\S]*?)```", text)
    )
    decoder = json.JSONDecoder()
    for index, char in enumerate(text):
        if char != "[":
            continue
        try:
            value, _ = decoder.raw_decode(text[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, list):
            candidates.append(value)

    for candidate in reversed(candidates):
        if isinstance(candidate, list):
            return candidate
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(value, list):
            return value
    return None


def run_rubric_judge(task: Task, artifact_dir: Path, profile: str = "claude"):
    rubric_lines = _rubric_text(task)
    spec = "\n\n".join(
        f"## {round_spec.name}\n{round_spec.spec}" for round_spec in task.rounds
    )
    prompt = SCORING_TEMPLATE.format(
        spec=spec,
        artifact=_artifact_digest(artifact_dir),
        rubrics=rubric_lines,
    )
    adapter = build_adapter(
        profile,
        load_profiles(Path(__file__).resolve().parent.parent / "profiles.yaml"),
        allow_writes=False,
    )
    res = adapter.generate(artifact_dir.parent, prompt, 0)
    raw = res.get("stdout", "") or ""
    arr = _extract_json_array(raw)
    if arr is None:
        return {"error": "no json from judge", "stdout": raw[:600]}
    scores = {
        item["id"]: max(0.0, min(5.0, float(item["score"])))
        for item in arr
        if isinstance(item, dict) and "id" in item and "score" in item
    }
    details = {x["id"]: x.get("detail", "") for x in arr if isinstance(x, dict)}
    expected_ids = {item["id"] for item in task.rubric}
    if set(scores) != expected_ids:
        return {
            "error": f"judge dimensions mismatch: expected {sorted(expected_ids)}, got {sorted(scores)}",
            "stdout": raw[:600],
        }
    return {"raw": raw[:2000], "scores": scores, "details": details}
