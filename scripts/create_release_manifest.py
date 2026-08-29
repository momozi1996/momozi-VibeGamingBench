#!/usr/bin/env python3
"""Create a deterministic release manifest from the current task pool."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def task_manifest_sha256(tasks_root: Path) -> str:
    digest = hashlib.sha256()
    files = sorted(
        path
        for path in tasks_root.rglob("*")
        if path.is_file()
    )
    for path in files:
        relative = path.relative_to(tasks_root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def build_manifest(tasks_root: Path, release: str) -> dict:
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
        "runtime_version": "1.0",
        "judge_version": "1.0",
        "scoring_version": "1.0",
        "statistics_version": "1.0",
        "hidden_split": "private",
        "task_semantics": "491 concepts x EN/ZH paired instances",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", default="v0.5.0")
    parser.add_argument("--tasks-root", type=Path, default=ROOT / "bench" / "tasks")
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "benchmark_releases" / "v0.5.0.json",
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
