# Magnet Dash

Build **Magnet Dash**, a platformer with magnetic attract/repel mechanics and
momentum traversal as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A magnetized robot navigates industrial chambers by attracting toward or
repelling away from metal surfaces scattered throughout each level. Holding
attract pulls the robot toward the nearest metal anchor, building speed as it
approaches. Releasing at the right moment converts that pull into ballistic
momentum. Repel pushes the robot away explosively, launching it across gaps or
up shafts. The interplay between attract and repel creates a swinging,
slingshotting movement vocabulary that feels like controlled chaos. Thirty
levels across three zones introduce increasingly complex magnetic puzzles,
and three boss encounters require using magnetic mechanics offensively —
deflecting projectiles or pulling shields away from enemies.

## What the Player Experiences

A title screen shows the robot suspended between two magnets. A zone-select
menu shows three zones of ten levels each, plus a boss at each zone's end.

In gameplay, metal surfaces glow with a distinct color. Holding the attract
button pulls the robot toward the nearest metal surface — the closer it gets,
the faster it accelerates. Releasing converts momentum into free flight.
Pressing repel near a metal surface launches the robot away at high speed.
Levels require chaining these moves to cross gaps, ascend shafts, and avoid
hazards like electric fields and crushers.

Boss fights take place in arenas with metal anchors. Bosses fire projectiles
that can be magnetically deflected, or have metal armor plates that can be
ripped away with attract. Defeating a boss unlocks the next zone. A completion
screen shows time, collectibles gathered, and a style rating based on momentum
chains.

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