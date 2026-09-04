# Academy of Forgotten Students

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A magical campus mystery where students are being erased from records and memory. The player freely explores halls, towers, gardens, and sealed archives, preserving unstable memories before the academy rewrites itself around each disappearance.

## Required Playable Systems

1. **System 1** - Explore at least four connected campus zones with day/night schedules, moving stairways, secret doors, and student routines.
2. **System 2** - Use a memory lens to reveal erased people, reconstruct shared moments, and pin unstable memories before they dissolve.
3. **System 3** - Cross-reference portraits, attendance ledgers, dorm objects, and witness recollections in a searchable archive interface.
4. **System 4** - Build trust with rival student groups whose memories conflict and whose cooperation opens different investigation routes.
5. **System 5** - Avoid or confront corrective magical entities that alter corridors and remove collected evidence when the player is detected.
6. **System 6** - Identify the erasure mechanism and choose whom or what to restore in a final ritual with multiple campus-wide outcomes.

## Progression

Preserved memories strengthen the lens, reveal deeper historical layers, and unlock spells for stabilizing spaces and protecting evidence.

## Art Direction

Whimsical gothic academia with luminous ink, moving portraits, moonlit courtyards, impossible staircases, and dissolving paper-particle memory effects.

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