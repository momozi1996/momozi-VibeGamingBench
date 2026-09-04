# Neon Gravity Marble Run

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

A tactile 3D neon marble labyrinth controlled by keyboard tilt or device orientation. Real gravity, collisions, moving geometry, and momentum are the puzzle; the player learns to bank, brake, and redirect the ball through increasingly dangerous transparent courses.

## Required Playable Systems

1. **System 1** - Simulate the marble with Cannon.js, including gravity, rolling acceleration, restitution, friction, ramps, rails, and physically credible collisions.
2. **System 2** - Support arrow-key tilt and device orientation with calibration, sensitivity control, and an always-available desktop fallback.
3. **System 3** - Create collision feedback with camera impulse, sparks, sound, and Vibration API on supported devices without making input unreadable.
4. **System 4** - Provide at least three courses with checkpoints, moving platforms, launch pads, narrow rails, hazards, collectibles, and finish gates.
5. **System 5** - Track time, falls, checkpoint progress, best run, and optional pickups, with quick recovery after leaving the course.
6. **System 6** - Use speed-sensitive trails or postprocessing to communicate motion blur and increasing danger at high velocity.

## Progression

Later courses introduce stronger gravity, rotating frames, polarity zones, and branching risk/reward routes while preserving deterministic resets.

## Art Direction

A dark synthwave void with translucent emissive tracks, contrasting hazard colors, luminous particles, glossy marbles, and restrained bloom.

## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use Three.js and WebGL for the playable presentation.
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