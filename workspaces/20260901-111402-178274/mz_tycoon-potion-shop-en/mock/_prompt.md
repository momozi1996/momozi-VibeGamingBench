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