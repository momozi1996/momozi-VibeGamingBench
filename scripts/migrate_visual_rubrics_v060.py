"""Remove stale anti-procedural penalties and reward authored runtime polish."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "bench" / "tasks"
POLISH_ANCHOR = (
    " Full credit may be earned with runtime-authored procedural textures, "
    "layered materials, deliberate multi-light rigs, particles, synthesized "
    "audio, or post-processing; external asset files are not required."
)
STALE_SENTENCES = (
    re.compile(
        r"\s*Score 1 requires[^.]*"
        r"(?:real sprites|illustrated assets|real authored art|real assets)[^.]*\."
    ),
    re.compile(
        r"\s*Score 0\.5 at most if[^.]*\."
    ),
)


def migrate(path: Path) -> bool:
    payload = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    visual_anchor_added = False
    for requirement in payload.get("requirements", []):
        description = str(requirement.get("description", ""))
        revised = description
        for pattern in STALE_SENTENCES:
            revised = pattern.sub("", revised)
        if requirement.get("id", "").startswith("A") and not visual_anchor_added:
            if "runtime-authored procedural textures" not in revised:
                revised = revised.rstrip() + POLISH_ANCHOR
            visual_anchor_added = True
        if revised != description:
            requirement["description"] = revised
            changed = True
    if changed:
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    paths = sorted(TASKS.glob("mz_*/rubric.original.json"))
    if len(paths) != 982:
        raise SystemExit(f"expected 982 rubric files, found {len(paths)}")
    changed = 0
    for path in paths:
        if args.check:
            text = path.read_text(encoding="utf-8")
            if "Score 0.5 at most if" in text:
                raise SystemExit(f"stale procedural penalty remains: {path}")
            if "runtime-authored procedural textures" not in text:
                raise SystemExit(f"v0.6 visual polish anchor missing: {path}")
        else:
            changed += int(migrate(path))
    print(f"{'checked' if args.check else 'migrated'} {len(paths)} visual rubrics")
    if not args.check:
        print(f"updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
