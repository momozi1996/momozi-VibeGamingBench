# Train Heist

Build **Train Heist**, a procedural train-car roguelike with car-by-car
encounters as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A bandit boards the caboose of a procedurally generated train and must fight
forward car by car to reach the engine before the train arrives at the station.
Each car is a self-contained encounter: a passenger car with civilians to rob,
a guard car with armed defenders, a cargo car with locked safes to crack, a
dining car with cover-based shootouts, or a mail car with time-locked vaults.
The bandit carries limited ammo and health, spending both as they push forward.
Loot from earlier cars funds purchases at a black-market car that appears
mid-train. A turn counter represents distance to the station — if it hits zero
before reaching the engine, the heist fails. Each run generates a new train
with different car sequences and lengths.

## What the Player Experiences

A title screen shows a steam train silhouette against a sunset. Starting a run
shows the full train in side-view with car types partially visible (some
hidden).

The player enters the caboose and encounters the first car's challenge. Combat
is turn-based with cover mechanics — the bandit and enemies take positions
behind furniture and exchange fire. Ammo is limited and must be looted from
fallen guards. Passenger cars offer robbery choices: intimidate for quick cash
or search thoroughly for better loot but risk alerting guards ahead.

A progress bar shows position along the train and turns remaining. The black-
market car offers health kits, ammo, special weapons, and disguises. Reaching
the engine triggers a boss fight against the conductor. Victory shows total
loot, cars cleared, and turns remaining. Failure (health zero or time out)
shows how far along the train the bandit reached.

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