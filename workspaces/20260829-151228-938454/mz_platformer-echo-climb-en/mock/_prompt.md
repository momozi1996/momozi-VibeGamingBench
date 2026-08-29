# Echo Climb

Build **Echo Climb**, a tower-climbing platformer where past runs become ghost
platforms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A climber ascends an impossibly tall tower, but the tower is mostly empty air.
The trick: every failed attempt leaves behind a ghost that replays the run, and
the ghost's body becomes a solid platform for future attempts. The first run
might reach only a few ledges before falling. The second run can stand on the
ghost of the first to reach higher. Each attempt layers another ghost into the
tower, gradually building a scaffold of past selves that makes previously
impossible heights reachable. The player decides when to sacrifice a run to
create a useful stepping stone versus when to push for maximum height. A
persistent best-height marker and ghost count track progress across sessions.

## What the Player Experiences

A title screen shows the tower stretching upward with ghost silhouettes
visible. Starting a run places the player at the tower base.

The climber can run, jump, and wall-slide. The tower has sparse fixed platforms
but large vertical gaps that seem impassable. When the player falls or quits,
the run is recorded as a ghost. On the next attempt, all previous ghosts replay
simultaneously — their bodies are semi-transparent but physically solid. The
player can stand on ghosts, use them as moving platforms, or ride them upward.

A height meter shows current altitude and best-ever altitude. Every five
attempts the player can choose to "solidify" one ghost into a permanent
platform (it stops replaying and becomes a fixed ledge). The game saves ghost
data between sessions. Reaching milestone heights unlocks cosmetic trail
effects for the climber.

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