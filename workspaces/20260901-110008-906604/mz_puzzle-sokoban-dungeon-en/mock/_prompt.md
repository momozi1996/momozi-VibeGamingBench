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

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use HTML Canvas 2D or Three.js/WebGL for the playable presentation.
- `game_logic.js` - the deterministic state and rules layer. Use a classic script
  and expose `createGame(opts)` and `advance(game, input, dt)`; an optional
  `render(gameState, renderCtx)` hook may be exposed.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Assets must be generated at runtime with no network
requests: procedural geometry, Canvas2D-drawn textures encoded as `data:` URIs,
offscreen-canvas particle sprites, Web Audio API synthesized sound, shaders,
post-processing, and CSS are all allowed and encouraged. Do not embed or fetch
external image, model, video, or audio files at runtime. Three.js may be loaded
from its pinned official CDN; if post-processing is used, pin the matching
`examples/jsm/postprocessing/*` modules to the same Three.js version.

Interaction scheme (pointer-first): Use click, hover, drag, or selection as the primary controls; add keyboard shortcuts only where they are natural.
Keep the complete play area and HUD readable at 1280x720. Include a clear start
flow, concise in-game guidance, pause and restart controls, a complete win/loss
or scored outcome loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest` for external URLs; only
the pinned Three.js CDN above is allowed. Keep `index.html` at or below 400 KB.
The `game_logic.js` line count is advisory and is not a BUILD-gate failure.

### Logic and rendering scaffold

```html
<script src="./game_logic.js"></script>
<script>
  const { createGame, advance, render } = window.GameLogic;
  const game = createGame({});
  // The loop calls advance; render(game, { THREE, scene, ... }) is optional.
</script>
```

```javascript
(function (root) {
  function createGame(opts) { return { phase: "title", score: 0 }; }
  function advance(game, input, dt) { return game; }
  function render(gameState, renderCtx) { /* optional visual hook */ }
  const api = { createGame, advance, render };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` must be pure and must not access DOM or Three.js objects. The optional
`render()` hook is called by the main loop and may map state to scenes, materials,
particles, and post-processing.