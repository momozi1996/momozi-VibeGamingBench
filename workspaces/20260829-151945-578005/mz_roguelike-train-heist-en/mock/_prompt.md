# Train Heist

Build **Train Heist**, a procedural train-car roguelike with car-by-car
encounters as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A bandit boards the caboose of a procedurally generated train and must fight
forward car by car to reach the engine before the train arrives at the station.
Each car is a self-contained encounter: a passenger car with civilians to rob,
a guard car with armed defenders, a cargo car with locked safes to crack, a
dining car with cover-based shootouts, or a mail car with time-locked vaults.
The bandit carries limited ammo and health, spending both as they push forward.
Loot from earlier cars funds purchases at a black-market car that appears
mid-train. A turn counter represents distance to the station — if it hits zero
before reaching the engine, the heist fails. Each run generates a new train
with different car sequences and lengths.

## What the Player Experiences

A title screen shows a steam train silhouette against a sunset. Starting a run
shows the full train in side-view with car types partially visible (some
hidden).

The player enters the caboose and encounters the first car's challenge. Combat
is turn-based with cover mechanics — the bandit and enemies take positions
behind furniture and exchange fire. Ammo is limited and must be looted from
fallen guards. Passenger cars offer robbery choices: intimidate for quick cash
or search thoroughly for better loot but risk alerting guards ahead.

A progress bar shows position along the train and turns remaining. The black-
market car offers health kits, ammo, special weapons, and disguises. Reaching
the engine triggers a boss fight against the conductor. Victory shows total
loot, cars cleared, and turns remaining. Failure (health zero or time out)
shows how far along the train the bandit reached.

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