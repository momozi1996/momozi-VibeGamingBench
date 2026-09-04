# The Missing Second

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A compact open-city investigation game about a superhero who vanished during one impossible missing second. The player patrols several connected districts, reconstructs frozen incidents, and decides whether the city's celebrated rescue was actually a coordinated cover-up.

## Required Playable Systems

1. **System 1** - Explore at least three connected city districts, move freely between rooftops and streets, and locate temporal anomaly scenes through a scanner.
2. **System 2** - Reconstruct each missing-second scene by rotating a time echo, matching evidence positions, and locking a plausible sequence before the timer expires.
3. **System 3** - Interview witnesses whose testimony changes with trust and discovered evidence, then connect clues on an interactive conspiracy board.
4. **System 4** - Include multiple anomaly types, such as displaced vehicles, duplicated civilians, frozen projectiles, and corrupted security drones.
5. **System 5** - Track public trust and institutional suspicion; accusations, leaked evidence, and reckless scanning must change NPC reactions and available routes.
6. **System 6** - End with a playable confrontation where the player selects and proves one of several theories, producing visibly different city outcomes.

## Progression

Solving district cases upgrades scan range and time-echo control, opens restricted locations, and unlocks increasingly complex reconstructions.

## Art Direction

A rain-slick near-future metropolis with cyan forensic projections, amber street lighting, graphic-novel shadows, and sharp temporal fracture effects.

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