#!/usr/bin/env python3
"""Create and analyze a small human calibration sample."""
from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
DIMENSIONS = ("functional_visual", "presentation", "overall_quality")


def _load_tasks(tasks_root: Path) -> dict[str, dict[str, Any]]:
    by_base: dict[str, dict[str, Any]] = defaultdict(dict)
    for path in sorted(tasks_root.glob("*/*.task.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        base = raw.get("base_task_id")
        language = raw.get("language")
        if base and language:
            by_base[base][language] = {
                "task_id": raw["id"],
                "family": raw.get("family", "unspecified"),
                "difficulty": raw.get("difficulty", "unspecified"),
            }
    return by_base


def sample_tasks(tasks_root: Path, count: int = 50, seed: int = 20260829) -> list[dict]:
    if count % 2:
        raise ValueError("count must be even so each selected concept has EN and ZH")
    by_base = _load_tasks(tasks_root)
    concepts = list(by_base.items())
    rng = random.Random(seed)
    rng.shuffle(concepts)

    # Round-robin selection keeps families and heuristic difficulty represented.
    buckets: dict[tuple[str, str], list[tuple[str, dict]]] = defaultdict(list)
    for base, variants in concepts:
        if "en" not in variants or "zh" not in variants:
            continue
        key = (variants["en"]["family"], variants["en"]["difficulty"])
        buckets[key].append((base, variants["en"]))
    selected: list[tuple[str, dict]] = []
    keys = sorted(buckets)
    while buckets and len(selected) < count // 2:
        progressed = False
        for key in list(keys):
            if buckets[key]:
                selected.append(buckets[key].pop())
                progressed = True
                if len(selected) >= count // 2:
                    break
            else:
                keys.remove(key)
        if not progressed:
            break

    rows = []
    for base, english in selected:
        variants = by_base[base]
        for language in ("en", "zh"):
            row = variants[language]
            rows.append(
                {
                    "task_id": row["task_id"],
                    "base_task_id": base,
                    "language": language,
                    "family": row["family"],
                    "difficulty": row["difficulty"],
                }
            )
    return rows


def write_template(rows: list[dict], output: Path, raters: int = 2) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "task_id",
        "base_task_id",
        "language",
        "family",
        "difficulty",
        "rater",
        *DIMENSIONS,
        "vlm_functional_visual",
        "vlm_presentation",
        "vlm_overall_quality",
    ]
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            for rater in range(1, raters + 1):
                writer.writerow({**row, "rater": f"rater-{rater}"})


def _numeric(value: str | None) -> float | None:
    try:
        return float(value) if value not in (None, "") else None
    except (TypeError, ValueError):
        return None


def _rank(values: list[float]) -> list[float]:
    order = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    index = 0
    while index < len(order):
        end = index
        while end + 1 < len(order) and order[end + 1][1] == order[index][1]:
            end += 1
        rank = (index + end + 2) / 2
        for position in range(index, end + 1):
            ranks[order[position][0]] = rank
        index = end + 1
    return ranks


def _pearson(left: list[float], right: list[float]) -> float:
    if len(left) < 2:
        return 0.0
    mean_left = sum(left) / len(left)
    mean_right = sum(right) / len(right)
    numerator = sum(
        (a - mean_left) * (b - mean_right)
        for a, b in zip(left, right)
    )
    denominator = math.sqrt(
        sum((a - mean_left) ** 2 for a in left)
        * sum((b - mean_right) ** 2 for b in right)
    )
    return numerator / denominator if denominator else 0.0


def spearman(left: list[float], right: list[float]) -> float:
    return _pearson(_rank(left), _rank(right))


def analyze_csv(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    complete = [
        row for row in rows
        if _numeric(row.get("overall_quality")) is not None
    ]
    if not complete:
        return {
            "status": "pending",
            "rows": len(rows),
            "message": "No human ratings available; calibration remains pending.",
        }

    human = [_numeric(row["overall_quality"]) for row in complete]
    vlm = [
        _numeric(row.get("vlm_overall_quality"))
        for row in complete
    ]
    paired = [
        (h, v) for h, v in zip(human, vlm) if h is not None and v is not None
    ]
    metrics: dict[str, Any] = {}
    if paired:
        human_values, vlm_values = zip(*paired)
        metrics["spearman_overall"] = round(
            spearman(list(human_values), list(vlm_values)), 4
        )
        metrics["mae_overall"] = round(
            sum(abs(a - b) for a, b in paired) / len(paired), 4
        )

    by_task: dict[str, list[float]] = defaultdict(list)
    for row in complete:
        score = _numeric(row.get("overall_quality"))
        if score is not None:
            by_task[row["task_id"]].append(score)
    pairwise_diffs = []
    for values in by_task.values():
        if len(values) >= 2:
            pairwise_diffs.append(abs(values[0] - values[1]))
    metrics["inter_rater_agreement_within_1"] = round(
        sum(value <= 1.0 for value in pairwise_diffs) / len(pairwise_diffs),
        4,
    ) if pairwise_diffs else None
    metrics["inter_rater_mae"] = round(
        sum(pairwise_diffs) / len(pairwise_diffs), 4
    ) if pairwise_diffs else None
    return {
        "status": "complete" if paired else "partial",
        "rows": len(rows),
        "rated_rows": len(complete),
        "metrics": metrics,
    }


def render_report(data: dict[str, Any]) -> str:
    lines = [
        "# Human Calibration",
        "",
        f"Status: **{data['status']}**",
        "",
        data.get("message", "Calibration analysis uses only supplied human ratings."),
        "",
        "```json",
        json.dumps(data, ensure_ascii=False, indent=2),
        "```",
        "",
        "No synthetic human scores are generated by this tool.",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sample = sub.add_parser("sample")
    sample.add_argument("--tasks-root", type=Path, default=ROOT / "bench" / "tasks")
    sample.add_argument("--count", type=int, default=50)
    sample.add_argument("--seed", type=int, default=20260829)
    sample.add_argument("--out", type=Path, default=ROOT / "reports" / "calibration_template.csv")
    sample.add_argument("--raters", type=int, default=2)
    analyze = sub.add_parser("analyze")
    analyze.add_argument("csv", type=Path)
    analyze.add_argument("--json-out", type=Path, default=ROOT / "reports" / "calibration.json")
    analyze.add_argument("--md-out", type=Path, default=ROOT / "reports" / "calibration.md")
    args = parser.parse_args(argv)
    if args.command == "sample":
        rows = sample_tasks(args.tasks_root, args.count, args.seed)
        write_template(rows, args.out, args.raters)
        print(f"wrote {len(rows)} annotation rows to {args.out}")
        return 0
    data = analyze_csv(args.csv)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.md_out.write_text(render_report(data), encoding="utf-8")
    print(render_report(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
