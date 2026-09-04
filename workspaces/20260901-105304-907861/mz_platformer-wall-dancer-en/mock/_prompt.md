# Wall Dancer

Build **Wall Dancer**, a precision platformer with wall-climb and dash mechanics
as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A nimble climber ascends through crystalline caverns one screen at a time,
clinging to walls, launching off with a directional dash, and threading through
spike-lined corridors that demand pixel-perfect timing. The game is built around
two verbs: cling and dash. Clinging to a wall lets the player slide slowly
downward while scanning the room for the next safe surface. Dashing consumes a
single charge that resets on landing or wall-grab, creating a rhythm of
commit-recover-commit that makes every room feel like a tiny puzzle solved
through muscle memory. Five chapters introduce new hazards — wind currents,
crumbling walls, moving spikes, gravity flips, and timed gates — each layering
complexity without changing the core two-verb vocabulary.

## What the Player Experiences

A title screen presents the game name and a chapter-select option (locked until
cleared). Pressing Start drops the player into Chapter 1, Room 1.

Each room fills exactly one screen. The player character clings to walls on
contact, sliding slowly downward. Pressing jump while clinging launches away
from the wall. Pressing dash mid-air sends the character in the aimed direction
at high speed, consuming the dash charge. Landing on ground or grabbing another
wall restores the charge. Spikes, pits, and moving hazards kill instantly,
respawning the player at the room entrance with no loading screen.

Clearing a room scrolls the camera to the next. Each chapter contains 8-12
rooms culminating in a final room that combines all chapter hazards. Completing
a chapter returns to the hub with the next chapter unlocked. A death counter
and best-time tracker per chapter encourage mastery replays.

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

Interaction scheme (keyboard-first): Use arrows or WASD plus clear Space, Enter, and Escape actions; add pointer input where it naturally improves aiming or menus.
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