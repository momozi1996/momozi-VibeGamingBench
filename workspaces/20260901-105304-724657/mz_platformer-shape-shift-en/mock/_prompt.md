# Shape Shift

Build **Shape Shift**, a puzzle-platformer with three transformable forms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A polymorphic creature navigates chambers by switching between three physical
forms mid-air: a heavy cube that falls fast and activates pressure plates, a
bouncy sphere that ricochets off walls and reaches high places, and a gliding
triangle that floats across wide gaps. Each form has distinct physics — the cube
is dense and grippy, the sphere is elastic and slippery, the triangle is light
and drifty. Puzzles require chaining transformations in sequence: launch as
sphere, shift to triangle mid-arc to glide over spikes, then drop as cube onto
a switch. Forty levels across four worlds teach each form individually before
demanding fluid mid-air combos.

## What the Player Experiences

A title screen shows the three forms orbiting the game name. A world-select
menu reveals four worlds of ten levels each, unlocked sequentially.

World 1 teaches the cube: weight, pressure plates, breaking fragile floors.
World 2 introduces the sphere: bouncing, wall-ricochets, momentum preservation.
World 3 adds the triangle: gliding, updrafts, precision floating. World 4
combines all three with puzzles requiring rapid mid-air switching.

The player presses 1/2/3 or cycles with a button to transform instantly. Each
form change produces a satisfying visual morph and a physics shift the player
feels immediately. Levels contain a goal crystal — reaching it completes the
level. Optional collectible stars reward creative form usage. A level-complete
screen shows time, stars collected, and form-switch count.

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