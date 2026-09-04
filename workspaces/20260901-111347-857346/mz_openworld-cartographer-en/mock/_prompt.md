# Open-World Cartographer

Build an **Open-World Cartographer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a cartographer venturing into unmapped wilderness, drawing the map
as they explore. The fantasy is discovery and mastery of the unknown: every step
reveals new terrain, every landmark sketched onto the map brings profit and
prestige. Tension comes from dangerous terrain — cliffs, swamps, predator
territories — and limited supplies. Completed maps sell to merchants in town,
funding better equipment for deeper expeditions. The map itself is the primary
UI element, filling in as the player moves.

## What the Player Experiences

1. **Title Screen** — A parchment-styled title with the game name in hand-drawn
   lettering, an ink bottle and quill motif, and a play button.
2. **The Wilderness** — The player moves freely through procedurally varied
   terrain: forests, mountains, rivers, caves, and ruins. Fog of war hides
   unexplored areas.
3. **Map Drawing** — As the player explores, a minimap and full-screen map fill
   in with terrain details. Landmarks (ruins, unique trees, cave entrances) can
   be annotated for bonus value.
4. **Dangers** — Hostile wildlife, treacherous cliffs, and quicksand threaten the
   player. Health is limited and healing requires returning to camp or using
   scarce supplies.
5. **Supplies** — The player carries food, ink, and rope. Food depletes over time;
   ink is consumed when annotating landmarks; rope is needed to cross cliffs.
   Running out forces a retreat.
6. **Selling Maps** — Returning to the starting town lets the player sell completed
   map sections. Larger, more detailed maps with annotations fetch higher prices.
7. **Equipment Upgrades** — Profits buy better boots (faster movement), a compass
   (reveals terrain type ahead), a lantern (explores caves), and a sturdy pack
   (more supply capacity).

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