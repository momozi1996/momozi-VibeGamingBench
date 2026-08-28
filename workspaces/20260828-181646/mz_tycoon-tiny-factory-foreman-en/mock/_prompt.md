# Tiny Factory Foreman

Build **Tiny Factory Foreman**, a compact 2D automation and production-planning
game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is running a miniature factory floor where raw materials flow in one
end and finished goods roll out the other — if the player has wired everything
together correctly. The interesting tension is spatial: belts only carry forward,
sorters only split, and machines only accept certain inputs, so every tile
placement is a routing puzzle under time pressure. Orders arrive on a board with
ticking deadlines, and the player must decide whether to retool the line for a
new product or squeeze more throughput from the current layout. The risk is
always a cascade failure — one misrouted material jams a machine, the backup
stalls the belt, and suddenly three orders expire at once. Growth comes from
earning enough to unlock faster belts, smarter sorters, or multi-output machines,
but each upgrade reshapes the routing problem rather than simply solving it.

## What the Player Experiences

The player opens to a compact workshop view: a few raw-material sources on one
side, empty order bins on the other, and a grid of open floor between them. An
order board shows what products are needed and how long remains. The first
minutes are about laying a simple belt path from source to machine to bin and
watching the first coloured crate trundle across the floor.

As orders grow more complex the player drops sorters to split material streams,
places different machine types that transform inputs into intermediate or final
goods, and reroutes belts to avoid collisions. The floor fills with motion —
little icons sliding along conveyors, machines pulsing as they process, sorters
flicking left or right. A well-designed line hums; a badly planned one backs up
and flashes warnings.

Between rounds or when cash allows, the player visits an upgrade screen to
improve belt speed, unlock a new machine recipe, or expand storage capacity.
These choices shape what orders can be accepted next. Eventually the shift ends
and a result screen tallies fulfilled orders, missed deadlines, and coins earned,
offering a retry or a return to the title.

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