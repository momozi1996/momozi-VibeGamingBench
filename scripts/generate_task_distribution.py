"""Validate task metadata and generate bench/TASK_DISTRIBUTION.md."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from task_metadata import classify_difficulty


ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "bench" / "tasks"
REPORT = ROOT / "bench" / "TASK_DISTRIBUTION.md"
EXPECTED_CONCEPTS = 711
EXPECTED_LANGUAGES = {"en", "zh"}
EXPECTED_TASK_FILES = {
    "prompt.md",
    "rubric.mapping.json",
    "rubric.original.json",
}
DIFFICULTIES = ("low", "medium", "high")

PROVENANCE_KINDS = {
    "existing_pool",
    "adapted_article_prompt",
    "adapted_user_prompt",
    "adapted_summerengine_template",
    "adapted_cnblogs_prompt",
    "adapted_evolink_prompt",
    "adapted_aiga_shared_world",
    "adapted_feishu_game_prompt",
    "structured_feishu_game_seed",
}


def _task_yaml_path(task_dir: Path) -> Path:
    paths = sorted(task_dir.glob("*.task.yaml"))
    if len(paths) != 1:
        raise ValueError(f"{task_dir}: expected one task YAML, found {len(paths)}")
    return paths[0]


def _read_tasks() -> list[dict]:
    records = []
    task_dirs = sorted(path for path in TASKS.iterdir() if path.is_dir())
    for task_dir in task_dirs:
        yaml_path = _task_yaml_path(task_dir)
        raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        prompt = (task_dir / "prompt.md").read_text(encoding="utf-8").strip()
        records.append(
            {
                "dir": task_dir,
                "yaml_path": yaml_path,
                "raw": raw,
                "prompt": prompt,
            }
        )
    return records


def _group_records(records: list[dict]) -> dict[str, dict[str, dict]]:
    groups: dict[str, dict[str, dict]] = defaultdict(dict)
    for record in records:
        raw = record["raw"]
        groups[raw.get("base_task_id", "")][raw.get("language", "")] = record
    return groups


def _expected_difficulties(records: list[dict]) -> dict[str, str]:
    expected = {}
    for base_id, variants in _group_records(records).items():
        if set(variants) != EXPECTED_LANGUAGES:
            raise ValueError(f"{base_id}: expected en/zh pair, found {sorted(variants)}")
        english = variants["en"]
        expected[base_id] = classify_difficulty(
            english["raw"].get("family", "unspecified"),
            english["prompt"],
        )
    return expected


def _normalize_yaml(record: dict, difficulty: str) -> None:
    path = record["yaml_path"]
    text = path.read_text(encoding="utf-8")
    text, count = re.subn(
        r"(?m)^difficulty:\s*\S+\s*$",
        f"difficulty: {difficulty}",
        text,
        count=1,
    )
    if count != 1:
        raise ValueError(f"{path}: missing unique difficulty field")

    text = text.replace("  path: project.html\n", "  path: index.html\n")
    text = text.replace(
        "- kind: required_file\n  path: demo_outputs\n",
        "- kind: required_file\n  role: logic\n  path: game_logic.js\n",
    )
    text = text.replace(
        "Same pattern as `bench/references/tg1/game_logic.js`.",
        "Keep the rules layer independent of DOM and rendering code.",
    )
    text = text.replace(
        "规范参考 `bench/references/tg1/game_logic.js`。",
        "规则层需独立于 DOM 和渲染代码。",
    )
    if "\nprovenance:\n" not in text:
        marker = "\nrounds:\n"
        if marker not in text:
            raise ValueError(f"{path}: cannot insert provenance before rounds")
        text = text.replace(
            marker,
            "\nprovenance:\n  kind: existing_pool\nrounds:\n",
            1,
        )
    path.write_text(text, encoding="utf-8")


def _normalize_prompt(record: dict) -> None:
    path = record["dir"] / "prompt.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "Same pattern as `bench/references/tg1/game_logic.js`.",
        "Keep the rules layer independent of DOM and rendering code.",
    )
    text = text.replace(
        "规范参考 `bench/references/tg1/game_logic.js`。",
        "规则层需独立于 DOM 和渲染代码。",
    )
    path.write_text(text, encoding="utf-8")


def _normalize_rubric(task_dir: Path) -> None:
    path = task_dir / "rubric.original.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    build = raw.setdefault("build_check", {})
    expected = {
        "id": "BUILD",
        "cmd": "momozi HTML static BUILD gate",
        "description": (
            "index.html and game_logic.js exist, a canvas/WebGL renderer is present, "
            "and no disallowed heavy runtime asset references are used."
        ),
    }
    if build != expected:
        raw["build_check"] = expected
        path.write_text(
            json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def _write_metadata(records: list[dict]) -> None:
    expected = _expected_difficulties(records)
    for record in records:
        base_id = record["raw"]["base_task_id"]
        _normalize_yaml(record, expected[base_id])
        _normalize_prompt(record)
        _normalize_rubric(record["dir"])


def _validate(records: list[dict]) -> dict[str, dict[str, dict]]:
    groups = _group_records(records)
    if len(records) != EXPECTED_CONCEPTS * 2:
        raise ValueError(
            f"expected {EXPECTED_CONCEPTS * 2} tasks, found {len(records)}"
        )
    if len(groups) != EXPECTED_CONCEPTS:
        raise ValueError(f"expected {EXPECTED_CONCEPTS} concepts, found {len(groups)}")

    expected_difficulty = _expected_difficulties(records)
    public_tests = {path.name for path in (ROOT / "bench" / "tests").glob("*.mjs")}

    for base_id, variants in groups.items():
        if set(variants) != EXPECTED_LANGUAGES:
            raise ValueError(f"{base_id}: incomplete language pair")
        pair_family = {record["raw"].get("family") for record in variants.values()}
        pair_source = {
            (record["raw"].get("provenance") or {}).get("kind")
            for record in variants.values()
        }
        if len(pair_family) != 1 or len(pair_source) != 1:
            raise ValueError(f"{base_id}: paired family or audit metadata differs")

        for language, record in variants.items():
            raw = record["raw"]
            task_dir = record["dir"]
            expected_names = EXPECTED_TASK_FILES | {f"{raw['id']}.task.yaml"}
            actual_names = {path.name for path in task_dir.iterdir() if path.is_file()}
            if actual_names != expected_names:
                raise ValueError(
                    f"{task_dir}: expected {sorted(expected_names)}, found {sorted(actual_names)}"
                )
            if raw["id"] != task_dir.name:
                raise ValueError(f"{record['yaml_path']}: id differs from directory")
            if raw["base_task_id"] != base_id or raw["language"] != language:
                raise ValueError(f"{record['yaml_path']}: invalid pair metadata")
            rounds = raw.get("rounds") or []
            if len(rounds) != 1 or rounds[0].get("spec", "").strip() != record["prompt"]:
                raise ValueError(f"{record['yaml_path']}: prompt and R1 spec differ")
            if raw.get("difficulty") != expected_difficulty[base_id]:
                raise ValueError(
                    f"{record['yaml_path']}: difficulty={raw.get('difficulty')}, "
                    f"expected {expected_difficulty[base_id]}"
                )
            source_kind = (raw.get("provenance") or {}).get("kind")
            if source_kind not in PROVENANCE_KINDS:
                raise ValueError(
                    f"{record['yaml_path']}: unknown provenance kind {source_kind}"
                )

            required = {
                (item.get("role"), item.get("path"))
                for item in raw.get("static", [])
                if item.get("kind") == "required_file"
            }
            if required != {("entry", "index.html"), ("logic", "game_logic.js")}:
                raise ValueError(f"{record['yaml_path']}: stale static file contract")
            behavior_script = (raw.get("behavior") or {}).get("script")
            if behavior_script not in public_tests:
                raise ValueError(
                    f"{record['yaml_path']}: missing public behavior script {behavior_script}"
                )

            rubric = raw.get("rubric") or []
            rubric_ids = [item.get("id") for item in rubric]
            if rubric_ids != ["completeness", "richness", "player_exp", "visual"]:
                raise ValueError(f"{record['yaml_path']}: unexpected rubric dimensions")
            if abs(sum(float(item.get("weight", 0)) for item in rubric) - 1.0) > 1e-9:
                raise ValueError(f"{record['yaml_path']}: rubric weights do not sum to 1")

            mapping = json.loads(
                (task_dir / "rubric.mapping.json").read_text(encoding="utf-8")
            )
            original = json.loads(
                (task_dir / "rubric.original.json").read_text(encoding="utf-8")
            )
            if list(mapping) != rubric_ids:
                raise ValueError(f"{task_dir}: rubric mapping dimensions differ")
            requirement_ids = {
                item.get("id") for item in original.get("requirements", [])
            }
            mapped_ids = {item for items in mapping.values() for item in items}
            if not mapped_ids or not mapped_ids <= requirement_ids:
                raise ValueError(f"{task_dir}: rubric mapping references missing anchors")
            if original.get("build_check", {}).get("cmd") != "momozi HTML static BUILD gate":
                raise ValueError(f"{task_dir}: stale rubric BUILD command")
    return groups


def _percent(count: int, total: int) -> str:
    return f"{count * 100 / total:.1f}%"


def _render_report(groups: dict[str, dict[str, dict]]) -> str:
    concepts = [variants["en"] for variants in groups.values()]
    family_counts = Counter(record["raw"]["family"] for record in concepts)
    difficulty_counts = Counter(record["raw"]["difficulty"] for record in concepts)

    family_difficulty: dict[str, Counter] = defaultdict(Counter)
    for record in concepts:
        difficulty = record["raw"]["difficulty"]
        family_difficulty[record["raw"]["family"]][difficulty] += 1

    lines = [
        "# momozi-VibeGamingBench 题目分布统计",
        "",
        "本报告由任务 YAML、提示词和 rubric 文件自动生成。",
        "运行 `python3 scripts/generate_task_distribution.py --check` 可确认统计与题池一致。",
        "",
        "## 总览",
        "",
        f"- 游戏概念：**{len(concepts)}**",
        f"- 按语言拆分后的题目：**{len(concepts) * 2}**",
        f"- 英文题：**{len(concepts)}**",
        f"- 中文题：**{len(concepts)}**",
        f"- 游戏类型：**{len(family_counts)}**",
        "",
        "## 题目设计组成",
        "",
        "每道语言独立题都是一个严格的四文件评测记录：",
        "",
        "| 文件 | 作用 | 数量 |",
        "|---|---|---:|",
        f"| `*.task.yaml` | ID、语言、类型、难度、产物契约和评分维度 | {len(concepts) * 2} |",
        f"| `prompt.md` | 直接提供给 coding agent 的生成提示词 | {len(concepts) * 2} |",
        f"| `rubric.original.json` | 具体玩法、深度、体验与美术锚点 | {len(concepts) * 2} |",
        f"| `rubric.mapping.json` | 细粒度锚点到四个评分维度的映射 | {len(concepts) * 2} |",
        "",
        "每个概念都有独立的英文题和中文题。两者共享游戏类型、难度和 rubric 结构，",
        "但生成提示词严格保持单语隔离。",
        "",
        "题目由四层设计共同组成：",
        "",
        "| 设计层 | 作用 |",
        "|---|---|",
        "| 单语需求层 | 描述核心循环、操作、系统关系、反馈和完成条件 |",
        "| 确定性合同层 | 固定 `index.html + game_logic.js` 交付，并检查规则层导出 |",
        "| 评分锚点层 | 将可验证需求映射到完整度、丰富度、玩家体验和视觉四维 |",
        "| 分层元数据 | 标记语言、游戏类型与实现难度，支持筛选和分组评测 |",
        "",
        "### 语言设计",
        "",
        "| 语言 | 概念数 | 独立题数 | 占比 |",
        "|---|---:|---:|---:|",
        f"| `en` | {len(concepts)} | {len(concepts)} | 50.0% |",
        f"| `zh` | {len(concepts)} | {len(concepts)} | 50.0% |",
        f"| **Total** | **{len(concepts)}** | **{len(concepts) * 2}** | **100.0%** |",
        "",
        "## 游戏类型分布",
        "",
        "| 游戏类型 | 概念数 | 题目数 | 占比 |",
        "|---|---:|---:|---:|",
    ]
    for family in sorted(family_counts):
        count = family_counts[family]
        lines.append(
            f"| `{family}` | {count} | {count * 2} | {_percent(count, len(concepts))} |"
        )
    lines.extend(
        [
            f"| **Total** | **{len(concepts)}** | **{len(concepts) * 2}** | **100.0%** |",
            "",
            "## 难度等级分布",
            "",
            "难度衡量浏览器垂直切片的实现复杂度，不表示类型价值或模型预期得分。确定性分类器",
            "综合游戏类型基础分、3D 范围、系统数量，以及物理、AI、模拟、持久状态、联网、",
            "程序生成和高级渲染信号。4 分及以下为 `low`，5-7 分为 `medium`，8 分及以上",
            "为 `high`。同一概念的中英文题始终共享一个难度等级。",
            "",
            "| 难度 | 概念数 | 题目数 | 占比 |",
            "|---|---:|---:|---:|",
        ]
    )
    for difficulty in DIFFICULTIES:
        count = difficulty_counts[difficulty]
        lines.append(
            f"| `{difficulty}` | {count} | {count * 2} | {_percent(count, len(concepts))} |"
        )
    lines.extend(
        [
            f"| **Total** | **{len(concepts)}** | **{len(concepts) * 2}** | **100.0%** |",
            "",
            "### 各游戏类型难度分布",
            "",
            "| 游戏类型 | 低 | 中 | 高 | 概念总数 |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for family in sorted(family_counts):
        counts = family_difficulty[family]
        lines.append(
            f"| `{family}` | {counts['low']} | {counts['medium']} | "
            f"{counts['high']} | {sum(counts.values())} |"
        )
    lines.extend(
        [
            "",
            "## 一致性门禁",
            "",
            f"- {len(concepts)} 个完整的中英文概念对。",
            "- 每个任务目录严格四个文件。",
            "- Task ID、目录名、语言后缀和 `base_task_id` 一致。",
            "- `prompt.md` 与 `rounds[0].spec` 完全一致。",
            "- 中英文变体共享类型和难度。",
            "- 静态产物契约要求 `index.html` 和 `game_logic.js`。",
            "- Rubric 权重合计为 1.0，所有映射锚点均存在。",
            "- 每个声明的行为检查脚本都存在于 `bench/tests/`。",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="normalize task metadata and write the generated Markdown report",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when task metadata or the generated report is stale",
    )
    args = parser.parse_args(argv)
    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")

    records = _read_tasks()
    if args.write:
        _write_metadata(records)
        records = _read_tasks()
    groups = _validate(records)
    rendered = _render_report(groups)

    if args.write:
        REPORT.write_text(rendered, encoding="utf-8")
        print(f"wrote {REPORT}: {len(groups)} concepts, {len(records)} tasks")
        return 0
    if args.check:
        if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(
                f"{REPORT} is stale; run scripts/generate_task_distribution.py --write"
            )
        print(f"task distribution current: {len(groups)} concepts, {len(records)} tasks")
        return 0

    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
