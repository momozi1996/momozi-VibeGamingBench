# Crowns of Twelve Ashes

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A compact fantasy campaign across twelve fractured realms represented on one explorable strategic map. The player gathers crown fragments through diplomacy, field battles, and risky alliances while ash storms slowly erase unprotected territory.

## Required Playable Systems

1. **System 1** - Traverse a world map containing twelve recognizable realms or realm nodes, each with a settlement, ruler, local conflict, and travel hazard.
2. **System 2** - Resolve negotiations through reputation, promises, tribute, evidence, and faction relationships rather than a single dialogue choice.
3. **System 3** - Fight real-time tactical encounters with movement, attacks, dodging, companion commands, and clear victory or retreat conditions.
4. **System 4** - Collect crown fragments with distinct powers and costs that alter travel, diplomacy, combat, or ash resistance.
5. **System 5** - Simulate an advancing ash front that changes routes, destroys resources, and pressures the order in which realms are visited.
6. **System 6** - Conclude with an assembly or conquest sequence whose playable structure and ending depend on surviving realms and alliances.

## Progression

Fragments, companions, and realm treaties create a flexible build, while permanent realm losses ensure campaign decisions cannot all be reversed.

## Art Direction

A stylized dark-fantasy atlas brought to life in 3D, with twelve strong regional palettes, ash-filled skies, heraldic UI, and magical crown effects.

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