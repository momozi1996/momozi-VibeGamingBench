# Rhythm Striker

Build a complete, playable **3D rhythm-action game** as a polished browser vertical slice.

## Core Vision

A minimal 3D rhythm game inside an endless emissive tunnel. Geometric targets arrive on musical beats; accurate key strikes shatter them into physical debris while the tunnel, materials, and camera react to synthesized audio.

## Required Playable Systems

1. **System 1** - Spawn geometric beat targets in multiple lanes and judge key input with Perfect, Good, and Miss timing windows tied to a deterministic chart.
2. **System 2** - Use Web Audio API synthesis and an analyser so emissive materials, tunnel segments, and camera impulses respond to current frequency bands.
3. **System 3** - Shatter successful targets into velocity-aware physical fragments while misses pass the player and cause a distinct tunnel distortion.
4. **System 4** - Implement combo, multiplier, score, health, song progress, pause, retry, and a results screen with timing breakdown.
5. **System 5** - Provide at least three charts or difficulty modes with distinct rhythms, speeds, lane patterns, and visual identities.
6. **System 6** - Keep timing readable despite bloom, camera motion, debris, and audio-reactive effects; accessibility settings must reduce shake and flash.

## Progression

Clearing charts unlocks denser patterns, hold targets, alternating strike directions, and cosmetic tunnel themes without compromising deterministic timing.

## Art Direction

A restrained neon tunnel with black negative space, strong lane colors, emissive geometry, frequency-reactive surfaces, and crisp impact typography.

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