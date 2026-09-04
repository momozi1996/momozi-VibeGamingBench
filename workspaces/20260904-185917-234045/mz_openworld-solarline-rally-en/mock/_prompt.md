# Solarline Rally

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A solar-system racing adventure built around route choice rather than a single closed track. The player pilots a modular racer between orbital gates, balances heat and fuel, encounters rivals, and decides how much danger or compromise is acceptable to reach the final line.

## Required Playable Systems

1. **System 1** - Drive or fly a responsive 3D racer across at least three planetary regions with drifting, boost, braking, jumps, and checkpoint validation.
2. **System 2** - Choose branching routes on a navigable system map, trading distance against storms, gravity wells, tolls, and repair opportunities.
3. **System 3** - Manage fuel, battery, hull, and engine heat; overboosting must create visible performance loss and possible breakdown.
4. **System 4** - Race distinct rivals with recognizable vehicles and tactics, including drafting, blocking, shortcuts, and opportunistic rescues.
5. **System 5** - Collect sponsors, upgrades, and route intelligence through optional events that create meaningful mechanical tradeoffs.
6. **System 6** - Complete a multi-leg championship with standings, stage results, rival consequences, and at least two final outcomes.

## Progression

Between legs, players install mutually exclusive modules that alter handling, efficiency, durability, scanning, or boost behavior.

## Art Direction

Bright retro-futurist motorsport with saturated planetary skies, holographic gates, heat trails, modular vehicles, and readable cosmic route graphics.

## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use Three.js and WebGL for the playable presentation.
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