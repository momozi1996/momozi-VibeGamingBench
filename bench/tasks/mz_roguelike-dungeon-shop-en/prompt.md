# Dungeon Shop

Build **Dungeon Shop**, a shopkeeper roguelike where you price items and defend
from thieves as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player runs a dungeon item shop, stocking shelves with weapons, potions,
and armor that adventurers browse and buy. The twist: the player sets prices,
and pricing is the core mechanic. Price too high and adventurers leave empty-
handed. Price too low and profit evaporates. Some customers are thieves who
grab items and bolt for the door — the player must physically chase and tackle
them or deploy traps. Between shopping days, the player ventures into a
procedural dungeon to acquire new stock, fighting monsters with whatever unsold
inventory is on hand. Gold funds shop upgrades: display cases, security
measures, and larger floor space. Each run spans multiple days until the shop
either thrives to a target gold amount or goes bankrupt.

## What the Player Experiences

A title screen shows a cozy shop interior with a sword on display. Starting a
run opens the shop on Day 1 with basic starter inventory.

During the shop phase, adventurers enter and browse. The player drags items
onto shelves and sets prices via a slider. Adventurers have visible budget
indicators and preferences. Satisfied customers pay and leave; overcharged
customers scoff and exit. Thieves grab items and run — the player clicks to
chase or activates pre-placed traps.

During the dungeon phase, the player enters a procedural side-scrolling dungeon
with simple combat, collecting loot to stock the shop. Better dungeon
performance means better inventory. Between days, an upgrade screen offers shop
improvements. The run ends in victory (reaching a gold target) or bankruptcy
(running out of stock and gold). A results screen shows days survived, total
profit, and thieves caught.

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
