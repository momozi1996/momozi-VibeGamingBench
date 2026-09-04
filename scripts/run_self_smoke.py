#!/usr/bin/env python3
"""Run five real generated games through the benchmark pipeline.

The self judge is deliberately temporary and deterministic. Its scores are
diagnostic only and are marked ``leaderboard_eligible: false``.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momozi.auto_eval import _score_agent_result
from momozi.protocol import (
    AGENT_EVALUATION_PROTOCOL,
    BENCHMARK_RELEASE,
    SCHEMA_VERSION,
    agent_metadata,
    validate_result_schema,
)
from momozi.runtime_smoke import RuntimeConfig, run_runtime_smoke
from momozi.static_eval import StaticEvaluator
from momozi.task import Task


DEFAULT_TASKS = [
    "mz_feishu-structured-001-en",
    "mz_feishu-structured-002-en",
    "mz_feishu-structured-003-en",
    "mz_feishu-structured-004-en",
    "mz_feishu-structured-005-en",
]


def self_judgement(task: Task, product_dir: Path, runtime: dict, static_eval: dict) -> dict:
    """Transparent placeholder judge; never eligible for the leaderboard."""
    html = (product_dir / "index.html").read_text(encoding="utf-8", errors="ignore")
    logic = (product_dir / "game_logic.js").read_text(encoding="utf-8", errors="ignore")
    build_ok = bool(static_eval.get("build", {}).get("ok"))
    contract_ok = static_eval.get("contract", {}).get("pass_rate") == 1.0
    runtime_ok = runtime.get("status") == "pass"
    richness_signal = min(5.0, 2.0 + (len(html) > 2000) + (len(logic) > 800))
    visual_signal = min(
        5.0,
        2.5
        + ("<canvas" in html)
        + ("button" in html.lower())
        + ("@media" in html.lower()),
    )
    # This harness intentionally implements a small generic playable slice,
    # not the full assigned game. Keep the temporary score conservative so a
    # passing artifact is not mistaken for high prompt fidelity.
    scores = {
        "completeness": 1.5 if build_ok and contract_ok else 0.0,
        "richness": 1.5 if build_ok else 0.0,
        "player_exp": 3.0 if runtime_ok else 0.0,
        "visual": float(visual_signal) if build_ok else 0.0,
    }
    dimensions = {
        key: {
            "score": value,
            "reason": (
                "Temporary deterministic self-smoke score based on artifact signals; "
                "not a human or external model quality judgment."
            ),
            "evidence": [
                f"task family={task.family}",
                f"html_bytes={(product_dir / 'index.html').stat().st_size}",
                f"logic_bytes={(product_dir / 'game_logic.js').stat().st_size}",
                f"runtime_status={runtime.get('status')}",
            ],
            "missing": [],
        }
        for key, value in scores.items()
    }
    return {
        "dimensions": dimensions,
        "fatal_issues": [],
        "confidence": 0.25,
        "judge_kind": "temporary-self-smoke",
    }


def run_one(task_id: str, out_root: Path) -> dict:
    task_path = ROOT / "bench" / "tasks" / task_id / f"{task_id}.task.yaml"
    task = Task.load(task_path)
    case_dir = out_root / task_id
    product_dir = case_dir / "product"
    evidence_dir = case_dir / "evidence"
    case_dir.mkdir(parents=True, exist_ok=True)
    harness = ROOT / "scripts" / "self_smoke_harness.py"
    generated = subprocess.run(
        [
            "python3",
            str(harness),
            "--task-file",
            str(task_path),
            "--product-dir",
            str(product_dir),
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )
    generation = {
        "mode": "self-smoke-harness",
        "ok": generated.returncode == 0,
        "stdout": generated.stdout[-2000:],
        "stderr": generated.stderr[-2000:],
        "returncode": generated.returncode,
    }
    static_eval = StaticEvaluator().evaluate(task, product_dir)
    scheme = str((task.evaluation or {}).get("input_scheme") or "auto")
    runtime = run_runtime_smoke(
        product_dir,
        evidence_dir,
        RuntimeConfig(
            input_scheme=scheme,
            start_keys=tuple((task.evaluation or {}).get("start_keys") or ("Enter", "Space")),
            stabilization_ms=250,
            capture_gameplay=True,
        ),
    )
    judgement = self_judgement(task, product_dir, runtime, static_eval)
    failure_details = list(static_eval.get("failure_details", []))
    failure_details.extend(runtime.get("failure_details", []))
    failure_codes = [item.get("code") for item in failure_details if item.get("code")]
    visual = {
        "functional_visual": {
            "score": judgement["dimensions"]["player_exp"]["score"],
            "evidence": ["runtime screenshots captured by Chromium", "temporary self-smoke judge"],
        },
        "presentation": {
            "score": judgement["dimensions"]["visual"]["score"],
            "evidence": ["HTML/CSS/Canvas presentation signals", "temporary self-smoke judge"],
        },
        "confidence": judgement["confidence"],
    }
    scores = _score_agent_result(
        judgement=judgement,
        static_eval=static_eval,
        runtime=runtime,
        visual=visual,
        failure_codes=failure_codes,
    )
    result = {
        "benchmark": "momozi-VibeGamingBench",
        "version": "0.7.0",
        "schema_version": SCHEMA_VERSION,
        "benchmark_release": BENCHMARK_RELEASE,
        "evaluation_protocol": AGENT_EVALUATION_PROTOCOL,
        "run_id": out_root.name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_label": "temporary-self-smoke",
        "agent": agent_metadata(
            name="temporary-self-smoke",
            model="self",
            harness="scripts/self_smoke_harness.py",
            version="1.0",
            model_version="local-deterministic",
        ),
        "task": task.id,
        "task_id": task.id,
        "base_task_id": task.base_task_id,
        "family": task.family,
        "difficulty": task.difficulty,
        "language": task.language,
        "generation": generation,
        "harness": {"name": "self-smoke-harness", "command": True, "contract_version": 1},
        "static": {
            **static_eval,
            "score": scores["static"],
            "judge": {"provider": "temporary-self-smoke", "model": "self"},
        },
        "dynamic": {**runtime, "score": scores["dynamic"]},
        "runtime": {**runtime, "score": scores["dynamic"]},
        "visual": {
            **visual,
            "score": scores["visual"],
            "judge": {"provider": "temporary-self-smoke", "model": "self", "version": "1.0"},
        },
        "build_gate": static_eval["build"],
        "contract": static_eval["contract"],
        "dimensions": judgement["dimensions"],
        "fatal_issues": judgement["fatal_issues"],
        "confidence": judgement["confidence"],
        "scores": scores,
        "judge": {"provider": "temporary-self-smoke", "model": "self"},
        "leaderboard_eligible": False,
        "evaluation_error": None,
        "primary_failure": failure_codes[0] if failure_codes else None,
        "failure_details": failure_details,
        "workspace": str(case_dir),
        "product_dir": str(product_dir),
    }
    validate_result_schema(result)
    (case_dir / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT / "reports" / "self_smoke" / "v0.7.0")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="allow clearing the explicitly selected smoke output directory",
    )
    parser.add_argument("--task", action="append", dest="tasks")
    args = parser.parse_args(argv)
    tasks = args.tasks or DEFAULT_TASKS
    if len(tasks) != 5:
        parser.error("provide exactly five --task values")
    if args.out.exists() and not args.overwrite:
        parser.error(
            f"{args.out} already exists; choose a new --out path or pass --overwrite explicitly"
        )
    if args.out.exists() and args.overwrite:
        for child in args.out.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    args.out.mkdir(parents=True, exist_ok=True)
    results = [run_one(task_id, args.out) for task_id in tasks]
    summary = {
        "benchmark_release": BENCHMARK_RELEASE,
        "judge": "temporary-self-smoke",
        "leaderboard_eligible": False,
        "tasks": tasks,
        "results": [
            {
                "task_id": result["task_id"],
                "family": result["family"],
                "language": result["language"],
                "build_ok": result["build_gate"]["ok"],
                "runtime_status": result["runtime"]["status"],
                "contract_pass_rate": result["contract"]["pass_rate"],
                "final_score": result["scores"]["final"],
                "screenshots": result["runtime"]["screenshots"],
            }
            for result in results
        ],
    }
    (args.out / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# VibeGamingBench Self Smoke Record",
        "",
        "This is a five-case real artifact smoke run. Scores use a temporary deterministic self judge and are not leaderboard eligible.",
        "",
        f"- Release: `{BENCHMARK_RELEASE}`",
        f"- Cases: **{len(results)}**",
        f"- Build pass: **{sum(item['build_gate']['ok'] for item in results)} / {len(results)}**",
        f"- Runtime pass: **{sum(item['runtime']['status'] == 'pass' for item in results)} / {len(results)}**",
        "",
        "| Task | Family | Build | Contract | Runtime | Final |",
        "|---|---|---:|---:|---|---:|",
    ]
    for result in results:
        lines.append(
            f"| `{result['task_id']}` | `{result['family']}` | "
            f"{'PASS' if result['build_gate']['ok'] else 'FAIL'} | "
            f"{result['contract']['pass_rate']:.2f} | "
            f"{result['runtime']['status']} | {result['scores']['final']:.2f} |"
        )
    lines.extend(
        [
            "",
            "## Artifact Layout",
            "",
            "Each task directory contains `product/index.html`, `product/game_logic.js`, `evidence/boot.png`, `evidence/gameplay_start.png`, `evidence/gameplay_mid.png`, and `result.json`.",
            "",
            "The local self judge is diagnostic only. It must not be used as an official quality label or leaderboard score.",
        ]
    )
    (args.out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
