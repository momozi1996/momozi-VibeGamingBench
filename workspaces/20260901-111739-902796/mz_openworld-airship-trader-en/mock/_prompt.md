# Open-World Airship Trader

Build a **2D open-world airship trading game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player pilots an airship through a sky filled with floating islands, each
with its own economy and goods to trade. The fantasy is freedom above the clouds:
charting routes between distant ports, buying low and selling high, upgrading
your vessel with better engines and cargo holds, and fending off sky pirates who
lurk along trade lanes. Tension comes from fuel management, pirate ambushes, and
volatile market prices that shift as you trade.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name over a parallax sky
   backdrop with drifting clouds and distant islands. A play button begins the
   journey.
2. **The Sky Map** — The player flies their airship freely across a large open
   sky. Multiple floating islands are visible, each with a distinct silhouette
   and colour palette. Clouds drift in parallax layers.
3. **Docking** — Approaching an island triggers a docking prompt. Once docked,
   the player enters a trade menu showing local goods, prices, and their cargo
   hold contents.
4. **Trading** — Each island produces certain goods cheaply and demands others at
   premium prices. The player buys cargo, flies to another island, and sells for
   profit. Prices fluctuate over time.
5. **Upgrades** — Profits fund ship upgrades: faster engines, larger cargo hold,
   better fuel efficiency, and hull armour. Upgrades are visible on the ship
   sprite.
6. **Sky Pirates** — Along certain routes, pirate ships appear and chase the
   player. The player can outrun them, fight with a mounted cannon, or pay a
   toll. Combat is real-time with simple projectile shooting.
7. **Fuel & Risk** — The airship consumes fuel while flying. Running out means
   drifting helplessly. Fuel can be bought at islands or found in floating
   crates.

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