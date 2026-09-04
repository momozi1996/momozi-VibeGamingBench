# The Last Reservoir

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A drought-management exploration game around the final functioning reservoir. The player travels between settlements, inspects infrastructure, and returns to a council chamber to allocate water before climate events turn political compromise into physical survival.

## Required Playable Systems

1. **System 1** - Explore the reservoir basin and at least four connected districts, inspecting pumps, canals, wells, farms, and damaged treatment equipment.
2. **System 2** - Operate a physical water-control board with valves and allocation sliders that visibly redirect animated flow through the 3D map.
3. **System 3** - Balance reservoir volume, contamination, pressure, and district demand across a changing multi-day forecast.
4. **System 4** - Negotiate with factions whose needs and trust change based on inspections, promises, shortages, and previous allocations.
5. **System 5** - Respond to fires, pipe failures, dust storms, and illegal tapping through timed field missions and emergency rerouting.
6. **System 6** - Finish with a council vote and final drought event whose playable outcome reflects both infrastructure and social legitimacy.

## Progression

Repairs and negotiated agreements unlock efficient infrastructure, better forecasts, and new allocation options while permanently changing district resilience.

## Art Direction

A sun-bleached low-poly basin with cracked earth, turquoise flow overlays, weathered civic machinery, heat haze, and urgent red emergency lighting.

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