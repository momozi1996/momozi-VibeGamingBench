# AI Agent Evolution Lab

Build a complete, playable **3D simulation game** as a polished browser vertical slice.

## Core Vision

A controlled 3D behavioral sandbox inside a transparent glass habitat. Several autonomous agents sense resources, hazards, temperature, and gravity; the player changes the environment and runs scored experiments to observe adaptation rather than watching random motion.

## Required Playable Systems

1. **System 1** - Simulate multiple autonomous agents with visible goals, sensing range, energy, memory, and behavior-state transitions such as explore, seek, avoid, rest, and cooperate.
2. **System 2** - Let players adjust temperature, gravity magnitude and direction, resource density, hazard level, and time scale with responsive controls.
3. **System 3** - Click an agent to inspect its current perception, target, energy, recent decisions, and trajectory, highlighting sensed objects in the habitat.
4. **System 4** - Display live charts for entropy, population energy, movement diversity, collisions, resource use, and agent-state distribution.
5. **System 5** - Provide repeatable experiment scenarios with hypotheses and success conditions, plus seeded reset and side-by-side result comparison.
6. **System 6** - Make environmental changes visibly affect trajectories and group behavior without instantly teleporting or directly scripting agents.

## Progression

Completed experiments unlock new sensors, agent traits, environment presets, and more complex multi-variable research objectives.

## Art Direction

A clean scientific glass-box diorama with soft laboratory lighting, distinct agent colors, translucent sensor cones, plotted trajectories, and precise dashboard graphics.

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