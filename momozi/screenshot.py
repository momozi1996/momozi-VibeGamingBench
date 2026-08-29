"""Stable screenshot capture used by the dynamic evaluator."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCREENSHOT_VERSION = "1.0"


@dataclass
class ScreenshotResult:
    path: str
    width: int
    height: int
    timestamp: str
    browser: str
    browser_version: str
    viewport: dict[str, int]
    version: str = SCREENSHOT_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def capture_screenshot(
    page,
    output_path: Path,
    *,
    width: int,
    height: int,
    browser: str,
    browser_version: str,
    timeout_ms: int,
) -> ScreenshotResult:
    """Capture a full viewport screenshot after the caller stabilizes the page."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(
        path=str(output_path),
        full_page=False,
        timeout=timeout_ms,
    )
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(f"screenshot was not written: {output_path}")
    return ScreenshotResult(
        path=str(output_path),
        width=width,
        height=height,
        timestamp=datetime.now(timezone.utc).isoformat(),
        browser=browser,
        browser_version=browser_version,
        viewport={"width": width, "height": height},
    )
