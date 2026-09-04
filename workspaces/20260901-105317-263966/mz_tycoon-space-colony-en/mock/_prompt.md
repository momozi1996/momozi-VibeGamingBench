# Space Colony

Build **Space Colony**, an **asteroid colony management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A small crew lands on a barren asteroid and must build a self-sustaining colony
from nothing. Oxygen, food, and power are the three lifelines — lose any one
and colonists die. The player builds modules on a grid surface: habitats for
living, farms for food, solar arrays for power, and oxygen generators to keep
everyone breathing. Each colonist has needs and a job assignment; idle colonists
consume without producing. The tension is that expansion requires resources
that are already stretched thin, and random meteor strikes can destroy modules
without warning. The fantasy is frontier survival in the void — every new
module is a small victory against the emptiness of space.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
top-down asteroid surface with a grid overlay. The initial lander provides
minimal oxygen, food, and power for a small crew.

The player builds modules by spending materials mined from the asteroid.
Habitats house colonists, farms grow food, solar panels generate power, and
oxygen recyclers keep the air breathable. Each module connects to adjacent
ones, and the colony must maintain positive balance in all three resources or
colonists begin dying.

Colonists are assigned to jobs: miners extract materials, farmers tend crops,
engineers maintain modules, and researchers unlock new building types. Each
colonist has morale affected by living conditions, workload, and whether their
habitat has amenities.

Meteor events strike randomly, damaging or destroying modules. The player must
maintain redundancy and repair capacity. Research unlocks advanced modules:
greenhouses, fusion reactors, shield generators, and deep-mining rigs.

The game tracks population, days survived, and colony rating. A styled result
screen shows colony achievements when the colony is lost or reaches a
population milestone.

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

Interaction scheme (pointer-first): Use click, hover, drag, or selection as the primary controls; add keyboard shortcuts only where they are natural.
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