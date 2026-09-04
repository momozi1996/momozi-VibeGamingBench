# Siege Engineer

Build **Siege Engineer**, a **physics-based siege weapon strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player builds and aims siege weapons to demolish castle fortifications
using realistic projectile physics. Each level presents a castle with walls,
towers, and defenders that must be reduced to rubble within a limited number
of shots. The player chooses weapon type, adjusts angle and power, and fires —
watching the projectile arc through the air and crash into destructible
terrain. The tension is resource scarcity: ammunition is limited, each shot
must count, and the castle's geometry creates puzzles about where to strike
for maximum structural collapse. The tone is medieval engineering: wood and
iron machines, stone dust, and the satisfying crunch of masonry giving way.

## What the Player Experiences

From the title screen the player enters a campaign map of increasingly
fortified castles. Each level shows the target castle on the right and the
player's siege position on the left, with terrain between them.

The player selects from available weapon types: trebuchets for high arcs over
walls, ballistae for flat direct shots, and catapults for medium-range
bombardment. Each weapon has different projectile weight, speed, and blast
radius. The player aims by adjusting angle and power with a drag interface,
seeing a trajectory preview line.

Firing launches the projectile with physics-based flight. On impact, castle
blocks take damage and can crack, crumble, or collapse depending on structural
support — removing a load-bearing wall brings everything above it down. The
player has a limited shot count per level and must destroy enough of the castle
to meet a destruction threshold.

Later levels add wind that shifts projectile paths, armored walls that resist
certain weapon types, and defenders that repair damage between shots. The
campaign escalates from simple walls to complex multi-tower fortresses.

A styled result screen shows destruction percentage, shots used, and stars
earned. Three stars require efficient demolition with minimal shots.

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

Interaction scheme (pointer-first): Use click, hover, drag, or selection as the primary controls; add keyboard shortcuts only where they are natural.
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