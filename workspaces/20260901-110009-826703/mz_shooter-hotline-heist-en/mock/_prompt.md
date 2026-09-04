# Hotline Heist

Build **Hotline Heist**, a top-down fast-action shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is bursting through doors into rooms full of armed guards, clearing
entire floors in seconds with precise aim and brutal efficiency. The interesting
tension is fragility: both the player and enemies die in one hit, making every
room entry a lethal puzzle where hesitation means death. Combo scoring rewards
speed — chaining kills without pause multiplies the score, encouraging reckless
aggression balanced against the instant-death stakes. Weapon variety scattered
across floors forces improvisation: a shotgun clears a cluster but alerts the
next room, while a silenced pistol preserves surprise but demands accuracy.

## What the Player Experiences

The player sees a stylized title screen, selects a floor from the campaign list,
and spawns outside the building's entrance. The camera shows the full floor plan
from above — rooms, corridors, doors, and enemy patrol routes are partially
visible. The player moves with WASD, aims with the mouse, and clicks to attack.
Doors can be kicked open to stun enemies behind them.

Each floor is a self-contained puzzle of 4-8 rooms connected by doors and
hallways. Guards patrol set routes; some stand still, others pace. Weapons litter
the ground — bats, pistols, shotguns, SMGs, thrown knives — each with limited
ammo or single-use. Clearing all enemies on a floor triggers a score screen
showing time, combo chain, and weapon variety bonus. Dying restarts the floor
instantly. The campaign offers 8+ floors with escalating guard density, new enemy
types (armored, dogs, gunners), and tighter layouts.

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