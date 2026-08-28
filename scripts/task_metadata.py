"""Shared task metadata rules for the benchmark generators and audits."""
from __future__ import annotations

import re


FAMILY_BASE_SCORE = {
    "arcade": 1,
    "idle": 1,
    "visualnovel": 1,
    "narrative": 2,
    "sports": 2,
    "cardgame": 3,
    "platformer": 3,
    "puzzle": 3,
    "rhythm": 3,
    "tycoon": 3,
    "action": 4,
    "adventure": 4,
    "horror": 4,
    "racing": 4,
    "shooter": 4,
    "openworld": 5,
    "roguelike": 5,
    "rpg": 5,
    "simulation": 5,
    "strategy": 5,
    "survival": 5,
}

SIGNAL_GROUPS = (
    (
        "physics",
        "gravity",
        "collision",
        "vehicle",
        "flight",
        "fluid",
        "kinematic",
        "ballistic",
        "drift",
    ),
    (
        "pathfinding",
        "a*",
        "autonomous",
        "ai opponent",
        "faction",
        "patrol",
        "prediction",
        "agent behavior",
    ),
    (
        "economy",
        "production",
        "crafting",
        "ecosystem",
        "logistics",
        "territory",
        "persistent",
        "resource network",
    ),
    (
        "shader",
        "gpgpu",
        "kalman",
        "motion blur",
        "procedural",
        "multiplayer",
        "network",
        "audio context",
        "vibration api",
    ),
)


def difficulty_score(family: str, prompt: str) -> int:
    """Estimate implementation complexity from stable, language-neutral signals.

    Generators call this with the English prompt so paired English and Chinese
    tasks always receive the same tier.
    """
    core = prompt.split("## HTML Submission Format", 1)[0].lower()
    score = FAMILY_BASE_SCORE.get(family, 3)

    opening = core[:800]
    if re.search(r"\b3d\b", opening):
        score += 1

    score += sum(1 for signals in SIGNAL_GROUPS if any(signal in core for signal in signals))

    numbered_requirements = len(re.findall(r"(?m)^\s*\d+\.\s+\*\*", core))
    if numbered_requirements >= 7:
        score += 2
    elif numbered_requirements >= 5:
        score += 1
    return score


def classify_difficulty(family: str, prompt: str) -> str:
    score = difficulty_score(family, prompt)
    if score <= 4:
        return "low"
    if score <= 7:
        return "medium"
    return "high"

