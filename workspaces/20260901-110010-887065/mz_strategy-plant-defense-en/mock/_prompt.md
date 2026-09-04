# Plant Defense

Build **Plant Defense**, a **lane-based tower defense strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A garden grid stands between a homestead and waves of encroaching creatures.
The player plants defenders on a multi-lane lawn, spending sunlight that must
be actively collected. Each plant type fills a tactical role — some shoot, some
block, some generate economy — and the creatures come in varieties that punish
a one-note defense. The tension is resource scarcity: sunlight arrives slowly,
plants cost real economy, and a misplaced defender means a lane falls before
reinforcements grow. An adventure map connects levels with escalating challenge
and new plant unlocks, giving the player a reason to master each tool before
the next threat arrives.

## What the Player Experiences

From the title screen the player enters an adventure map showing a trail of
levels. Selecting a level shows the upcoming creature types and lets the player
pick a loadout of plant defenders from their unlocked roster.

The level plays on a grid of lanes. Sunlight drops periodically and the player
clicks to collect it, building a resource pool. Plants are dragged from a
toolbar onto empty grid cells, each costing sunlight. Shooters fire
projectiles down their lane, walls absorb hits, and sun-producers accelerate
the economy. Creatures march from the right edge in waves, each lane
independent.

Creature variety forces adaptation: armored types shrug off weak shots, fast
types outrun slow-firing plants, and flying types bypass ground walls. Later
levels introduce night conditions where sun production drops, forcing the
player to rely on alternative economy plants.

A level is won when all waves are defeated; lost when any creature reaches the
left edge. Victory unlocks the next map node and sometimes a new plant type.
The result screen shows stars earned and the map updates visibly.

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