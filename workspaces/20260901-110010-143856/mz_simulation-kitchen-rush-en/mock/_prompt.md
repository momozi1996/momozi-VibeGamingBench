# Kitchen Rush

Build **Kitchen Rush**, a 2D time-pressure cooking simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a restaurant kitchen during a dinner rush, juggling
multiple orders across different cooking stations while timers tick down and
customers grow impatient. The interesting tension is multitasking under pressure:
each recipe requires specific steps at specific stations in a specific order, and
the player must mentally track multiple dishes simultaneously. Burning food wastes
ingredients and time; serving wrong orders loses reputation. Between shifts the
player unlocks new recipes, upgrades stations, and expands the kitchen layout,
but more capacity means more complex orders and higher customer expectations.

## What the Player Experiences

The player opens to a restaurant storefront title screen, then enters the first
shift. The kitchen view shows stations arranged spatially: chopping board, stove,
fryer, oven, plating area, and serving window. Orders appear at the top with
recipe requirements and countdown timers. The player clicks a station to interact,
drags ingredients from the pantry to stations, and monitors cooking progress.

Recipes start simple — chop lettuce, plate it, serve — but quickly layer:
burger requires chopping, grilling, assembling bun with toppings, then plating.
Multiple orders run simultaneously. Overcooking triggers smoke and waste.
Completing orders earns coins and tips based on speed. Between shifts a shop
screen offers station upgrades (faster stove, larger fryer), new recipe unlocks,
and kitchen expansions. The campaign progresses through 10+ shifts with
increasing order complexity, customer volume, and recipe variety. A shift
summary shows orders completed, failed, tips earned, and star rating.

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

Interaction scheme (both): Support both keyboard and pointer controls: use keyboard for movement or actions and the pointer for spatial selection, menus, or targeting.
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