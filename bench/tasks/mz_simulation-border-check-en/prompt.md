# Border Check

Build **Border Check**, a 2D document-inspection simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is working as a border checkpoint inspector in a fictional
authoritarian state, examining travelers' documents against an ever-changing
rulebook while trying to earn enough to keep your family alive. The interesting
tension is moral versus mechanical: the rules say deny this person, but their
story is sympathetic — and every wrong decision costs money your family needs for
heat and medicine. Speed matters because each day has a time limit and pay is
per-person processed, but rushing causes mistakes that trigger citations and
fines. The rules grow more complex each day — new document types, new
contraband checks, new exceptions — until the player is juggling five documents
simultaneously while a queue of desperate faces waits.

## What the Player Experiences

The player opens to a bleak title screen showing the checkpoint booth, then
begins Day 1. The workspace shows a desk surface with an inspection area, a
rulebook panel, and stamps for APPROVE and DENY. Travelers approach one at a
time, presenting documents that slide onto the desk. The player drags documents
around, opens the rulebook to check current rules, compares photo to face,
checks expiration dates, and cross-references permit numbers.

Each day introduces new rules: Day 1 might only require matching names, while
Day 5 requires valid work permits, vaccination records, and weight discrepancy
checks. End-of-day shows earnings, family expenses, and any citations received.
Story events interrupt between days — a guard offers bribes, a rebel asks for
help, family members fall ill. Choices affect the narrative path. The game spans
10+ days with escalating complexity and multiple ending conditions based on
accumulated choices and financial survival.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Keep the rules layer independent of DOM and rendering code.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.
