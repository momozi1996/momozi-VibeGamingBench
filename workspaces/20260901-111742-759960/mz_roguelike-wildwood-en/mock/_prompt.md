# Roguelike: Wildwood

Build a **node-map forest-exploration roguelike with turn-based combat** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The fantasy is reading a dangerous forest. Every fork in the trail is a bet
placed with incomplete information: claw marks on a trunk, smoke curling above
the canopy, a glint of metal in the undergrowth. The player pushes deeper not
because the path is safe but because the clues make the risk feel knowable. When
a beast appears, combat is deliberate and positional — a small kit of skills
spent against creatures that each punish a different mistake. Health never
refills for free, so every scratch from three clearings ago still matters at the
final gate. Death is permanent for the run, but not for the player: banked gold
and a dwindling supply of entry tickets give each expedition weight without
making failure a dead end. The tone is hushed and watchful — dappled light,
distant howls, the crackle of a campfire earned by surviving one more node.

## What the Player Experiences

The player begins at a trailhead camp that remembers them between sessions —
tickets, gold, and whatever lasting advantages they have earned are all visible
here. Entering the forest costs a ticket, so the decision to set out already
carries stakes.

Once inside, the run unfolds as a branching map of trail nodes stretching deeper
into the wood. Nodes are not fully revealed; instead the map offers partial
evidence — tracks, smoke, glitter, disturbed brush — that lets the player weigh
risk against their current health, gold, and depth. Committing to a node strips
away the mystery: it might be a beast, a chest, a campfire, a trader, a trap, or
something worse.

Combat is turn-based and skill-driven. The hero carries several distinct
abilities that cost a resource, and different beasts demand different responses —
a fast wolf, an armored bear, a venomous serpent. Lingering conditions like
poison or bleed play out over multiple turns, rewarding the player who reads the
threat and plans ahead.

Between fights the player collects relics and gear that reshape how the hero
fights, not just refill health. Growth within a run is tangible: new buttons, new
options, new ways to handle what the forest throws next.

A run ends in victory — reaching the heart of the wood and overcoming its
guardian — or in death, which sends the player back to camp minus a ticket but
richer in banked gold. Progress persists across sessions, so quitting and
returning picks up the same hoard and the same slow accumulation of power.

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