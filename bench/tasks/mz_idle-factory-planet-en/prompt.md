# Idle Factory Planet

Build an **Idle Factory Planet** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player places machines on a planet surface that automatically produce
resources, chains production lines together, and researches upgrades until the
planet is depleted — then prestiges to a new planet with better technology. The
fantasy is industrial scale: watching conveyor belts carry ore to smelters to
fabricators, output numbers climbing exponentially, and the planet surface
filling with an intricate factory network. The idle loop runs production
continuously; the player optimises layouts and unlocks new machine types.

## What the Player Experiences

1. **Title Screen** — A small planet covered in tiny factories with conveyor
   belts, the game name in industrial stencil font, and a play button shaped
   like a gear.
2. **Planet Surface** — A top-down grid representing the planet surface. The
   player places machines on tiles. Conveyor belts connect machines visually,
   showing resources flowing between them.
3. **Machine Placement** — Machines include: miners (extract raw ore), smelters
   (ore to metal), fabricators (metal to parts), and sellers (parts to credits).
   Each machine auto-produces when supplied. The player drags machines from a
   panel onto the grid.
4. **Production Chains** — Machines must be connected in sequence. Output from
   one feeds input of the next via conveyor. Longer chains produce more valuable
   goods. A production rate display shows throughput.
5. **Research** — Credits fund research that unlocks better machines: faster
   miners, multi-input fabricators, and storage buffers. A tech tree shows
   available upgrades with costs and effects.
6. **Planet Depletion** — The planet has finite resources. A depletion meter
   shows remaining ore. As resources thin, miners slow down. When depleted, the
   player must prestige.
7. **Prestige (New Planet)** — Prestiging moves to a fresh planet with more
   resources. The player keeps research progress and gains a permanent production
   multiplier. Each new planet starts faster and scales higher.

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
