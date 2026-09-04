# Garden Crawl

Build **Garden Crawl**, a garden-dungeon roguelike with plants as allies and
seed deckbuilding as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A gardener descends through a dungeon that is also a garden — soil tiles can be
planted with seeds that grow into allies, barriers, or resource producers over
several turns. The player carries a seed deck and plays seeds onto the grid
before and during encounters. A sunflower provides energy each turn, a thorn
bush damages adjacent enemies, a vine wall blocks paths, and a healing bloom
restores the gardener. Seasons rotate every few floors, changing which seeds
thrive: spring boosts growth speed, summer strengthens attack plants, autumn
yields bonus harvests, and winter slows everything. Between floors the player
drafts new seeds, composts unwanted ones, and tends a persistent greenhouse
that provides starting bonuses for future runs.

## What the Player Experiences

A title screen shows a garden growing over dungeon stones. Starting a run gives
the player a starter seed deck of 8 basic seeds.

Each floor is a grid-based encounter. The gardener stands on one side, enemies
approach from the other. Before enemies reach the gardener, the player plants
seeds on soil tiles. Seeds grow over turns: sprout -> mature -> active. Mature
plants provide their effect (damage, healing, blocking, energy generation).
The player manages an energy resource to plant seeds and activate abilities.

Between floors, a draft screen offers three new seed choices. A compost option
removes a seed from the deck. Every 3 floors the season changes, visually
transforming the environment and modifying plant stats. A greenhouse meta-layer
persists between runs — seeds planted there provide small starting bonuses.
The run ends at a boss floor or when the gardener's health reaches zero. A
results screen shows floors cleared, plants grown, and seeds collected.

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