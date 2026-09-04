# Every Road Returns Before Midnight

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A surreal road-loop exploration game. Every route taken across a lonely region folds back toward the same motel before midnight, while landmarks subtly decay and memories persist between loops. The player must map contradictions and break the topology.

## Required Playable Systems

1. **System 1** - Drive and walk through a connected road network with at least four distinct landmarks, branching junctions, and navigable interiors.
2. **System 2** - Run a visible day-to-midnight loop in which roads reconnect differently while selected evidence, map annotations, and player knowledge persist.
3. **System 3** - Let the player place map pins and compare road lengths, signs, shadows, and landmark states to identify impossible connections.
4. **System 4** - Introduce changing hitchhikers, radio broadcasts, weather, and roadside hazards that reveal different clues on later loops.
5. **System 5** - Track vehicle condition, fuel, fatigue, and a distortion meter that changes controls and scenery as midnight approaches.
6. **System 6** - Provide several topology-breaking solutions that require performing a learned route sequence before the final midnight reset.

## Progression

Each verified contradiction unlocks new map tools and memory anchors, allowing more state to persist and exposing deeper routes.

## Art Direction

Dreamlike nocturnal Americana with wet asphalt, sodium lights, analog dashboard glow, impossible horizon folds, and escalating spatial distortion.

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