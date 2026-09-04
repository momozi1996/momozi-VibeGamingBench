"""Split each bilingual MZ task into independent English and Chinese tasks.

The script is intentionally idempotent:

- On an unsplit concept pool, it validates every prompt and writes two language tasks per concept
  when called with ``--write``.
- On the current split pool, it validates all language pairs and exits.

``prompt.md`` is the canonical generation prompt. The selected language text is
also written to ``rounds[0].spec`` so every runner entry point sees identical
instructions.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "bench"
TASKS = BENCH / "tasks"
STAGING = BENCH / ".tasks_split_staging"
BACKUP = BENCH / ".tasks_unsplit_backup"
EXPECTED_BASE_TASKS = None
ZH_MARKER = re.compile(r"^# 中文版提示词\s*$", re.MULTILINE)
LANGUAGES = {
    "en": {"title_suffix": " (English)"},
    "zh": {"title_suffix": " (中文)"},
}


class LiteralDumper(yaml.SafeDumper):
    """Render multiline strings as readable YAML block scalars."""


def _represent_str(dumper: yaml.Dumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


LiteralDumper.add_representer(str, _represent_str)


def _task_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.glob("mz_*") if path.is_dir())


def _is_split_task(path: Path) -> bool:
    return path.name.endswith(("-en", "-zh"))


def _split_prompt(text: str, source: Path) -> dict[str, str]:
    matches = list(ZH_MARKER.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"{source}: expected one Chinese marker, found {len(matches)}")
    marker = matches[0]
    prompts = {
        "en": text[:marker.start()].strip(),
        "zh": text[marker.end():].strip(),
    }
    if not all(prompts.values()):
        raise ValueError(f"{source}: English or Chinese prompt is empty")
    return prompts


def _load_single_yaml(task_dir: Path) -> tuple[Path, dict]:
    yaml_files = sorted(task_dir.glob("*.task.yaml"))
    if len(yaml_files) != 1:
        raise ValueError(f"{task_dir}: expected one task YAML, found {len(yaml_files)}")
    yaml_path = yaml_files[0]
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if len(raw.get("rounds", [])) != 1:
        raise ValueError(f"{yaml_path}: expected exactly one round")
    return yaml_path, raw


def _validate_unsplit(task_dirs: list[Path]) -> None:
    if not task_dirs:
        raise ValueError("expected at least one unsplit task")
    for task_dir in task_dirs:
        prompt_path = task_dir / "prompt.md"
        if not prompt_path.is_file():
            raise ValueError(f"{task_dir}: prompt.md missing")
        _split_prompt(prompt_path.read_text(encoding="utf-8"), prompt_path)
        yaml_path, raw = _load_single_yaml(task_dir)
        if raw.get("id") != task_dir.name:
            raise ValueError(f"{yaml_path}: id does not match directory name")


def _validate_split(task_dirs: list[Path]) -> None:
    if not task_dirs:
        raise ValueError("expected at least one split task")

    pairs: dict[str, set[str]] = {}
    for task_dir in task_dirs:
        match = re.fullmatch(r"(.+)-(en|zh)", task_dir.name)
        if not match:
            raise ValueError(f"{task_dir}: split task must end in -en or -zh")
        base_id, language = match.groups()
        pairs.setdefault(base_id, set()).add(language)

        prompt_path = task_dir / "prompt.md"
        prompt = prompt_path.read_text(encoding="utf-8").strip()
        if ZH_MARKER.search(prompt):
            raise ValueError(f"{prompt_path}: bilingual marker remains after split")

        yaml_path, raw = _load_single_yaml(task_dir)
        expected_yaml_name = f"{task_dir.name}.task.yaml"
        if yaml_path.name != expected_yaml_name:
            raise ValueError(f"{yaml_path}: expected filename {expected_yaml_name}")
        if raw.get("id") != task_dir.name:
            raise ValueError(f"{yaml_path}: id does not match directory name")
        if raw.get("base_task_id") != base_id:
            raise ValueError(f"{yaml_path}: invalid base_task_id")
        if raw.get("language") != language:
            raise ValueError(f"{yaml_path}: invalid language")
        if raw["rounds"][0]["spec"].strip() != prompt:
            raise ValueError(f"{yaml_path}: rounds[0].spec differs from prompt.md")

    bad_pairs = {base: langs for base, langs in pairs.items() if langs != set(LANGUAGES)}
    if bad_pairs:
        raise ValueError(
            f"expected complete language pairs; found {len(pairs)}, incomplete={bad_pairs}"
        )


def _write_variant(source: Path, destination: Path, language: str, prompt: str) -> None:
    shutil.copytree(source, destination)
    old_yaml_path, raw = _load_single_yaml(destination)
    base_id = raw["id"]
    variant_id = f"{base_id}-{language}"

    raw["id"] = variant_id
    raw["title"] = f"{raw.get('title', base_id)}{LANGUAGES[language]['title_suffix']}"
    raw["language"] = language
    raw["base_task_id"] = base_id
    raw["rounds"][0]["spec"] = prompt

    new_yaml_path = destination / f"{variant_id}.task.yaml"
    old_yaml_path.unlink()
    new_yaml_path.write_text(
        yaml.dump(
            raw,
            Dumper=LiteralDumper,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )
    (destination / "prompt.md").write_text(f"{prompt}\n", encoding="utf-8")


def _replace_pool(source_dirs: list[Path]) -> None:
    if STAGING.exists() or BACKUP.exists():
        raise RuntimeError(
            f"remove stale migration paths before retrying: {STAGING}, {BACKUP}"
        )

    STAGING.mkdir()
    try:
        source_names = {path.name for path in source_dirs}
        for item in TASKS.iterdir():
            if item.name in source_names:
                continue
            target = STAGING / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)

        for source in source_dirs:
            prompts = _split_prompt(
                (source / "prompt.md").read_text(encoding="utf-8"),
                source / "prompt.md",
            )
            for language, prompt in prompts.items():
                destination = STAGING / f"{source.name}-{language}"
                _write_variant(source, destination, language, prompt)

        _validate_split(_task_dirs(STAGING))
        os.replace(TASKS, BACKUP)
        try:
            os.replace(STAGING, TASKS)
        except Exception:
            os.replace(BACKUP, TASKS)
            raise
        shutil.rmtree(BACKUP)
    except Exception:
        if STAGING.exists():
            shutil.rmtree(STAGING)
        raise


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="replace an unsplit bilingual task pool with language-specific tasks",
    )
    args = parser.parse_args(argv)

    task_dirs = _task_dirs(TASKS)
    split_count = sum(_is_split_task(path) for path in task_dirs)
    if split_count == len(task_dirs):
        _validate_split(task_dirs)
        print(
            f"validated {len(task_dirs)} tasks: "
            f"{len(task_dirs) // len(LANGUAGES)} concepts x {len(LANGUAGES)} languages"
        )
        return 0
    if split_count:
        raise ValueError("task pool mixes split and unsplit task IDs")

    _validate_unsplit(task_dirs)
    if not args.write:
        print(
            f"ready to split {len(task_dirs)} bilingual tasks into "
            f"{len(task_dirs) * len(LANGUAGES)} tasks; rerun with --write"
        )
        return 0

    _replace_pool(task_dirs)
    print(
        f"split complete: {len(task_dirs)} concepts x "
        f"{len(LANGUAGES)} languages = {len(task_dirs) * len(LANGUAGES)} tasks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
