# Pirate Fleet

Build **Pirate Fleet**, a **naval tactics strategy game with wind mechanics** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A fleet of pirate ships navigates a hex-sea where wind direction dictates
everything. Sailing with the wind is fast; tacking against it is slow and
costly. The player commands multiple ship types — nimble sloops, heavy
galleons, boarding frigates — positioning them to exploit wind advantage while
denying it to the enemy. Combat is broadside-based: ships deal damage from
their flanks, so facing matters as much as range. Treasure islands dot the map
as objectives worth fighting over. The tone is golden-age piracy: sun-bleached
sails, cannon smoke, and the creak of timber under fire.

## What the Player Experiences

From the title screen the player selects a scenario or campaign mission. The
map shows a hex-grid sea with islands, shallows, and a wind-direction indicator
that shifts every few turns. The player's fleet starts on one side; the enemy
on the other. Treasure islands sit between them as objectives.

Each turn the player moves ships. Movement cost depends on direction relative
to wind: downwind is cheap, crosswind moderate, upwind expensive. Ships have
limited movement points per turn. After moving, ships with enemies in their
broadside arc can fire cannons — damage depends on range and facing angle.

Ship types serve different roles: sloops scout and flank quickly, galleons
absorb damage and carry heavy guns, and frigates can initiate boarding actions
on adjacent ships for a chance to capture rather than sink. Captured ships join
the player's fleet.

Treasure islands are captured by moving a ship adjacent and holding for one
turn. Controlling islands earns victory points. The scenario ends when one side
reaches the point target or loses all ships. A styled result screen shows the
battle outcome with ships sunk, captured, and treasure claimed.

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