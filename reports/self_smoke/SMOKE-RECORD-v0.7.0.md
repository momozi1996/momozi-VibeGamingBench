# VibeGamingBench v0.7.0 · Five-Case Self Smoke Record

## Purpose

This record validates that five assigned prompts can be turned into real
`index.html` + `game_logic.js` artifacts, loaded by Chromium, exercised by
pointer/keyboard probes, and scored through the benchmark's standard
Static/Dynamic/Visual/Design score-fusion path.

This is a **diagnostic smoke run**, not an official model leaderboard result.
The generator is `scripts/self_smoke_harness.py` and the scorer is a
transparent deterministic placeholder. Every result is marked
`leaderboard_eligible: false`.

## Selected Cases

| Case | Task | Source gameplay family | Purpose |
|---:|---|---|---|
| 1 | `mz_feishu-structured-001-en` | Traditional pixel turn-based RPG | Pixel/grid presentation |
| 2 | `mz_feishu-structured-002-en` | Top-down action ARPG | Arena/action presentation |
| 3 | `mz_feishu-structured-003-en` | SFC-style JRPG | Dialogue/narrative presentation |
| 4 | `mz_feishu-structured-004-en` | Western CRPG | Tactical grid presentation |
| 5 | `mz_feishu-structured-005-en` | Single-player simulated MMORPG | Open-map presentation |

The five source briefs are different. The self-smoke harness intentionally
implements a small playable diagnostic slice for each visual family; it does
not claim to implement the complete source game. The final screenshots use
different scene layouts and rendering treatments so smoke evidence is not
mistaken for five identical generated games.

## Results

| Task | BUILD | Contract | Chromium | Screenshots | Self score |
|---|---:|---:|---|---:|---:|
| `mz_feishu-structured-001-en` | PASS | 1.00 | pass | 3 | 78.7 |
| `mz_feishu-structured-002-en` | PASS | 1.00 | pass | 3 | 78.7 |
| `mz_feishu-structured-003-en` | PASS | 1.00 | pass | 3 | 78.7 |
| `mz_feishu-structured-004-en` | PASS | 1.00 | pass | 3 | 78.7 |
| `mz_feishu-structured-005-en` | PASS | 1.00 | pass | 3 | 78.7 |

## Evidence

The reproducible final run is stored under:

```text
reports/self_smoke/v0.7.0-final4/
```

Each Case directory contains:

```text
product/index.html
product/game_logic.js
evidence/boot.png
evidence/gameplay_start.png
evidence/gameplay_mid.png
result.json
```

The aggregate result is:

```text
reports/self_smoke/v0.7.0-final4/summary.json
```

## Scoring

The smoke runner calls the same production score functions:

```text
Static  40%
Dynamic 25%
Visual  20%
Design  15%
```

The temporary self judge is deliberately conservative. It scores artifact and
runtime signals, not full source-game fidelity. Its result must not be merged
into `leaderboard.json` or used as a published quality claim.

## Re-run

```bash
python3 scripts/run_self_smoke.py \
  --out reports/self_smoke/v0.7.0-new-run
```

The script refuses to clear an existing output directory unless
`--overwrite` is explicitly provided.
