# Perspective Path

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

An orthographic 3D puzzle game about impossible architecture. The player rotates a sculptural building until separated paths overlap on screen, creating temporary walkable connections for a small character.

## Required Playable Systems

1. **System 1** - Rotate an orthographic camera around a 3D monument with snapped and free-drag controls while preserving stable framing and depth order.
2. **System 2** - Detect screen-space alignment between path endpoints and enable traversal only while geometric and occlusion conditions are valid.
3. **System 3** - Let the player click reachable nodes to move a character along connected routes, blocking invalid moves with clear feedback.
4. **System 4** - Provide at least six escalating puzzles using rotating towers, movable bridges, elevators, switches, occluders, and multiple alignment steps.
5. **System 5** - Include undo, restart, camera reset, selected-node highlighting, optional hints, and deterministic puzzle state.
6. **System 6** - Complete each level by carrying or activating a goal object, then unlock a level-select path through the monument.

## Progression

New chapters introduce layered alignment rules, moving parts, split characters, and simultaneous path conditions while teaching each mechanic visually.

## Art Direction

A calm architectural diorama with clean stone, jewel-like accents, soft shadows, impossible silhouettes, and minimal illustrated UI.

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