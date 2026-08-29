# Garden Crawl

Build **Garden Crawl**, a garden-dungeon roguelike with plants as allies and
seed deckbuilding as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A gardener descends through a dungeon that is also a garden — soil tiles can be
planted with seeds that grow into allies, barriers, or resource producers over
several turns. The player carries a seed deck and plays seeds onto the grid
before and during encounters. A sunflower provides energy each turn, a thorn
bush damages adjacent enemies, a vine wall blocks paths, and a healing bloom
restores the gardener. Seasons rotate every few floors, changing which seeds
thrive: spring boosts growth speed, summer strengthens attack plants, autumn
yields bonus harvests, and winter slows everything. Between floors the player
drafts new seeds, composts unwanted ones, and tends a persistent greenhouse
that provides starting bonuses for future runs.

## What the Player Experiences

A title screen shows a garden growing over dungeon stones. Starting a run gives
the player a starter seed deck of 8 basic seeds.

Each floor is a grid-based encounter. The gardener stands on one side, enemies
approach from the other. Before enemies reach the gardener, the player plants
seeds on soil tiles. Seeds grow over turns: sprout -> mature -> active. Mature
plants provide their effect (damage, healing, blocking, energy generation).
The player manages an energy resource to plant seeds and activate abilities.

Between floors, a draft screen offers three new seed choices. A compost option
removes a seed from the deck. Every 3 floors the season changes, visually
transforming the environment and modifying plant stats. A greenhouse meta-layer
persists between runs — seeds planted there provide small starting bonuses.
The run ends at a boss floor or when the gardener's health reaches zero. A
results screen shows floors cleared, plants grown, and seeds collected.

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