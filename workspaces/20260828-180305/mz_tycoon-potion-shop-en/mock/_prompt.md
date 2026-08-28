# Potion Shop

Build **Potion Shop**, an **alchemy shop management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player runs a fantasy apothecary, brewing potions from gathered ingredients
and selling them to customers with specific ailments. The core loop is
recipe-driven: combine ingredients at a cauldron following discovered recipes,
stock shelves with the results, and set prices that balance profit against
customer satisfaction. Customers arrive with visible symptoms — a coughing
knight, a cursed merchant, a poisoned child — and buy the potion that matches
their need. The tension is inventory management: rare ingredients run out,
popular potions sell faster than they can be brewed, and a shop with empty
shelves loses reputation. The tone is cozy-magical: bubbling cauldrons, glowing
vials, and a cluttered shop full of character.

## What the Player Experiences

From the title screen the player opens their shop for the day. The shop view
shows shelves, a cauldron, an ingredient cabinet, and a counter where customers
queue. The day cycle drives the rhythm: morning for brewing, afternoon for
selling, evening for restocking.

Brewing happens at the cauldron: the player selects ingredients from their
cabinet and combines them. Known recipes show the required ingredients; new
recipes can be discovered by experimentation. Each potion has a type (healing,
curing, buffing) and quality level based on ingredient freshness and correct
procedure.

Customers enter with visible ailments shown as icons. They browse shelves and
buy matching potions at the set price. Happy customers return and spread word;
unhappy ones (wrong potion, too expensive, out of stock) leave bad reviews
that reduce foot traffic.

Gold earned buys ingredient restocks from a supplier menu, shop upgrades
(larger shelves, faster cauldron, ingredient garden), and recipe books that
unlock advanced potions. The game tracks gold, reputation, and days operated.
A styled result screen shows shop statistics at the end of each week.

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