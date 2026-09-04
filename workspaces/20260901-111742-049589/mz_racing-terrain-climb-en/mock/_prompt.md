# Racing Terrain Climb

Build a Racing Terrain Climb as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A side-scrolling physics vehicle game where the player drives over rugged
terrain, managing momentum and fuel to reach the farthest distance possible.
The vehicle bounces, tilts, and flips over hills and valleys — too much
throttle on a steep incline flips you backward; too little and you stall on
the slope. Fuel is limited and refilled at checkpoints, creating tension between
speed and conservation. Earned coins buy vehicle upgrades (engine power,
suspension, fuel capacity) and new vehicle types, each with different physics
properties. The fantasy is conquering impossible terrain through smart driving
and incremental improvement.

## What the Player Experiences

1. **Title Screen** — A rugged outdoor scene with the game name in bold blocky
   letters, a vehicle silhouette mid-jump against a sunset sky, and Play/Garage
   buttons. No plain HTML grey.
2. **Stage Select** — Multiple terrain environments (countryside hills, moon
   surface, arctic ice, desert dunes) each with distinct physics properties
   (friction, gravity). Stages unlock by reaching distance milestones.
3. **Driving Physics** — The vehicle has realistic 2D physics: wheels grip
   terrain, the chassis tilts with slope angle, and momentum carries over
   crests. The player controls gas (right) and brake (left), plus tilt
   (up/down) to adjust the vehicle's angle mid-air.
4. **Fuel Management** — A fuel gauge depletes as the player drives. Running
   out stops the vehicle. Fuel canisters appear along the route at intervals.
   The tension between driving fast (burning fuel) and conserving creates
   meaningful decisions.
5. **Coins and Distance** — Coins scatter along the terrain and award currency.
   Distance is tracked as a high score. Each run ends when fuel runs out or
   the vehicle is destroyed (landing on the roof).
6. **Garage/Upgrades** — Between runs, the player spends coins on upgrades:
   engine power, fuel capacity, suspension stiffness, tyre grip. At least 3
   different vehicle types (jeep, motorcycle, monster truck) with visibly
   different sprites and handling characteristics.
7. **Distance Records** — A persistent leaderboard shows best distance per
   stage. Beating a personal record triggers a celebration effect.

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

Interaction scheme (keyboard-first): Use arrows or WASD plus clear Space, Enter, and Escape actions; add pointer input where it naturally improves aiming or menus.
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