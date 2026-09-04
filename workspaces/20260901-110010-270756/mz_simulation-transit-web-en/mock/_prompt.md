# Transit Web

Build **Transit Web**, a 2D transit network simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is designing a city's transit network from scratch, connecting
stations with colored lines and watching passengers flow through the system like
blood through veins. The interesting tension is resource scarcity: the player has
limited lines, carriages, and tunnels to serve a city that keeps growing. New
stations appear over time with different shapes representing passenger
destinations, and overcrowded stations eventually fail, ending the game. Every
line placement is a commitment — rerouting wastes precious time while passengers
pile up. The elegance of the solution matters: a well-designed network handles
growth gracefully while a tangled mess collapses under its own complexity.

## What the Player Experiences

The player opens to a minimalist city-map title screen, then begins with a small
map showing 3 stations of different shapes (circle, triangle, square). The player
draws a line connecting two or more stations by clicking them in sequence. Tiny
passenger icons appear at stations, each shaped to indicate their destination
type. Passengers board trains that travel along lines and disembark at matching
stations.

As time passes new stations appear across the map. The player receives periodic
resource grants: new lines, extra carriages (increasing line capacity), or
tunnels (allowing river crossings). Stations that accumulate too many waiting
passengers flash warnings and eventually overflow, ending the run. The player
can reroute lines at any time but must manage the transition. Different map
layouts offer varied challenges — river cities, island chains, sprawling
suburbs. A run-end screen shows days survived, passengers delivered, and
network efficiency stats.

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