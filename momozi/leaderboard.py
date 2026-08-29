"""Aggregate Agent Benchmark results into a release-aware leaderboard."""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import PROJECT_NAME, __version__
from .protocol import AGENT_EVALUATION_PROTOCOL, BENCHMARK_RELEASE
from .statistics import aggregate_results, bootstrap_ci, rank_stability


AUTO_PROTOCOL = AGENT_EVALUATION_PROTOCOL
DIMENSIONS = ("completeness", "richness", "player_exp", "visual")
SUPPORTED_PROTOCOLS = {AUTO_PROTOCOL, "auto-v1"}


def _load_runs(results_dir: str | Path) -> list[dict]:
    rows = []
    for path in sorted(Path(results_dir).rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (
            isinstance(data, dict)
            and data.get("evaluation_protocol") in SUPPORTED_PROTOCOLS
            and (data.get("task_id") or data.get("task"))
            and isinstance(data.get("scores"), dict)
            and data.get("leaderboard_eligible", True)
        ):
            rows.append(data)
    return rows


def _model_label(row: dict) -> str:
    agent = row.get("agent")
    if isinstance(agent, dict):
        agent = agent.get("model")
    return str(row.get("model_label") or agent or "unknown")


def _score_mean(rows: list[dict], key: str) -> float:
    values = [
        float(row.get("scores", {}).get(key, 0.0))
        for row in rows
        if row.get("scores", {}).get(key) is not None
    ]
    return round(sum(values) / len(values), 4) if values else 0.0


def _contract_mean(rows: list[dict]) -> float:
    values = [
        float(row.get("contract", {}).get("pass_rate", 0.0))
        for row in rows
    ]
    return round(sum(values) / len(values), 4) if values else 0.0


def _fmt(value: Any) -> str:
    return "—" if value is None else f"{float(value):.2f}"


def build_leaderboard(results_dir: str | Path = "runs") -> dict:
    rows = _load_runs(results_dir)
    by_release_model: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        release = str(row.get("benchmark_release") or "legacy-v0.4.0")
        by_release_model[(release, _model_label(row))].append(row)

    leaderboard = []
    grouped_for_rank: dict[str, dict[str, list[dict]]] = defaultdict(dict)
    for (release, model_label), model_rows in by_release_model.items():
        metrics = aggregate_results(model_rows)
        bootstrap = bootstrap_ci(model_rows)
        grouped_for_rank[release][model_label] = model_rows
        leaderboard.append(
            {
                "model": model_label,
                "release": release,
                "benchmark_release": release,
                "family_balanced_score": metrics["family_balanced_score"],
                "concept_balanced_score": metrics["concept_balanced_score"],
                "micro_score": metrics["micro_score"],
                "overall_score": metrics["micro_score"],
                "en_score": metrics["en_score"],
                "zh_score": metrics["zh_score"],
                "language_gap": metrics["language_gap"],
                "family_scores": metrics["family_scores"],
                "static_score": _score_mean(model_rows, "static"),
                "dynamic_score": _score_mean(model_rows, "dynamic"),
                "visual_score": _score_mean(model_rows, "visual"),
                "design_score": _score_mean(model_rows, "design"),
                "build_pass_rate": round(
                    sum(
                        1.0 if row.get("build_gate", {}).get("ok") else 0.0
                        for row in model_rows
                    )
                    / len(model_rows),
                    4,
                )
                if model_rows
                else 0.0,
                "runtime_pass_rate": round(
                    sum(
                        1.0
                        if row.get("dynamic", {}).get("status") == "pass"
                        else 0.0
                        for row in model_rows
                    )
                    / len(model_rows),
                    4,
                )
                if model_rows
                else 0.0,
                "contract_pass_rate": _contract_mean(model_rows),
                "tasks": metrics["n_instances"],
                "concepts": metrics["n_concepts"],
                "runs": len(model_rows),
                "bootstrap_ci95": bootstrap["ci95"],
            }
        )

    for release, model_groups in grouped_for_rank.items():
        stability = rank_stability(model_groups)
        for row in leaderboard:
            if row["release"] == release:
                row["rank_stability"] = stability.get(row["model"], {})

    leaderboard.sort(
        key=lambda row: (
            row["family_balanced_score"],
            row["concept_balanced_score"],
            row["micro_score"],
            row["model"],
        ),
        reverse=True,
    )
    return {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "benchmark_release": (
            BENCHMARK_RELEASE
            if any(row["release"] == BENCHMARK_RELEASE for row in leaderboard)
            else None
        ),
        "evaluation_protocol": AUTO_PROTOCOL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "leaderboard": leaderboard,
        "n_runs": len(rows),
        "n_models": len({(row["release"], row["model"]) for row in leaderboard}),
    }


def to_markdown(data: dict[str, Any]) -> str:
    rows = data.get("leaderboard", [])
    title = f"# {PROJECT_NAME} Leaderboard"
    if not rows:
        return (
            f"{title}\n\n"
            "当前没有可发布的 Agent Benchmark 结果。"
            "mock judge/runtime 结果不会进入正式榜单。\n"
        )

    lines = [
        title,
        "",
        "VibeGamingBench 是面向 Coding Agent / Agent Harness 的 Agent Benchmark。",
        "Static 与 Dynamic 独立评测，主指标为 family-balanced score；micro score 仅作兼容参考。",
        "",
        "| 排名 | 模型 | Release | Family-balanced | Concept-balanced | Micro | EN | ZH | Gap | Static | Dynamic | Visual | Design | Runtime | 题目 |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, row in enumerate(rows, 1):
        model = str(row["model"]).replace("|", "\\|")
        lines.append(
            f"| {rank} | `{model}` | `{row['release']}` | "
            f"**{row['family_balanced_score']:.2f}** | "
            f"{row['concept_balanced_score']:.2f} | {row['micro_score']:.2f} | "
            f"{_fmt(row['en_score'])} | {_fmt(row['zh_score'])} | "
            f"{_fmt(row['language_gap'])} | {row['static_score']:.2f} | "
            f"{row['dynamic_score']:.2f} | {row['visual_score']:.2f} | "
            f"{row['design_score']:.2f} | {row['runtime_pass_rate'] * 100:.1f}% | "
            f"{row['tasks']} |"
        )
    return "\n".join(lines) + "\n"


def write_leaderboard(
    results_dir: str | Path,
    json_path: str | Path,
    markdown_path: str | Path | None = None,
) -> dict:
    data = build_leaderboard(results_dir)
    json_target = Path(json_path)
    json_target.parent.mkdir(parents=True, exist_ok=True)
    json_target.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if markdown_path:
        markdown_target = Path(markdown_path)
        markdown_target.parent.mkdir(parents=True, exist_ok=True)
        markdown_target.write_text(to_markdown(data), encoding="utf-8")
    return data


if __name__ == "__main__":
    import sys

    print(to_markdown(build_leaderboard(sys.argv[1] if len(sys.argv) > 1 else "runs")))
