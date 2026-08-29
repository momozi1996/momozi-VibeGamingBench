"""Recompute deterministic gates and score arithmetic for a result archive."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path

from momozi.run import ROOT
from momozi.run_zhen import _weighted_judge_score, build_gate_product
from momozi.scoring import fuse_scores
from momozi.protocol import AGENT_EVALUATION_PROTOCOL, result_schema_errors
from momozi.task import Task
from momozi.verifiers import StaticChecker, BehaviorSuite

AUTO_DIMENSION_WEIGHTS = {
    "completeness": 0.15,
    "richness": 0.35,
    "player_exp": 0.15,
    "visual": 0.35,
}


def _run_verification(task: Task, product_dir: Path):
    suite_name = task.behavior.get("script", "beh_html.mjs")
    suite_path = product_dir / suite_name
    public_suite = ROOT / "bench" / "tests" / Path(suite_name).name
    if not suite_path.exists() and public_suite.exists():
        shutil.copy2(public_suite, suite_path)
    static = StaticChecker(task.static)
    req = task.artifact_requirements()
    s_items = static.run(product_dir, req)
    suite = BehaviorSuite(product_dir, suite_name)
    b_items = suite.run()
    b_total = len(b_items)
    b_ok = len([r for r in b_items if r["ok"]])
    return {
        "static": s_items,
        "static_pass_rate": (sum(x["weight"] for x in s_items if x["ok"] is True) /
                             max(1e-9, sum(x["weight"] for x in s_items))) if s_items else 1.0,
        "behavior": b_items,
        "behavior_pass_rate": b_ok / b_total if b_total else 0.0,
    }


def _extract_archive(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    with tarfile.open(archive) as tf:
        for member in tf.getmembers():
            target = (destination / member.name).resolve()
            if destination != target and destination not in target.parents:
                raise ValueError(f"archive member escapes destination: {member.name}")
            if member.issym() or member.islnk():
                raise ValueError(f"archive links are not allowed: {member.name}")
        tf.extractall(destination)


def _resolve_task(claim: dict) -> Task:
    if claim.get("task_path"):
        path = Path(claim["task_path"])
        if path.exists():
            return Task.load(path)
    task_id = claim.get("task_id") or claim.get("task")
    if not task_id:
        raise ValueError("result JSON does not identify a task")
    path = ROOT / "bench" / "tasks" / task_id / f"{task_id}.task.yaml"
    if not path.exists():
        raise FileNotFoundError(f"cannot resolve task metadata: {path}")
    return Task.load(path)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="momozi verify")
    ap.add_argument("json_path")
    ap.add_argument("archive")
    args = ap.parse_args(argv)
    sub = Path(args.json_path)
    claim = json.loads(sub.read_text(encoding="utf-8"))
    task = _resolve_task(claim)

    tmp = Path(tempfile.mkdtemp(prefix="momozi-verify-"))
    _extract_archive(Path(args.archive), tmp)
    # tar 里结构可能是 product/ 或平铺
    candidate = tmp / "product"
    if not candidate.exists():
        candidate = tmp if (tmp / "game_logic.js").exists() else tmp
    if claim.get("evaluation_protocol") == AGENT_EVALUATION_PROTOCOL:
        gate = build_gate_product(candidate)
        scores = claim.get("scores", {})
        failure_codes = [
            item.get("code")
            for item in claim.get("failure_details", [])
            if item.get("code")
        ]
        recomputed_scores = fuse_scores(
            static_score=float(scores.get("static", claim.get("static", {}).get("score", 0.0))),
            dynamic_score=float(scores.get("dynamic", claim.get("dynamic", {}).get("score", 0.0))),
            visual_score=float(scores.get("visual", claim.get("visual", {}).get("score", 0.0))),
            design_score=float(scores.get("design", 0.0)),
            failure_codes=failure_codes,
        )
        claimed_total = scores.get("final", scores.get("overall_score"))
        recomputed = recomputed_scores["final"]
        schema_errors = result_schema_errors(claim)
        match = (
            claimed_total is not None
            and abs(float(claimed_total) - recomputed) <= 0.01
            and not schema_errors
        )
        payload = {
            "claimed_total": claimed_total,
            "recomputed_total": recomputed,
            "verified": match,
            "build_gate": gate,
            "schema_errors": schema_errors,
            "note": (
                "Verified schema, score arithmetic, and deterministic static gates; "
                "recorded browser/VLM observations are not replayed."
            ),
        }
    elif claim.get("evaluation_protocol") == "auto-v1":
        gate = build_gate_product(candidate)
        result = _run_verification(task, candidate)
        claimed_scores = claim.get("scores", {})
        dimensions = {
            dimension: max(0.0, min(5.0, float(claimed_scores.get(dimension, 0.0))))
            for dimension in AUTO_DIMENSION_WEIGHTS
        }
        rubric_score = 100.0 * sum(
            dimensions[dimension] / 5.0 * weight
            for dimension, weight in AUTO_DIMENSION_WEIGHTS.items()
        )
        recomputed = round(
            rubric_score
            * (1.0 if gate["ok"] else 0.0)
            * result["behavior_pass_rate"],
            4,
        )
        claimed_total = claimed_scores.get("overall_score")
        match = claimed_total is not None and abs(claimed_total - recomputed) <= 0.01
        payload = {
            "claimed_total": claimed_total,
            "recomputed_total": recomputed,
            "verified": match,
            "build_gate": gate,
            "contract_pass_rate": result["behavior_pass_rate"],
            "note": "Score arithmetic and deterministic gates verified; LLM observations are not replayed.",
        }
    elif task.id.startswith("mz_"):
        gate = build_gate_product(candidate)
        scores = claim.get("scores", {})
        dimensions = scores.get("dimensions") or {}
        claimed_total = scores.get("rubric_score", scores.get("zhen_score"))
        recomputed = round(
            _weighted_judge_score(task, dimensions) * (1.0 if gate["ok"] else 0.0),
            4,
        )
        match = claimed_total is not None and abs(claimed_total - recomputed) <= 0.01
        payload = {
            "claimed_total": claimed_total,
            "recomputed_total": recomputed,
            "verified": match,
            "build_gate": gate,
            "note": "Rubric arithmetic and artifact BUILD gate verified; judge observations are not replayed.",
        }
    else:
        result = _run_verification(task, candidate)
        recomputed = round(
            0.55 * result["behavior_pass_rate"] + 0.20 * result["static_pass_rate"],
            4,
        )
        claimed_total = claim.get("scores", {}).get("total")
        match = claimed_total is not None and abs(claimed_total - recomputed) <= 0.01
        payload = {
            "claimed_total": claimed_total,
            "recomputed_total": recomputed,
            "verified": match,
            "behavior_pass_rate": result["behavior_pass_rate"],
            "static_pass_rate": result["static_pass_rate"],
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if match else 1


if __name__ == "__main__":
    sys.exit(main())
