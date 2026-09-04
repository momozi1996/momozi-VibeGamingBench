# Automatic Evaluation Protocol

This document describes the v0.6 `agent-v2` evaluation path for
VibeGamingBench. The legacy v0.x runner and `auto-v1` result records remain
readable for continuity, but new publishable runs should use this protocol.

## 1. Scoring Key

The judges use OpenAI-compatible Chat Completions. For screenshot judging,
configure an official Doubao/Ark deployment that accepts image input and strict
JSON output; legacy DeepSeek variables remain supported:

```env
MOMOZI_JUDGE_API_KEY=your-key
MOMOZI_JUDGE_PROVIDER=ark
MOMOZI_JUDGE_MODEL=your-endpoint-model-id
MOMOZI_JUDGE_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
MOMOZI_VLM_API_KEY=your-key
MOMOZI_VLM_PROVIDER=ark
MOMOZI_VLM_MODEL=your-vision-endpoint-model-id
MOMOZI_VLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

Legacy configuration:

```env
DEEPSEEK_API_KEY=sk-your-key
DEEPSEEK_JUDGE_MODEL=deepseek-v4-flash
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_VLM_MODEL=deepseek-v4-flash
DEEPSEEK_VLM_BASE_URL=https://api.deepseek.com
```

`DEEPSEEK_API_KEY` is the only secret and is ignored by git. Do not place a
real key in source files, result JSON, or shell history. `--judge-model`,
`--judge-base-url`, `--vlm-model`, and `--vlm-base-url` override these values.
`--judge-samples` and `--vlm-samples` default to three and use a per-dimension
median to reduce single-call variance.

## 2. Agent Harness

The harness must write `index.html` and `game_logic.js` into the supplied
product directory. See [`AGENT_HARNESS.md`](AGENT_HARNESS.md) for the complete
contract.

Profile-based execution:

```bash
python3 scripts/auto_evaluate.py \
  --task mz_sports-fishing-tournament-en \
  --agent codex \
  --model-label your-model
```

External harness:

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --harness-command 'my-harness --prompt {prompt_file} --output {product_dir}' \
  --model-label your-model \
  --harness-label my-harness \
  --workers 4
```

Supported placeholders are `{prompt_file}`, `{product_dir}`, `{workspace}`,
`{task_file}`, and `{task_id}`. The same values are exported as
`MOMOZI_PROMPT_FILE`, `MOMOZI_PRODUCT_DIR`, `MOMOZI_WORKSPACE`,
`MOMOZI_TASK_FILE`, and `MOMOZI_TASK_ID`. Commands are executed as argument
arrays without shell interpolation.

## 3. Task Selection

Selection must be explicit:

```bash
--task TASK_ID
--all
--family FAMILY
--difficulty low|medium|high
--language en|zh
--offset N --limit N
```

Use `--dry-run` to inspect selection without generation or judging. `--resume`
requires `--run-id` and only reuses results produced with the same model and
judge configuration.

## 4. Evaluation Pipeline

For each task:

1. The harness generates an isolated artifact.
2. `StaticEvaluator` runs the deterministic BUILD gate and Node contract.
3. The code judge scores the legacy four dimensions when deterministic gates allow it.
4. Chromium runtime smoke starts a local server, loads the page, observes errors,
   sends the task's family-aware start/input probe, and captures `boot.png`,
   `gameplay_start.png`, and `gameplay_mid.png`.
5. The multimodal judge scores all available gameplay screenshots on Functional
   Visual and Presentation using a three-sample median.
6. `momozi.scoring` fuses components and applies diagnostic hard caps.
7. Results are written with schema v2 and aggregated into the release-aware leaderboard.

Dynamic evaluation is intentionally a smoke test. A pass means launch,
stability, input-probe success when enabled, and screenshot capture; it is not
full gameplay verification.

## 5. Scores

Component weights are fixed by scoring version `1.1`:

| Component | Weight |
|---|---:|
| Static | 0.40 |
| Dynamic | 0.25 |
| Visual | 0.20 |
| Design | 0.15 |

The visual component is the average of Functional Visual and Presentation,
converted from 0–5 to 0–100. Hard caps are applied to the fused raw score:

