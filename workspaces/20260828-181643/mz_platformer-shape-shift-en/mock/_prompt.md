# Shape Shift

Build **Shape Shift**, a puzzle-platformer with three transformable forms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A polymorphic creature navigates chambers by switching between three physical
forms mid-air: a heavy cube that falls fast and activates pressure plates, a
bouncy sphere that ricochets off walls and reaches high places, and a gliding
triangle that floats across wide gaps. Each form has distinct physics — the cube
is dense and grippy, the sphere is elastic and slippery, the triangle is light
and drifty. Puzzles require chaining transformations in sequence: launch as
sphere, shift to triangle mid-arc to glide over spikes, then drop as cube onto
a switch. Forty levels across four worlds teach each form individually before
demanding fluid mid-air combos.

## What the Player Experiences

A title screen shows the three forms orbiting the game name. A world-select
menu reveals four worlds of ten levels each, unlocked sequentially.

World 1 teaches the cube: weight, pressure plates, breaking fragile floors.
World 2 introduces the sphere: bouncing, wall-ricochets, momentum preservation.
World 3 adds the triangle: gliding, updrafts, precision floating. World 4
combines all three with puzzles requiring rapid mid-air switching.

The player presses 1/2/3 or cycles with a button to transform instantly. Each
form change produces a satisfying visual morph and a physics shift the player
feels immediately. Levels contain a goal crystal — reaching it completes the
level. Optional collectible stars reward creative form usage. A level-complete
screen shows time, stars collected, and form-switch count.

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