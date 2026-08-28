# Momentum Lab

Build **Momentum Lab**, a momentum-based physics platformer with wall-jumps and
gold collection as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A sleek capsule-shaped runner slides, bounces, and wall-jumps through minimalist
laboratory chambers where momentum is everything. The character accelerates
continuously while grounded, preserves speed through wall-jumps, and loses it on
hard landings or collisions. Gold pieces are scattered through each level — some
on the obvious path, others requiring risky momentum-preserving detours. A
countdown timer per level creates urgency: collect the exit key and reach the
door before time expires. Two hundred compact levels across ten themed labs
escalate from gentle slopes to brutal momentum puzzles requiring perfect chains
of wall-jumps, slides, and mid-air redirects. Leaderboards track best times.

## What the Player Experiences

A title screen shows the game name and a level-select grid organized by lab
(10 labs of 20 levels each). Completed levels show gold count and best time.

Entering a level starts the timer. The player moves left/right with
acceleration physics — the character builds speed over time and slides on
slopes. Wall-jumping preserves horizontal momentum and adds vertical boost.
Gold pieces line paths and reward exploration. A key item unlocks the exit door.

Reaching the exit stops the timer and awards a rating based on time and gold
collected. Failing the timer or falling into a void restarts the level
instantly. Each lab introduces a new element: ice surfaces, conveyor belts,
gravity zones, bounce pads, moving walls, laser gates, wind tunnels, rotating
platforms, teleporters, and finally a gauntlet combining everything.

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