# Goo Architect

Build **Goo Architect**, a 2D physics-based structure-building puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player attaches stretchy blob creatures to
each other to build towers, bridges, and other structures that reach a goal
pipe, while gravity and wind threaten to topple their creation.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a construction puzzle driven by soft-body physics. Each level
presents a landscape with a goal pipe placed in a hard-to-reach location. The
player has a limited supply of goo blobs that can be dragged and attached to
existing structure nodes, forming elastic bonds that stretch and sway under
gravity. The tension comes from structural engineering under constraint: too
tall and the tower buckles, too thin and it snaps, too heavy on one side and
it topples. Different goo types add strategic variety — rigid blobs for
foundations, balloon blobs for lift, flammable blobs that burn through
obstacles. The best version feels like building with living putty, where every
placement decision has visible physical consequences.

## What the Player Experiences

A title screen sets the whimsical tone with animated goo creatures and a clear
way to begin. The player enters a level where terrain, hazards, and a goal pipe
are visible. Available goo blobs sit in a supply area. The player drags a blob
from supply and attaches it near existing structure nodes; elastic bonds form
automatically to nearby attachment points.

Early levels teach basic tower-building: stack blobs upward to reach a pipe
above. Soon terrain gaps require bridges, wind gusts demand reinforced
structures, and spike hazards force creative routing. Multiple goo types
appear: standard green goo forms flexible bonds, rigid gray goo creates stiff
joints, balloon pink goo provides upward lift, and flammable red goo can be
ignited to clear obstacles. Each level has a minimum blob quota — saving extra
blobs earns bonus recognition.

The structure sways and settles in real-time as the player builds. When blobs
reach the goal pipe, they are sucked in with a satisfying animation and the
level completes. A results screen shows blobs saved and offers the next
challenge. The campaign progresses through themed worlds with escalating
structural demands.

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