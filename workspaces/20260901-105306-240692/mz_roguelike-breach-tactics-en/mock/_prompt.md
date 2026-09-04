# Breach Tactics

Build **Breach Tactics**, a tactics roguelike on a small grid with visible enemy
intents as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A squad of three mechs defends a city grid from waves of alien invaders. The
twist: every enemy telegraphs its next move before the player acts, turning
each turn into a spatial puzzle of displacement, blocking, and sacrifice. The
grid is small (8x8) and buildings occupy tiles that must be protected — if too
many are destroyed, the timeline is lost. Between battles the player earns
reactor cores to upgrade mech abilities or unlock new pilots with passive
traits. A timeline-reset mechanic gives the player a limited number of full
turn undos per battle, allowing recovery from catastrophic mistakes. Four
islands of escalating difficulty each culminate in a boss encounter with unique
grid mechanics.

## What the Player Experiences

A title screen shows mechs dropping onto a grid. An island-select map shows
four islands with branching mission paths.

Each mission places the mech squad on a grid with buildings and spawning
enemies. Before the player moves, every enemy displays its intended action:
attack direction, movement target, or spawn location. The player moves each
mech and uses one ability per mech — push, shoot, shield, repair, or special.
After all mechs act, enemies execute their telegraphed moves simultaneously.

Protecting buildings is the priority — each destroyed building reduces a
structural integrity bar. Losing all integrity fails the mission. Timeline
resets (limited per battle) rewind one full turn. Between missions, upgrade
screens offer new weapons, pilot abilities, and reactor power allocation.
Completing an island unlocks the next. A final victory screen shows missions
completed, buildings saved, and resets used.

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