# Gravity Shift

Build **Gravity Shift**, a 2D gravity-rotation puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player rotates the direction of gravity to guide a
ball through obstacle-filled chambers to an exit, using destructible terrain
and chain reactions to clear paths.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a physics puzzle built on directional gravity. The player cannot
move the ball directly but can rotate gravity in 90-degree increments (down,
left, up, right), causing everything in the chamber to fall in the new
direction. The tension comes from planning gravity sequences: rotating right
sends the ball sliding into a wall, but also drops a boulder onto a
destructible platform, opening a path for the next rotation. Chain reactions
emerge naturally — explosive crates detonate on impact, crumbling blocks
break after one landing, and weighted objects trigger pressure switches as
they settle. The best version feels like orchestrating a Rube Goldberg machine
where gravity itself is the only tool.

## What the Player Experiences

A title screen sets the tone with floating geometry and directional arrows.
The player enters a chamber where the ball, exit portal, walls, platforms,
hazards, and special objects are visible. Gravity direction indicators show
the current pull. The player presses arrow keys or buttons to rotate gravity.

Early chambers teach basic rotation: shift gravity right to roll the ball
toward the exit. Soon obstacles require multi-step sequences — rotate down
to drop through a gap, then left to slide past spikes. Mid-game introduces
destructible terrain (crumbling blocks that break on second impact, explosive
crates that blast nearby walls), weighted objects that trigger switches, and
conveyor surfaces that add lateral movement during falls. Late chambers
demand precise rotation sequences where each gravity shift triggers a chain
reaction that reshapes the level geometry.

An undo system lets the player rewind gravity shifts. Reaching the exit
portal completes the chamber with a celebration screen. Death from hazards
offers instant retry. The campaign progresses through themed worlds with
escalating physics complexity.

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
