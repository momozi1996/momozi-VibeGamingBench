# Dread Wings

Build **Dread Wings**, a **one-button endless flyer** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a dark cyberpunk score-chaser where a fragile metallic bird
fights gravity through an infinite corridor of industrial hazards.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player fights physics with a single input. Every tap buys a moment of lift
against relentless downward pull, threading the bird through narrow gaps that
demand precise timing and rhythm. The tension comes from the gap between what
the player sees coming and what their reflexes can execute -- each successful
pass raises the stakes because the score is now worth protecting. Death is
instant, retry is instant, and the "just one more try" loop is the entire
product. The world is a dark industrial wasteland: neon-lit pipes, smog, and
a distant ruined skyline scrolling beneath a crimson sky.

## What the Player Experiences

The player opens to a moody title screen showing their all-time best score and
a clear way to launch. Once they begin, the bird hovers in place, waiting for
the first tap. The moment input arrives, gravity takes hold and the corridor
begins scrolling. Each tap fires an upward impulse that fights the bird's
falling arc, creating a rhythmic bobbing flight path. Paired hazards scroll in
from the right with randomized vertical placement but a consistent gap size,
demanding constant micro-adjustments. Passing a hazard pair ticks the score
upward. Over time the challenge escalates -- faster scrolling, tighter margins,
or new hazard presentations keep the player adapting. Contact with any surface
ends the run immediately: the world freezes, a result panel reveals the final
score and whether a new record was set, and a single button drops the player
back to the ready state without restarting the executable. The high score
persists between sessions.

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