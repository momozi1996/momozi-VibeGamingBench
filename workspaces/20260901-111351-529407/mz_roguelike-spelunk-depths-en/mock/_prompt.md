# Spelunk Depths

Build **Spelunk Depths**, a procedural platformer roguelike with physics objects
and shopkeepers as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

An explorer descends through procedurally generated cave floors, using ropes,
bombs, and whatever objects are at hand to navigate traps, defeat creatures, and
collect treasure. Every object in the world has physics — pots can be thrown at
enemies, rocks tumble when supports are destroyed, and explosions chain through
destructible terrain. Shopkeepers sell items on certain floors but turn hostile
if the player steals. A ghost timer activates after lingering too long on any
floor, creating an invincible pursuer that forces forward progress. Shortcuts
unlock after meeting specific conditions, allowing experienced players to skip
early floors. Death is permanent and sends the player back to the surface with
nothing but knowledge.

## What the Player Experiences

A title screen shows the cave entrance with depth markers. Starting a run
places the explorer at floor 1 with basic equipment: 4 ropes and 4 bombs.

Each floor is a procedurally generated platformer level with an exit at the
bottom. The explorer runs, jumps, whips enemies, throws ropes upward to create
climbable lines, and places bombs to blast through terrain. Pots, crates, and
skulls can be picked up and thrown. Traps include arrow traps, spike pits, and
crush blocks. Enemies patrol with simple AI.

Shops appear every few floors with items for sale — buying requires gold
collected from gems and chests. Stealing triggers shopkeeper aggression for the
rest of the run. After 3 minutes on a floor, a ghost spawns and chases the
player relentlessly. Every 5 floors the environment theme changes. Death shows
a summary of depth reached, gold collected, and enemies defeated.

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