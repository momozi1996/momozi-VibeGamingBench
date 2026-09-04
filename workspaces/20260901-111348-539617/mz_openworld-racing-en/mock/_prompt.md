# Open-World Racing

Build a **2D open-world racing game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player drives a vehicle across a large open-world map with multiple
biomes, discovering and racing on scattered tracks. Each track has a unique
layout, terrain type, and time-trial record to beat. Tension comes from
momentum management — braking too late sends you off the road, drifting at
the right moment rewards a speed boost, and each biome demands a different
driving style. The art style should feel **fast, vibrant, and arcade-like** —
think *Burnout* meets *A Short Hike* at a smaller scale.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a play button, and
   a dynamic racing backdrop (speed lines, car silhouette, sunset highway).
   No naked HTML 引擎 grey.
2. **The World** — The player spawns in an open-world map with at least three
   visually distinct biomes: coastal road, desert canyon, and mountain pass.
   The vehicle can drive freely in all directions, exploring at will.
3. **Scattered Tracks** — Each biome contains at least one race track marked
   by a visible start/finish line and checkpoint gates. Tracks have different
   layouts suited to their terrain: long straights, tight switchbacks, or
   elevation hairpins.
4. **Vehicle Physics** — The vehicle accelerates, brakes, and steers with
   visible momentum. Drifting around corners produces a skid-mark trail and
   a brief speed boost when released. The vehicle sprite visibly tilts when
   turning.
5. **Timer and Records** — A lap timer starts when the player crosses the
   start line and stops at the finish. The HUD shows current lap time, best
   lap time, and a medal ranking (Gold/Silver/Bronze based on time).
6. **Track Unlocking** — Winning a bronze or better medal on one track unlocks
   the next track with a visible unlock animation. The player progresses
   through the world by earning medals.
7. **Speed Feedback** — A speedometer is always visible on the HUD. At high
   speed, the screen edges show a subtle motion-blur or speed-line effect.

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