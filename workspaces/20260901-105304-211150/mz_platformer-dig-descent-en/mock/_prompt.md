# Dig Descent

Build **Dig Descent**, a vertical descent platformer with downward shooting and
combo scoring as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A diver plunges endlessly downward through procedurally assembled shafts,
firing a weapon beneath their feet to destroy blocks, slow their fall, and
chain kills into escalating combos. The gun is both offense and movement tool —
shooting downward provides upward recoil that buys precious milliseconds to
steer around hazards. Gems collected from destroyed blocks fund visits to
mid-run shops where weapon upgrades and health refills await. The deeper the
player descends, the faster the screen scrolls and the denser the hazards
become. Death resets to the surface with nothing carried over except skill.

## What the Player Experiences

A title screen shows the game name, high score, and a Start button. Pressing
Start begins the descent immediately.

The player character falls continuously. Pressing the fire button shoots
downward, destroying soft blocks and nudging the character upward slightly.
Enemies drift across the shaft — shooting them adds to a combo counter that
multiplies gem value. Landing on a platform resets the combo but provides a
safe moment to breathe. Touching spikes, enemies, or the top of the screen
costs health.

Every few depth tiers a shop platform appears with three purchasable upgrades:
weapon spread, fire rate, health refill, or a shield. The player spends
collected gems and continues downward. Procedural generation ensures no two
runs are identical. When health reaches zero, a game-over screen shows depth
reached, gems collected, max combo, and a retry button.

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