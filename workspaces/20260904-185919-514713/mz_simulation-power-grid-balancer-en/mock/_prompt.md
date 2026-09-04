# Power Grid Balancer

Build a complete, playable **3D simulation game** as a polished browser vertical slice.

## Core Vision

A real-time 3D city power-dispatch simulation. The player switches buildings between consumption, storage, and vehicle-to-grid modes while renewable output and demand fluctuate, trying to prevent cascading overloads without blacking out essential services.

## Required Playable Systems

1. **System 1** - Render a low-poly city with animated wind turbines, solar fields, substations, charging hubs, storage buildings, and visible transmission links.
2. **System 2** - Let players click buildings to switch operating modes and drag or select substations to reroute capacity between grid zones.
3. **System 3** - Simulate changing generation, demand, storage charge, line capacity, frequency stability, and overload propagation in real time.
4. **System 4** - Animate directional energy flow and transition overloaded buildings from normal blue states to flashing red warnings before failure.
5. **System 5** - Provide multiple scenarios involving calm weather, evening peaks, renewable collapse, heat waves, and emergency service priorities.
6. **System 6** - Score reliability, renewable usage, cost, unmet demand, and recovery time, with clear success and cascading-blackout loss states.

## Progression

Campaign scenarios unlock batteries, demand-response tools, stronger lines, and forecasting aids that introduce new strategic options rather than flat upgrades.

## Art Direction

A crisp low-poly infrastructure diorama with varied green spaces, warm city windows, cyan energy streams, and unambiguous amber/red fault states.

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