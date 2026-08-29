"""Deterministic DEV/PUBLIC/HIDDEN concept split helpers."""
from __future__ import annotations

import hashlib
import json
import random
from typing import Iterable


SPLIT_VERSION = "1.0"
DEFAULT_COUNTS = {"DEV": 300, "PUBLIC": 100, "HIDDEN": 91}


def split_concepts(
    base_task_ids: Iterable[str],
    *,
    seed: int = 20260829,
    counts: dict[str, int] | None = None,
) -> dict[str, list[str]]:
    ids = sorted({str(value) for value in base_task_ids})
    expected = counts or DEFAULT_COUNTS
    if sum(expected.values()) != len(ids):
        raise ValueError(
            f"split counts sum to {sum(expected.values())}, but there are {len(ids)} concepts"
        )
    if set(expected) != {"DEV", "PUBLIC", "HIDDEN"}:
        raise ValueError("counts must contain DEV, PUBLIC, and HIDDEN")
    rng = random.Random(seed)
    rng.shuffle(ids)
    output = {}
    cursor = 0
    for name in ("DEV", "PUBLIC", "HIDDEN"):
        output[name] = sorted(ids[cursor : cursor + expected[name]])
        cursor += expected[name]
    return output


def hidden_digest(hidden_ids: Iterable[str]) -> str:
    payload = "\n".join(sorted(str(value) for value in hidden_ids)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def public_manifest(split: dict[str, list[str]], *, seed: int) -> dict:
    return {
        "split_version": SPLIT_VERSION,
        "seed": seed,
        "public": {
            "DEV": list(split["DEV"]),
            "PUBLIC": list(split["PUBLIC"]),
        },
        "hidden": {
            "count": len(split["HIDDEN"]),
            "sha256": hidden_digest(split["HIDDEN"]),
            "content": "private",
        },
    }


def private_manifest(split: dict[str, list[str]], *, seed: int) -> dict:
    payload = public_manifest(split, seed=seed)
    payload["private_hidden_ids"] = list(split["HIDDEN"])
    return payload


def manifest_json(split: dict[str, list[str]], *, seed: int, private: bool = False) -> str:
    data = (
        private_manifest(split, seed=seed)
        if private
        else public_manifest(split, seed=seed)
    )
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"
