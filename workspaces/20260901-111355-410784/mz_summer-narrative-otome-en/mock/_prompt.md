# Otome Game

Build a complete, playable **2D narrative game** as a polished
browser vertical slice, presented from a **front facing** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Route system with affinity gates, Protagonist customization and voice, Route-specific story events, and CG gallery and completion tracking. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Route system with affinity gates**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Protagonist customization and voice**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Route-specific story events**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - CG gallery and completion tracking**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Affinity system per love interest; Route detection and lock-in system; Protagonist personality and name customization; Route-specific event sequences; CG scene gallery with unlock tracking; Good and bad ending system per route; True or secret ending unlock after route completion; Chapter select and route replay.
6. **Playable breadth and outcome**: Include at least three consequential decision points, persistent relationship or evidence state, visibly different branches, and two reachable endings with replay navigation.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Character-focused staging, expressive portraits or models, legible dialogue hierarchy, motivated transitions, and scene composition that changes with relationships and choices.

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