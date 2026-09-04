# Slot Fortune

Build **Slot Fortune**, a slot machine roguelike with interacting symbols and
escalating rent as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A slot machine spins each turn, and the symbols that land interact with each
other to generate coins. Between spins the player adds new symbols, removes
unwanted ones, and builds synergies — cats multiply adjacent milk symbols, ore
feeds adjacent furnaces, thieves steal from neighbors. The catch: rent is due
every few spins and escalates relentlessly. The player must build a symbol
engine that generates enough coins to pay rent while investing in new symbols
that compound future earnings. Fail to pay rent and the run ends. The deeper
the run goes, the rarer and more powerful the symbols available, but rent
climbs to match. It is a deckbuilding game disguised as a slot machine.

## What the Player Experiences

A title screen shows a stylized slot machine with glowing symbols. Starting a
run presents a 3x5 slot grid with a few basic symbols (coins, cherries, gems).

Each turn the reels spin and land on random positions. Symbols activate
left-to-right: adjacent matching symbols pay out, and special symbols trigger
effects on their neighbors. A coin counter tallies earnings for the turn. After
the spin, a shop offers three new symbols to add to the reel pool and an option
to remove one existing symbol for a fee.

Every 5 spins, rent is due — a fixed amount that increases each cycle. If the
player cannot pay, the run ends with a score screen showing spins survived,
peak coins, and best symbol combos. Symbols have rarity tiers (common, rare,
legendary) with increasingly powerful interactions. The strategy lies in
curating the symbol pool to create reliable high-paying combinations.

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