# The Winter Clause

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A winter survival mystery inside and around a sprawling family estate. A will-reading locks the heirs in during an unnatural freeze, and the player must explore the house, manage heat, observe family routines, and uncover which clause controls the weather.

## Required Playable Systems

1. **System 1** - Explore a multi-floor mansion, greenhouse, frozen grounds, service tunnels, and weather-vane tower with unlockable shortcuts.
2. **System 2** - Manage room temperature by operating boilers, vents, fireplaces, shutters, and power circuits while fuel remains limited.
3. **System 3** - Observe and question family members whose schedules, alliances, and access permissions change after each discovered clause.
4. **System 4** - Solve inheritance puzzles using portraits, keys, legal documents, mechanical locks, and environmental temperature states.
5. **System 5** - Survive escalating cold effects such as frozen doors, brittle floors, blackouts, and blizzard exposure during exterior trips.
6. **System 6** - Reach the weather-vane mechanism and enforce, reinterpret, or destroy the final clause, producing different family outcomes.

## Progression

Recovered clauses and repaired heating zones expand safe exploration time, reveal hidden wings, and grant leverage in family negotiations.

## Art Direction

A snowbound gothic manor with warm candle interiors, icy blue encroachment, brass heating machinery, stained glass, and wind-driven snow effects.

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