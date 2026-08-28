# Air Control

Build **Air Control**, a 2D air traffic control simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is directing aircraft safely to their runways from a radar-style
control screen, drawing flight paths through increasingly crowded airspace while
avoiding collisions and managing weather disruptions. The interesting tension is
spatial planning under time pressure: planes enter from screen edges at different
speeds and altitudes, each needing to reach a specific runway. The player draws
paths that planes follow, but new arrivals constantly force replanning. Near-miss
warnings create panic moments where quick rerouting prevents disaster. Weather
events close runways or create no-fly zones, demanding real-time adaptation of
carefully laid plans.

## What the Player Experiences

The player opens to a control-tower themed title screen, selects an airport from
a campaign list, and enters the radar view. The screen shows a stylized top-down
airport with runways, taxiways, and surrounding airspace. Planes appear at edges
with callsigns, types, and destination runway indicators. The player draws a
flight path from each plane to its assigned runway by clicking and dragging
waypoints.

Planes follow their paths at their own speed. Proximity warnings flash when two
planes get too close. Successful landings earn points; collisions or planes
leaving the screen without landing lose lives. Between levels the player can
upgrade: add runways, install weather radar, unlock speed-control commands, or
expand the airspace boundary. Weather events — fog reducing visibility, storms
creating no-fly zones, crosswinds affecting runway availability — increase
pressure. The campaign spans 12+ levels across 3 airports with escalating
traffic density and complexity. A level summary shows planes landed, near-misses,
and efficiency rating.

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
