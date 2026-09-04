"""Migrate the checked-in 982-task pool to the v0.6 prompt contract.

Only the generated HTML contract and the mirrored rounds[0].spec are changed.
Task IDs, provenance, rubric anchors, and source fields remain untouched.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from prompt_contract import clean_yaml, input_scheme_for_family, render_contract


ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "bench" / "tasks"


def _replace_contract(prompt: str, family: str, language: str, dimension: str) -> str:
    marker = re.search(
        r"(?m)^## (HTML Submission Format|HTML 提交格式|提交格式（HTML）)\s*$",
        prompt,
    )
    if not marker:
        raise ValueError("HTML submission marker is missing")
    prefix = prompt[: marker.start()].rstrip()
    return prefix + "\n\n" + render_contract(language, family, dimension).strip() + "\n"


def _replace_yaml_spec(text: str, prompt: str) -> str:
    marker = re.search(r"(?m)^rounds:\s*\n- name: R1\s*\n  spec: \|-\s*\n", text)
    if not marker:
        raise ValueError("R1 block marker is missing")
    start = marker.end()
    next_field = re.search(r"(?m)^[A-Za-z_][A-Za-z0-9_-]*:", text[start:])
    if not next_field:
        raise ValueError("top-level field after R1 spec is missing")
    end = start + next_field.start()
    block = "".join(
        f"    {line}\n" if line else "\n"
        for line in prompt.rstrip("\n").splitlines()
    )
    return text[:start] + block + text[end:]


def migrate_task(task_dir: Path) -> None:
    yaml_paths = sorted(task_dir.glob("*.task.yaml"))
    if len(yaml_paths) != 1:
        raise ValueError(f"{task_dir}: expected one task yaml")
    yaml_path = yaml_paths[0]
    yaml_text = yaml_path.read_text(encoding="utf-8")
    language = "zh" if task_dir.name.endswith("-zh") else "en"
    family_match = re.search(r"(?m)^family:\s*([^\s#]+)", yaml_text)
    if not family_match:
        raise ValueError(f"{yaml_path}: family is missing")
    family = family_match.group(1)
    prompt_path = task_dir / "prompt.md"
    old_prompt = prompt_path.read_text(encoding="utf-8")
    # The contract renderer only needs a dimension for the renderer hint. Keep
    # the existing task's dimensionality when it is stated in the task body.
    dimension_match = re.search(r"\b(2\.5D|3D|2D)\b", old_prompt)
    dimension = dimension_match.group(1) if dimension_match else ""
    new_prompt = _replace_contract(old_prompt, family, language, dimension)
    prompt_path.write_text(new_prompt, encoding="utf-8")
    yaml_text = _replace_yaml_spec(yaml_text, new_prompt)
    if not re.search(r"(?m)^evaluation:\s*$", yaml_text):
        insertion = (
            "evaluation:\n"
            f"  input_scheme: {input_scheme_for_family(family)}\n"
            "  start_keys:\n"
            "  - Enter\n"
            "  - Space\n"
        )
        language_marker = re.search(r"(?m)^language:", yaml_text)
        if language_marker:
            yaml_text = (
                yaml_text[: language_marker.start()]
                + insertion
                + yaml_text[language_marker.start() :]
            )
        else:
            yaml_text = yaml_text.rstrip() + "\n" + insertion
    yaml_path.write_text(clean_yaml(yaml_text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    task_dirs = sorted(path for path in TASKS.glob("mz_*") if path.is_dir())
    if len(task_dirs) != 982:
        raise SystemExit(f"expected 982 task directories, found {len(task_dirs)}")
    changed = 0
    for task_dir in task_dirs:
        prompt_path = task_dir / "prompt.md"
        before = prompt_path.read_text(encoding="utf-8")
        if args.check:
            if "Keyboard-only" in before or "键盘-only" in before:
                raise SystemExit(f"legacy keyboard-only contract remains: {prompt_path}")
            if "Assets must be generated at runtime" not in before and "资源必须在运行时自包含生成" not in before:
                raise SystemExit(f"v0.6 contract missing: {prompt_path}")
            continue
        migrate_task(task_dir)
        changed += 1
    print(f"{'checked' if args.check else 'migrated'} {len(task_dirs)} tasks")
    if not args.check:
        print(f"updated {changed} prompt/YAML pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
