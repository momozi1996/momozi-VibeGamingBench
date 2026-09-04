#!/usr/bin/env python3
"""Produce a release-freeze audit for momozi-VibeGamingBench.

The audit deliberately separates benchmark source files from historical
``runs/`` and ``workspaces/`` artifacts. Those artifacts are useful locally but
should not be included in a reproducible release archive.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from audit_tasks import audit_tasks


ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_DIRS = {".git", ".pytest_cache", "__pycache__", "runs", "workspaces"}
TEXT_SUFFIXES = {".py", ".js", ".mjs", ".sh", ".json", ".yaml", ".yml", ".md", ".txt", ".tsv", ".csv"}


def source_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)
        and path.name != ".DS_Store"
    ]


def parse_files(paths: list[Path]) -> dict:
    errors = []
    counts = Counter()
    for path in paths:
        suffix = path.suffix.lower()
        try:
            if suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
                counts["json"] += 1
            elif suffix in {".yaml", ".yml"}:
                yaml.safe_load(path.read_text(encoding="utf-8"))
                counts["yaml"] += 1
            elif suffix in TEXT_SUFFIXES:
                data = path.read_bytes()
                if b"\x00" in data:
                    errors.append({"file": str(path.relative_to(ROOT)), "error": "NUL byte"})
                path.read_text(encoding="utf-8")
                counts[suffix.lstrip(".")] += 1
        except Exception as exc:
            errors.append(
                {
                    "file": str(path.relative_to(ROOT)),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
    return {"counts": dict(counts), "errors": errors}


def syntax_checks(paths: list[Path]) -> dict:
    python_paths = [path for path in paths if path.suffix == ".py"]
    node_paths = [path for path in paths if path.suffix in {".js", ".mjs"}]
    shell_paths = [path for path in paths if path.suffix == ".sh"]
    results = {"python": [], "node": [], "shell": []}
    for path in python_paths:
        proc = subprocess.run(
            ["python3", "-m", "py_compile", str(path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode:
            results["python"].append({"file": str(path.relative_to(ROOT)), "stderr": proc.stderr[-500:]})
    for path in node_paths:
        proc = subprocess.run(
            ["node", "--check", str(path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode:
            results["node"].append({"file": str(path.relative_to(ROOT)), "stderr": proc.stderr[-500:]})
    for path in shell_paths:
        proc = subprocess.run(
            ["bash", "-n", str(path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode:
            results["shell"].append({"file": str(path.relative_to(ROOT)), "stderr": proc.stderr[-500:]})
    return {
        "checked": {
            "python": len(python_paths),
            "node": len(node_paths),
            "shell": len(shell_paths),
        },
        "errors": results,
    }


def release_hash() -> dict:
    release_path = ROOT / "benchmark_releases" / "v0.7.0.json"
    release = json.loads(release_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256()
    files = 0
    for path in sorted((ROOT / "bench" / "tasks").rglob("*")):
        if (
            path.is_file()
            and path.name != ".DS_Store"
            and "__pycache__" not in path.parts
        ):
            digest.update(path.relative_to(ROOT / "bench" / "tasks").as_posix().encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
            files += 1
    actual = digest.hexdigest()
    return {
        "release": release.get("release"),
        "release_hash": release.get("task_manifest_sha256"),
        "computed_hash": actual,
        "match": release.get("task_manifest_sha256") == actual,
        "manifest_task_files": files,
        "concept_count": release.get("concept_count"),
        "task_count": release.get("task_count"),
    }


def task_contract() -> dict:
    data = audit_tasks(ROOT / "bench" / "tasks")
    return {
        "status": data["status"],
        "concept_count": data["concept_count"],
        "task_count": data["task_count"],
        "language_counts": dict(data["language_counts"]),
        "pair_count": data["pair_count"],
        "bad_pairs": data["bad_pairs"],
        "schema_errors": len(data["schema_errors"]),
        "rubric_missing": len(data["rubric_missing"]),
        "duplicate_groups": len(data["exact_duplicate_groups"]) + len(data["normalized_duplicate_groups"]),
    }


def docs_and_links() -> dict:
    errors = []
    stale = []
    markdown_files = []
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        markdown_files.append(path)
        text = path.read_text(encoding="utf-8")
        if path.name != "CHANGELOG.md" and "v0.6.0" in text:
            stale.append(str(path.relative_to(ROOT)))
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists():
                errors.append({"file": str(path.relative_to(ROOT)), "target": target})
    return {"markdown_files": len(markdown_files), "broken_relative_links": errors, "stale_release_docs": stale}


def generated_artifacts() -> dict:
    try:
        tracked = subprocess.check_output(
            ["git", "ls-files", "runs", "workspaces"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
        git_repo = True
    except (OSError, subprocess.CalledProcessError):
        tracked = []
        git_repo = False
    return {
        "git_repo": git_repo,
        "tracked_generated_files": len(tracked),
        "tracked_runs_files": sum(path.startswith("runs/") for path in tracked),
        "tracked_workspaces_files": sum(path.startswith("workspaces/") for path in tracked),
        "warning": (
            "runs/ and workspaces/ are ignored for new files but historical files are still tracked; "
            "exclude them from a freeze archive or remove from the release index explicitly."
            if tracked
            else (
                "No tracked generated artifacts found in this directory."
                if git_repo
                else "Directory is not a Git checkout; tracked-artifact status cannot be inspected."
            )
        ),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, default=ROOT / "reports" / "freeze_audit.json")
    parser.add_argument("--md-out", type=Path, default=ROOT / "reports" / "freeze_audit.md")
    args = parser.parse_args(argv)

    files = source_files()
    parsed = parse_files(files)
    syntax = syntax_checks(files)
    tasks = task_contract()
    release = release_hash()
    docs = docs_and_links()
    artifacts = generated_artifacts()
    errors = (
        parsed["errors"]
        + syntax["errors"]["python"]
        + syntax["errors"]["node"]
        + syntax["errors"]["shell"]
        + docs["broken_relative_links"]
    )
    status = "pass" if not errors and tasks["status"] == "pass" and release["match"] else "fail"
    report = {
        "status": status,
        "root": str(ROOT),
        "source_file_count": len(files),
        "parse": parsed,
        "syntax": syntax,
        "tasks": tasks,
        "release": release,
        "docs": docs,
        "generated_artifacts": artifacts,
        "errors": errors,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Freeze Audit",
        "",
        f"Status: **{status.upper()}**",
        "",
        f"- Source files checked: **{len(files)}**",
        f"- Task concepts/tasks: **{tasks['concept_count']} / {tasks['task_count']}**",
        f"- EN/ZH counts: `{tasks['language_counts']}`",
        f"- Release hash match: **{release['match']}**",
        f"- Parse errors: **{len(parsed['errors'])}**",
        f"- Syntax errors: **{sum(len(v) for v in syntax['errors'].values())}**",
        f"- Broken relative links: **{len(docs['broken_relative_links'])}**",
        "",
        "## Freeze Warning",
        "",
        artifacts["warning"] or "No tracked generated run/workspace artifacts found.",
        "",
        "## Commands",
        "",
        "```text",
        "python3 scripts/freeze_audit.py",
        "python3 -m unittest discover -s tests -v",
        "bash scripts/smoke.sh",
        "python3 scripts/validate_pool.py --only-mz --workers 8",
        "```",
        "",
    ]
    args.md_out.write_text("\n".join(lines), encoding="utf-8")
    print(f"{status}: {len(files)} source files, {tasks['concept_count']} concepts, {tasks['task_count']} tasks")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
