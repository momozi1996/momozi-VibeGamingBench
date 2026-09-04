# Bullet Cathedral

Build **Bullet Cathedral**, a bullet-hell roguelike as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is descending through a procedurally arranged cathedral of hostile
rooms, each one a dense bullet-hell encounter where survival depends on
split-second dodge-rolls through curtains of projectiles. The interesting tension
is roguelike impermanence: death sends the player back to the top with nothing,
but each run offers different gun pickups and room layouts, rewarding adaptation
over memorization. The dodge-roll grants brief invincibility frames, creating a
rhythm of rolling through danger and firing back during recovery windows. Gun
variety — from tight railguns to wide shotgun blasts to bouncing orbs — means
each run plays differently depending on what the cathedral offers.

## What the Player Experiences

The player sees a gothic-styled title screen, starts a run, and enters the first
room of the cathedral. The top-down view shows a confined arena with the player
character at center. Enemies spawn and immediately begin firing patterned bullet
spreads. The player moves with WASD, aims with mouse, fires with click, and
dodge-rolls with spacebar. Clearing all enemies in a room opens exits to the
next.

Each floor consists of 5-7 rooms with a boss room at the end. Between rooms the
player may find gun pedestals offering a weapon swap, health pickups, or passive
upgrades. Guns have distinct firing patterns and ammo behavior. Floor bosses fill
the screen with elaborate bullet patterns that require precise rolling and
positioning. After defeating a floor boss, a brief interstitial shows stats
before descending to the next floor. Three floors complete a run with a victory
screen; death at any point shows a run summary with rooms cleared and enemies
defeated.

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