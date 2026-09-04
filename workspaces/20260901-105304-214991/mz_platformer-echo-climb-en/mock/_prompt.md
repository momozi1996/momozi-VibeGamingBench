# Echo Climb

Build **Echo Climb**, a tower-climbing platformer where past runs become ghost
platforms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A climber ascends an impossibly tall tower, but the tower is mostly empty air.
The trick: every failed attempt leaves behind a ghost that replays the run, and
the ghost's body becomes a solid platform for future attempts. The first run
might reach only a few ledges before falling. The second run can stand on the
ghost of the first to reach higher. Each attempt layers another ghost into the
tower, gradually building a scaffold of past selves that makes previously
impossible heights reachable. The player decides when to sacrifice a run to
create a useful stepping stone versus when to push for maximum height. A
persistent best-height marker and ghost count track progress across sessions.

## What the Player Experiences

A title screen shows the tower stretching upward with ghost silhouettes
visible. Starting a run places the player at the tower base.

The climber can run, jump, and wall-slide. The tower has sparse fixed platforms
but large vertical gaps that seem impassable. When the player falls or quits,
the run is recorded as a ghost. On the next attempt, all previous ghosts replay
simultaneously — their bodies are semi-transparent but physically solid. The
player can stand on ghosts, use them as moving platforms, or ride them upward.

A height meter shows current altitude and best-ever altitude. Every five
attempts the player can choose to "solidify" one ghost into a permanent
platform (it stops replaying and becomes a fixed ledge). The game saves ghost
data between sessions. Reaching milestone heights unlocks cosmetic trail
effects for the climber.

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