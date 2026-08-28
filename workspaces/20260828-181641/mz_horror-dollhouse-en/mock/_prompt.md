# Horror Dollhouse

Build a **Horror Dollhouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a dollhouse that mirrors a real house, manipulating miniature
objects to affect the full-size world and escape. The fantasy is uncanny scale:
moving a tiny chair in the dollhouse causes a crash upstairs, opening a miniature
door reveals a hidden passage in the real house. Tension comes from the dollhouse
responding to the player — figures move on their own, rooms rearrange when not
watched, and the boundary between miniature and real blurs. The player must solve
puzzles across both scales to find the way out.

## What the Player Experiences

1. **Title Screen** — A split-view showing a dollhouse and its real counterpart,
   the game name in childlike handwriting that drips, and a play button.
2. **The Real House** — The player moves through a dark, full-size house in
   side-view. Doors are locked, passages blocked, and something is wrong — rooms
   do not connect logically.
3. **The Dollhouse** — Found in the attic, the dollhouse is a miniature replica
   of the real house. The player can zoom into it and interact with tiny objects:
   move furniture, open doors, flip switches.
4. **Mirror Mechanics** — Actions in the dollhouse affect the real house.
   Moving a miniature bookcase reveals a passage in the real house. Turning on a
   tiny lamp illuminates a dark real room. Locking a dollhouse door traps
   something in the real house.
5. **Puzzle Progression** — Each room has a puzzle requiring manipulation across
   both scales. The player alternates between exploring the real house and
   adjusting the dollhouse to progress.
6. **The Dollhouse Responds** — As the player progresses, the dollhouse changes
   on its own: figures appear in rooms the player just left, furniture moves
   back, and new rooms appear that do not exist in the real house. Investigating
   these anomalies reveals the horror.
7. **Escape** — The final puzzle requires the player to manipulate both scales
   simultaneously to open the front door. The ending depends on whether the
   player investigated the anomalous rooms or ignored them.

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