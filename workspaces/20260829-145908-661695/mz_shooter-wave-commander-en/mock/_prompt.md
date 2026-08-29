# Wave Commander

Build **Wave Commander**, a 2D wave defense shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is commanding a lone turret or mobile defender at the center of an
arena, holding the line against increasingly organized enemy waves that attack
from all directions. The interesting tension is resource management between
waves: earned currency must be split between weapon upgrades, defensive barriers,
and consumable power-ups, and the player never has enough for everything. Enemy
formations grow more complex — flanking squads, shielded columns, fast rushers
mixed with slow tanks — demanding that the player adapt loadout and positioning
each round. Boss waves punctuate the escalation with massive enemies that require
sustained focused fire while their escorts continue the assault.

## What the Player Experiences

The player opens to a military-themed title screen, selects a difficulty, and
deploys into the first arena. The player character occupies the center with
360-degree aiming. Wave 1 begins with simple enemies approaching from one
direction. The player aims with mouse and fires with click, moving with WASD to
dodge return fire. Clearing a wave triggers a brief shop phase showing available
upgrades: fire rate, damage, spread, shield repair, deployable mines, or a
screen-clearing airstrike.

Waves escalate in enemy count, variety, and formation complexity. Some waves
attack from multiple directions simultaneously. Every 5 waves a boss wave
arrives featuring a large enemy with distinct attack phases surrounded by
support units. The arena may shift between waves — new cover appears, hazard
zones activate, or the playfield shrinks. After 20 waves or player death, a
results screen shows waves survived, enemies destroyed, and upgrades purchased.

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