# Pipe Crisis

Build **Pipe Crisis**, a 2D pipe-routing puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places and rotates pipe segments on a grid to
route colored fluids from sources to matching drains before pressure builds
and the system overflows.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a time-pressure spatial puzzle built on fluid routing. Each level
has one or more fluid sources that begin pumping after a countdown. The player
must lay pipe segments from a queue onto a grid, rotating and placing them to
create continuous paths from each source to its matching drain. The tension
comes from the countdown timer and multiple fluid types: red chemicals cannot
mix with blue coolant, green acid dissolves standard pipes, and crossing paths
require special junction pieces. The best version feels like a frantic plumbing
emergency where every second of planning pays off when the fluids start flowing
and the paths light up with color.

## What the Player Experiences

A title screen sets the industrial tone with pipe imagery and pressure gauges.
The player enters a grid-based facility where sources, drains, obstacles, and
empty cells are visible. A pipe queue shows upcoming pieces. The countdown
timer ticks toward flow start.

Early levels teach basic routing: connect one source to one drain with simple
straight and corner pipes. Soon multiple sources demand parallel paths, color
matching prevents cross-contamination, and obstacles force creative detours.
Mid-game introduces special pipe types: cross junctions that allow two fluids
to pass without mixing, reservoir tanks that buy extra time, and acid-resistant
pipes for corrosive fluids. Late levels combine all mechanics with tight
timers and complex multi-source layouts.

When flow begins, fluid visibly travels through the pipes. Successful routing
fills the drain and completes the level. Overflow from dead ends or mixing
violations triggers a failure state. A results screen shows completion time
and efficiency rating. The campaign progresses through themed facilities with
escalating routing demands.

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