# Air Control

Build **Air Control**, a 2D air traffic control simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is directing aircraft safely to their runways from a radar-style
control screen, drawing flight paths through increasingly crowded airspace while
avoiding collisions and managing weather disruptions. The interesting tension is
spatial planning under time pressure: planes enter from screen edges at different
speeds and altitudes, each needing to reach a specific runway. The player draws
paths that planes follow, but new arrivals constantly force replanning. Near-miss
warnings create panic moments where quick rerouting prevents disaster. Weather
events close runways or create no-fly zones, demanding real-time adaptation of
carefully laid plans.

## What the Player Experiences

The player opens to a control-tower themed title screen, selects an airport from
a campaign list, and enters the radar view. The screen shows a stylized top-down
airport with runways, taxiways, and surrounding airspace. Planes appear at edges
with callsigns, types, and destination runway indicators. The player draws a
flight path from each plane to its assigned runway by clicking and dragging
waypoints.

Planes follow their paths at their own speed. Proximity warnings flash when two
planes get too close. Successful landings earn points; collisions or planes
leaving the screen without landing lose lives. Between levels the player can
upgrade: add runways, install weather radar, unlock speed-control commands, or
expand the airspace boundary. Weather events — fog reducing visibility, storms
creating no-fly zones, crosswinds affecting runway availability — increase
pressure. The campaign spans 12+ levels across 3 airports with escalating
traffic density and complexity. A level summary shows planes landed, near-misses,
and efficiency rating.

## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use HTML Canvas 2D or Three.js/WebGL for the playable presentation.
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