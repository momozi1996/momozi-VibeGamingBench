# Momentum Lab

Build **Momentum Lab**, a momentum-based physics platformer with wall-jumps and
gold collection as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A sleek capsule-shaped runner slides, bounces, and wall-jumps through minimalist
laboratory chambers where momentum is everything. The character accelerates
continuously while grounded, preserves speed through wall-jumps, and loses it on
hard landings or collisions. Gold pieces are scattered through each level — some
on the obvious path, others requiring risky momentum-preserving detours. A
countdown timer per level creates urgency: collect the exit key and reach the
door before time expires. Two hundred compact levels across ten themed labs
escalate from gentle slopes to brutal momentum puzzles requiring perfect chains
of wall-jumps, slides, and mid-air redirects. Leaderboards track best times.

## What the Player Experiences

A title screen shows the game name and a level-select grid organized by lab
(10 labs of 20 levels each). Completed levels show gold count and best time.

Entering a level starts the timer. The player moves left/right with
acceleration physics — the character builds speed over time and slides on
slopes. Wall-jumping preserves horizontal momentum and adds vertical boost.
Gold pieces line paths and reward exploration. A key item unlocks the exit door.

Reaching the exit stops the timer and awards a rating based on time and gold
collected. Failing the timer or falling into a void restarts the level
instantly. Each lab introduces a new element: ice surfaces, conveyor belts,
gravity zones, bounce pads, moving walls, laser gates, wind tunnels, rotating
platforms, teleporters, and finally a gauntlet combining everything.

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