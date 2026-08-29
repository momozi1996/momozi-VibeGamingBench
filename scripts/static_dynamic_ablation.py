#!/usr/bin/env python3
"""Compare static-only, static+dynamic, and multimodal result records."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def _score(record: dict) -> float:
    scores = record.get("scores", {})
    return float(
        scores.get("final")
        if scores.get("final") is not None
        else scores.get("overall_score", scores.get("total", 0.0))
    )


def _static(record: dict) -> float:
    scores = record.get("scores", {})
    if scores.get("static") is not None:
        return float(scores["static"])
    if scores.get("rubric_score_100") is not None:
        return float(scores["rubric_score_100"])
    return _score(record)


def _dynamic(record: dict) -> float:
    scores = record.get("scores", {})
    if scores.get("dynamic") is not None:
        return float(scores["dynamic"])
    return 100.0 if record.get("dynamic", {}).get("status") == "pass" else 0.0


def _static_pass(record: dict) -> bool:
    """Treat both BUILD and the deterministic contract as static success."""
    static = record.get("static", {}) or {}
    build = record.get("build_gate", {}) or static.get("build", {}) or {}
    contract = record.get("contract", {}) or static.get("contract", {}) or {}
    try:
        contract_ok = float(contract.get("pass_rate", 0.0)) >= 1.0
    except (TypeError, ValueError):
        contract_ok = False
    return bool(build.get("ok")) and contract_ok


def load_records(results_dir: Path) -> list[dict]:
    rows = []
    for path in sorted(results_dir.rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and (data.get("task_id") or data.get("task")):
            rows.append(data)
    return rows


def analyze(records: list[dict]) -> dict:
    by_model = defaultdict(list)
    for record in records:
        agent = record.get("agent")
        if isinstance(agent, dict):
            agent = agent.get("model")
        label = record.get("model_label") or agent or "unknown"
        by_model[str(label)].append(record)

    models = {}
    scenario_values = {"static_only": {}, "static_dynamic": {}, "multimodal": {}}
    for model, rows in sorted(by_model.items()):
        static_values = [_static(row) for row in rows]
        dynamic_values = [_dynamic(row) for row in rows]
        final_values = [_score(row) for row in rows]
        scenario_values["static_only"][model] = sum(static_values) / len(static_values)
        scenario_values["static_dynamic"][model] = (
            sum(
                0.40 * s + 0.25 * d
                for s, d in zip(static_values, dynamic_values)
            )
            / len(rows)
            / 0.65
        )
        scenario_values["multimodal"][model] = sum(final_values) / len(final_values)
        static_pass = [_static_pass(row) for row in rows]
        dynamic_fail = [
            row.get("dynamic", {}).get("status") != "pass"
            for row in rows
        ]
        denominator = sum(static_pass)
        models[model] = {
            "tasks": len(rows),
            "static_dynamic_gap_mean": round(
                sum(s - d for s, d in zip(static_values, dynamic_values))
                / len(rows),
                4,
            ),
            "static_false_positive_rate": round(
                sum(
                    1 for passed, failed in zip(static_pass, dynamic_fail)
                    if passed and failed
                )
                / denominator,
                4,
            )
            if denominator
            else None,
        }

    rankings = {}
    for scenario, values in scenario_values.items():
        rankings[scenario] = [
            model
            for model, _ in sorted(
                values.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ]
    rank_changes = {}
    baseline = rankings.get("static_only", [])
    for scenario, ranking in rankings.items():
        if scenario == "static_only":
            continue
        rank_changes[scenario] = {
            model: {
                "from": baseline.index(model) + 1 if model in baseline else None,
                "to": ranking.index(model) + 1 if model in ranking else None,
            }
            for model in ranking
        }
    return {
        "records": len(records),
        "models": models,
        "scenario_mean_scores": scenario_values,
        "rankings": rankings,
        "rank_changes": rank_changes,
        "definition": {
            "static_false_positive_rate": (
                "static_pass AND dynamic_fail / static_pass"
            ),
            "static_dynamic": "weighted active components renormalized by 0.65",
        },
    }


def render_markdown(data: dict) -> str:
    lines = [
        "# Static-Dynamic Ablation",
        "",
        f"Result records: **{data['records']}**",
        "",
        "| Model | Static-only | Static + Dynamic | Static + Dynamic + Multimodal |",
        "|---|---:|---:|---:|",
    ]
    scores = data["scenario_mean_scores"]
    for model in sorted(data["models"]):
        lines.append(
            f"| `{model}` | {scores['static_only'].get(model, 0):.2f} | "
            f"{scores['static_dynamic'].get(model, 0):.2f} | "
            f"{scores['multimodal'].get(model, 0):.2f} |"
        )
    lines.extend(["", "## Model Diagnostics", ""])
    for model, details in sorted(data["models"].items()):
        lines.append(
            f"- `{model}`: gap={details['static_dynamic_gap_mean']:.2f}, "
            f"static FPR={details['static_false_positive_rate']}"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    args = parser.parse_args(argv)
    data = analyze(load_records(args.results_dir))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(render_markdown(data), encoding="utf-8")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
