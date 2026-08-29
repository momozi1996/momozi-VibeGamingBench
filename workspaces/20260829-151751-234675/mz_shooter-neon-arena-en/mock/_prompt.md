# Neon Arena

Build **Neon Arena**, a twin-stick arena shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being the last pilot standing in a sealed geometric arena as
waves of hostile shapes pour in from every edge. The interesting tension is the
score multiplier: every kill within a short window raises the multiplier, but
taking a single hit resets it to zero. The player must constantly push forward
into danger to keep the chain alive rather than retreating to safety. Bombs
offer a panic button that clears the screen but sacrifice potential multiplier
growth. Multiple arenas with different layouts and hazard placements force the
player to adapt movement patterns rather than memorizing one safe route.

## What the Player Experiences

The player opens to a pulsing title screen with neon wireframe aesthetics, then
selects an arena from a small roster. Gameplay begins immediately: the ship sits
center-screen, one stick (or WASD) moves, the other (or arrow keys) aims and
fires continuously. Enemies spawn at arena edges in escalating waves — small
darts, splitting hexagons, homing diamonds, shielded rings. Each kill adds to a
visible multiplier counter; a timer bar shows how long until the multiplier
decays. Grazing bullets without dying builds a secondary graze bonus.

Between waves a brief upgrade prompt offers weapon mods — wider spread, faster
fire rate, piercing shots, or an extra bomb. The arena itself may shift: walls
retract, hazard zones ignite, or gravity wells appear. Every few waves a boss
shape enters with patterned attacks. Losing all lives shows a final score
breakdown with multiplier stats, highest chain, and arena-specific leaderboard
position.

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