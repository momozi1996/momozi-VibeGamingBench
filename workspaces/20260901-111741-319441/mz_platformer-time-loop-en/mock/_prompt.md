# Time Loop

Build **Time Loop**, a 30-second time loop platformer where past-self replays
help solve puzzles as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

Each level is a 30-second loop. When the timer expires, time rewinds and the
player starts again — but a ghost of the previous loop replays simultaneously,
interacting with the world. The ghost can hold switches, distract enemies, or
stand on pressure plates while the current player tackles other objectives.
Multiple loops layer: loop 1's ghost holds a door open, loop 2's ghost stands
on a platform to create a bridge, and in loop 3 the player finally reaches the
exit using both ghosts' contributions. The puzzle is temporal coordination —
planning what each loop-self needs to do and when, so that all versions
cooperate across time. Twenty-four levels across four chapters escalate from
single-ghost puzzles to four-loop orchestrations.

## What the Player Experiences

A title screen shows overlapping clock hands and ghost silhouettes. A chapter
menu reveals four chapters of six levels each.

Entering a level starts a 30-second countdown. The player runs, jumps, and
interacts with switches and objects. When the timer hits zero, the screen
flashes and rewinds — the player restarts at the spawn point, but a translucent
ghost replays exactly what they did in the previous loop. The ghost physically
interacts with the world: it presses buttons, holds doors, and blocks lasers.

The player can layer up to four loops. A timeline bar at the top shows all
active ghosts and their current positions in the 30-second window. Reaching the
exit crystal with all required switches held (by ghosts or player) completes
the level. A reset button clears all ghosts to start fresh. Level-complete
shows loops used and time of exit within the final loop.

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