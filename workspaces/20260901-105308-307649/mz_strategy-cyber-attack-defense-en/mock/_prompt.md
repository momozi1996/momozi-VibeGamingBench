# Cyber Attack Defense

Build a complete, playable **3D strategy game** as a polished browser vertical slice.

## Core Vision

A 3D network-defense action strategy game. Red attack packets travel through a topology toward a central server; the player intercepts threats, hardens nodes, and reads a visual prediction model to survive escalating coordinated attacks.

## Required Playable Systems

1. **System 1** - Build a readable 3D topology with a core server, relay nodes, routes, normal traffic, and multiple attack packet types moving along paths.
2. **System 2** - Let the player click packets or nodes to intercept, quarantine, reroute, or detonate threats using cooldown-limited defensive tools.
3. **System 3** - Visualize a Kalman-filter-inspired prediction layer that estimates future packet paths and updates uncertainty as observations arrive.
4. **System 4** - Run discrete waves with decoys, split packets, armored payloads, compromised nodes, and a final coordinated boss attack.
5. **System 5** - Add node upgrades, firewall placement, resource income, combo scoring, server health, and meaningful tradeoffs between active and passive defense.
6. **System 6** - Pair every intercept, miss, prediction update, and node failure with distinct 8-bit synthesized audio and visible feedback.

## Progression

Later waves expand topology complexity and unlock specialized defenses while enemy behaviors adapt to overused strategies.

## Art Direction

A high-contrast cyber operations space with luminous topology lines, volumetric packet trails, green code rain, red threat pulses, and pixel-audio visualizers.

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