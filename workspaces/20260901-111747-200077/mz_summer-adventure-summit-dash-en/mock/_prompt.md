# Summit Dash

Build a complete, playable **2D adventure and exploration game** as a polished
browser vertical slice, presented from a **side scrolling** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Precision platformer controller, Screen transition and checkpoint system, Collectible and completion tracking, and Configurable assist mode. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Precision platformer controller**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Screen transition and checkpoint system**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Collectible and completion tracking**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Configurable assist mode**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Precision controller: eight-directional dash, wall climb with stamina, coyote time, input buffering; Screen-based level system with instant respawn on death; Strawberry collectibles on optional challenge paths; challenge tapes unlocking harder chapter variants; Crystal heart secret collectibles; Assist mode: game speed, dash count, stamina, invincibility toggles; Death counter per chapter and total; Chapter completion tracking with percentage.
6. **Playable breadth and outcome**: Build at least three connected locations with distinct discoveries, one optional route, an escalating objective chain, and a final resolution changed by player actions.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Authored landmarks, layered routes, environmental storytelling, clear interaction highlights, and lighting that guides exploration without flattening the scene.

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