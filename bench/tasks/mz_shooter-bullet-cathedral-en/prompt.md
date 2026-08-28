# Bullet Cathedral

Build **Bullet Cathedral**, a bullet-hell roguelike as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is descending through a procedurally arranged cathedral of hostile
rooms, each one a dense bullet-hell encounter where survival depends on
split-second dodge-rolls through curtains of projectiles. The interesting tension
is roguelike impermanence: death sends the player back to the top with nothing,
but each run offers different gun pickups and room layouts, rewarding adaptation
over memorization. The dodge-roll grants brief invincibility frames, creating a
rhythm of rolling through danger and firing back during recovery windows. Gun
variety — from tight railguns to wide shotgun blasts to bouncing orbs — means
each run plays differently depending on what the cathedral offers.

## What the Player Experiences

The player sees a gothic-styled title screen, starts a run, and enters the first
room of the cathedral. The top-down view shows a confined arena with the player
character at center. Enemies spawn and immediately begin firing patterned bullet
spreads. The player moves with WASD, aims with mouse, fires with click, and
dodge-rolls with spacebar. Clearing all enemies in a room opens exits to the
next.

Each floor consists of 5-7 rooms with a boss room at the end. Between rooms the
player may find gun pedestals offering a weapon swap, health pickups, or passive
upgrades. Guns have distinct firing patterns and ammo behavior. Floor bosses fill
the screen with elaborate bullet patterns that require precise rolling and
positioning. After defeating a floor boss, a brief interstitial shows stats
before descending to the next floor. Three floors complete a run with a victory
screen; death at any point shows a run summary with rooms cleared and enemies
defeated.

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
