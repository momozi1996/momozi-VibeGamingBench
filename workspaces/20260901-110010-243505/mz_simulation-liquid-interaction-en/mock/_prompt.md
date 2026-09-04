# Liquid Interaction Lab

Build a complete, playable **3D simulation game** as a polished browser vertical slice.

## Core Vision

A playable real-time particle-fluid laboratory centered on a sphere of roughly ten thousand particles. The player repels and attracts the fluid to complete shape, containment, and energy challenges while learning how velocity and force alter the system.

## Required Playable Systems

1. **System 1** - Simulate approximately 10,000 particles through GPGPU or an equivalent GPU texture technique, with a graceful lower-count fallback.
2. **System 2** - Use pointer movement as a repulsive force and pointer press as an attractive force, with radius and strength controlled by readable UI.
3. **System 3** - Map particle color continuously from cool to warm based on velocity and show force direction, center of mass, and turbulence feedback.
4. **System 4** - Provide playable challenge modes for forming target silhouettes, moving fluid through rings, containing an unstable core, and restoring equilibrium.
5. **System 5** - Track stability, escaped particles, energy use, target accuracy, and elapsed time, with reset and slow-motion experimentation controls.
6. **System 6** - Maintain smooth interaction and clear input response under load, automatically adjusting quality without changing game-state rules.

## Progression

Completing experiments unlocks multi-source force fields, vortices, obstacles, viscosity presets, and more demanding target shapes.

## Art Direction

An elegant black laboratory void with luminous fluid color gradients, subtle grids, glass target volumes, and precise scientific UI.

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