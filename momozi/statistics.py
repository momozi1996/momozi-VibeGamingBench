"""Language-aware aggregation and paired bootstrap statistics."""
from __future__ import annotations

import random
from collections import Counter, defaultdict
from typing import Any, Iterable


STATISTICS_VERSION = "1.0"
DEFAULT_BOOTSTRAP_ITERATIONS = 1000
DEFAULT_BOOTSTRAP_SEED = 1337


def _mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def _score(record: dict) -> float:
    scores = record.get("scores", {})
    for key in ("final", "overall_score", "total"):
        if scores.get(key) is not None:
            return float(scores[key])
    return 0.0


def _task_id(record: dict) -> str:
    return str(record.get("task_id") or record.get("task") or "")


def _base_task_id(record: dict) -> str:
    value = record.get("base_task_id")
    if value:
        return str(value)
    task_id = _task_id(record)
    return task_id.removesuffix("-en").removesuffix("-zh")


def _concept_units(records: Iterable[dict]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[_base_task_id(record)].append(record)
    units = []
    for base_task_id, rows in sorted(grouped.items()):
        language_scores: dict[str, list[float]] = defaultdict(list)
        for row in rows:
            language_scores[str(row.get("language") or "")].append(_score(row))
        normalized_languages = {
            language: _mean(values)
            for language, values in language_scores.items()
            if language
        }
        units.append(
            {
                "base_task_id": base_task_id,
                "family": str(rows[0].get("family") or "unspecified"),
                "score": _mean(normalized_languages.values()),
                "languages": normalized_languages,
            }
        )
    return units


def aggregate_results(records: Iterable[dict]) -> dict[str, Any]:
    records = list(records)
    units = _concept_units(records)
    family_values: dict[str, list[float]] = defaultdict(list)
    language_values: dict[str, list[float]] = defaultdict(list)
    for unit in units:
        family_values[unit["family"]].append(unit["score"])
        for language, score in unit["languages"].items():
            language_values[language].append(score)
    family_scores = {
        family: round(_mean(values), 4)
        for family, values in sorted(family_values.items())
    }
    en_score = _mean(language_values.get("en", []))
    zh_score = _mean(language_values.get("zh", []))
    language_gap = (
        abs(en_score - zh_score)
        if language_values.get("en") and language_values.get("zh")
        else None
    )
    return {
        "micro_score": round(_mean(_score(row) for row in records), 4),
        "concept_balanced_score": round(
            _mean(unit["score"] for unit in units), 4
        ),
        "family_balanced_score": round(_mean(family_scores.values()), 4),
        "family_scores": family_scores,
        "en_score": round(en_score, 4),
        "zh_score": round(zh_score, 4),
        "language_gap": round(language_gap, 4) if language_gap is not None else None,
        "n_instances": len(records),
        "n_concepts": len(units),
        "n_families": len(family_scores),
        "statistics_version": STATISTICS_VERSION,
    }


def _metric_from_units(units: list[dict], metric: str) -> float:
    if metric == "concept_balanced_score":
        return _mean(unit["score"] for unit in units)
    if metric == "family_balanced_score":
        families: dict[str, list[float]] = defaultdict(list)
        for unit in units:
            families[unit["family"]].append(unit["score"])
        return _mean(_mean(values) for values in families.values())
    if metric == "micro_score":
        values = []
        for unit in units:
            values.extend(unit["languages"].values())
        return _mean(values)
    raise ValueError(f"unsupported metric: {metric}")


def _percentile(values: list[float], probability: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def bootstrap_ci(
    records: Iterable[dict],
    *,
    metric: str = "family_balanced_score",
    iterations: int = DEFAULT_BOOTSTRAP_ITERATIONS,
    seed: int = DEFAULT_BOOTSTRAP_SEED,
) -> dict[str, Any]:
    units = _concept_units(records)
    if not units:
        return {
            "mean": 0.0,
            "ci95": [0.0, 0.0],
            "iterations": iterations,
            "seed": seed,
            "sampling_unit": "base_task_id",
        }
    rng = random.Random(seed)
    sampled_values = []
    for _ in range(iterations):
        sample = [rng.choice(units) for _ in range(len(units))]
        sampled_values.append(_metric_from_units(sample, metric))
    return {
        "mean": round(_metric_from_units(units, metric), 4),
        "ci95": [
            round(_percentile(sampled_values, 0.025), 4),
            round(_percentile(sampled_values, 0.975), 4),
        ],
        "iterations": iterations,
        "seed": seed,
        "sampling_unit": "base_task_id",
        "metric": metric,
    }


def paired_delta_ci(
    records_a: Iterable[dict],
    records_b: Iterable[dict],
    *,
    metric: str = "family_balanced_score",
    iterations: int = DEFAULT_BOOTSTRAP_ITERATIONS,
    seed: int = DEFAULT_BOOTSTRAP_SEED,
) -> dict[str, Any]:
    a_by_id = {unit["base_task_id"]: unit for unit in _concept_units(records_a)}
    b_by_id = {unit["base_task_id"]: unit for unit in _concept_units(records_b)}
    common = sorted(set(a_by_id) & set(b_by_id))
    if not common:
        raise ValueError("paired comparison has no common base_task_id values")
    paired = [(a_by_id[key], b_by_id[key]) for key in common]
    rng = random.Random(seed)
    deltas = []
    for _ in range(iterations):
        sample = [rng.choice(paired) for _ in range(len(paired))]
        a_units = [item[0] for item in sample]
        b_units = [item[1] for item in sample]
        deltas.append(
            _metric_from_units(a_units, metric)
            - _metric_from_units(b_units, metric)
        )
    observed = _metric_from_units(
        [a_by_id[key] for key in common], metric
    ) - _metric_from_units([b_by_id[key] for key in common], metric)
    return {
        "delta": round(observed, 4),
        "ci95": [
            round(_percentile(deltas, 0.025), 4),
            round(_percentile(deltas, 0.975), 4),
        ],
        "iterations": iterations,
        "seed": seed,
        "paired_concepts": len(common),
        "metric": metric,
    }


def rank_stability(
    model_records: dict[str, list[dict]],
    *,
    metric: str = "family_balanced_score",
    iterations: int = DEFAULT_BOOTSTRAP_ITERATIONS,
    seed: int = DEFAULT_BOOTSTRAP_SEED,
) -> dict[str, Any]:
    units_by_model = {
        model: {
            unit["base_task_id"]: unit
            for unit in _concept_units(records)
        }
        for model, records in model_records.items()
    }
    if not units_by_model:
        return {}
    common = set.intersection(
        *(set(units) for units in units_by_model.values())
    )
    if not common:
        return {}
    common_ids = sorted(common)
    rng = random.Random(seed)
    ranks: dict[str, Counter] = {
        model: Counter() for model in units_by_model
    }
    for _ in range(iterations):
        sampled_ids = [rng.choice(common_ids) for _ in range(len(common_ids))]
        values = {}
        for model, units in units_by_model.items():
            sample = [units[base_id] for base_id in sampled_ids]
            values[model] = _metric_from_units(sample, metric)
        ordered = sorted(values.items(), key=lambda item: (-item[1], item[0]))
        for rank, (model, _) in enumerate(ordered, 1):
            ranks[model][rank] += 1
    return {
        model: {
            "rank_distribution": {
                str(rank): count / iterations
                for rank, count in sorted(counter.items())
            },
            "p_rank_1": round(counter.get(1, 0) / iterations, 6),
        }
        for model, counter in ranks.items()
    }
