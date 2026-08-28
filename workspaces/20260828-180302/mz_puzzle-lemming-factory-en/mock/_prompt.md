# Lemming Factory

Build **Lemming Factory**, a 2D creature-guiding puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player assigns jobs to a stream of marching factory
workers — diggers, builders, blockers, climbers — to guide them safely from
an entrance hatch to an exit door, saving a required quota each level.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a real-time puzzle about indirect control. Creatures march
autonomously in a straight line, turning at walls, falling off ledges, and
walking into hazards unless the player intervenes. The player cannot move
creatures directly but can click on individual workers to assign them a job
from a limited toolbar. Each job transforms the creature's behavior: diggers
carve downward through terrain, builders construct diagonal staircases, blockers
become impassable walls that redirect traffic, and climbers scale vertical
surfaces. The tension comes from limited job supplies, time pressure as
creatures march toward danger, and the spatial reasoning needed to route a
crowd through complex terrain. The best version feels like conducting an
orchestra of tiny workers where every assignment ripples through the crowd's
path.

## What the Player Experiences

A title screen sets the factory tone with marching creature silhouettes and a
clear way to begin. The player enters a level where terrain, hazards (pits,
saws, lava), an entrance hatch, and an exit door are visible. A toolbar shows
available jobs with remaining counts. The hatch opens and creatures begin
marching out at a steady rate.

Early levels teach one job at a time: assign a digger to carve through a floor,
or a builder to bridge a gap. Soon levels require combining jobs — a blocker
redirects traffic while a digger opens an alternate path. Mid-game introduces
climbers for vertical navigation, floaters for safe falls, and bombers for
emergency terrain removal. Each level specifies a save quota; losing too many
creatures to hazards means failure.

The player can adjust release rate and pause to plan. When enough creatures
reach the exit, a results screen shows the save percentage and offers the next
challenge. The campaign has levels grouped into difficulty tiers, each
introducing new terrain types and job combinations.

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