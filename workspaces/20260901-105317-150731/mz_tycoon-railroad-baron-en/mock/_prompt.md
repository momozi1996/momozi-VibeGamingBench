# Railroad Baron

Build **Railroad Baron**, a **railroad empire tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player lays rail tracks across a map of cities, buys trains, and profits
from cargo demand. Each city produces and consumes different goods — connecting
a lumber town to a construction city creates a profitable route, but only if
the track is efficient and the train has capacity. Terrain drives costs:
mountains require expensive tunnels, rivers need bridges, and flat plains are
cheap but long. A competitor AI builds its own network, racing to claim the
most lucrative routes. The tension is capital allocation: every mile of track
is an investment that only pays off once trains run, and overbuilding before
revenue flows means bankruptcy. The tone is industrial-era ambition: steam,
iron, and the romance of connecting a frontier.

## What the Player Experiences

From the title screen the player starts a new map. The view shows a top-down
terrain map with cities marked by icons showing their goods (lumber, grain,
ore, manufactured goods). The player lays track by clicking city-to-city,
paying costs that vary by terrain crossed.

Once two cities are connected, the player buys a train and assigns it to the
route. Trains move automatically along tracks, picking up goods at one city
and delivering to another. Revenue depends on distance, cargo value, and
demand — delivering goods a city needs pays well; delivering surplus pays
poorly.

The player expands by connecting more cities, upgrading tracks for speed,
buying faster trains, and reading the demand map to find profitable routes.
A competitor AI builds its own network and competes for the same demand — if
they connect a route first, the player must find alternatives.

Money management is critical: track costs are upfront, train purchases are
large, and revenue trickles in over time. Taking on debt accelerates growth
but interest compounds. The game ends after a set number of years; the player
with the highest net worth wins. A styled result screen shows network maps,
revenue history, and final ranking.

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

Interaction scheme (pointer-first): Use click, hover, drag, or selection as the primary controls; add keyboard shortcuts only where they are natural.
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