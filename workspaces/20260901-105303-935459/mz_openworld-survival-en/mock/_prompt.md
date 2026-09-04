# Open-World Survival

Build a **2D open-world survival game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player awakens alone in a wilderness and must gather resources, craft tools,
build shelter, and survive the night. The fantasy is **self-reliance under
pressure** -- every decision matters because daylight is finite, hunger is
constant, and the world turns hostile after dark. The interesting tension is
choosing what to prioritize: food now or tools for later, exploration or
fortification, risk or safety. Temperature drops, visibility shrinks, and
survival depends on preparation. The art style should feel **earthy, raw, and
immersive** -- think *Don't Starve* meets *A Short Hike* at a smaller scale.

## What the Player Experiences

1. **Title Screen** -- A stylised opening with the game name, a play button, and
   a wilderness backdrop (forest, campsite, or mountain vista). No naked HTML 引擎
   grey.

2. **The Wilderness** -- The player spawns in an open-world map with multiple
   visually distinct biomes: grassy plains, dense forest, and rocky terrain or
   water. The player moves freely in 8 directions across a large explorable
   space.

3. **Resource Gathering** -- Scattered across the map are interactable resources:
   trees for wood, stone outcrops for stone, and berry bushes for food. The
   player approaches a resource and interacts to gather it, with visible feedback
   (animation, particle effect, or resource disappearing).

4. **Survival Metrics** -- Status bars are always visible (hunger, thirst, or
   temperature). They drain over time. When a bar hits critical levels, the
   player suffers consequences: slowed movement, screen vignette, health loss, or
   other visible penalties.

5. **Crafting** -- A crafting panel shows available recipes that consume gathered
   materials. Recipes produce useful items: a campfire for warmth, a shelter for
   protection, an axe for faster gathering. The player sees what they can and
   cannot afford to build.

6. **Building and Placement** -- Crafted structures can be placed into the world
   as persistent objects. A campfire provides warmth and light. A shelter
   restores health or blocks environmental damage. Placement has clear visual
   indicators.

7. **Day-Night Cycle** -- Time passes automatically. Day is bright and safe.
   Night darkens the map, shrinks visibility, and accelerates survival drain.
   Being near a campfire at night extends the player's safe radius. Surviving a
   full day-night cycle is the minimal success condition.

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