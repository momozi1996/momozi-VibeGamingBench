# Space Colony

Build **Space Colony**, an **asteroid colony management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A small crew lands on a barren asteroid and must build a self-sustaining colony
from nothing. Oxygen, food, and power are the three lifelines — lose any one
and colonists die. The player builds modules on a grid surface: habitats for
living, farms for food, solar arrays for power, and oxygen generators to keep
everyone breathing. Each colonist has needs and a job assignment; idle colonists
consume without producing. The tension is that expansion requires resources
that are already stretched thin, and random meteor strikes can destroy modules
without warning. The fantasy is frontier survival in the void — every new
module is a small victory against the emptiness of space.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
top-down asteroid surface with a grid overlay. The initial lander provides
minimal oxygen, food, and power for a small crew.

The player builds modules by spending materials mined from the asteroid.
Habitats house colonists, farms grow food, solar panels generate power, and
oxygen recyclers keep the air breathable. Each module connects to adjacent
ones, and the colony must maintain positive balance in all three resources or
colonists begin dying.

Colonists are assigned to jobs: miners extract materials, farmers tend crops,
engineers maintain modules, and researchers unlock new building types. Each
colonist has morale affected by living conditions, workload, and whether their
habitat has amenities.

Meteor events strike randomly, damaging or destroying modules. The player must
maintain redundancy and repair capacity. Research unlocks advanced modules:
greenhouses, fusion reactors, shield generators, and deep-mining rigs.

The game tracks population, days survived, and colony rating. A styled result
screen shows colony achievements when the colony is lost or reaches a
population milestone.

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