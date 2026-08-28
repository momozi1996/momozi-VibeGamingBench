# Sokoban Dungeon

Build **Sokoban Dungeon**, a 2D turn-based crate-pushing dungeon puzzle as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player pushes crates through procedurally
generated dungeon rooms while enemies move simultaneously on each turn,
collecting keys and items to unlock deeper floors.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a turn-based puzzle-roguelike hybrid where every player step
triggers an enemy step. Each dungeon room is a spatial puzzle: crates must be
pushed onto pressure plates to open doors, but enemies patrol the grid and
move toward the player whenever the player moves. The tension comes from the
simultaneous-turn system — pushing a crate takes a turn, during which enemies
close in, so the player must solve spatial puzzles under mounting threat. Keys
unlock new rooms, items provide one-use abilities (freeze enemies, pull crates,
teleport), and procedural room layouts ensure variety. The best version feels
like chess merged with a warehouse puzzle, where every move has tactical
consequences.

## What the Player Experiences

A title screen sets the dungeon tone with stone textures and a clear way to
begin. The player enters a dungeon room where walls, crates, pressure plates,
locked doors, keys, enemies, and the exit staircase are visible on a grid.
Movement is turn-based: arrow keys move one tile, and all enemies move one
tile simultaneously.

Early rooms teach basic pushing: move a crate onto a plate to open a door.
Soon enemies appear that mirror the player's movement timing, forcing the
player to plan push sequences that also avoid or trap threats. Mid-game
introduces multiple crate types (heavy crates need two pushes, ice crates
slide until hitting a wall), keys that unlock color-coded doors, and items
found in chests. Late rooms combine all mechanics in procedurally arranged
layouts where the player must solve the spatial puzzle while managing enemy
positions.

An undo system lets the player rewind turns. Reaching the exit staircase
advances to the next floor. Death from enemy contact offers retry. The
campaign generates increasingly complex floors with more enemies, more crate
types, and tighter spatial constraints.

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