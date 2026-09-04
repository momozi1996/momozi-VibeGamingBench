# Thunder Valkyrie

Build **Thunder Valkyrie**, a 2D vertical scrolling bullet-hell shoot-'em-up as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A lone starfighter threads through mathematically dense curtains of enemy fire,
where every pixel of the hitbox matters and every split-second dodge buys another
breath. The tension lives in reading bullet geometry: patterns sweep, spiral, and
converge while the player traces the one safe seam through the chaos. Between
sorties the pilot reinvests plundered gold into hull upgrades, sub-weapons, and
wingman attachments, reshaping how the next wave feels. The tone is bright,
kinetic, and relentless — an arcade reflex challenge wrapped in deep-space neon
and spectacular particle destruction.

## What the Player Experiences

A styled title screen introduces the game with a cosmic backdrop and a clear
path into the hangar.

In the hangar the player reviews their persistent loadout — starfighter level,
shield type, sub-weapon, wingman — and spends gold earned from prior runs to
upgrade slots. Each upgrade visibly changes projectile patterns or survivability
for the next sortie.

From a sector map the player selects a constellation stage. Each stage has a
distinct stellar backdrop and its own enemy composition. Locked stages remain
gated until the previous boss falls.

Once deployed, the screen scrolls vertically over a layered starfield. The
starfighter moves smoothly in response to input, its tiny glowing core hitbox
the only vulnerable point. Primary lasers fire continuously; sub-weapons and
wingmen add flanking fire. Waves of enemy interceptors enter in geometric
formations, releasing scripted bullet configurations that sweep downward. Elite
capital ships drop red power crystals; collecting them triggers a frenzy state
that doubles fire rate and vacuums nearby pickups.

Each stage culminates in a multi-phase boss that locks the scroll and floods the
arena with layered patterns. Taking damage degrades the shield; if it breaks the
run ends with a results overlay showing gold earned and waves survived. Defeating
the boss unlocks the next stage and awards premium components.

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