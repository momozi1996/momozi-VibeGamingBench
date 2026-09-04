# Changelog

## v0.7.0 - 2026-09-04

Expanded the benchmark from 491 to 711 concepts (982 to 1,422 bilingual
tasks) and added the Feishu Prompt Catalog source:

- imported 100 complete prompts from the `直接1` sheet and 120 complete prompts
  from the `直接生成` sheet;
- generated paired English and Chinese task variants with immutable source-brief
  provenance;
- kept the `index.html` + `game_logic.js` artifact contract and the v1.1
  Static/Dynamic/Visual/Design score fusion unchanged;
- made bilingual validation, distribution reporting, hidden-split generation,
  release manifests, and smoke checks work from the expanded concept count;
- added a reusable Vibe Gaming quality-bar upgrader for existing task prompts.

The Feishu source snapshot is dated September 4, 2026. The 1,422-task mock
BUILD/runtime compatibility audit and 19 unit tests pass.

## v0.6.0 - 2026-09-01

Breaking task-spec and evaluation update based on pilot generation findings:

- widened runtime-authored visual/audio options while keeping the offline network boundary;
- assigned pointer-first, keyboard-first, or mixed interaction by task family;
- embedded a classic-script `GameLogic` scaffold and optional `render()` hook in every task prompt;
- changed runtime evidence from boot-only to boot, gameplay-start, and gameplay-mid screenshots;
- added multi-sample median aggregation for code and screenshot judges;
- preserved full judge response content in structured `failure_details`;
- added official OpenAI-compatible endpoint configuration for Doubao/Ark, DeepSeek, and other providers;
- removed stale rubric penalties against procedural textures and authored runtime effects.

The release is intentionally breaking for task specifications. Existing v0.5.0
results remain valid under their recorded release and are not mixed into v0.6.0
comparisons.
