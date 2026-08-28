# Detective Noir

Build **Detective Noir**, a **detective deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A private investigator works cases in a rain-soaked city, examining crime
scenes, interviewing suspects, and piecing together who did what, when, and
why on a deduction board. Each case is a self-contained mystery with physical
evidence, witness statements, and a web of connections that the player must
untangle. The tension is cognitive: all the clues are available, but connecting
them correctly requires careful reading and logical elimination. Wrong
accusations waste credibility and lock out information. The tone is classic
noir: shadows, trench coats, jazz undertones, and morally grey characters who
all have something to hide.

## What the Player Experiences

From the title screen the player selects a case from a case board. Each case
opens with a crime scene — a location rendered in noir style with interactive
hotspots. Clicking hotspots reveals evidence: a bloodstain, a torn letter, a
misplaced object. Each piece of evidence is added to the player's notebook
with its details.

The player then visits locations to interview suspects and witnesses. Each
character has dialogue that reveals information — some truthful, some
misleading. The player can press on statements to probe deeper, sometimes
unlocking new evidence or contradictions.

The deduction board is the core puzzle interface: the player connects evidence
to suspects, timelines, and motives by dragging links between cards. When
enough connections are made, the player can make an accusation — selecting
who, what weapon, and when. A correct accusation solves the case with a
dramatic reveal sequence. An incorrect one costs credibility points; too many
wrong guesses and the case goes cold.

Multiple cases are available with different difficulty levels. A styled result
screen shows the case outcome, evidence found, and deduction accuracy.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Same pattern as `bench/references/tg1/game_logic.js`.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.