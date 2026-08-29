"""Versioned static/dynamic score fusion for the Agent Benchmark."""
from __future__ import annotations

from typing import Any, Iterable


SCORING_VERSION = "1.0"
COMPONENT_WEIGHTS = {
    "static": 0.40,
    "dynamic": 0.25,
    "visual": 0.20,
    "design": 0.15,
}
HARD_CAPS = {
    "D_SERVER_START_FAIL": 10.0,
    "STATIC_BUILD_FAIL": 20.0,
    "D_PAGE_LOAD_FAIL": 10.0,
    "D_RUNTIME_FATAL": 35.0,
}
CAP_PRECEDENCE = (
    "D_SERVER_START_FAIL",
    "D_PAGE_LOAD_FAIL",
    "STATIC_BUILD_FAIL",
    "D_RUNTIME_FATAL",
)
DYNAMIC_FAILURE_SCORES = {
    "D_SERVER_START_FAIL": 0.0,
    "D_PAGE_LOAD_FAIL": 0.0,
    "D_RUNTIME_FATAL": 35.0,
    "D_RUNTIME_UNAVAILABLE": 0.0,
    "D_TIMEOUT": 30.0,
    "D_INPUT_PROBE_FAIL": 80.0,
    "D_SCREENSHOT_FAIL": 85.0,
}


def _bounded(value: Any, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, float(value)))


def dimension_scores(judgement: dict) -> dict[str, float]:
    dimensions = judgement.get("dimensions", {})
    return {
        key: _bounded(item.get("score", 0.0), 0.0, 5.0)
        for key, item in dimensions.items()
        if isinstance(item, dict)
    }


def static_component_score(
    *,
    build_ok: bool,
    contract_rate: float,
    judgement: dict,
) -> float:
    """Blend artifact, API contract, and implementation evidence."""
    scores = dimension_scores(judgement)
    implementation = 10.0 * (
        scores.get("completeness", 0.0) + scores.get("player_exp", 0.0)
    )
    value = (
        0.25 * (100.0 if build_ok else 0.0)
        + 0.25 * (_bounded(contract_rate, 0.0, 1.0) * 100.0)
        + 0.50 * implementation
    )
    return round(_bounded(value), 4)


def design_component_score(judgement: dict) -> float:
    """Reuse the static code judge for design evidence without replacing it."""
    scores = dimension_scores(judgement)
    value = 100.0 * (
        0.60 * scores.get("richness", 0.0) / 5.0
        + 0.40 * scores.get("visual", 0.0) / 5.0
    )
    return round(_bounded(value), 4)


def dynamic_component_score(runtime: dict) -> float:
    if runtime.get("status") == "pass":
        return 100.0
    return DYNAMIC_FAILURE_SCORES.get(runtime.get("failure_code"), 0.0)


def visual_component_score(visual: dict) -> float:
    functional = _bounded(
        (visual.get("functional_visual") or {}).get("score", 0.0),
        0.0,
        5.0,
    )
    presentation = _bounded(
        (visual.get("presentation") or {}).get("score", 0.0),
        0.0,
        5.0,
    )
    return round(10.0 * (functional + presentation), 4)


def legacy_rubric_score(judgement: dict) -> float:
    weights = {
        "completeness": 0.15,
        "richness": 0.35,
        "player_exp": 0.15,
        "visual": 0.35,
    }
    scores = dimension_scores(judgement)
    return round(
        100.0
        * sum(scores.get(key, 0.0) / 5.0 * weight for key, weight in weights.items()),
        4,
    )


def fuse_scores(
    *,
    static_score: float,
    dynamic_score: float,
    visual_score: float,
    design_score: float,
    failure_codes: Iterable[str] = (),
) -> dict[str, Any]:
    components = {
        "static": _bounded(static_score),
        "dynamic": _bounded(dynamic_score),
        "visual": _bounded(visual_score),
        "design": _bounded(design_score),
    }
    raw = sum(
        components[name] * COMPONENT_WEIGHTS[name]
        for name in COMPONENT_WEIGHTS
    )
    codes = set(failure_codes)
    applicable = [
        (code, HARD_CAPS[code])
        for code in CAP_PRECEDENCE
        if code in codes
    ]
    applied_cap = min(applicable, key=lambda item: item[1]) if applicable else None
    final = min(raw, applied_cap[1]) if applied_cap else raw
    return {
        **{key: round(value, 4) for key, value in components.items()},
        "weights": dict(COMPONENT_WEIGHTS),
        "raw": round(raw, 4),
        "final": round(final, 4),
        "overall_score": round(final, 4),
        "hard_cap": (
            {"code": applied_cap[0], "maximum": applied_cap[1]}
            if applied_cap
            else None
        ),
        "scoring_version": SCORING_VERSION,
    }
