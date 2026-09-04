# Wave Commander

Build **Wave Commander**, a 2D wave defense shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is commanding a lone turret or mobile defender at the center of an
arena, holding the line against increasingly organized enemy waves that attack
from all directions. The interesting tension is resource management between
waves: earned currency must be split between weapon upgrades, defensive barriers,
and consumable power-ups, and the player never has enough for everything. Enemy
formations grow more complex — flanking squads, shielded columns, fast rushers
mixed with slow tanks — demanding that the player adapt loadout and positioning
each round. Boss waves punctuate the escalation with massive enemies that require
sustained focused fire while their escorts continue the assault.

## What the Player Experiences

The player opens to a military-themed title screen, selects a difficulty, and
deploys into the first arena. The player character occupies the center with
360-degree aiming. Wave 1 begins with simple enemies approaching from one
direction. The player aims with mouse and fires with click, moving with WASD to
dodge return fire. Clearing a wave triggers a brief shop phase showing available
upgrades: fire rate, damage, spread, shield repair, deployable mines, or a
screen-clearing airstrike.

Waves escalate in enemy count, variety, and formation complexity. Some waves
attack from multiple directions simultaneously. Every 5 waves a boss wave
arrives featuring a large enemy with distinct attack phases surrounded by
support units. The arena may shift between waves — new cover appears, hazard
zones activate, or the playfield shrinks. After 20 waves or player death, a
results screen shows waves survived, enemies destroyed, and upgrades purchased.

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