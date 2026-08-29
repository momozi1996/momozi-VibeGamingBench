# Kitchen Rush

Build **Kitchen Rush**, a 2D time-pressure cooking simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a restaurant kitchen during a dinner rush, juggling
multiple orders across different cooking stations while timers tick down and
customers grow impatient. The interesting tension is multitasking under pressure:
each recipe requires specific steps at specific stations in a specific order, and
the player must mentally track multiple dishes simultaneously. Burning food wastes
ingredients and time; serving wrong orders loses reputation. Between shifts the
player unlocks new recipes, upgrades stations, and expands the kitchen layout,
but more capacity means more complex orders and higher customer expectations.

## What the Player Experiences

The player opens to a restaurant storefront title screen, then enters the first
shift. The kitchen view shows stations arranged spatially: chopping board, stove,
fryer, oven, plating area, and serving window. Orders appear at the top with
recipe requirements and countdown timers. The player clicks a station to interact,
drags ingredients from the pantry to stations, and monitors cooking progress.

Recipes start simple — chop lettuce, plate it, serve — but quickly layer:
burger requires chopping, grilling, assembling bun with toppings, then plating.
Multiple orders run simultaneously. Overcooking triggers smoke and waste.
Completing orders earns coins and tips based on speed. Between shifts a shop
screen offers station upgrades (faster stove, larger fryer), new recipe unlocks,
and kitchen expansions. The campaign progresses through 10+ shifts with
increasing order complexity, customer volume, and recipe variety. A shift
summary shows orders completed, failed, tips earned, and star rating.

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