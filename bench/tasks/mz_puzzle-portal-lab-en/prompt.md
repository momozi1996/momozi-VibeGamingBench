# Portal Lab

Build **Portal Lab**, a 2D portal-placement puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places entry and exit portals on designated
wall surfaces to redirect lasers, launch objects, and transport themselves
through test chambers, using momentum conservation and spatial reasoning.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a spatial puzzle built on linked teleportation. Each test chamber
has walls, floors, laser emitters, targets, weighted cubes, buttons, and a
locked exit. The player can place two portal endpoints on valid surfaces;
anything entering one emerges from the other with conserved momentum and
direction. The tension comes from chaining portals with physics: drop a cube
from height through a floor portal to launch it horizontally from a wall
portal onto a distant button, or redirect a laser through multiple portal
bounces to hit a sensor. The best version feels like bending space itself,
where each chamber is an "aha" moment of seeing how two linked holes solve
an impossible geometry.

## What the Player Experiences

A title screen sets the laboratory tone with portal imagery and a clean
scientific aesthetic. The player enters a test chamber where walls, laser
emitters, targets, cubes, buttons, and the exit door are visible. Valid portal
surfaces are subtly highlighted.

Early chambers teach basic portal use: place two portals to walk through a
wall, or redirect a single laser to a target. Soon chambers require momentum
tricks — falling through a floor portal to gain speed and launching from a
wall portal to cross a gap. Mid-game introduces weighted cubes that must be
portaled onto pressure plates, laser grids requiring multiple redirections,
and timed sequences where portals must be repositioned mid-puzzle. Late
chambers combine all mechanics: redirect lasers, launch cubes, and navigate
the player through a single interconnected portal network.

Placing a portal shows a preview of where it will link. Objects passing through
portals have visible trajectory trails. When all targets are activated, the
exit unlocks. A completion screen shows the chamber number and offers the next
challenge. The campaign progresses through increasingly complex test chambers.

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
