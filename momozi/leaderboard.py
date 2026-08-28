"""Aggregate automatic evaluation results into the public leaderboard."""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from . import PROJECT_NAME, __version__

AUTO_PROTOCOL = "auto-v1"
DIMENSIONS = ("completeness", "richness", "player_exp", "visual")


def _load_runs(results_dir: str | Path) -> list[dict]:
    rows = []
    for path in sorted(Path(results_dir).rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (
            isinstance(data, dict)
            and data.get("evaluation_protocol") == AUTO_PROTOCOL
            and data.get("task")
            and isinstance(data.get("scores"), dict)
            and data.get("leaderboard_eligible", True)
        ):
            rows.append(data)
    return rows


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def build_leaderboard(results_dir: str | Path = "runs") -> dict:
    rows = _load_runs(results_dir)
    by_model: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        label = row.get("model_label") or row.get("agent") or "unknown"
        by_model[str(label)].append(row)

    leaderboard = []
    for model_label, model_rows in by_model.items():
        overall = [
            float(row["scores"]["overall_score"])
            for row in model_rows
            if row["scores"].get("overall_score") is not None
        ]
        rubric = [
            float(row["scores"]["rubric_score_100"])
            for row in model_rows
            if row["scores"].get("rubric_score_100") is not None
        ]
        dimension_means = {}
        for dimension in DIMENSIONS:
            values = [
                float(row["scores"][dimension])
                for row in model_rows
                if row["scores"].get(dimension) is not None
            ]
            dimension_means[dimension] = round(_mean(values) or 0.0, 4)

        build_values = [
            1.0 if row.get("build_gate", {}).get("ok") else 0.0
            for row in model_rows
        ]
        contract_values = [
            float(row.get("contract", {}).get("pass_rate", 0.0))
            for row in model_rows
        ]
        leaderboard.append(
            {
                "model": model_label,
                "overall_score": round(_mean(overall) or 0.0, 4),
                "rubric_score_100": round(_mean(rubric) or 0.0, 4),
                "completeness": dimension_means["completeness"],
                "richness": dimension_means["richness"],
                "player_exp": dimension_means["player_exp"],
                "visual": dimension_means["visual"],
                "build_pass_rate": round(_mean(build_values) or 0.0, 4),
                "contract_pass_rate": round(_mean(contract_values) or 0.0, 4),
                "tasks": len({row["task"] for row in model_rows}),
                "runs": len(model_rows),
            }
        )
    leaderboard.sort(
        key=lambda row: (
            row["overall_score"],
            row["rubric_score_100"],
            row["contract_pass_rate"],
        ),
        reverse=True,
    )
    return {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "evaluation_protocol": AUTO_PROTOCOL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "leaderboard": leaderboard,
        "n_runs": len(rows),
        "n_models": len(leaderboard),
    }


def to_markdown(data: dict) -> str:
    rows = data.get("leaderboard", [])
    title = f"# {PROJECT_NAME} Leaderboard"
    if not rows:
        return (
            f"{title}\n\n"
            "当前没有可发布的 `auto-v1` 自动评测结果。mock judge 结果不会进入正式榜单。\n"
        )

    lines = [
        title,
        "",
        "总分按 `BUILD × CONTRACT × 四维加权分` 计算，满分 100。",
        "",
        "| 排名 | 模型 | 总分 | 完整度 | 丰富度 | 玩家体验 | 视觉 | BUILD | CONTRACT | 题数 |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, row in enumerate(rows, 1):
        model = str(row["model"]).replace("|", "\\|")
        lines.append(
            f"| {rank} | `{model}` | **{row['overall_score']:.2f}** | "
            f"{row['completeness']:.2f} | {row['richness']:.2f} | "
            f"{row['player_exp']:.2f} | {row['visual']:.2f} | "
            f"{row['build_pass_rate'] * 100:.1f}% | "
            f"{row['contract_pass_rate'] * 100:.1f}% | {row['tasks']} |"
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
