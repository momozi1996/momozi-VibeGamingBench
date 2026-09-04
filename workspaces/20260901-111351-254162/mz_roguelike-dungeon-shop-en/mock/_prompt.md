# Dungeon Shop

Build **Dungeon Shop**, a shopkeeper roguelike where you price items and defend
from thieves as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player runs a dungeon item shop, stocking shelves with weapons, potions,
and armor that adventurers browse and buy. The twist: the player sets prices,
and pricing is the core mechanic. Price too high and adventurers leave empty-
handed. Price too low and profit evaporates. Some customers are thieves who
grab items and bolt for the door — the player must physically chase and tackle
them or deploy traps. Between shopping days, the player ventures into a
procedural dungeon to acquire new stock, fighting monsters with whatever unsold
inventory is on hand. Gold funds shop upgrades: display cases, security
measures, and larger floor space. Each run spans multiple days until the shop
either thrives to a target gold amount or goes bankrupt.

## What the Player Experiences

A title screen shows a cozy shop interior with a sword on display. Starting a
run opens the shop on Day 1 with basic starter inventory.

During the shop phase, adventurers enter and browse. The player drags items
onto shelves and sets prices via a slider. Adventurers have visible budget
indicators and preferences. Satisfied customers pay and leave; overcharged
customers scoff and exit. Thieves grab items and run — the player clicks to
chase or activates pre-placed traps.

During the dungeon phase, the player enters a procedural side-scrolling dungeon
with simple combat, collecting loot to stock the shop. Better dungeon
performance means better inventory. Between days, an upgrade screen offers shop
improvements. The run ends in victory (reaching a gold target) or bankruptcy
(running out of stock and gold). A results screen shows days survived, total
profit, and thieves caught.

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