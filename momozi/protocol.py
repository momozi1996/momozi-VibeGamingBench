"""Shared Agent Harness and result protocols.

The harness owns agent execution and artifact delivery. VibeGamingBench owns
static evaluation, dynamic evaluation, scoring, and statistics.
"""
from __future__ import annotations

from typing import Any


BEHAVIOR_PROTOCOL_VERSION = 1
RUNNER_ARGS = ["node", "<script.mjs>", "<artifact_dir>"]
OUTPUT_FORMAT = [
    {"id": "B0_xxx", "ok": "true|false", "detail": "string"},
]

SCHEMA_VERSION = 2
BENCHMARK_RELEASE = "v0.7.0"
AGENT_EVALUATION_PROTOCOL = "agent-v2"
LEGACY_AUTO_PROTOCOL = "auto-v1"

HARNESS_PLACEHOLDERS = (
    "{prompt_file}",
    "{product_dir}",
    "{workspace}",
    "{task_file}",
    "{task_id}",
)
HARNESS_ENV_VARS = (
    "MOMOZI_PROMPT_FILE",
    "MOMOZI_PRODUCT_DIR",
    "MOMOZI_WORKSPACE",
    "MOMOZI_TASK_FILE",
    "MOMOZI_TASK_ID",
)

FAILURE_CODES = {
    "STATIC_BUILD_FAIL",
    "STATIC_CONTRACT_FAIL",
    "D_SERVER_START_FAIL",
    "D_PAGE_LOAD_FAIL",
    "D_RUNTIME_FATAL",
    "D_RUNTIME_UNAVAILABLE",
    "D_TIMEOUT",
    "D_INPUT_PROBE_FAIL",
    "D_SCREENSHOT_FAIL",
    "JUDGE_FAIL",
    "SCHEMA_FAIL",
}


def agent_metadata(
    *,
    name: str,
    model: str,
    harness: str,
    version: str = "",
    model_version: str = "",
) -> dict[str, str]:
    """Create the stable agent identity block used by schema v2 results."""
    return {
        "name": name,
        "version": version,
        "model": model,
        "model_version": model_version,
        "harness": harness,
    }


def result_schema_errors(payload: dict[str, Any]) -> list[str]:
    """Return schema-v2 validation errors without mutating the result."""
    errors: list[str] = []
    required = {
        "schema_version",
        "benchmark_release",
        "evaluation_protocol",
        "task_id",
        "base_task_id",
        "language",
        "agent",
        "static",
        "visual",
        "scores",
        "failure_details",
    }
    missing = sorted(required - set(payload))
    if missing:
        errors.append(f"missing fields: {missing}")
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    if payload.get("evaluation_protocol") != AGENT_EVALUATION_PROTOCOL:
        errors.append(
            f"evaluation_protocol must be {AGENT_EVALUATION_PROTOCOL!r}"
        )
    if payload.get("language") not in {"en", "zh"}:
        errors.append("language must be 'en' or 'zh'")
    if not isinstance(payload.get("agent"), dict):
        errors.append("agent must be an object")
    else:
        for field in ("name", "model", "harness"):
            if not isinstance(payload["agent"].get(field), str):
                errors.append(f"agent.{field} must be a string")
    if "dynamic" not in payload and "runtime" not in payload:
        errors.append("result must contain 'dynamic' or 'runtime'")
    for field in ("static", "dynamic", "runtime", "visual", "scores"):
        if field not in payload:
            continue
        if not isinstance(payload.get(field), dict):
            errors.append(f"{field} must be an object")
    scores = payload.get("scores")
    if isinstance(scores, dict):
        final = scores.get("final")
        if not isinstance(final, (int, float)) or not 0.0 <= float(final) <= 100.0:
            errors.append("scores.final must be between 0 and 100")
    primary = payload.get("primary_failure")
    if primary is not None and primary not in FAILURE_CODES:
        errors.append(f"unsupported primary_failure: {primary!r}")
    details = payload.get("failure_details")
    if not isinstance(details, list) or any(
        not isinstance(item, dict) for item in details
    ):
        errors.append("failure_details must be a list of objects")
    return errors


def validate_result_schema(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate a schema-v2 result and return it unchanged."""
    errors = result_schema_errors(payload)
    if errors:
        raise ValueError("; ".join(errors))
    return payload
