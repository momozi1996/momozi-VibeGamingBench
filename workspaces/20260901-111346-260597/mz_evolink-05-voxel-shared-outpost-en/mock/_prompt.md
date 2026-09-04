# Voxel Shared Outpost

Build a complete, playable **3D survival and crafting game** as
a polished browser vertical slice from a **first person** viewpoint.

## Core Vision

A small browser voxel world supports multi-tab local players who gather, build, and defend one synchronized outpost.

## Required Playable Systems

1. **System 1** - Move in first person through a generated voxel world with grounded collision and tool use.
2. **System 2** - Place and remove blocks through valid range, inventory, and authoritative conflict rules.
3. **System 3** - Synchronize player names, transforms, and block edits between tabs using BroadcastChannel with a solo fallback.
4. **System 4** - Gather resources and cooperatively defend a shared objective before a timed extraction.
5. **System 5** - Provide at least three functionally distinct content variations that change timing, route choice, resource use, or risk rather than only labels and colors.
6. **System 6** - Use a three-stage arc that teaches the core interaction, combines systems under pressure, and ends in a complete win, loss, or scored completion loop.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

Tactile resources and tools, readable environmental danger, changing weather and time, visible wear and construction, and a world that records intervention.

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