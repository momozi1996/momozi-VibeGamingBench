# Tiny Factory Foreman

Build **Tiny Factory Foreman**, a compact 2D automation and production-planning
game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is running a miniature factory floor where raw materials flow in one
end and finished goods roll out the other — if the player has wired everything
together correctly. The interesting tension is spatial: belts only carry forward,
sorters only split, and machines only accept certain inputs, so every tile
placement is a routing puzzle under time pressure. Orders arrive on a board with
ticking deadlines, and the player must decide whether to retool the line for a
new product or squeeze more throughput from the current layout. The risk is
always a cascade failure — one misrouted material jams a machine, the backup
stalls the belt, and suddenly three orders expire at once. Growth comes from
earning enough to unlock faster belts, smarter sorters, or multi-output machines,
but each upgrade reshapes the routing problem rather than simply solving it.

## What the Player Experiences

The player opens to a compact workshop view: a few raw-material sources on one
side, empty order bins on the other, and a grid of open floor between them. An
order board shows what products are needed and how long remains. The first
minutes are about laying a simple belt path from source to machine to bin and
watching the first coloured crate trundle across the floor.

As orders grow more complex the player drops sorters to split material streams,
places different machine types that transform inputs into intermediate or final
goods, and reroutes belts to avoid collisions. The floor fills with motion —
little icons sliding along conveyors, machines pulsing as they process, sorters
flicking left or right. A well-designed line hums; a badly planned one backs up
and flashes warnings.

Between rounds or when cash allows, the player visits an upgrade screen to
improve belt speed, unlock a new machine recipe, or expand storage capacity.
These choices shape what orders can be accepted next. Eventually the shift ends
and a result screen tallies fulfilled orders, missed deadlines, and coins earned,
offering a retry or a return to the title.

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