# Potion Craft

Build **Potion Craft**, a potion-brewing roguelike with ingredient maps and
recipe discovery as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

An alchemist navigates a procedural ingredient map, gathering herbs, minerals,
and essences to brew potions that fulfill customer orders. Brewing is a
navigation puzzle on an alchemy map — the player steers a mixing cursor through
ingredient space, and the path taken determines the potion's properties. Each
customer wants a specific potion type (healing, fire resistance, invisibility)
and the alchemist must discover recipes by experimentation, then reproduce them
reliably. Between days the shop earns reputation that unlocks rarer ingredients
and harder customers. Failing too many orders loses reputation until the shop
closes. Each run is a fresh start with a new ingredient layout to discover.

## What the Player Experiences

A title screen shows bubbling cauldrons and potion bottles. Starting a run
opens the shop on Day 1 with three customer orders visible.

The brewing screen shows an alchemy map — a 2D space with ingredient nodes
connected by paths. The player navigates a cursor from the center outward,
passing through ingredient zones that add properties to the brew. Reaching a
recipe zone and bottling creates a potion of that type. The map is partially
hidden and revealed through exploration.

Customers arrive with orders (icons showing desired potion type). Fulfilling
an order earns gold and reputation. Gold buys map reveals, better tools (faster
navigation, wider paths), and ingredient restocks. Each day brings new
customers with harder requests. After a set number of days, a final evaluation
scores the run based on reputation, gold earned, and recipes discovered. Losing
all reputation ends the run early.

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