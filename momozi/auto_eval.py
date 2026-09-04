"""End-to-end automatic generation, contract checking, LLM judging, and scoring."""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import dataclasses
import json
import os
import re
import shlex
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import PROJECT_NAME, __version__
from .adapters import build_adapter, load_profiles
from .judge import _artifact_digest, _rubric_text
from .judge_errors import JudgeFailure
from .leaderboard import DIMENSIONS, write_leaderboard
from .run import PROFILES_PATH, ROOT, _collect_product, _prepare_workspace
from .multimodal_judge import MultimodalJudge, mock_visual_judgement
from .protocol import (
    AGENT_EVALUATION_PROTOCOL,
    BENCHMARK_RELEASE,
    agent_metadata,
    validate_result_schema,
)
from .runtime_smoke import (
    RuntimeConfig,
    mock_runtime_result,
    run_runtime_smoke,
)
from .scoring import (
    design_component_score,
    dynamic_component_score,
    fuse_scores,
    legacy_rubric_score,
    static_component_score,
    visual_component_score,
)
from .static_eval import StaticEvaluator
from .statistics import aggregate_results, bootstrap_ci
from .task import Task

AUTO_PROTOCOL = AGENT_EVALUATION_PROTOCOL
# Keep the legacy environment names working while allowing an official
# OpenAI-compatible vision endpoint such as Volcano Engine Ark/Doubao.
DEFAULT_JUDGE_MODEL = os.getenv(
    "MOMOZI_JUDGE_MODEL",
    os.getenv(
        "ARK_JUDGE_MODEL",
        os.getenv(
            "DOUBAO_MODEL",
            os.getenv("DEEPSEEK_JUDGE_MODEL", "deepseek-v4-flash"),
        ),
    ),
)
DEFAULT_JUDGE_BASE_URL = os.getenv(
    "MOMOZI_JUDGE_BASE_URL",
    os.getenv(
        "ARK_BASE_URL",
        os.getenv(
            "DOUBAO_BASE_URL",
            os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        ),
    ),
)
DEFAULT_VLM_MODEL = os.getenv(
    "MOMOZI_VLM_MODEL",
    os.getenv("DEEPSEEK_VLM_MODEL", DEFAULT_JUDGE_MODEL),
)
MOCK_HTML = """<!doctype html>
<html><head><meta charset="utf-8"><title>auto-eval protocol fixture</title></head>
<body><canvas id="game"></canvas>
<script type="module">
import { createGame, advance } from './game_logic.js';
const game = createGame({});
function frame(){ advance(game, {}, 1 / 60); requestAnimationFrame(frame); }
frame();
</script></body></html>
"""
MOCK_LOGIC = """export function createGame(){return {state:'playing',score:0};}
export function advance(game,input,dt){return game;}
"""

JUDGE_SYSTEM_PROMPT = """You are the blind code judge for a browser-game benchmark.
Judge only the supplied task specification, rubric anchors, and artifact code. The
generator identity is intentionally hidden. Never infer implementation from filenames,
variable names, comments, plans, TODOs, or claims that are not backed by executable code.
Return only one valid JSON object."""

JUDGE_USER_TEMPLATE = """# Evaluation protocol

Score each dimension from 0 to 5 using these anchors:
- 0: missing, unusable, or no verifiable implementation.
- 1: nominal presence but critically broken or almost entirely superficial.
- 2: partially implemented; major requirements or loop connections are missing.
- 3: the main requirements are implemented and form a usable core experience.
- 4: strong completion with meaningful depth, feedback, and visible polish.
- 5: excellent, thoroughly evidenced implementation that materially exceeds the baseline.

Evidence rules:
- Base every score on concrete code evidence from index.html or game_logic.js.
- Name functions, state fields, event handlers, rendering blocks, or short code fragments.
- State important missing or broken requirements for every dimension.
- Do not award functionality merely because a label, menu, variable, comment, or TODO exists.
- Evaluate visual quality from authored rendering/CSS/canvas/WebGL code only; do not imagine
  runtime output that is not evidenced by the artifact.

# Task specification
{spec}

# Rubric anchors
{rubrics}

# Artifact code
{artifact}

# Required JSON shape
{{
  "dimensions": {{
    "completeness": {{
      "score": 0,
      "reason": "concise evidence-based explanation",
      "evidence": ["file and concrete code evidence"],
      "missing": ["important missing or broken item"]
    }},
    "richness": {{
      "score": 0,
      "reason": "concise evidence-based explanation",
      "evidence": ["file and concrete code evidence"],
      "missing": ["important missing or broken item"]
    }},
    "player_exp": {{
      "score": 0,
      "reason": "concise evidence-based explanation",
      "evidence": ["file and concrete code evidence"],
      "missing": ["important missing or broken item"]
    }},
    "visual": {{
      "score": 0,
      "reason": "concise evidence-based explanation",
      "evidence": ["file and concrete code evidence"],
      "missing": ["important missing or broken item"]
    }}
  }},
  "fatal_issues": [],
  "confidence": 0.0
}}"""


