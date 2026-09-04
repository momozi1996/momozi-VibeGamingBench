# Battlefield of the Machine Gods

Build a complete, playable **3D strategy game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

A rookie pilot bonds with an old experimental machine and navigates conflict among corporate armies, rebels, and autonomous AI forces.

## World Parameters

Treat this as an original adaptation of a **scifi** shared world with **huge** scope and a **survival** tone. Do not reproduce commercial characters, names, lore, logos, or protected visual designs.

## Required Playable Systems

1. **System 1** - Explore at least three connected districts or territories from Battlefield of the Machine Gods, each with distinct opportunities, hazards, and ownership state.
2. **System 2** - Complete jobs through negotiation, trade, tactical conflict, or service to earn reputation with transparent gain and loss rules.
3. **System 3** - Manage at least three factions whose trust, hostility, alliances, and control change after persistent player choices.
4. **System 4** - Balance health, resources, influence, and attention while territory events continue to evolve without waiting for the player.
5. **System 5** - Persist reputation, faction relations, owned or protected locations, depleted resources, and unresolved consequences across the whole run.
6. **System 6** - Reach a playable influence milestone that combines territory, faction, resource, and reputation systems, then support continued play or a scored conclusion.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

A scan-friendly tactical field, distinct roles, visible ranges and ownership, restrained effects, and information hierarchy for repeated decisions.

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