```text
BUILD failure       → final ≤ 20
boot/page-load fail → final ≤ 10
runtime fatal       → final ≤ 35
```

The result keeps both new scores and compatibility fields:

```text
scores.raw
scores.final
scores.overall_score
scores.rubric_score_100
scores.legacy_overall_score
```

## 6. Judge Rules

Code and screenshot judges must return strict JSON. Scores are 0–5:

| Score | Meaning |
|---:|---|
| 0 | Missing, unusable, or no verifiable implementation |
| 1 | Nominal presence but critically broken or superficial |
| 2 | Partial implementation with major omissions |
| 3 | Main requirements form a usable core experience |
| 4 | Strong completion with meaningful depth and polish |
| 5 | Excellent, thoroughly evidenced implementation |

The code judge must provide `score`, `reason`, `evidence`, and `missing` for
each dimension. It may use only concrete artifact code evidence. The VLM must
provide numeric `functional_visual`, `presentation`, and `confidence` plus
concrete visual evidence. Free-form or malformed output is a `JUDGE_FAIL` and
is not leaderboard eligible.

## 7. Result Schema

Each v0.7 result contains at least:

```json
{
  "schema_version": 2,
  "benchmark_release": "v0.7.0",
  "evaluation_protocol": "agent-v2",
  "task_id": "…-en",
  "base_task_id": "…",
  "language": "en",
  "agent": {"name": "…", "model": "…", "harness": "…"},
  "static": {"build": {}, "contract": {}, "score": 0.0},
  "dynamic": {"status": "pass", "screenshots": []},
  "visual": {"functional_visual": {}, "presentation": {}, "score": 0.0},
  "scores": {"raw": 0.0, "final": 0.0},
  "primary_failure": null,
  "failure_details": []
}
```

Failure details use structured codes such as
`STATIC_BUILD_FAIL`, `STATIC_CONTRACT_FAIL`, `D_SERVER_START_FAIL`,
`D_PAGE_LOAD_FAIL`, `D_RUNTIME_FATAL`, `D_RUNTIME_UNAVAILABLE`, `D_TIMEOUT`,
`D_INPUT_PROBE_FAIL`, `D_SCREENSHOT_FAIL`, `JUDGE_FAIL`, and `SCHEMA_FAIL`.

## 8. Leaderboard and Statistics

`leaderboard.json` and `LEADERBOARD.md` are generated after each run. Official
rows require a non-mock, schema-valid, infrastructure-complete run. Mock judge,
mock runtime, mock visual, and judge infrastructure failures are excluded.

The primary metric is family-balanced score. The leaderboard also reports
micro, concept-balanced, EN, ZH, language gap, static/dynamic/visual/design
components, runtime pass rate, bootstrap CI, and rank stability.

EN and ZH are paired by `base_task_id`. Bootstrap samples concepts with
replacement (default 1,000 iterations, seed 1337), and pairwise model deltas
use the same concept-level pairing.

## 9. Verification and Ablation

Recompute deterministic gates and score arithmetic from a result plus artifact
archive:

```bash
python3 -m momozi.verify result.json artifact.tar.gz
```

Compare static-only and runtime-grounded conditions:

```bash
python3 scripts/static_dynamic_ablation.py \
  --results-dir runs/auto/my-run \
  --json-out reports/ablation.json \
  --md-out reports/ablation.md
```

The key diagnostic is:

```text
static_false_positive_rate
  = count(static_pass AND runtime_fail) / count(static_pass)
```

Human calibration is intentionally small and honest:

```bash
python3 scripts/calibration.py sample --count 50
python3 scripts/calibration.py analyze reports/calibration_template.csv
```

No synthetic human scores are generated; the checked-in report remains
`pending` until ratings are supplied.

## 10. Validation Commands

```bash
bash scripts/smoke.sh
python3 -m unittest discover -s tests -v
python3 scripts/audit_tasks.py
python3 scripts/generate_task_distribution.py --check
python3 scripts/validate_pool.py --only-mz --workers 8
```

The release manifest is regenerated with:

```bash
python3 scripts/create_release_manifest.py
```