def _input_scheme_for_family(family: str) -> str:
    """Pick a conservative generic probe for the task's native interaction."""
    if family in {"puzzle", "strategy", "tycoon", "cardgame", "idle"}:
        return "pointer"
    if family in {"racing", "platformer", "shooter", "rhythm", "action", "arcade"}:
        return "keyboard"
    if family in {"openworld", "rpg", "simulation", "survival", "adventure"}:
        return "both"
    return "both"


def load_dotenv(path: Path) -> None:
    """Load a minimal KEY=VALUE .env file without overriding the process env."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ.setdefault(key, value)


def _json_object(text: str) -> dict:
    candidates: list[str | dict] = [text.strip()]
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
    raise ValueError("judge response does not contain a JSON object")


def _string_list(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"{field} must be a list of strings")
    return value


def validate_judgement(payload: dict) -> dict:
    dimensions = payload.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != set(DIMENSIONS):
        raise ValueError(f"judge dimensions must be exactly {list(DIMENSIONS)}")
    normalized = {}
    for dimension in DIMENSIONS:
        item = dimensions[dimension]
        if not isinstance(item, dict):
            raise ValueError(f"{dimension} must be an object")
        try:
            score = float(item["score"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"{dimension}.score must be numeric") from exc
        if not 0.0 <= score <= 5.0:
            raise ValueError(f"{dimension}.score must be between 0 and 5")
        reason = item.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"{dimension}.reason must be non-empty")
        evidence = _string_list(item.get("evidence"), f"{dimension}.evidence")
        if not evidence:
            raise ValueError(f"{dimension}.evidence must not be empty")
        missing = _string_list(item.get("missing", []), f"{dimension}.missing")
        normalized[dimension] = {
            "score": round(score, 4),
            "reason": reason.strip(),
            "evidence": evidence,
            "missing": missing,
        }
    fatal_issues = _string_list(payload.get("fatal_issues", []), "fatal_issues")
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    return {
        "dimensions": normalized,
        "fatal_issues": fatal_issues,
        "confidence": round(confidence, 4),
    }


def _aggregate_judgements(judgements: list[dict]) -> dict:
    """Use a robust median score and merge concrete evidence across samples."""
    if not judgements:
        raise ValueError("cannot aggregate an empty judgement list")
    dimensions = {}
    for dimension in DIMENSIONS:
        items = [judgement["dimensions"][dimension] for judgement in judgements]
        scores = [float(item["score"]) for item in items]
        evidence = []
        missing = []
        for item in items:
            for value in item.get("evidence", []):
                if value not in evidence:
                    evidence.append(value)
            for value in item.get("missing", []):
                if value not in missing:
                    missing.append(value)
        dimensions[dimension] = {
            "score": round(statistics.median(scores), 4),
            "reason": max(
                (item.get("reason", "").strip() for item in items),
                key=len,
            ),
            "evidence": evidence[:8] or ["No concrete evidence returned."],
            "missing": missing[:8],
        }
    fatal_issues = []
    for judgement in judgements:
        for issue in judgement.get("fatal_issues", []):
            if issue not in fatal_issues:
                fatal_issues.append(issue)
    return {
        "dimensions": dimensions,
        "fatal_issues": fatal_issues,
        "confidence": round(
            statistics.median(
                float(judgement.get("confidence", 0.0))
                for judgement in judgements
            ),
            4,
        ),
    }


class DeepSeekJudge:
    """OpenAI-compatible structured code judge.

    The historical class name is retained so existing callers keep working.
    Set ``base_url`` to an Ark/Doubao endpoint and ``model`` to the endpoint's
    deployed model ID to use a vision-capable official judge alongside the
    screenshot judge.
    """

    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_JUDGE_MODEL,
        base_url: str = DEFAULT_JUDGE_BASE_URL,
        timeout: int = 240,
        retries: int = 3,
        samples: int = 3,
        provider: str = "openai-compatible",
    ):
        if not api_key:
            raise ValueError(
                "Judge API key is empty. Set MOMOZI_JUDGE_API_KEY, "
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

    def _evaluate_once(
        self,
        task: Task,
        product_dir: Path,
        sample_index: int,
    ) -> tuple[dict, dict]:
        spec = "\n\n".join(
            f"## {round_spec.name}\n{round_spec.spec}" for round_spec in task.rounds
        )
        prompt = JUDGE_USER_TEMPLATE.format(
            spec=spec,
            rubrics=_rubric_text(task),
            artifact=_artifact_digest(product_dir, max_chars=48000),
        )
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "max_tokens": 4096,
        }
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        last_error: Exception | None = None
        details: list[dict[str, Any]] = []
        raw_content = ""
        raw_response = ""
        for attempt in range(self.retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    raw_response = response.read().decode("utf-8", errors="replace")
                    raw = json.loads(raw_response)
                content = raw["choices"][0]["message"]["content"]
                if not isinstance(content, str):
                    raise ValueError("judge response content is not text")
                raw_content = content
                return validate_judgement(_json_object(content)), raw.get("usage", {})
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")
                last_error = RuntimeError(f"DeepSeek HTTP {exc.code}: {detail}")
                details.append(
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
                details.append(
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
                time.sleep(min(8, 2**attempt))
        raise JudgeFailure(
            f"structured code judge failed after retries: {last_error}",
            details=details,
        )

    def evaluate(self, task: Task, product_dir: Path) -> tuple[dict, dict]:
        judgements = []
        usages = []
        failures = []
        for sample_index in range(self.samples):
            try:
                judgement, usage = self._evaluate_once(
                    task, product_dir, sample_index
                )
                judgements.append(judgement)
                usages.append(usage)
            except JudgeFailure as exc:
                failures.extend(exc.details)
        if not judgements:
            raise JudgeFailure(
                "all structured code judge samples failed",
                details=failures,
            )
        usage = {
            "samples_requested": self.samples,
            "samples_succeeded": len(judgements),
            "sample_failures": failures,
            "by_sample": usages,
        }
        return _aggregate_judgements(judgements), usage


# New name for integrations; the legacy class remains the public compatibility
# surface used by existing runners.
OpenAICompatibleJudge = DeepSeekJudge


def mock_judgement() -> dict:
    return {
        "dimensions": {
            dimension: {
                "score": 3.0,
                "reason": "Protocol fixture score; not a publishable quality judgement.",
                "evidence": ["index.html and game_logic.js protocol fixtures are present"],
                "missing": [],
            }
            for dimension in DIMENSIONS
        },
        "fatal_issues": [],
        "confidence": 1.0,
    }


def _safe_label(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-") or "model"


def _replace_placeholders(value: str, replacements: dict[str, str]) -> str:
    for key, replacement in replacements.items():
        value = value.replace(key, replacement)
    return value


def _run_harness(
    command: str,
    task: Task,
    work: Path,
    product_dir: Path,
    timeout: int,
) -> dict:
    prompt_file = work / "_prompt.md"
    replacements = {
        "{prompt_file}": str(prompt_file),
        "{product_dir}": str(product_dir),
        "{workspace}": str(work),
        "{task_file}": str(task.path),
        "{task_id}": task.id,
    }
    argv = [
        _replace_placeholders(argument, replacements)
        for argument in shlex.split(command)
    ]
    env = os.environ.copy()
    env.update(
        {
            "MOMOZI_PROMPT_FILE": str(prompt_file),
            "MOMOZI_PRODUCT_DIR": str(product_dir),
            "MOMOZI_WORKSPACE": str(work),
            "MOMOZI_TASK_FILE": str(task.path),
            "MOMOZI_TASK_ID": task.id,
        }
    )
    started = time.time()
    try:
        proc = subprocess.run(
            argv,
            cwd=work,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return {
            "mode": "harness-command",
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "duration_s": round(time.time() - started, 2),
            "stdout": proc.stdout[-2000:],
            "stderr": proc.stderr[-2000:],
        }
    except subprocess.TimeoutExpired:
        return {
            "mode": "harness-command",
            "ok": False,
            "duration_s": round(time.time() - started, 2),
            "stderr": f"harness timed out after {timeout}s",
        }
    except OSError as exc:
        return {
            "mode": "harness-command",
            "ok": False,
            "duration_s": round(time.time() - started, 2),
            "stderr": str(exc),
        }


def _generate(
    task: Task,
    model_label: str,
    agent: str | None,
    harness_command: str | None,
    run_id: str,
    harness_timeout: int,
) -> tuple[Path, Path, dict]:
    stamp = f"auto-{_safe_label(run_id)}"
    work = _prepare_workspace(task, _safe_label(model_label), stamp)
    product_dir = work / "product"
    prompt = "\n\n".join(round_spec.spec for round_spec in task.rounds)
    (work / "_prompt.md").write_text(prompt, encoding="utf-8")

    if harness_command:
        generation = _run_harness(
            harness_command,
            task,
            work,
            product_dir,
            harness_timeout,
        )
    elif agent == "mock":
        (product_dir / "index.html").write_text(MOCK_HTML, encoding="utf-8")
        (product_dir / "game_logic.js").write_text(MOCK_LOGIC, encoding="utf-8")
        generation = {
            "mode": "profile",
            "profile": "mock",
            "ok": True,
            "duration_s": 0.0,
            "stdout": "wrote auto-eval protocol fixture",
            "stderr": "",
        }
    else:
        adapter = build_adapter(agent or "", load_profiles(PROFILES_PATH))
        result = adapter.generate(work, prompt, 0)
        generation = {
            "mode": "profile",
            "profile": agent,
            "ok": bool(result.get("ok")),
            "returncode": result.get("returncode"),
            "duration_s": result.get("duration_s"),
            "stdout": (result.get("stdout") or "")[-2000:],
            "stderr": (result.get("stderr") or "")[-2000:],
        }
    generation["collected_from"] = _collect_product(work, product_dir)
    return work, product_dir, generation


def _empty_visual_judgement(reason: str) -> dict:
    return {
        "functional_visual": {"score": 0.0, "evidence": [reason]},
        "presentation": {"score": 0.0, "evidence": [reason]},
        "confidence": 0.0,
    }


def _score_agent_result(
    *,
    judgement: dict,
    static_eval: dict,
    runtime: dict,
    visual: dict,
    failure_codes: list[str],
) -> dict:
    build = static_eval.get("build", {})
    contract = static_eval.get("contract", {})
    static_score = static_component_score(
        build_ok=bool(build.get("ok")),
        contract_rate=float(contract.get("pass_rate", 0.0)),
        judgement=judgement,
    )
    dynamic_score = dynamic_component_score(runtime)
    visual_score = visual_component_score(visual)
    design_score = design_component_score(judgement)
    scores = fuse_scores(
        static_score=static_score,
        dynamic_score=dynamic_score,
        visual_score=visual_score,
        design_score=design_score,
        failure_codes=failure_codes,
    )
    scores["rubric_score_100"] = legacy_rubric_score(judgement)
    scores["build_multiplier"] = 1.0 if build.get("ok") else 0.0
    scores["contract_multiplier"] = round(
        max(0.0, min(1.0, float(contract.get("pass_rate", 0.0)))),
        6,
    )
    scores["legacy_overall_score"] = round(
        scores["rubric_score_100"]
        * scores["build_multiplier"]
        * scores["contract_multiplier"],
        4,
    )
    return scores


def _failure_details(
    static_eval: dict,
    runtime: dict,
    evaluation_error: str | None,
) -> list[dict]:
    details = list(static_eval.get("failure_details", []))
    details.extend(runtime.get("failure_details", []))
    if evaluation_error:
        details.append({"code": "JUDGE_FAIL", "detail": evaluation_error})
    return details


def evaluate_task(
    task_path: Path,
    *,
    run_id: str,
    run_dir: Path,
    model_label: str,
    agent: str | None,
    harness_command: str | None,
    harness_timeout: int,
    judge: DeepSeekJudge | None,
    mock_judge: bool,
    resume: bool,
    dynamic_enabled: bool = True,
    mock_runtime: bool = False,
    runtime_config: RuntimeConfig | None = None,
    visual_judge: MultimodalJudge | None = None,
    mock_visual: bool = False,
    agent_info: dict | None = None,
    harness_label: str = "",
    benchmark_release: str = BENCHMARK_RELEASE,
) -> dict:
    task = Task.load(task_path)
    result_path = run_dir / f"{task.id}.json"
    if resume and result_path.exists():
        existing = json.loads(result_path.read_text(encoding="utf-8"))
        if existing.get("model_label") != model_label:
            raise ValueError(
                f"{task.id}: resume result belongs to {existing.get('model_label')!r}, "
                f"not {model_label!r}"
            )
        if judge and existing.get("judge", {}).get("model") not in {None, judge.model}:
            raise ValueError(f"{task.id}: resume result uses a different judge model")
        return existing

    work, product_dir, generation = _generate(
        task,
        model_label,
        agent,
        harness_command,
        run_id,
        harness_timeout,
    )
    static_eval = StaticEvaluator().evaluate(task, product_dir)
    build_gate = static_eval["build"]
    contract = static_eval["contract"]
    evaluation_error = None
    evaluation_failure_details: list[dict[str, Any]] = []
    usage = {}

    if mock_judge:
        judgement = mock_judgement()
        judge_meta = {"provider": "mock", "model": "protocol-fixture"}
    elif not build_gate["ok"] or contract["pass_rate"] == 0:
        judgement = {
            "dimensions": {
                dimension: {
                    "score": 0.0,
                    "reason": "Deterministic gate failed; subjective judging was skipped.",
                    "evidence": ["See build_gate and contract results."],
                    "missing": ["A valid build and importable rules contract are required."],
                }
                for dimension in DIMENSIONS
            },
            "fatal_issues": ["deterministic gate failure"],
            "confidence": 1.0,
        }
        judge_meta = {
            "provider": judge.provider if judge else "openai-compatible",
            "model": judge.model if judge else DEFAULT_JUDGE_MODEL,
            "skipped": True,
        }
    else:
        try:
            judgement, usage = judge.evaluate(task, product_dir) if judge else ({}, {})
            judge_meta = {
                "provider": judge.provider if judge else "openai-compatible",
                "model": judge.model if judge else "",
            }
        except Exception as exc:
            evaluation_error = str(exc)
            evaluation_failure_details.extend(
                getattr(exc, "details", []) or []
            )
            judgement = {
                "dimensions": {
                    dimension: {
                        "score": 0.0,
                        "reason": "Judge infrastructure error; result is not leaderboard eligible.",
                        "evidence": ["No valid judge response was available."],
                        "missing": [],
                    }
                    for dimension in DIMENSIONS
                },
                "fatal_issues": ["judge infrastructure error"],
                "confidence": 0.0,
            }
            judge_meta = {
                "provider": judge.provider if judge else "openai-compatible",
                "model": judge.model if judge else "",
                "error": evaluation_error,
            }

    if not dynamic_enabled:
        runtime = {
            "status": "skipped",
            "server_start": False,
            "page_load": False,
            "runtime_stable": False,
            "fatal_console_errors": 0,
            "input_probe": {"attempted": False, "success": False},
            "screenshots": [],
            "failure_code": None,
            "failure_details": [],
            "runtime_config": {"skipped": True},
        }
    elif mock_runtime:
        runtime = mock_runtime_result()
    else:
        effective_runtime_config = dataclasses.replace(
            runtime_config or RuntimeConfig(),
            input_scheme=str(
                (task.evaluation or {}).get("input_scheme")
                or _input_scheme_for_family(task.family)
            ),
            start_keys=tuple(
                (task.evaluation or {}).get("start_keys")
                or ("Enter", "Space")
            ),
        )
        runtime = run_runtime_smoke(
            product_dir,
            run_dir / "evidence" / task.id,
            effective_runtime_config,
        )

    visual_usage = {}
    visual_meta = {
        "provider": "none",
        "model": "",
        "version": "",
    }
    if mock_judge or mock_visual:
        visual = mock_visual_judgement()
        visual_meta = {
            "provider": "mock",
            "model": "protocol-fixture",
            "version": "1.0",
        }
    else:
        screenshot_paths = [
            Path(item["path"])
            for item in runtime.get("screenshots", [])
            if item.get("path")
        ]
        if visual_judge and screenshot_paths and runtime.get("status") == "pass":
            try:
                visual, visual_usage = visual_judge.evaluate(
                    task,
                    runtime,
                    screenshot_paths,
                )
                visual_meta = {
                    "provider": visual_judge.provider,
                    "model": visual_judge.model,
                    "version": visual_judge.version,
                }
            except Exception as exc:
                evaluation_error = evaluation_error or str(exc)
                evaluation_failure_details.extend(
                    getattr(exc, "details", []) or []
                )
                visual = _empty_visual_judgement(
                    "No valid multimodal judge response was available."
                )
                visual_meta = {
                    "provider": visual_judge.provider,
                    "model": visual_judge.model,
                    "version": visual_judge.version,
                    "error": str(exc),
                }
        elif dynamic_enabled and runtime.get("status") == "pass" and not mock_runtime:
            evaluation_error = evaluation_error or (
                "multimodal judge is not configured"
            )
            visual = _empty_visual_judgement(
                "Multimodal judge was not configured."
            )
        else:
            visual = _empty_visual_judgement(
                "No successful runtime screenshot was available."
            )

    failure_details = _failure_details(
        static_eval,
        runtime,
        evaluation_error,
    )
    failure_details.extend(evaluation_failure_details)
    failure_codes = [
        item.get("code")
        for item in failure_details
        if item.get("code")
    ]
    scores = _score_agent_result(
        judgement=judgement,
        static_eval=static_eval,
        runtime=runtime,
        visual=visual,
        failure_codes=failure_codes,
    )
    primary_failure = next(
        (code for code in (
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
        ) if code in failure_codes),
        None,
    )
    agent_block = agent_info or agent_metadata(
        name=agent or "harness",
        model=model_label,
        harness=harness_label or ("profile" if agent else "external"),
    )
    eligible = (
        not mock_judge
        and not mock_visual
        and not mock_runtime
        and evaluation_error is None
        and model_label != "mock"
        and dynamic_enabled
        and not runtime.get("infrastructure_error")
    )
    result = {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "schema_version": 2,
        "benchmark_release": benchmark_release,
        "evaluation_protocol": AUTO_PROTOCOL,
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_label": model_label,
        "agent": agent_block,
        "task": task.id,
        "task_id": task.id,
        "base_task_id": task.base_task_id,
        "family": task.family,
        "difficulty": task.difficulty,
        "language": task.language,
        "generation": generation,
        "harness": {
            "name": harness_label or ("profile" if agent else "external"),
            "command": bool(harness_command),
            "contract_version": 1,
        },
        "static": {
            **static_eval,
            "score": scores["static"],
            "judge": {
                **judge_meta,
                "usage": usage,
            },
        },
        "dynamic": {
            **runtime,
            "score": scores["dynamic"],
        },
        # `runtime` is the schema-facing alias; `dynamic` remains the
        # benchmark terminology and backwards-compatible access path.
        "runtime": {
            **runtime,
            "score": scores["dynamic"],
        },
        "visual": {
            **visual,
            "score": scores["visual"],
            "judge": {
                **visual_meta,
                "usage": visual_usage,
            },
        },
        "build_gate": build_gate,
        "contract": contract,
        "dimensions": judgement["dimensions"],
        "fatal_issues": judgement["fatal_issues"],
        "confidence": judgement["confidence"],
        "scores": scores,
        "judge": {**judge_meta, "usage": usage},
        "leaderboard_eligible": eligible,
        "evaluation_error": evaluation_error,
        "primary_failure": primary_failure,
        "failure_details": failure_details,
        "workspace": str(work),
        "product_dir": str(product_dir),
    }
    try:
        validate_result_schema(result)
    except ValueError as exc:
        result["primary_failure"] = "SCHEMA_FAIL"
        result["failure_details"].append(
            {"code": "SCHEMA_FAIL", "detail": str(exc)}
        )
        result["leaderboard_eligible"] = False
    run_dir.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def discover_tasks(args: argparse.Namespace) -> list[Path]:
    all_paths = sorted((ROOT / "bench" / "tasks").glob("*/*.task.yaml"))
    by_id = {path.parent.name: path for path in all_paths}
    if args.task:
        selected = []
        for value in args.task:
            candidate = Path(value)
            if candidate.exists():
                selected.append(candidate.resolve())
            elif value in by_id:
                selected.append(by_id[value])
            else:
                raise ValueError(f"unknown task or path: {value}")
    else:
        selected = list(all_paths)

    def matches(path: Path) -> bool:
        task = Task.load(path)
        return (
            (not args.family or task.family in args.family)
            and (not args.difficulty or task.difficulty in args.difficulty)
            and (not args.language or task.language in args.language)
        )

    selected = [path for path in selected if matches(path)]
    selected = selected[args.offset :]
    if args.limit is not None:
        selected = selected[: args.limit]
    return selected


def _summary(
    run_id: str,
    model_label: str,
    results: list[dict],
    benchmark_release: str = BENCHMARK_RELEASE,
) -> dict:
    aggregate = aggregate_results(results)
    bootstrap = bootstrap_ci(results)
    return {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "schema_version": 2,
        "benchmark_release": benchmark_release,
        "evaluation_protocol": AUTO_PROTOCOL,
        "run_id": run_id,
        "model_label": model_label,
        "tasks": len(results),
        "build_passed": sum(1 for result in results if result["build_gate"]["ok"]),
        "runtime_passed": sum(
            1 for result in results
            if result.get("dynamic", {}).get("status") == "pass"
        ),
        "contract_mean": round(
            sum(result["contract"]["pass_rate"] for result in results) / len(results),
            6,
        )
        if results
        else 0.0,
        "overall_score_mean": aggregate["micro_score"],
        "metrics": aggregate,
        "bootstrap": bootstrap,
        "evaluation_errors": sum(
            1 for result in results if result.get("evaluation_error")
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="auto_evaluate.py",
        description="Generate games, run deterministic gates, judge them, and update leaderboard.",
    )
    parser.add_argument("--all", action="store_true", help="explicitly select the full task pool")
    parser.add_argument("--task", action="append", help="task ID or task YAML path; repeatable")
    parser.add_argument("--family", action="append")
    parser.add_argument(
        "--difficulty",
        action="append",
        choices=("low", "medium", "high"),
    )
    parser.add_argument("--language", action="append", choices=("en", "zh"))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--workers", type=int, default=1)
    generation = parser.add_mutually_exclusive_group(required=True)
    generation.add_argument(
        "--agent",
        help="profile name from profiles.yaml, such as codex or claude",
    )
    generation.add_argument(
        "--harness-command",
        help=(
            "command template with optional {prompt_file}, {product_dir}, {workspace}, "
            "{task_file}, and {task_id} placeholders"
        ),
    )
    parser.add_argument("--model-label", help="name displayed on the leaderboard")
    parser.add_argument("--model-version", default="")
    parser.add_argument("--agent-version", default="")
    parser.add_argument("--harness-label", default="")
    parser.add_argument("--harness-timeout", type=int, default=1800)
    parser.add_argument(
        "--judge-model",
        default=os.getenv(
            "MOMOZI_JUDGE_MODEL",
            os.getenv(
                "ARK_JUDGE_MODEL",
                os.getenv("DOUBAO_MODEL", os.getenv("DEEPSEEK_JUDGE_MODEL", DEFAULT_JUDGE_MODEL)),
            ),
        ),
    )
    parser.add_argument(
        "--judge-base-url",
        default=os.getenv(
            "MOMOZI_JUDGE_BASE_URL",
            os.getenv(
                "ARK_BASE_URL",
                os.getenv("DOUBAO_BASE_URL", os.getenv("DEEPSEEK_BASE_URL", DEFAULT_JUDGE_BASE_URL)),
            ),
        ),
    )
    parser.add_argument("--judge-timeout", type=int, default=240)
    parser.add_argument("--judge-samples", type=int, default=3)
    parser.add_argument("--judge-provider", default=os.getenv("MOMOZI_JUDGE_PROVIDER", "openai-compatible"))
    parser.add_argument(
        "--vlm-model",
        default=os.getenv(
            "MOMOZI_VLM_MODEL",
            os.getenv(
                "ARK_VLM_MODEL",
                os.getenv("DOUBAO_VLM_MODEL", os.getenv("DEEPSEEK_VLM_MODEL", DEFAULT_VLM_MODEL)),
            ),
        ),
    )
    parser.add_argument(
        "--vlm-base-url",
        default=os.getenv(
            "MOMOZI_VLM_BASE_URL",
            os.getenv(
                "ARK_VLM_BASE_URL",
                os.getenv(
                    "DOUBAO_VLM_BASE_URL",
                    os.getenv("DEEPSEEK_VLM_BASE_URL", os.getenv("DEEPSEEK_BASE_URL", DEFAULT_JUDGE_BASE_URL)),
                ),
            ),
        ),
    )
    parser.add_argument("--vlm-timeout", type=int, default=240)
    parser.add_argument("--vlm-samples", type=int, default=3)
    parser.add_argument("--vlm-provider", default=os.getenv("MOMOZI_VLM_PROVIDER", "openai-compatible"))
    parser.add_argument("--mock-judge", action="store_true", help="CI protocol check only")
    parser.add_argument(
        "--mock-runtime",
        action="store_true",
        help="protocol fixture only; never leaderboard eligible",
    )
    parser.add_argument(
        "--mock-visual",
        action="store_true",
        help="protocol fixture only; never leaderboard eligible",
    )
    parser.add_argument(
        "--skip-dynamic",
        action="store_true",
        help="static-only ablation path; never leaderboard eligible",
    )
    parser.add_argument("--runtime-timeout", type=int, default=10000)
    parser.add_argument("--stabilization-ms", type=int, default=1000)
    parser.add_argument(
        "--no-input-probe",
        action="store_true",
        help="disable the family-aware start and gameplay input probe",
    )
    parser.add_argument("--benchmark-release", default=BENCHMARK_RELEASE)
    parser.add_argument("--run-id")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-root", type=Path, default=ROOT / "runs" / "auto")
    parser.add_argument(
        "--leaderboard-out",
        type=Path,
        default=ROOT / "leaderboard.json",
    )
    parser.add_argument(
        "--leaderboard-md-out",
        type=Path,
        default=ROOT / "LEADERBOARD.md",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    load_dotenv(ROOT / ".env")
    parser = build_parser()
    args = parser.parse_args(argv)
    if not (args.all or args.task or args.family or args.difficulty or args.language):
        parser.error("select tasks with --all, --task, --family, --difficulty, or --language")
    if args.resume and not args.run_id:
        parser.error("--resume requires --run-id")
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.judge_samples < 1 or args.vlm_samples < 1:
        parser.error("--judge-samples and --vlm-samples must be at least 1")
    if args.offset < 0:
        parser.error("--offset must be non-negative")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    model_label = args.model_label or args.agent
    if not model_label:
        parser.error("--model-label is required with --harness-command")

    try:
        task_paths = discover_tasks(args)
    except ValueError as exc:
        parser.error(str(exc))
    if not task_paths:
        parser.error("task selection is empty")
    if args.dry_run:
        for path in task_paths:
            print(path.parent.name)
        print(f"{len(task_paths)} task(s) selected")
        return 0

    run_id = args.run_id or datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = args.output_root / _safe_label(run_id)
    judge = None
    if not args.mock_judge:
        api_key = (
            os.getenv("MOMOZI_JUDGE_API_KEY")
            or os.getenv("ARK_API_KEY")
            or os.getenv("DOUBAO_API_KEY")
            or os.getenv("DEEPSEEK_API_KEY", "")
        )
        try:
            judge = DeepSeekJudge(
                api_key,
                model=args.judge_model,
                base_url=args.judge_base_url,
                timeout=args.judge_timeout,
                samples=args.judge_samples,
                provider=args.judge_provider,
            )
        except ValueError as exc:
            parser.error(str(exc))

    visual_judge = None
    if not (args.mock_judge or args.mock_visual or args.skip_dynamic):
        api_key = (
            os.getenv("MOMOZI_VLM_API_KEY")
            or os.getenv("MOMOZI_JUDGE_API_KEY")
            or os.getenv("ARK_API_KEY")
            or os.getenv("DOUBAO_API_KEY")
            or os.getenv("DEEPSEEK_API_KEY", "")
        )
        try:
            visual_judge = MultimodalJudge(
                api_key,
                model=args.vlm_model,
                base_url=args.vlm_base_url,
                timeout=args.vlm_timeout,
                samples=args.vlm_samples,
                provider=args.vlm_provider,
            )
        except ValueError as exc:
            parser.error(str(exc))

    runtime_config = RuntimeConfig(
        navigation_timeout_ms=args.runtime_timeout,
        stabilization_ms=args.stabilization_ms,
        input_probe=not args.no_input_probe,
    )
    profile = (
        load_profiles(PROFILES_PATH).get(args.agent, {})
        if args.agent
        else {}
    )
    agent_info = agent_metadata(
        name=args.agent or "external-harness",
        model=model_label,
        harness=args.harness_label or (
            f"profile:{args.agent}" if args.agent else "external-command"
        ),
        version=args.agent_version or str(profile.get("agent_version", "")),
        model_version=args.model_version
        or str(profile.get("model_version", profile.get("model", ""))),
    )
    kwargs = {
        "run_id": run_id,
        "run_dir": run_dir,
        "model_label": model_label,
        "agent": args.agent,
        "harness_command": args.harness_command,
        "harness_timeout": args.harness_timeout,
        "judge": judge,
        "mock_judge": args.mock_judge,
        "resume": args.resume,
        "dynamic_enabled": not args.skip_dynamic,
        "mock_runtime": args.mock_runtime,
        "runtime_config": runtime_config,
        "visual_judge": visual_judge,
        "mock_visual": args.mock_visual,
        "agent_info": agent_info,
        "harness_label": args.harness_label or (
            f"profile:{args.agent}" if args.agent else "external-command"
        ),
        "benchmark_release": args.benchmark_release,
    }
    results = []
    with futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        jobs = {
            executor.submit(evaluate_task, path, **kwargs): path for path in task_paths
        }
        for index, future in enumerate(futures.as_completed(jobs), 1):
            path = jobs[future]
            try:
                result = future.result()
            except Exception as exc:
                print(
                    f"[{index}/{len(jobs)}] {path.parent.name}: infrastructure error: {exc}",
                    file=sys.stderr,
                )
                continue
            results.append(result)
            print(
                f"[{index}/{len(jobs)}] {result['task']}: "
                f"{result['scores']['overall_score']:.2f}"
            )

    summary = _summary(run_id, model_label, results, args.benchmark_release)
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    leaderboard = write_leaderboard(
        args.output_root,
        args.leaderboard_out,
        args.leaderboard_md_out,
    )
    (run_dir / "leaderboard.json").write_text(
        json.dumps(leaderboard, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if len(results) != len(task_paths) or summary["evaluation_errors"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
