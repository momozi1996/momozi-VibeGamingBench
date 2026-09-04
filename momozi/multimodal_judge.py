"""Screenshot-grounded visual judge with strict structured output."""
from __future__ import annotations

import base64
import json
import mimetypes
import os
import re
import statistics
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from .judge_errors import JudgeFailure


MULTIMODAL_JUDGE_VERSION = "1.1"
DEFAULT_VLM_MODEL = os.getenv(
    "MOMOZI_VLM_MODEL",
    os.getenv("ARK_VLM_MODEL", os.getenv("DOUBAO_VLM_MODEL", os.getenv("DEEPSEEK_VLM_MODEL", "deepseek-v4-flash"))),
)
DEFAULT_VLM_BASE_URL = os.getenv(
    "MOMOZI_VLM_BASE_URL",
    os.getenv(
        "ARK_VLM_BASE_URL",
        os.getenv("DOUBAO_VLM_BASE_URL", os.getenv("DEEPSEEK_VLM_BASE_URL", "https://api.deepseek.com")),
    ),
)

SYSTEM_PROMPT = """You are the screenshot-grounded visual judge for an Agent
Benchmark for Vibe Gaming. Use runtime facts as authoritative. Judge only what is
visible in the supplied screenshots relative to the task. Return one JSON object
and do not infer executable behavior that is not present in the runtime evidence."""

USER_TEXT = """# Task
{task}

# High-level visual rubric
- Functional Visual: main game content, requested objects, readable UI, coherent
  visible state, and visible match to the core task intent.
- Presentation: layout, visual coherence, consistency, readability, and basic polish.

# Runtime evidence
{runtime}

# Required JSON
{{
  "functional_visual": {{"score": 0, "evidence": []}},
  "presentation": {{"score": 0, "evidence": []}},
  "confidence": 0.0
}}

Scores must be numeric from 0 to 5. Evidence must be a list of concrete visual
observations. Return JSON only."""


