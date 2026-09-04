# Last Broadcast from Vanta

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A lonely space-exploration campaign across a small star system. The player pilots a salvage vessel toward a dead colony's repeating emergency signal while storms, failing systems, and contradictory recordings turn navigation into a survival mystery.

## Required Playable Systems

1. **System 1** - Pilot a ship across a navigable star map with manual thrust, docking, scanning, and at least three explorable orbital locations.
2. **System 2** - Tune a multi-band receiver to isolate fragments of the Vanta broadcast while interference and false echoes obscure the correct signal.
3. **System 3** - Manage hull, power, fuel, and heat by rerouting ship systems during radiation storms and debris encounters.
4. **System 4** - Recover logs and physical evidence from derelicts, then arrange them on a timeline that changes the meaning of the final message.
5. **System 5** - Include hazards and optional rescues that force tradeoffs between mission progress, crew safety, and dwindling resources.
6. **System 6** - Reach Vanta and complete one of several playable approaches to the beacon, with different discoveries and endings.

## Progression

Recovered components improve engines, scanner precision, and power capacity, enabling access to harsher regions and deeper signal layers.

## Art Direction

Hard-sci-fi solitude: dark planetary silhouettes, instrument-lit interiors, volumetric signal waves, electrical arcs, and pale emergency beacons.

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