# Sports Manager

Build a complete, playable **2D racing and sports game** as a polished
browser vertical slice, presented from a **top down** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Squad and contract management, Match simulation with tactical input, Transfer market and scouting, and Finance and board management. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Squad and contract management**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Match simulation with tactical input**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Transfer market and scouting**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Finance and board management**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Player and staff database with attributes; Contract and wage negotiation system; Transfer market with AI club competition; Scouting and player discovery system; Training system with development modeling; Tactical formation and instruction editor; Match simulation engine; Season and fixture calendar.
6. **Playable breadth and outcome**: Include a complete event with practice or setup, at least three competitors or challenge tiers, rule-valid scoring, escalating pressure, final standings, and replay.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Strong speed and trajectory cues, readable competitors, clear field markings, dynamic cameras, and replay-worthy finish, collision, and scoring moments.

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