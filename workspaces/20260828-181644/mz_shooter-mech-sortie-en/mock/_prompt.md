# Mech Sortie

Build **Mech Sortie**, a top-down mech shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a heavily armed walking mech through hostile territory,
customizing its weapon hardpoints between missions to match the threats ahead.
The interesting tension is loadout planning: the mech has limited hardpoint slots
(arms, shoulders, back) and each weapon has weight, ammo, and range tradeoffs.
A missile rack dominates at range but leaves the mech vulnerable up close; dual
autocannons shred nearby targets but overheat. Missions yield salvage from
destroyed enemies that funds new weapons and chassis upgrades, creating a
satisfying loop of deploy, destroy, salvage, customize, redeploy.

## What the Player Experiences

The player opens to a hangar screen showing their mech with labeled hardpoints.
Available weapons are listed in an armory panel; dragging a weapon onto a
hardpoint equips it, with weight and energy constraints shown. Selecting a
mission from the campaign map deploys the mech into a top-down battlefield.

The mech moves with WASD (slower than infantry, with momentum), rotates the
torso independently with mouse aim, and fires equipped weapons with mouse
buttons and number keys. Missions have objectives: destroy all enemies, defend a
point, escort a convoy, or eliminate a target. Enemy variety includes infantry,
light vehicles, rival mechs, and turret emplacements. Destroying enemies drops
salvage crates collected on contact. Mission completion shows a debrief with
salvage earned, damage taken, and accuracy stats. The campaign spans 8+ missions
with escalating difficulty and a final boss mech encounter.

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