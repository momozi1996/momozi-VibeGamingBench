# Final Audition at Aurora Studio

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A supernatural exploration game set across an abandoned film studio. The player is an actor summoned for one final audition and must traverse connected sound stages where unfinished scenes replay themselves and the studio evaluates every performance.

## Required Playable Systems

1. **System 1** - Explore a studio backlot with at least three themed stages, backstage corridors, prop storage, and unlockable shortcuts.
2. **System 2** - Perform interactive audition scenes by hitting movement, dialogue, lighting, and camera marks in the correct dramatic sequence.
3. **System 3** - Manipulate rotating sets, spotlights, curtains, and practical effects to reveal paths and appease or provoke the studio presence.
4. **System 4** - Meet spectral cast members with distinct motives and recover production notes that alter scene objectives.
5. **System 5** - Track composure and audience approval; mistakes should distort sets, summon hazards, or rewrite the current scene.
6. **System 6** - Complete a final live take that combines previous mechanics and branches according to the roles and truths the player accepted.

## Progression

Successful takes earn role tokens that unlock new stage controls, costumes with abilities, and access to the sealed director's wing.

## Art Direction

Decaying golden-age cinema with dusty spotlights, velvet reds, monochrome projections, painted backdrops, and theatrical supernatural transitions.

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