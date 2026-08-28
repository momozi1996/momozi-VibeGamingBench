# FTL Voyage

Build **FTL Voyage**, a spaceship management roguelike with crew and sector
navigation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A small starship flees through procedurally generated sectors toward a final
confrontation, managing crew, fuel, scrap, and ship systems along the way. Each
sector is a node map of encounters — hostile ships, traders, distress signals,
asteroid fields, and empty space. Combat is a real-time-with-pause system where
the player assigns crew to ship systems (weapons, shields, engines, medbay),
targets enemy rooms, and manages power distribution as systems take damage and
fires break out. Between jumps, scrap funds repairs and upgrades. Fuel limits
how many nodes can be visited before the sector exit must be reached. The final
sector pits the ship against a powerful flagship in a multi-phase battle that
tests every system the player has invested in.

## What the Player Experiences

A title screen shows the ship silhouette against a star field. Starting a run
presents a ship layout with rooms, three crew members, and starting resources.

The sector map shows connected nodes with partial information — icons hint at
combat, shops, or events. Jumping to a node costs fuel and triggers an
encounter. Combat shows both ships in cross-section: the player drags crew
between rooms, powers systems on/off, and fires weapons at targeted enemy rooms.
Damage breaches hulls, starts fires, and injures crew. Winning yields scrap.

Shops sell weapons, augments, crew, and fuel. Events present narrative choices
with risk/reward outcomes. Reaching the sector exit advances to the next sector
with harder encounters. After several sectors, the flagship battle begins — a
multi-phase fight with unique mechanics. Victory shows a run summary; defeat
shows how far the player reached.

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
