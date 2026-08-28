# Racing Terrain Climb

Build a Racing Terrain Climb as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A side-scrolling physics vehicle game where the player drives over rugged
terrain, managing momentum and fuel to reach the farthest distance possible.
The vehicle bounces, tilts, and flips over hills and valleys — too much
throttle on a steep incline flips you backward; too little and you stall on
the slope. Fuel is limited and refilled at checkpoints, creating tension between
speed and conservation. Earned coins buy vehicle upgrades (engine power,
suspension, fuel capacity) and new vehicle types, each with different physics
properties. The fantasy is conquering impossible terrain through smart driving
and incremental improvement.

## What the Player Experiences

1. **Title Screen** — A rugged outdoor scene with the game name in bold blocky
   letters, a vehicle silhouette mid-jump against a sunset sky, and Play/Garage
   buttons. No plain HTML grey.
2. **Stage Select** — Multiple terrain environments (countryside hills, moon
   surface, arctic ice, desert dunes) each with distinct physics properties
   (friction, gravity). Stages unlock by reaching distance milestones.
3. **Driving Physics** — The vehicle has realistic 2D physics: wheels grip
   terrain, the chassis tilts with slope angle, and momentum carries over
   crests. The player controls gas (right) and brake (left), plus tilt
   (up/down) to adjust the vehicle's angle mid-air.
4. **Fuel Management** — A fuel gauge depletes as the player drives. Running
   out stops the vehicle. Fuel canisters appear along the route at intervals.
   The tension between driving fast (burning fuel) and conserving creates
   meaningful decisions.
5. **Coins and Distance** — Coins scatter along the terrain and award currency.
   Distance is tracked as a high score. Each run ends when fuel runs out or
   the vehicle is destroyed (landing on the roof).
6. **Garage/Upgrades** — Between runs, the player spends coins on upgrades:
   engine power, fuel capacity, suspension stiffness, tyre grip. At least 3
   different vehicle types (jeep, motorcycle, monster truck) with visibly
   different sprites and handling characteristics.
7. **Distance Records** — A persistent leaderboard shows best distance per
   stage. Beating a personal record triggers a celebration effect.

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
