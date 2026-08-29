#!/usr/bin/env python3
"""Audit task schema, bilingual pairs, duplicates, provenance, and rubrics."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TASKS_ROOT = ROOT / "bench" / "tasks"
DEFAULT_JSON = ROOT / "reports" / "task_audit.json"
DEFAULT_MD = ROOT / "reports" / "task_audit.md"


def _normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def audit_tasks(tasks_root: Path = DEFAULT_TASKS_ROOT) -> dict[str, Any]:
    tasks_root = Path(tasks_root)
    try:
        display_root = tasks_root.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        display_root = str(tasks_root)
    records = []
    errors: list[dict[str, str]] = []
    exact: Counter[str] = Counter()
    normalized: Counter[str] = Counter()
    family = Counter()
    difficulty = Counter()
    provenance = Counter()
    rubric_missing = []
    directories = sorted(path for path in tasks_root.iterdir() if path.is_dir())

    for task_dir in directories:
        yaml_files = sorted(task_dir.glob("*.task.yaml"))
        record: dict[str, Any] = {"task_dir": task_dir.name}
        if len(yaml_files) != 1:
            errors.append(
                {
                    "task": task_dir.name,
                    "error": f"expected one YAML, found {len(yaml_files)}",
                }
            )
            continue
        path = yaml_files[0]
        try:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise ValueError("YAML root must be an object")
            prompt_path = task_dir / "prompt.md"
            prompt = prompt_path.read_text(encoding="utf-8").strip()
            if raw.get("id") != task_dir.name:
                raise ValueError("id does not match directory")
            if not raw.get("base_task_id"):
                raise ValueError("base_task_id is missing")
            if raw.get("language") not in {"en", "zh"}:
                raise ValueError("language must be en or zh")
            if not raw.get("rounds"):
                raise ValueError("rounds is missing")
            if raw["rounds"][0].get("spec", "").strip() != prompt:
                raise ValueError("prompt.md differs from rounds[0].spec")
            record.update(
                {
                    "id": raw["id"],
                    "base_task_id": raw["base_task_id"],
                    "language": raw["language"],
                    "family": raw.get("family", "unspecified"),
                    "difficulty": raw.get("difficulty", "unspecified"),
                    "prompt": prompt,
                    "provenance": raw.get("provenance") or {},
                    "rubric": raw.get("rubric") or [],
                }
            )
            exact[prompt] += 1
            normalized[_normalized(prompt)] += 1
            family[record["family"]] += 1
            difficulty[record["difficulty"]] += 1
            provenance[record["provenance"].get("kind", "<missing>")] += 1
            if not record["rubric"]:
                rubric_missing.append(task_dir.name)
        except Exception as exc:
            errors.append({"task": task_dir.name, "error": str(exc)})
            continue
        expected_files = {
            f"{task_dir.name}.task.yaml",
            "prompt.md",
            "rubric.original.json",
            "rubric.mapping.json",
        }
        actual_files = {path.name for path in task_dir.iterdir() if path.is_file()}
        if actual_files != expected_files:
            errors.append(
                {
                    "task": task_dir.name,
                    "error": f"file contract differs: {sorted(actual_files)}",
                }
            )
        records.append(record)

    pairs: dict[str, dict[str, dict]] = defaultdict(dict)
    for record in records:
        pairs[record["base_task_id"]][record["language"]] = record
    bad_pairs = {
        base: sorted(languages)
        for base, languages in pairs.items()
        if set(languages) != {"en", "zh"}
    }
    family_concepts = Counter(
        variants["en"]["family"]
        for variants in pairs.values()
        if "en" in variants
    )
    difficulty_concepts = Counter(
        variants["en"]["difficulty"]
        for variants in pairs.values()
        if "en" in variants
    )
    exact_groups = {
        hashlib.sha256(text.encode("utf-8")).hexdigest(): count
        for text, count in exact.items()
        if count > 1
    }
    normalized_groups = {
        hashlib.sha256(text.encode("utf-8")).hexdigest(): count
        for text, count in normalized.items()
        if count > 1
    }
    return {
        "tasks_root": display_root,
        "task_count": len(records),
        "concept_count": len(pairs),
        "language_counts": Counter(
            record["language"] for record in records
        ),
        "pair_count": len(pairs),
        "bad_pairs": bad_pairs,
        "exact_duplicate_groups": exact_groups,
        "normalized_duplicate_groups": normalized_groups,
        "provenance_counts": provenance,
        "family_task_counts": family,
        "difficulty_task_counts": difficulty,
        "family_concept_counts": family_concepts,
        "difficulty_concept_counts": difficulty_concepts,
        "rubric_missing": rubric_missing,
        "schema_errors": errors,
        "status": "pass"
        if not bad_pairs
        and not exact_groups
        and not normalized_groups
        and not rubric_missing
        and not errors
        else "fail",
    }


def _jsonable(value: Any) -> Any:
    if isinstance(value, Counter):
        return dict(value)
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def render_markdown(data: dict[str, Any]) -> str:
    lines = [
        "# Task Audit",
        "",
        f"Status: **{data['status']}**",
        "",
        f"- Tasks: **{data['task_count']}**",
        f"- Concepts: **{data['concept_count']}**",
        f"- Language counts: `{data['language_counts']}`",
        f"- Complete EN/ZH pairs: **{data['pair_count'] - len(data['bad_pairs'])}**",
        f"- Exact duplicate groups: **{len(data['exact_duplicate_groups'])}**",
        f"- Normalized duplicate groups: **{len(data['normalized_duplicate_groups'])}**",
        f"- Missing rubric: **{len(data['rubric_missing'])}**",
        f"- Schema errors: **{len(data['schema_errors'])}**",
        "",
        "## Family (Concepts)",
        "",
        "| Family | Concepts |",
        "|---|---:|",
    ]
    for key, value in sorted(data["family_concept_counts"].items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Difficulty (Concepts)",
            "",
            "| Difficulty | Concepts |",
            "|---|---:|",
        ]
    )
    for key, value in sorted(data["difficulty_concept_counts"].items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Provenance",
            "",
            "| Kind | Tasks |",
            "|---|---:|",
        ]
    )
    for key, value in sorted(data["provenance_counts"].items()):
        lines.append(f"| `{key}` | {value} |")
    if data["bad_pairs"]:
        lines.extend(["", "## Bad Pairs", ""])
        lines.extend(
            f"- `{base}`: {languages}"
            for base, languages in sorted(data["bad_pairs"].items())
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks-root", type=Path, default=DEFAULT_TASKS_ROOT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args(argv)
    data = audit_tasks(args.tasks_root)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(_jsonable(data), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.md_out.write_text(render_markdown(_jsonable(data)), encoding="utf-8")
    print(
        f"{data['status']}: {data['concept_count']} concepts, "
        f"{data['task_count']} tasks; reports at {args.md_out}"
    )
    return 0 if data["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
