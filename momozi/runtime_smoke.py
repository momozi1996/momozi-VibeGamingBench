"""Lightweight browser runtime smoke evaluation.

This module verifies that an artifact launches and remains alive. It deliberately
does not contain task-specific gameplay semantics.
"""
from __future__ import annotations

import threading
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterator, Optional
from urllib.parse import urlparse

from .screenshot import capture_screenshot


RUNTIME_VERSION = "1.1"
DEFAULT_ALLOWED_HOSTS = ("unpkg.com", "cdn.jsdelivr.net", "cdnjs.cloudflare.com")


@dataclass
class RuntimeConfig:
    viewport_width: int = 1280
    viewport_height: int = 720
    locale: str = "en-US"
    timezone_id: str = "UTC"
    device_scale_factor: float = 1.0
    navigation_timeout_ms: int = 10000
    action_timeout_ms: int = 5000
    stabilization_ms: int = 1000
    input_probe: bool = True
    capture_after_input: bool = False
    capture_gameplay: bool = True
    auto_start: bool = True
    input_scheme: str = "auto"
    start_keys: tuple[str, ...] = ("Enter", "Space")
    gameplay_actions: int = 4
    allow_external_network: bool = False
    allowed_hosts: tuple[str, ...] = DEFAULT_ALLOWED_HOSTS


@dataclass
class RuntimeResult:
    status: str = "fail"
    server_start: bool = False
    page_load: bool = False
    runtime_stable: bool = False
    page_load_ms: Optional[int] = None
    fatal_console_errors: int = 0
    console_errors: list[str] = field(default_factory=list)
    page_errors: list[str] = field(default_factory=list)
    input_probe: dict[str, Any] = field(
        default_factory=lambda: {"attempted": False, "success": False}
    )
    screenshots: list[dict[str, Any]] = field(default_factory=list)
    browser: dict[str, Any] = field(default_factory=dict)
    viewport: dict[str, int] = field(default_factory=dict)
    runtime_config: dict[str, Any] = field(default_factory=dict)
    failure_code: Optional[str] = None
    failure_details: list[dict[str, str]] = field(default_factory=list)
    infrastructure_error: bool = False
    version: str = RUNTIME_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class _QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        return


