# Racing Drift Circuit

Build a Racing Drift Circuit as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A precision time-trial racing game where mastering the drift is everything. The
player pilots a car through tight circuits, initiating controlled drifts around
corners to maintain speed. Each track is a puzzle of racing lines — brake too
early and you lose seconds; drift too wide and you clip the barrier. Ghost
replays of your best run haunt every attempt, pushing you to shave milliseconds.
A medal system (Gold/Silver/Bronze) across 10+ tracks provides clear progression
goals, and the satisfaction of a perfect drift chain through a complex chicane
is the core reward.

## What the Player Experiences

1. **Title Screen** — A dynamic menu with the game name in speed-styled italic
   font, a blurred track in the background with a ghost car drifting past, and
   buttons for Campaign and Time Trial. No plain HTML grey.
2. **Track Select** — A grid of 10+ tracks with preview thumbnails, medal
   status (empty/bronze/silver/gold), and best time displayed. Tracks unlock
   sequentially by earning at least bronze on the previous track.
3. **Driving Feel** — Top-down or angled-top view. The car accelerates smoothly,
   brakes with visible deceleration, and steers with momentum. Holding a drift
   key while turning initiates a drift: the car slides sideways with tyre smoke
   particles trailing behind.
4. **Drift Boost** — Maintaining a drift builds a boost meter. Releasing the
   drift at the right moment grants a speed burst with a visible flame/trail
   effect. Longer drifts yield bigger boosts but risk hitting walls.
5. **Ghost Replay** — A translucent ghost of the player's best lap drives
   alongside them in real time. The ghost is clearly distinguishable (different
   colour, slight transparency) and shows exactly where time is being gained
   or lost.
6. **Medal System** — Each track has Gold/Silver/Bronze time thresholds shown
   before the race. Finishing awards the appropriate medal with a podium
   animation. Medals are tracked on the track select screen.
7. **Track Variety** — Tracks range from simple ovals to complex circuits with
   hairpins, chicanes, elevation changes (visual only), and varying widths.
   Each track has a distinct visual theme (city, desert, forest, night).

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