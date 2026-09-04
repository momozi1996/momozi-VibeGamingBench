# Garden Ecosystem Keeper

Build **Garden Ecosystem Keeper**, a compact **ecosystem gardening management
game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player tends a small restoration garden where every tile is part of a living
web. Plants compete for moisture and light, pollinators follow bloom corridors,
pests exploit monoculture, and weather shifts the whole balance overnight. The
core tension is stewardship under scarcity: limited actions per turn, finite
water, unpredictable seasons, and biodiversity goals that punish brute-force
planting. A thriving garden is one the player composed, not one they clicked
into existence.

The tone is gentle but systemic — readable beds, seed packets, pollinator
trails, pest warnings, seasonal color shifts, and clear biodiversity meters.
The garden should feel alive and authored, not a raw grid of colored squares.

## What the Player Experiences

The player opens to a garden restoration scene and chooses a plot to tend. The
first planting is simple: a few seed types, moist soil, calm weather. Plants
grow visibly over turns, and the player learns the rhythm of water, wait,
harvest.

Soon the ecosystem asserts itself. A pollinator visits one flower bed but
ignores another. A pest cluster appears near a monoculture row. Companion
planting hints emerge — herbs near tomatoes deter aphids, wildflowers draw
bees toward fruit trees. The player starts composing beds rather than filling
them.

Weather and seasons raise the stakes. A dry spell forces triage: which beds
get the last water? An early frost threatens unprotected seedlings. A rainy
season floods low tiles but lets the pond habitat flourish. The player adapts
their plan each turn, balancing short-term survival against long-term
biodiversity targets.

Late game, the garden is a dense web of interactions. The player manages
pollinator corridors, pest barriers, moisture zones, and seasonal rotations.
When the restoration goal is met — a target biodiversity score, a bloom
festival, or a full habitat chain — the result screen reflects the garden's
health and composition. Failure shows what collapsed and why, inviting a
different strategy next time.

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