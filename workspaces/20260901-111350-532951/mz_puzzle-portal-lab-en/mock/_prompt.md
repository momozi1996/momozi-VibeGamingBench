# Portal Lab

Build **Portal Lab**, a 2D portal-placement puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places entry and exit portals on designated
wall surfaces to redirect lasers, launch objects, and transport themselves
through test chambers, using momentum conservation and spatial reasoning.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a spatial puzzle built on linked teleportation. Each test chamber
has walls, floors, laser emitters, targets, weighted cubes, buttons, and a
locked exit. The player can place two portal endpoints on valid surfaces;
anything entering one emerges from the other with conserved momentum and
direction. The tension comes from chaining portals with physics: drop a cube
from height through a floor portal to launch it horizontally from a wall
portal onto a distant button, or redirect a laser through multiple portal
bounces to hit a sensor. The best version feels like bending space itself,
where each chamber is an "aha" moment of seeing how two linked holes solve
an impossible geometry.

## What the Player Experiences

A title screen sets the laboratory tone with portal imagery and a clean
scientific aesthetic. The player enters a test chamber where walls, laser
emitters, targets, cubes, buttons, and the exit door are visible. Valid portal
surfaces are subtly highlighted.

Early chambers teach basic portal use: place two portals to walk through a
wall, or redirect a single laser to a target. Soon chambers require momentum
tricks — falling through a floor portal to gain speed and launching from a
wall portal to cross a gap. Mid-game introduces weighted cubes that must be
portaled onto pressure plates, laser grids requiring multiple redirections,
and timed sequences where portals must be repositioned mid-puzzle. Late
chambers combine all mechanics: redirect lasers, launch cubes, and navigate
the player through a single interconnected portal network.

Placing a portal shows a preview of where it will link. Objects passing through
portals have visible trajectory trails. When all targets are activated, the
exit unlocks. A completion screen shows the chamber number and offers the next
challenge. The campaign progresses through increasingly complex test chambers.

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