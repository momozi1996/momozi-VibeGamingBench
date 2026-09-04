# FTL Voyage

Build **FTL Voyage**, a spaceship management roguelike with crew and sector
navigation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A small starship flees through procedurally generated sectors toward a final
confrontation, managing crew, fuel, scrap, and ship systems along the way. Each
sector is a node map of encounters — hostile ships, traders, distress signals,
asteroid fields, and empty space. Combat is a real-time-with-pause system where
the player assigns crew to ship systems (weapons, shields, engines, medbay),
targets enemy rooms, and manages power distribution as systems take damage and
fires break out. Between jumps, scrap funds repairs and upgrades. Fuel limits
how many nodes can be visited before the sector exit must be reached. The final
sector pits the ship against a powerful flagship in a multi-phase battle that
tests every system the player has invested in.

## What the Player Experiences

A title screen shows the ship silhouette against a star field. Starting a run
presents a ship layout with rooms, three crew members, and starting resources.

The sector map shows connected nodes with partial information — icons hint at
combat, shops, or events. Jumping to a node costs fuel and triggers an
encounter. Combat shows both ships in cross-section: the player drags crew
between rooms, powers systems on/off, and fires weapons at targeted enemy rooms.
Damage breaches hulls, starts fires, and injures crew. Winning yields scrap.

Shops sell weapons, augments, crew, and fuel. Events present narrative choices
with risk/reward outcomes. Reaching the sector exit advances to the next sector
with harder encounters. After several sectors, the flagship battle begins — a
multi-phase fight with unique mechanics. Victory shows a run summary; defeat
shows how far the player reached.

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