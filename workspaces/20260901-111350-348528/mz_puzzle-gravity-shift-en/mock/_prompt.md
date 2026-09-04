# Gravity Shift

Build **Gravity Shift**, a 2D gravity-rotation puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player rotates the direction of gravity to guide a
ball through obstacle-filled chambers to an exit, using destructible terrain
and chain reactions to clear paths.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a physics puzzle built on directional gravity. The player cannot
move the ball directly but can rotate gravity in 90-degree increments (down,
left, up, right), causing everything in the chamber to fall in the new
direction. The tension comes from planning gravity sequences: rotating right
sends the ball sliding into a wall, but also drops a boulder onto a
destructible platform, opening a path for the next rotation. Chain reactions
emerge naturally — explosive crates detonate on impact, crumbling blocks
break after one landing, and weighted objects trigger pressure switches as
they settle. The best version feels like orchestrating a Rube Goldberg machine
where gravity itself is the only tool.

## What the Player Experiences

A title screen sets the tone with floating geometry and directional arrows.
The player enters a chamber where the ball, exit portal, walls, platforms,
hazards, and special objects are visible. Gravity direction indicators show
the current pull. The player presses arrow keys or buttons to rotate gravity.

Early chambers teach basic rotation: shift gravity right to roll the ball
toward the exit. Soon obstacles require multi-step sequences — rotate down
to drop through a gap, then left to slide past spikes. Mid-game introduces
destructible terrain (crumbling blocks that break on second impact, explosive
crates that blast nearby walls), weighted objects that trigger switches, and
conveyor surfaces that add lateral movement during falls. Late chambers
demand precise rotation sequences where each gravity shift triggers a chain
reaction that reshapes the level geometry.

An undo system lets the player rewind gravity shifts. Reaching the exit
portal completes the chamber with a celebration screen. Death from hazards
offers instant retry. The campaign progresses through themed worlds with
escalating physics complexity.

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