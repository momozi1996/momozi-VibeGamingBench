# Voxel Tower Defense

Build a complete, playable **3D strategy game** as a polished browser vertical slice.

## Core Vision

A bright voxel tower-defense game on a miniature island. Players place and upgrade towers while enemies use A* to route around terrain and legal obstacles, creating a tactical relationship between construction and path shape.

## Required Playable Systems

1. **System 1** - Allow pointer-based tower placement on a voxel grid with ghost previews, range indicators, cost checks, smoke particles, and a landing bounce.
2. **System 2** - Move enemies with A* pathfinding from spawn to base, recalculating legal routes after placement and rejecting constructions that fully block the path.
3. **System 3** - Implement at least three tower types with distinct targeting, laser or projectile behavior, damage roles, cooldowns, and upgrade branches.
4. **System 4** - Run multiple waves with several enemy types, escalating stats, rewards, base health, victory, defeat, pause, and speed controls.
5. **System 5** - Add destructible or changing terrain, branching lanes, and tactical tiles that influence range, speed, or damage.
6. **System 6** - Create volumetric-looking hit and death explosions, readable health feedback, economy UI, and a complete results/retry flow.

## Progression

New islands introduce route constraints, tower synergies, enemy resistances, and persistent unlock choices across a short campaign.

## Art Direction

A polished pastel voxel diorama with lush terrain, toy-like towers and enemies, crisp laser lines, chunky smoke, and colorful volumetric explosions.

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