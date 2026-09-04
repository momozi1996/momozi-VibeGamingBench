# Horror Dollhouse

Build a **Horror Dollhouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a dollhouse that mirrors a real house, manipulating miniature
objects to affect the full-size world and escape. The fantasy is uncanny scale:
moving a tiny chair in the dollhouse causes a crash upstairs, opening a miniature
door reveals a hidden passage in the real house. Tension comes from the dollhouse
responding to the player — figures move on their own, rooms rearrange when not
watched, and the boundary between miniature and real blurs. The player must solve
puzzles across both scales to find the way out.

## What the Player Experiences

1. **Title Screen** — A split-view showing a dollhouse and its real counterpart,
   the game name in childlike handwriting that drips, and a play button.
2. **The Real House** — The player moves through a dark, full-size house in
   side-view. Doors are locked, passages blocked, and something is wrong — rooms
   do not connect logically.
3. **The Dollhouse** — Found in the attic, the dollhouse is a miniature replica
   of the real house. The player can zoom into it and interact with tiny objects:
   move furniture, open doors, flip switches.
4. **Mirror Mechanics** — Actions in the dollhouse affect the real house.
   Moving a miniature bookcase reveals a passage in the real house. Turning on a
   tiny lamp illuminates a dark real room. Locking a dollhouse door traps
   something in the real house.
5. **Puzzle Progression** — Each room has a puzzle requiring manipulation across
   both scales. The player alternates between exploring the real house and
   adjusting the dollhouse to progress.
6. **The Dollhouse Responds** — As the player progresses, the dollhouse changes
   on its own: figures appear in rooms the player just left, furniture moves
   back, and new rooms appear that do not exist in the real house. Investigating
   these anomalies reveals the horror.
7. **Escape** — The final puzzle requires the player to manipulate both scales
   simultaneously to open the front door. The ending depends on whether the
   player investigated the anomalous rooms or ignored them.

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