@contextmanager
def artifact_server(product_dir: Path) -> Iterator[str]:
    """Serve one artifact directory on an ephemeral localhost port."""
    handler = partial(_QuietHandler, directory=str(product_dir))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    try:
        thread.start()
        host, port = server.server_address[:2]
        yield f"http://{host}:{port}/index.html"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def _route_request(route, request, config: RuntimeConfig) -> None:
    if config.allow_external_network:
        route.continue_()
        return
    parsed = urlparse(request.url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme in {"about", "blob", "data"}:
        route.continue_()
    elif host in {"127.0.0.1", "localhost"}:
        route.continue_()
    elif host in config.allowed_hosts and "three" in request.url.lower():
        route.continue_()
    else:
        route.abort("blockedbyclient")


def mock_runtime_result() -> dict[str, Any]:
    """Protocol fixture only; never eligible for an official leaderboard."""
    result = RuntimeResult(
        status="pass",
        server_start=True,
        page_load=True,
        runtime_stable=True,
        page_load_ms=1,
        input_probe={"attempted": True, "success": True, "mock": True},
        browser={"name": "mock", "version": "protocol-fixture"},
        viewport={"width": 1280, "height": 720},
        runtime_config={"mock": True},
    )
    return result.to_dict()


def run_runtime_smoke(
    product_dir: Path,
    evidence_dir: Path,
    config: Optional[RuntimeConfig] = None,
) -> dict[str, Any]:
    """Launch an artifact in Chromium and return inspectable runtime evidence."""
    config = config or RuntimeConfig()
    result = RuntimeResult(
        viewport={
            "width": config.viewport_width,
            "height": config.viewport_height,
        },
        runtime_config={
            "locale": config.locale,
            "timezone": config.timezone_id,
            "device_scale_factor": config.device_scale_factor,
            "stabilization_ms": config.stabilization_ms,
            "input_probe": config.input_probe,
            "auto_start": config.auto_start,
            "input_scheme": config.input_scheme,
            "start_keys": list(config.start_keys),
            "gameplay_actions": config.gameplay_actions,
            "network_policy": (
                "unrestricted"
                if config.allow_external_network
                else "local-plus-pinned-threejs-cdn"
            ),
            "allowed_hosts": list(config.allowed_hosts),
        },
    )
    if not (product_dir / "index.html").is_file():
        result.failure_code = "D_PAGE_LOAD_FAIL"
        result.failure_details.append(
            {"code": result.failure_code, "detail": "index.html is missing"}
        )
        return result.to_dict()

    try:
        from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        result.failure_code = "D_RUNTIME_UNAVAILABLE"
        result.infrastructure_error = True
        result.failure_details.append(
            {
                "code": result.failure_code,
                "detail": f"Playwright is not installed: {exc}",
            }
        )
        return result.to_dict()

    browser = None
    try:
        with artifact_server(product_dir) as url:
            result.server_start = True
            with sync_playwright() as playwright:
                try:
                    browser = playwright.chromium.launch(headless=True)
                except Exception as exc:
                    result.failure_code = "D_RUNTIME_UNAVAILABLE"
                    result.infrastructure_error = True
                    result.failure_details.append(
                        {
                            "code": result.failure_code,
                            "detail": f"Chromium launch failed: {exc}",
                        }
                    )
                    return result.to_dict()
                result.browser = {
                    "name": "chromium",
                    "version": browser.version,
                }
                context = browser.new_context(
                    viewport={
                        "width": config.viewport_width,
                        "height": config.viewport_height,
                    },
                    locale=config.locale,
                    timezone_id=config.timezone_id,
                    device_scale_factor=config.device_scale_factor,
                )
                context.set_default_timeout(config.action_timeout_ms)
                page = context.new_page()
                page.route(
                    "**/*",
                    lambda route, request: _route_request(
                        route, request, config
                    ),
                )
                page.on(
                    "console",
                    lambda message: (
                        result.console_errors.append(message.text)
                        if message.type == "error"
                        else None
                    ),
                )
                page.on(
                    "pageerror",
                    lambda error: result.page_errors.append(str(error)),
                )

                started = time.perf_counter()
                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=config.navigation_timeout_ms,
                )
                result.page_load_ms = round(
                    (time.perf_counter() - started) * 1000
                )
                result.page_load = True
                page.wait_for_timeout(config.stabilization_ms)

                try:
                    boot = capture_screenshot(
                        page,
                        evidence_dir / "boot.png",
                        width=config.viewport_width,
                        height=config.viewport_height,
                        browser="chromium",
                        browser_version=browser.version,
                        timeout_ms=config.action_timeout_ms,
                    )
                    result.screenshots.append(boot.to_dict())
                except Exception as exc:
                    result.failure_code = "D_SCREENSHOT_FAIL"
                    result.failure_details.append(
                        {
                            "code": result.failure_code,
                            "detail": str(exc),
                        }
                    )
                    return result.to_dict()

                if config.input_probe:
                    result.input_probe["attempted"] = True
                    try:
                        if config.auto_start:
                            # Pointer-native tasks often expose a visible start
                            # button instead of binding Enter/Space.
                            for selector in (
                                "#btnStartCampaign",
                                "#startButton",
                                "button:has-text('Start')",
                                "button:has-text('开始')",
                            ):
                                try:
                                    locator = page.locator(selector)
                                    if locator.count():
                                        locator.first.click()
                                        page.wait_for_timeout(120)
                                        break
                                except Exception:
                                    continue
                            for key in config.start_keys:
                                page.keyboard.press(key)
                                page.wait_for_timeout(80)
                        page.wait_for_timeout(180)
                        result.input_probe["success"] = True
                        if config.capture_gameplay:
                            gameplay_start = capture_screenshot(
                                page,
                                evidence_dir / "gameplay_start.png",
                                width=config.viewport_width,
                                height=config.viewport_height,
                                browser="chromium",
                                browser_version=browser.version,
                                timeout_ms=config.action_timeout_ms,
                            )
                            result.screenshots.append(gameplay_start.to_dict())
                        scheme = config.input_scheme
                        if scheme == "auto":
                            scheme = "keyboard"
                        if scheme in {
                            "pointer",
                            "pointer-first",
                            "both",
                        }:
                            width = config.viewport_width
                            height = config.viewport_height
                            page.mouse.click(width * 0.5, height * 0.52)
                            page.mouse.move(width * 0.25, height * 0.52)
                            page.mouse.down()
                            page.mouse.move(width * 0.75, height * 0.52, steps=6)
                            page.mouse.up()
                            page.mouse.click(width * 0.68, height * 0.42)
                        if scheme in {"keyboard", "keyboard-first", "both"}:
                            keys = (
                                "ArrowRight",
                                "ArrowDown",
                                "ArrowLeft",
                                "ArrowUp",
                                "Space",
                            )
                            for index in range(max(1, config.gameplay_actions)):
                                page.keyboard.press(keys[index % len(keys)])
                                page.wait_for_timeout(90)
                        page.wait_for_timeout(180)
                        if config.capture_gameplay:
                            gameplay_mid = capture_screenshot(
                                page,
                                evidence_dir / "gameplay_mid.png",
                                width=config.viewport_width,
                                height=config.viewport_height,
                                browser="chromium",
                                browser_version=browser.version,
                                timeout_ms=config.action_timeout_ms,
                            )
                            result.screenshots.append(gameplay_mid.to_dict())
                        elif config.capture_after_input:
                            after_input = capture_screenshot(
                                page,
                                evidence_dir / "after_input.png",
                                width=config.viewport_width,
                                height=config.viewport_height,
                                browser="chromium",
                                browser_version=browser.version,
                                timeout_ms=config.action_timeout_ms,
                            )
                            result.screenshots.append(after_input.to_dict())
                    except Exception as exc:
                        result.failure_code = "D_INPUT_PROBE_FAIL"
                        result.failure_details.append(
                            {
                                "code": result.failure_code,
                                "detail": str(exc),
                            }
                        )
                        return result.to_dict()

                result.fatal_console_errors = (
                    len(result.console_errors) + len(result.page_errors)
                )
                if result.fatal_console_errors:
                    result.failure_code = "D_RUNTIME_FATAL"
                    result.failure_details.append(
                        {
                            "code": result.failure_code,
                            "detail": (
                                f"{len(result.page_errors)} page errors and "
                                f"{len(result.console_errors)} console errors"
                            ),
                        }
                    )
                    return result.to_dict()

                result.runtime_stable = True
                result.status = "pass"
                context.close()
    except PlaywrightTimeoutError as exc:
        result.failure_code = "D_TIMEOUT"
        result.failure_details.append(
            {"code": result.failure_code, "detail": str(exc)}
        )
    except OSError as exc:
        result.failure_code = "D_SERVER_START_FAIL"
        result.failure_details.append(
            {"code": result.failure_code, "detail": str(exc)}
        )
    except Exception as exc:
        result.failure_code = "D_RUNTIME_FATAL"
        result.failure_details.append(
            {"code": result.failure_code, "detail": str(exc)}
        )
    finally:
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass
    return result.to_dict()
