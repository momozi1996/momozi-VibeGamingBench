# VibeGamingBench Design (v0.7.0)

## 1. Positioning

VibeGamingBench is an **Agent Benchmark for Vibe Gaming**. It measures whether
a coding agent, executed through an Agent Harness, can transform a
single-language game brief into a complete browser-game artifact and whether
that artifact actually launches in a controlled browser smoke environment.

The benchmark is deliberately execution-grounded but minimal:

```text
Agent Harness → Coding Agent → Game Artifact
                               ↙           ↘
                         STATIC          DYNAMIC
                         artifact        browser smoke
                         contract        + screenshot
                               ↘           ↙
                              Judge
                               ↓
                          Score Fusion
                               ↓
                     Balanced Statistical BMK
```

Static and Dynamic are first-class evaluation modes. Dynamic is a bounded
runtime smoke test, not a full gameplay simulator.

## 2. Dataset Semantics

The release contains the existing pool plus the Feishu Prompt Catalog import:

- 711 unique game concepts.
- 1,422 evaluation instances: one English and one Chinese realization per concept.
- 21 normalized game families.
- Heuristic `low`, `medium`, and `high` implementation difficulty.

The 220 added concepts come from the Feishu Prompt Catalog workbook: 100
structured type/technology seeds from `直接1` and 120 full generation prompts
from `直接生成`. Each is wrapped without changing its core gameplay intent,
then paired as an English and Chinese task under the same contract and rubric.

`base_task_id` is the concept-level statistical unit. EN and ZH are paired
variants, not 1,422 independent concepts.

## 3. Task Record

Every task directory contains exactly four files:

| File | Purpose |
|---|---|
| `<task-id>.task.yaml` | identity, language, family, difficulty, contract, rubric |
| `prompt.md` | canonical single-language generation prompt |
| `rubric.original.json` | concrete requirements and BUILD anchor |
| `rubric.mapping.json` | requirement-to-dimension mapping |

The task YAML may opt into:

```yaml
evaluation:
  runtime_smoke: true
  screenshot: true
  primary_entrypoint: index.html
```

When omitted, v0.6 defaults apply. No task embeds custom runtime evaluator
code.

## 4. Artifact Contract

The generated product must contain:

```text
index.html
game_logic.js
```

The entry page must expose a Canvas or WebGL rendering path. The logic script
must expose `createGame(opts)` and `advance(game, input, dt)` through
`window.GameLogic` (with a CommonJS fallback) and should remain independent of
DOM/rendering code. An optional `render(gameState, renderCtx)` hook owns visual
side effects. Tasks prohibit build steps and arbitrary runtime downloads;
procedurally generated data-URI textures and synthesized audio are allowed,
while pinned Three.js CDN references are handled by the runtime policy.

## 5. Static Evaluation

Static evaluation answers **what the agent built**. It combines:

1. Deterministic BUILD gate for required files, rendering signal, and resource policy.
2. Deterministic Node behavior contract.
3. Existing code-based rubric judge for completeness, richness, player experience, and visual evidence.

The legacy v0.x runner and result paths remain available. The v0.6
`StaticEvaluator` wraps the same deterministic checks instead of replacing them.

## 6. Dynamic Evaluation

Dynamic evaluation answers **what the artifact does when launched**. The
runtime smoke runner:

1. Starts an ephemeral localhost HTTP server.
2. Launches headless Chromium.
3. Uses a fixed 1280×720 viewport, `en-US`, `UTC`, and device scale factor 1.
4. Loads the page and records browser version and page-load time.
5. Captures console/page errors during a bounded stabilization window.
6. Uses the task's family-aware start key and pointer/keyboard probe unless disabled.
7. Captures `boot.png`, `gameplay_start.png`, and `gameplay_mid.png`.

Runtime failures remain structured (`D_SERVER_START_FAIL`,
`D_PAGE_LOAD_FAIL`, `D_RUNTIME_FATAL`, `D_TIMEOUT`, `D_SCREENSHOT_FAIL`, and
related codes). A pass does not imply complete gameplay correctness.

## 7. Screenshot and VLM Judge

The screenshot is inspectable runtime evidence. The multimodal judge receives
the task prompt, high-level visual rubric, runtime facts, and gameplay
screenshots. It
must return strict JSON with two 0–5 dimensions:

- `functional_visual`: visible game content, requested objects, readable UI,
  coherent state, and match to prompt intent.
- `presentation`: layout, consistency, readability, and basic polish.

Malformed or unavailable VLM output is a judge infrastructure failure and is
excluded from the official leaderboard. Deterministic runtime observations have
priority over model inference.

## 8. Score Fusion

All component weights and caps are versioned in `momozi/scoring.py`:

| Component | Weight |
|---|---:|
| Static | 0.40 |
| Dynamic | 0.25 |
| Visual | 0.20 |
| Design | 0.15 |

`Visual = 0.5 × FunctionalVisual + 0.5 × Presentation` on a 0–100 scale.
Design reuses authored code-judge evidence without replacing the legacy rubric.

Hard caps are diagnostic caps, not extra multipliers:

```text
BUILD failure       → final ≤ 20
boot/page-load fail → final ≤ 10
runtime fatal       → final ≤ 35
```

Every result keeps raw component scores, final score, scoring version, and any
applied cap. The legacy rubric score is retained for v0.x continuity.

## 9. Statistical Aggregation

The leaderboard computes:

```text
micro_score          = mean of all evaluation instances
concept_balanced     = mean after pairing EN/ZH by base_task_id
family_balanced      = mean of family means
EN, ZH, language_gap = language-aware reporting
```

Paired bootstrap samples `base_task_id` with replacement, defaults to 1,000
iterations and seed 1337, and reports 95% confidence intervals. Pairwise model
comparisons use paired delta intervals. Ranking stability reuses the same
bootstrap concept samples and reports rank distributions plus `P(rank=1)`.

The official headline metric is family-balanced score; micro remains a
secondary compatibility metric.

## 10. Calibration and Ablation

`scripts/calibration.py` creates a 50-task EN/ZH-balanced human calibration
template covering families and heuristic difficulty. It never fabricates
human ratings; the checked-in report remains `pending` until ratings are
provided. The intended comparison is Functional Visual, Presentation, and
Overall Quality against the VLM using Spearman correlation, MAE, and
inter-rater agreement.

`scripts/static_dynamic_ablation.py` compares static-only with
static+dynamic+multimodal results and reports:

```text
static_false_positive_rate
  = static_pass AND runtime_fail / static_pass
```

## 11. Hidden Split and Releases

`scripts/create_hidden_split.py` creates deterministic concept-level
`DEV/PUBLIC/HIDDEN` partitions are derived from the current concept count while
preserving the historical proportions. The
public manifest is committed; the hidden manifest must be written to a private
path and is not a secrecy boundary while the full task pool remains in a
development checkout.

`benchmark_releases/v0.7.0.json` records the task-manifest hash, code tag,
runtime/judge/scoring versions, and paired task semantics. Published
leaderboards must identify the release.

## 12. Explicit Non-Goals

This release does not implement a full gameplay DSL, long-horizon play,
GameFix, GameOpt, GameEvolve, online evaluation service, IRT/Rasch difficulty,
or a claim that heuristic difficulty is empirically calibrated.
