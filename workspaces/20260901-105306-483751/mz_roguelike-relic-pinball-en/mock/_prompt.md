# Roguelike: Relic Pinball

Build **Relic Pinball**, a compact **pinball / brick-breaker roguelite** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: an original, polished vertical slice about
navigating a cursed mechanical table one chamber at a time, breaking target
banks, triggering arcane mechanisms, and collecting relics that visibly mutate
the ball's behavior across an escalating run.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is exploring a cursed mechanical table one chamber at a time. Each
chamber is a live pinball board fused with brick-breaker structure: target rows,
bumpers, switches, lanes, gates, spinners, and special blocks create readable
goals while the ball remains fast and physical. The tension lives in flipper
timing and relic synergy — every launch is a gamble, every save a small
triumph, and every relic choice reshapes how the ball interacts with the world.
A ball might split on contact, burn through cracked bricks, curve toward metal
targets, leave scoring echoes, charge bumpers on pass-through, or orbit after
paddle hits. The tone is arcane arcade machine: brass rails, glass reflections,
carved stone bricks, luminous relic icons, bright impact sparks, and snappy
flipper feedback.

## What the Player Experiences

From the title screen the player sees a styled pinball-table motif with at
least one relic or magical ball identity hinting at what lies ahead.

The run drops the player into a live table. A ball launches into a bounded
playfield and the player works left and right flippers to keep it alive,
threading it through bumpers, lanes, and brick banks. Every collision feels
different — bumpers kick the ball away, bricks crack and shatter, switches
light up lanes, spinners charge multipliers, and portals warp the ball across
the board. The table is not a passive backdrop; it reacts.

Clearing enough targets or triggering the right mechanisms opens a relic
choice. The player picks from several relics, each with a name, icon, and
concise rule. The chosen relic immediately changes how the next chamber plays —
the ball splits, pierces, magnetizes, or leaves fire trails. The active relic
row persists and stacks, so the run builds toward a strange loadout that no
two attempts share.

Chambers grow harder: new layouts, tighter drains, armored targets, hazard
bumpers, and eventually a boss table whose special rule demands more than
reflexes. Victory or defeat lands on a styled result screen that lets the
player try again without restarting the application.

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