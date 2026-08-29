#!/usr/bin/env python3
"""Create a deterministic public/private concept split without task mutation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momozi.splits import (  # noqa: E402
    DEFAULT_COUNTS,
    manifest_json,
    private_manifest,
    public_manifest,
    split_concepts,
)
import yaml  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks-root", type=Path, default=ROOT / "bench" / "tasks")
    parser.add_argument(
        "--public-out",
        type=Path,
        default=ROOT / "benchmark_releases" / "v0.5.0-split.public.json",
    )
    parser.add_argument(
        "--private-out",
        type=Path,
        required=True,
        help="private path for hidden IDs; never commit this file",
    )
    parser.add_argument("--seed", type=int, default=20260829)
    parser.add_argument("--dev", type=int, default=DEFAULT_COUNTS["DEV"])
    parser.add_argument("--public", type=int, default=DEFAULT_COUNTS["PUBLIC"])
    parser.add_argument("--hidden", type=int, default=DEFAULT_COUNTS["HIDDEN"])
    args = parser.parse_args(argv)
    base_ids = set()
    for path in args.tasks_root.glob("*/*.task.yaml"):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        if raw.get("base_task_id"):
            base_ids.add(raw["base_task_id"])
    split = split_concepts(
        base_ids,
        seed=args.seed,
        counts={"DEV": args.dev, "PUBLIC": args.public, "HIDDEN": args.hidden},
    )
    args.public_out.parent.mkdir(parents=True, exist_ok=True)
    args.private_out.parent.mkdir(parents=True, exist_ok=True)
    args.public_out.write_text(
        json.dumps(public_manifest(split, seed=args.seed), ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    args.private_out.write_text(
        json.dumps(private_manifest(split, seed=args.seed), ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(
        f"wrote public={args.public_out} and private={args.private_out}; "
        f"counts={ {key: len(value) for key, value in split.items()} }"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
