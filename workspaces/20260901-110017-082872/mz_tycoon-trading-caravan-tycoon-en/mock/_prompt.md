# Tycoon: Trading Caravan

Build a **route-planning and market trading tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a merchant captain steering a small caravan across a network of
towns that each want different things at different prices. The fantasy is reading
the map like a puzzle — spotting where silk is cheap and where it is gold, then
gambling on the road between. Every route is a bet: the short path is safe but
dull, the mountain pass saves days but invites bandits, and the cargo you chose
might spoil before you arrive. Growth compounds — better wagons carry more, hired
guards open dangerous shortcuts, cold crates unlock perishables — but so does
risk, because a bigger haul means a bigger loss when things go wrong. The
pressure is that markets shift while you travel, so yesterday's sure profit can
become tomorrow's dead weight. The tone is parchment-and-ink merchant strategy:
a world of trade routes, price boards, and calculated gambles.

## What the Player Experiences

The player opens a stylized map dotted with towns connected by roads of varying
length and danger. A caravan marker sits at the current town, and a ledger shows
cash, cargo hold, and any active contracts. The first minutes are about scanning
prices — this town sells spices cheap, the one across the river pays double —
and loading up the wagon.

Choosing a destination means weighing route options: the safe road costs more in
feed and tolls, the shortcut through bandit territory risks losing cargo
entirely. Once committed, the caravan moves and events unfold — a storm delays
travel, a toll gate demands coin, a merchant on the road offers a side deal. The
player watches cargo, money, and risk shift in real time.

Arriving at a new town, the player sells at local prices, checks what is scarce
here, and decides whether to restock or push onward. Earnings fund upgrades —
extra carts for capacity, scouts who reveal hazards ahead, cold storage that
opens perishable goods to trade. Each upgrade reshapes which routes and cargoes
become profitable.

Over time the network opens up: new towns appear, higher-value contracts become
available, and the caravan grows from a lone wagon into a proper trading
operation. The arc ends when the player hits a profit milestone and sees a
success screen, or when debt and failed contracts pile up into bankruptcy. Both
outcomes are navigable without restarting.

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