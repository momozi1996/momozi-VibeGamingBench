# Pirate Fleet

Build **Pirate Fleet**, a **naval tactics strategy game with wind mechanics** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A fleet of pirate ships navigates a hex-sea where wind direction dictates
everything. Sailing with the wind is fast; tacking against it is slow and
costly. The player commands multiple ship types — nimble sloops, heavy
galleons, boarding frigates — positioning them to exploit wind advantage while
denying it to the enemy. Combat is broadside-based: ships deal damage from
their flanks, so facing matters as much as range. Treasure islands dot the map
as objectives worth fighting over. The tone is golden-age piracy: sun-bleached
sails, cannon smoke, and the creak of timber under fire.

## What the Player Experiences

From the title screen the player selects a scenario or campaign mission. The
map shows a hex-grid sea with islands, shallows, and a wind-direction indicator
that shifts every few turns. The player's fleet starts on one side; the enemy
on the other. Treasure islands sit between them as objectives.

Each turn the player moves ships. Movement cost depends on direction relative
to wind: downwind is cheap, crosswind moderate, upwind expensive. Ships have
limited movement points per turn. After moving, ships with enemies in their
broadside arc can fire cannons — damage depends on range and facing angle.

Ship types serve different roles: sloops scout and flank quickly, galleons
absorb damage and carry heavy guns, and frigates can initiate boarding actions
on adjacent ships for a chance to capture rather than sink. Captured ships join
the player's fleet.

Treasure islands are captured by moving a ship adjacent and holding for one
turn. Controlling islands earns victory points. The scenario ends when one side
reaches the point target or loses all ships. A styled result screen shows the
battle outcome with ships sunk, captured, and treasure claimed.

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