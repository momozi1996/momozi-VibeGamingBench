# Breach Tactics

Build **Breach Tactics**, a tactics roguelike on a small grid with visible enemy
intents as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A squad of three mechs defends a city grid from waves of alien invaders. The
twist: every enemy telegraphs its next move before the player acts, turning
each turn into a spatial puzzle of displacement, blocking, and sacrifice. The
grid is small (8x8) and buildings occupy tiles that must be protected — if too
many are destroyed, the timeline is lost. Between battles the player earns
reactor cores to upgrade mech abilities or unlock new pilots with passive
traits. A timeline-reset mechanic gives the player a limited number of full
turn undos per battle, allowing recovery from catastrophic mistakes. Four
islands of escalating difficulty each culminate in a boss encounter with unique
grid mechanics.

## What the Player Experiences

A title screen shows mechs dropping onto a grid. An island-select map shows
four islands with branching mission paths.

Each mission places the mech squad on a grid with buildings and spawning
enemies. Before the player moves, every enemy displays its intended action:
attack direction, movement target, or spawn location. The player moves each
mech and uses one ability per mech — push, shoot, shield, repair, or special.
After all mechs act, enemies execute their telegraphed moves simultaneously.

Protecting buildings is the priority — each destroyed building reduces a
structural integrity bar. Losing all integrity fails the mission. Timeline
resets (limited per battle) rewind one full turn. Between missions, upgrade
screens offer new weapons, pilot abilities, and reactor power allocation.
Completing an island unlocks the next. A final victory screen shows missions
completed, buildings saved, and resets used.

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
