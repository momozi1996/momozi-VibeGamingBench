# City on the Sleeping Titan

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A vertical city-management adventure built on the back of a colossal sleeping creature. The player explores districts, studies tremors, repairs infrastructure, and decides whether to preserve the city, evacuate it, or wake the titan before involuntary movement tears everything apart.

## Required Playable Systems

1. **System 1** - Explore at least four vertically layered city districts connected by lifts, bridges, ladders, and routes that shift with the titan's posture.
2. **System 2** - Read a live tremor forecast and stabilize structures by placing braces, balancing loads, and repairing utilities before movement events.
3. **System 3** - Track the titan's breathing, stress, and sleep depth; loud construction and resource extraction must affect those systems.
4. **System 4** - Coordinate factions with conflicting plans for evacuation, sedation, awakening, and continued expansion.
5. **System 5** - Respond to playable disasters such as bridge collapse, fires, rolling debris, and district tilting while directing civilian movement.
6. **System 6** - Complete one of several city-scale plans during a major awakening sequence, producing materially different final city states.

## Progression

Survey data and district support unlock stronger engineering tools, safer transit, and larger coordinated operations.

## Art Direction

Monumental organic urbanism: dense low-poly districts over breathing stone-like skin, sweeping altitude views, warning beacons, and rhythmic titan motion.

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