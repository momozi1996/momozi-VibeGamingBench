# Magnet Dash

Build **Magnet Dash**, a platformer with magnetic attract/repel mechanics and
momentum traversal as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A magnetized robot navigates industrial chambers by attracting toward or
repelling away from metal surfaces scattered throughout each level. Holding
attract pulls the robot toward the nearest metal anchor, building speed as it
approaches. Releasing at the right moment converts that pull into ballistic
momentum. Repel pushes the robot away explosively, launching it across gaps or
up shafts. The interplay between attract and repel creates a swinging,
slingshotting movement vocabulary that feels like controlled chaos. Thirty
levels across three zones introduce increasingly complex magnetic puzzles,
and three boss encounters require using magnetic mechanics offensively —
deflecting projectiles or pulling shields away from enemies.

## What the Player Experiences

A title screen shows the robot suspended between two magnets. A zone-select
menu shows three zones of ten levels each, plus a boss at each zone's end.

In gameplay, metal surfaces glow with a distinct color. Holding the attract
button pulls the robot toward the nearest metal surface — the closer it gets,
the faster it accelerates. Releasing converts momentum into free flight.
Pressing repel near a metal surface launches the robot away at high speed.
Levels require chaining these moves to cross gaps, ascend shafts, and avoid
hazards like electric fields and crushers.

Boss fights take place in arenas with metal anchors. Bosses fire projectiles
that can be magnetically deflected, or have metal armor plates that can be
ripped away with attract. Defeating a boss unlocks the next zone. A completion
screen shows time, collectibles gathered, and a style rating based on momentum
chains.

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