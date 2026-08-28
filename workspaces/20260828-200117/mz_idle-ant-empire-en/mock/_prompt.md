# Idle Ant Empire

Build an **Idle Ant Empire** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds an ant colony from a single queen, assigning workers to tasks,
unlocking new ant types, and growing exponentially through prestige resets. The
fantasy is watching a tiny empire scale to absurd proportions: from gathering
crumbs to harvesting entire gardens, from a handful of workers to millions. The
idle loop runs continuously — ants gather resources even when the player is not
clicking. Tension comes from resource allocation decisions and seasonal challenges
that threaten the colony.

## What the Player Experiences

1. **Title Screen** — A cross-section of underground tunnels with ants marching,
   the game name in earthy brown font, and a play button styled as a leaf.
2. **Colony View** — A side-view ant colony with visible chambers: nursery, food
   storage, queen's chamber, and tunnels connecting them. Ants visibly move
   between chambers carrying resources.
3. **Worker Assignment** — The player assigns ants to roles: gatherers (collect
   food), builders (dig new chambers), soldiers (defend), and nurses (hatch eggs).
   Sliders or buttons control allocation. Production rates update in real-time.
4. **Resource Generation** — Food accumulates automatically based on gatherer
   count. The player can click to manually boost gathering. Resources fund new
   chambers, ant hatching, and upgrades.
5. **Ant Types** — Unlockable ant types with special abilities: leaf-cutters
   (bonus food), fire ants (defence), flying ants (exploration), and mega-ants
   (10x production). Each type has a distinct sprite.
6. **Prestige System** — When the colony reaches a threshold size, the player can
   prestige: reset the colony but gain permanent multipliers (queen fertility,
   gathering speed, defence strength). Each prestige makes the next run faster.
7. **Seasonal Challenges** — Periodic events threaten the colony: rain floods
   tunnels (need builders), predators attack (need soldiers), winter reduces food
   (need stockpiles). Surviving challenges grants bonus resources.

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