# Neon Arena

Build **Neon Arena**, a twin-stick arena shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being the last pilot standing in a sealed geometric arena as
waves of hostile shapes pour in from every edge. The interesting tension is the
score multiplier: every kill within a short window raises the multiplier, but
taking a single hit resets it to zero. The player must constantly push forward
into danger to keep the chain alive rather than retreating to safety. Bombs
offer a panic button that clears the screen but sacrifice potential multiplier
growth. Multiple arenas with different layouts and hazard placements force the
player to adapt movement patterns rather than memorizing one safe route.

## What the Player Experiences

The player opens to a pulsing title screen with neon wireframe aesthetics, then
selects an arena from a small roster. Gameplay begins immediately: the ship sits
center-screen, one stick (or WASD) moves, the other (or arrow keys) aims and
fires continuously. Enemies spawn at arena edges in escalating waves — small
darts, splitting hexagons, homing diamonds, shielded rings. Each kill adds to a
visible multiplier counter; a timer bar shows how long until the multiplier
decays. Grazing bullets without dying builds a secondary graze bonus.

Between waves a brief upgrade prompt offers weapon mods — wider spread, faster
fire rate, piercing shots, or an extra bomb. The arena itself may shift: walls
retract, hazard zones ignite, or gravity wells appear. Every few waves a boss
shape enters with patterned attacks. Losing all lives shows a final score
breakdown with multiplier stats, highest chain, and arena-specific leaderboard
position.

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