# Idle Factory Planet

Build an **Idle Factory Planet** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player places machines on a planet surface that automatically produce
resources, chains production lines together, and researches upgrades until the
planet is depleted — then prestiges to a new planet with better technology. The
fantasy is industrial scale: watching conveyor belts carry ore to smelters to
fabricators, output numbers climbing exponentially, and the planet surface
filling with an intricate factory network. The idle loop runs production
continuously; the player optimises layouts and unlocks new machine types.

## What the Player Experiences

1. **Title Screen** — A small planet covered in tiny factories with conveyor
   belts, the game name in industrial stencil font, and a play button shaped
   like a gear.
2. **Planet Surface** — A top-down grid representing the planet surface. The
   player places machines on tiles. Conveyor belts connect machines visually,
   showing resources flowing between them.
3. **Machine Placement** — Machines include: miners (extract raw ore), smelters
   (ore to metal), fabricators (metal to parts), and sellers (parts to credits).
   Each machine auto-produces when supplied. The player drags machines from a
   panel onto the grid.
4. **Production Chains** — Machines must be connected in sequence. Output from
   one feeds input of the next via conveyor. Longer chains produce more valuable
   goods. A production rate display shows throughput.
5. **Research** — Credits fund research that unlocks better machines: faster
   miners, multi-input fabricators, and storage buffers. A tech tree shows
   available upgrades with costs and effects.
6. **Planet Depletion** — The planet has finite resources. A depletion meter
   shows remaining ore. As resources thin, miners slow down. When depleted, the
   player must prestige.
7. **Prestige (New Planet)** — Prestiging moves to a fresh planet with more
   resources. The player keeps research progress and gains a permanent production
   multiplier. Each new planet starts faster and scales higher.

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