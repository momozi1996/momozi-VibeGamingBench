"""End-to-end automatic generation, contract checking, LLM judging, and scoring."""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import re
import shlex
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
from .leaderboard import AUTO_PROTOCOL, DIMENSIONS, write_leaderboard
from .run import PROFILES_PATH, ROOT, _collect_product, _prepare_workspace
from .run_zhen import build_gate_product
from .task import Task
from .verifiers import BehaviorSuite

DEFAULT_JUDGE_MODEL = "deepseek-v4-flash"
DEFAULT_JUDGE_BASE_URL = "https://api.deepseek.com"
DIMENSION_WEIGHTS = {
    "completeness": 0.15,
    "richness": 0.35,
    "player_exp": 0.15,
    "visual": 0.35,
}
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


class DeepSeekJudge:
    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_JUDGE_MODEL,
        base_url: str = DEFAULT_JUDGE_BASE_URL,
        timeout: int = 240,
        retries: int = 3,
    ):
        if not api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY is empty. Put it in the repository root .env file."
            )
        self.api_key = api_key
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries

    @property
    def endpoint(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url
        return f"{self.base_url}/chat/completions"

    def evaluate(self, task: Task, product_dir: Path) -> tuple[dict, dict]:
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
        for attempt in range(self.retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    raw = json.loads(response.read().decode("utf-8"))
                content = raw["choices"][0]["message"]["content"]
                if not isinstance(content, str):
                    raise ValueError("judge response content is not text")
                return validate_judgement(_json_object(content)), raw.get("usage", {})
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")[:1000]
                last_error = RuntimeError(f"DeepSeek HTTP {exc.code}: {detail}")
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
            if attempt < self.retries:
                time.sleep(min(8, 2**attempt))
        raise RuntimeError(f"DeepSeek judge failed after retries: {last_error}")


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


def _contract(task: Task, product_dir: Path) -> dict:
    suite_name = task.behavior.get("script", "beh_html.mjs")
    suite = BehaviorSuite(
        product_dir,
        suite_name,
        timeout=int(task.behavior.get("timeout", 300)),
    )
    results = suite.run()
    passed = sum(1 for item in results if item.get("ok"))
    total = len(results)
    return {
        "pass_rate": round(passed / total, 6) if total else 0.0,
        "passed": passed,
        "total": total,
        "results": results,
    }


def _score(task: Task, judgement: dict, build_ok: bool, contract_rate: float) -> dict:
    weights = dict(DIMENSION_WEIGHTS)
    dimension_scores = {
        dimension: float(judgement["dimensions"][dimension]["score"])
        for dimension in DIMENSIONS
    }
    rubric_fraction = sum(
        dimension_scores[dimension] / 5.0 * weights[dimension]
        for dimension in DIMENSIONS
    )
    rubric_score = 100.0 * rubric_fraction
    build_multiplier = 1.0 if build_ok else 0.0
    contract_multiplier = max(0.0, min(1.0, float(contract_rate)))
    overall = rubric_score * build_multiplier * contract_multiplier
    return {
        **{key: round(value, 4) for key, value in dimension_scores.items()},
        "weights": weights,
        "rubric_score_100": round(rubric_score, 4),
        "build_multiplier": build_multiplier,
        "contract_multiplier": round(contract_multiplier, 6),
        "overall_score": round(overall, 4),
    }


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
    build_gate = build_gate_product(product_dir)
    contract = _contract(task, product_dir)
    evaluation_error = None
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
            "provider": "deepseek",
            "model": judge.model if judge else DEFAULT_JUDGE_MODEL,
            "skipped": True,
        }
    else:
        try:
            judgement, usage = judge.evaluate(task, product_dir) if judge else ({}, {})
            judge_meta = {"provider": "deepseek", "model": judge.model if judge else ""}
        except Exception as exc:
            evaluation_error = str(exc)
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
                "provider": "deepseek",
                "model": judge.model if judge else "",
                "error": evaluation_error,
            }

    scores = _score(task, judgement, build_gate["ok"], contract["pass_rate"])
    eligible = not mock_judge and evaluation_error is None and model_label != "mock"
    result = {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "evaluation_protocol": AUTO_PROTOCOL,
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_label": model_label,
        "agent": model_label,
        "task": task.id,
        "base_task_id": task.base_task_id,
        "family": task.family,
        "difficulty": task.difficulty,
        "language": task.language,
        "generation": generation,
        "build_gate": build_gate,
        "contract": contract,
        "dimensions": judgement["dimensions"],
        "fatal_issues": judgement["fatal_issues"],
        "confidence": judgement["confidence"],
        "scores": scores,
        "judge": {**judge_meta, "usage": usage},
        "leaderboard_eligible": eligible,
        "evaluation_error": evaluation_error,
        "workspace": str(work),
        "product_dir": str(product_dir),
    }
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


def _summary(run_id: str, model_label: str, results: list[dict]) -> dict:
    overall = [float(result["scores"]["overall_score"]) for result in results]
    return {
        "benchmark": PROJECT_NAME,
        "version": __version__,
        "evaluation_protocol": AUTO_PROTOCOL,
        "run_id": run_id,
        "model_label": model_label,
        "tasks": len(results),
        "build_passed": sum(1 for result in results if result["build_gate"]["ok"]),
        "contract_mean": round(
            sum(result["contract"]["pass_rate"] for result in results) / len(results),
            6,
        )
        if results
        else 0.0,
        "overall_score_mean": round(sum(overall) / len(overall), 4)
        if overall
        else 0.0,
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
    parser.add_argument("--harness-timeout", type=int, default=1800)
    parser.add_argument(
        "--judge-model",
        default=os.getenv("DEEPSEEK_JUDGE_MODEL", DEFAULT_JUDGE_MODEL),
    )
    parser.add_argument(
        "--judge-base-url",
        default=os.getenv("DEEPSEEK_BASE_URL", DEFAULT_JUDGE_BASE_URL),
    )
    parser.add_argument("--judge-timeout", type=int, default=240)
    parser.add_argument("--mock-judge", action="store_true", help="CI protocol check only")
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
        api_key = os.getenv("DEEPSEEK_API_KEY", "")
        try:
            judge = DeepSeekJudge(
                api_key,
                model=args.judge_model,
                base_url=args.judge_base_url,
                timeout=args.judge_timeout,
            )
        except ValueError as exc:
            parser.error(str(exc))

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

    summary = _summary(run_id, model_label, results)
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
