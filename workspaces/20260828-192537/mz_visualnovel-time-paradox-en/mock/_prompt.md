# Time Paradox

Build **Time Paradox**, a **time-travel paradox visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player travels between past and present, making dialogue choices in the
past that ripple forward and change the present. But causality is fragile:
contradictory changes create paradoxes that must be resolved before reality
collapses. The player manages multiple timelines simultaneously, tracking which
changes are compatible and which create conflicts. The tension is combinatorial:
every past choice fixes one problem in the present but may create two new ones.
The tone is sci-fi mystery: temporal distortion effects, split-screen timeline
views, and the vertigo of watching reality rewrite itself.

## What the Player Experiences

From the title screen the player enters the present-day scene — something is
wrong (a friend is missing, a building is destroyed, a message makes no sense).
A time device allows jumping to the past version of the same location.

In the past, the player makes dialogue choices that change events. Returning
to the present shows the consequences: different characters present, different
objects in the scene, different dialogue available. A timeline indicator shows
the current state of reality and any active paradoxes.

Paradoxes occur when two past changes contradict each other (saving person A
requires an object that saving person B already consumed). The paradox meter
fills — if it maxes out, the timeline collapses and the game ends. The player
must find resolutions: alternative paths that satisfy both requirements without
contradiction.

Multiple timeline branches are tracked visually on a timeline map. The player
can jump between past moments to adjust choices. The true ending requires
resolving all paradoxes and reaching a stable timeline where all present-day
problems are fixed.

A styled result screen shows the timeline state, paradoxes resolved, and which
ending was reached.

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