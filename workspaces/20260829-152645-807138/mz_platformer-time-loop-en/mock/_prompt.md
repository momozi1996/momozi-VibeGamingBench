# Time Loop

Build **Time Loop**, a 30-second time loop platformer where past-self replays
help solve puzzles as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

Each level is a 30-second loop. When the timer expires, time rewinds and the
player starts again — but a ghost of the previous loop replays simultaneously,
interacting with the world. The ghost can hold switches, distract enemies, or
stand on pressure plates while the current player tackles other objectives.
Multiple loops layer: loop 1's ghost holds a door open, loop 2's ghost stands
on a platform to create a bridge, and in loop 3 the player finally reaches the
exit using both ghosts' contributions. The puzzle is temporal coordination —
planning what each loop-self needs to do and when, so that all versions
cooperate across time. Twenty-four levels across four chapters escalate from
single-ghost puzzles to four-loop orchestrations.

## What the Player Experiences

A title screen shows overlapping clock hands and ghost silhouettes. A chapter
menu reveals four chapters of six levels each.

Entering a level starts a 30-second countdown. The player runs, jumps, and
interacts with switches and objects. When the timer hits zero, the screen
flashes and rewinds — the player restarts at the spawn point, but a translucent
ghost replays exactly what they did in the previous loop. The ghost physically
interacts with the world: it presses buttons, holds doors, and blocks lasers.

The player can layer up to four loops. A timeline bar at the top shows all
active ghosts and their current positions in the 30-second window. Reaching the
exit crystal with all required switches held (by ghosts or player) completes
the level. A reset button clears all ghosts to start fresh. Level-complete
shows loops used and time of exit within the final loop.

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