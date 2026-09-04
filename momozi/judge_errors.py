"""Shared structured errors for code and multimodal judge calls."""
from __future__ import annotations

from typing import Any


class JudgeFailure(RuntimeError):
    """A judge failure that should be preserved in result failure_details."""

    def __init__(self, message: str, *, details: list[dict[str, Any]] | None = None):
        super().__init__(message)
        self.details = details or []
