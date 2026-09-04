# Zero-G Exploded View

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

An interactive 3D inspection and repair puzzle built around the exploded view of a precision drone or camera. The player disassembles the device, examines labeled components, diagnoses faults, and restores the assembly in the correct order.

## Required Playable Systems

1. **System 1** - Drive a smooth exploded-view amount with a slider and mouse wheel, giving component groups distinct spring and damping responses.
2. **System 2** - Support orbit, zoom, hover highlighting, isolation, and pinned 3D labels that remain readable and point to the correct moving part.
3. **System 3** - Create an inspection puzzle where players identify faulty components through visual clues, diagnostic readings, and functional descriptions.
4. **System 4** - Require a valid disassembly and reassembly order with tool selection, dependency checks, snap previews, and invalid-action feedback.
5. **System 5** - Include multiple device modules or fault scenarios involving optics, power, control boards, motors, cooling, and structural parts.
6. **System 6** - Verify the repair with a playable system test and show performance differences based on diagnosis and assembly accuracy.

## Progression

New repair jobs add denser assemblies, subtler faults, calibration steps, and optional efficiency challenges.

## Art Direction

Premium industrial visualization with brushed metal, transparent plastic, rubber, glass optics, studio lighting, crisp outlines, and restrained technical labels.

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