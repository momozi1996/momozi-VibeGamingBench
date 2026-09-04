#!/usr/bin/env python3
"""Create a deterministic release manifest from the current task pool."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def task_manifest_sha256(tasks_root: Path) -> str:
    digest = hashlib.sha256()
    files = sorted(
        path
        for path in tasks_root.rglob("*")
        if path.is_file()
        and path.name != ".DS_Store"
        and "__pycache__" not in path.parts
    )
    for path in files:
        relative = path.relative_to(tasks_root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def task_counts(tasks_root: Path) -> tuple[int, int]:
    rows = []
    for path in sorted(tasks_root.glob("*/*.task.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(raw, dict) and raw.get("base_task_id"):
            rows.append(raw)
    concepts = {row["base_task_id"] for row in rows}
    languages = {row.get("language") for row in rows}
    if languages != {"en", "zh"}:
        raise ValueError(f"release requires EN/ZH tasks, found {sorted(languages)}")
    if len(rows) != len(concepts) * 2:
        raise ValueError(
            f"release requires exactly two language tasks per concept: "
            f"{len(rows)} tasks / {len(concepts)} concepts"
        )
    return len(concepts), len(rows)


def build_manifest(tasks_root: Path, release: str) -> dict:
    concept_count, task_count = task_counts(tasks_root)
    return {
        "release": release,
        "benchmark": "momozi-VibeGamingBench",
        "benchmark_type": "agent",
        "schema_version": 1,
        "code_tag": release,
        "static_evaluation": True,
        "dynamic_evaluation": True,
        "multimodal_evaluation": True,
        "evaluation_protocol": "agent-v2",
        "result_schema_version": 2,
        "task_manifest_sha256": task_manifest_sha256(tasks_root),
        "runtime_version": "1.1",
        "judge_version": "1.1",
        "scoring_version": "1.1",
        "statistics_version": "1.0",
        "hidden_split": "private",
        "task_semantics": f"{concept_count} concepts x EN/ZH paired instances",
        "task_count": task_count,
        "concept_count": concept_count,
        "additional_sources": ["Feishu Prompt Catalog"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", default="v0.7.0")
    parser.add_argument("--tasks-root", type=Path, default=ROOT / "bench" / "tasks")
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "benchmark_releases" / "v0.7.0.json",
    )
    args = parser.parse_args(argv)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(build_manifest(args.tasks_root, args.release), indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