def _json_object(text: str) -> dict:
    candidates = [text.strip()]
    candidates.extend(
        match.group(1).strip()
        for match in re.finditer(r"```(?:json)?\s*([\s\S]*?)```", text)
    )
    decoder = json.JSONDecoder()
    for index, char in enumerate(text):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(text[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            candidates.append(value)
    for candidate in reversed(candidates):
        if isinstance(candidate, dict):
            return candidate
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    raise ValueError("visual judge response does not contain a JSON object")


def validate_visual_judgement(payload: dict) -> dict[str, Any]:
    normalized = {}
    for field in ("functional_visual", "presentation"):
        item = payload.get(field)
        if not isinstance(item, dict):
            raise ValueError(f"{field} must be an object")
        try:
            score = float(item["score"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"{field}.score must be numeric") from exc
        if not 0.0 <= score <= 5.0:
            raise ValueError(f"{field}.score must be between 0 and 5")
        evidence = item.get("evidence")
        if not isinstance(evidence, list) or any(
            not isinstance(value, str) for value in evidence
        ):
            raise ValueError(f"{field}.evidence must be a list of strings")
        normalized[field] = {
            "score": round(score, 4),
            "evidence": evidence,
        }
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    return {
        **normalized,
        "confidence": round(confidence, 4),
    }


def mock_visual_judgement() -> dict[str, Any]:
    return {
        "functional_visual": {
            "score": 3.0,
            "evidence": ["Protocol fixture visual score; not publishable."],
        },
        "presentation": {
            "score": 3.0,
            "evidence": ["Protocol fixture presentation score; not publishable."],
        },
        "confidence": 1.0,
    }


def _data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


class MultimodalJudge:
    version = MULTIMODAL_JUDGE_VERSION

    def __init__(
        self,
        api_key: str,
        *,
        model: str = DEFAULT_VLM_MODEL,
        base_url: str = DEFAULT_VLM_BASE_URL,
        timeout: int = 240,
        retries: int = 2,
        samples: int = 3,
        provider: str = "openai-compatible",
    ):
        if not api_key:
            raise ValueError(
                "VLM judge API key is empty. Set MOMOZI_VLM_API_KEY, "
                "ARK_API_KEY, or DEEPSEEK_API_KEY in the repository root .env file."
            )
        self.api_key = api_key
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.samples = max(1, int(samples))
        self.provider = provider

    @property
    def endpoint(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url
        return f"{self.base_url}/chat/completions"

    def evaluate(
        self,
        task,
        runtime: dict,
        screenshot_paths: list[Path],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        if not screenshot_paths:
            raise ValueError("multimodal judge requires at least one screenshot")
        text = USER_TEXT.format(
            task="\n\n".join(round_spec.spec for round_spec in task.rounds),
            runtime=json.dumps(runtime, ensure_ascii=False, indent=2),
        )
        content: list[dict[str, Any]] = [{"type": "text", "text": text}]
        for screenshot in screenshot_paths:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": _data_uri(screenshot)},
                }
            )
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "max_tokens": 2048,
        }
        judgements = []
        usages = []
        failures = []
        for sample_index in range(self.samples):
            last_error: Exception | None = None
            raw_content = ""
            raw_response = ""
            for attempt in range(self.retries + 1):
                request = urllib.request.Request(
                    self.endpoint,
                    data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                try:
                    with urllib.request.urlopen(
                        request, timeout=self.timeout
                    ) as response:
                        raw_response = response.read().decode(
                            "utf-8", errors="replace"
                        )
                        raw = json.loads(raw_response)
                    content_text = raw["choices"][0]["message"]["content"]
                    if not isinstance(content_text, str):
                        raise ValueError("visual judge response content is not text")
                    raw_content = content_text
                    judgements.append(
                        validate_visual_judgement(_json_object(content_text))
                    )
                    usages.append(raw.get("usage", {}))
                    break
                except urllib.error.HTTPError as exc:
                    detail = exc.read().decode("utf-8", errors="replace")
                    last_error = RuntimeError(
                        f"visual judge HTTP {exc.code}: {detail}"
                    )
                    failures.append(
                        {
                            "code": "JUDGE_FAIL",
                            "detail": (
                                f"sample={sample_index} attempt={attempt + 1} "
                                f"HTTP {exc.code}: {detail}"
                            ),
                        }
                    )
                    if exc.code != 429 and not 500 <= exc.code < 600:
                        break
                except (
                    urllib.error.URLError,
                    TimeoutError,
                    json.JSONDecodeError,
                    KeyError,
                    ValueError,
                ) as exc:
                    last_error = exc
                    failures.append(
                        {
                            "code": "JUDGE_FAIL",
                            "detail": (
                                f"sample={sample_index} attempt={attempt + 1}: {exc}"
                                + (
                                    f" raw_response={raw_content or raw_response}"
                                    if (raw_content or raw_response)
                                    else ""
                                )
                            ),
                        }
                    )
                if attempt < self.retries:
                    time.sleep(min(4, 2**attempt))
            else:
                failures.append(
                    {
                        "code": "JUDGE_FAIL",
                        "detail": (
                            f"sample={sample_index} exhausted retries: {last_error}"
                        ),
                    }
                )
        if not judgements:
            raise JudgeFailure(
                "all multimodal judge samples failed",
                details=failures,
            )
        functional_scores = [item["functional_visual"]["score"] for item in judgements]
        presentation_scores = [item["presentation"]["score"] for item in judgements]
        functional_evidence = []
        presentation_evidence = []
        for item in judgements:
            for value in item["functional_visual"]["evidence"]:
                if value not in functional_evidence:
                    functional_evidence.append(value)
            for value in item["presentation"]["evidence"]:
                if value not in presentation_evidence:
                    presentation_evidence.append(value)
        judgement = {
            "functional_visual": {
                "score": round(statistics.median(functional_scores), 4),
                "evidence": functional_evidence[:10],
            },
            "presentation": {
                "score": round(statistics.median(presentation_scores), 4),
                "evidence": presentation_evidence[:10],
            },
            "confidence": round(
                statistics.median(item["confidence"] for item in judgements),
                4,
            ),
        }
        return judgement, {
            "samples_requested": self.samples,
            "samples_succeeded": len(judgements),
            "sample_failures": failures,
            "by_sample": usages,
        }
