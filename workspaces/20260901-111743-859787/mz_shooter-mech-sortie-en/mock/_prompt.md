# Mech Sortie

Build **Mech Sortie**, a top-down mech shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a heavily armed walking mech through hostile territory,
customizing its weapon hardpoints between missions to match the threats ahead.
The interesting tension is loadout planning: the mech has limited hardpoint slots
(arms, shoulders, back) and each weapon has weight, ammo, and range tradeoffs.
A missile rack dominates at range but leaves the mech vulnerable up close; dual
autocannons shred nearby targets but overheat. Missions yield salvage from
destroyed enemies that funds new weapons and chassis upgrades, creating a
satisfying loop of deploy, destroy, salvage, customize, redeploy.

## What the Player Experiences

The player opens to a hangar screen showing their mech with labeled hardpoints.
Available weapons are listed in an armory panel; dragging a weapon onto a
hardpoint equips it, with weight and energy constraints shown. Selecting a
mission from the campaign map deploys the mech into a top-down battlefield.

The mech moves with WASD (slower than infantry, with momentum), rotates the
torso independently with mouse aim, and fires equipped weapons with mouse
buttons and number keys. Missions have objectives: destroy all enemies, defend a
point, escort a convoy, or eliminate a target. Enemy variety includes infantry,
light vehicles, rival mechs, and turret emplacements. Destroying enemies drops
salvage crates collected on contact. Mission completion shows a debrief with
salvage earned, damage taken, and accuracy stats. The campaign spans 8+ missions
with escalating difficulty and a final boss mech encounter.

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