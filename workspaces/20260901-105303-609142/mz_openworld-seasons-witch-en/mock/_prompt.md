# Open-World Seasons Witch

Build an **Open-World Seasons Witch** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a witch who controls the seasons in a small valley, shifting between
spring, summer, autumn, and winter to solve problems and help villagers. The
fantasy is elemental mastery: freezing a river to cross it, blooming flowers to
attract bees for honey, melting snow to reveal buried items, or withering vines
blocking a path. Tension comes from villager requests that require specific
seasonal combinations and potion ingredients that only grow in certain seasons.
Each season transforms the entire world visually and mechanically.

## What the Player Experiences

1. **Title Screen** — A four-panel title showing the same valley in each season,
   with the game name in flowing script. A play button surrounded by seasonal
   icons.
2. **The Valley** — The player moves freely through a valley with a village,
   forest, lake, mountain path, and farmland. The entire world changes appearance
   based on the active season.
3. **Season Switching** — The player can cast a season spell to change the world.
   A radial menu shows four seasons; selecting one triggers a visual transition
   that transforms terrain, water, vegetation, and sky colour.
4. **World Reactions** — Each season has mechanical effects: winter freezes water
   and reveals ice caves; spring grows plants and fills rivers; summer dries
   swamps and ripens fruit; autumn drops leaves revealing hidden paths and
   weakens wooden structures.
5. **Villager Quests** — NPCs in the village request help that requires seasonal
   manipulation: a farmer needs rain (spring) then sun (summer) for crops; a
   builder needs frozen lake (winter) to transport stone; a healer needs autumn
   mushrooms.
6. **Potion Brewing** — Ingredients gathered in different seasons combine into
   potions at the witch's cottage. Potions grant abilities: speed boost, barrier
   shield, creature charm. A recipe book tracks discovered combinations.
7. **Progression** — Completing quests earns reputation and unlocks new areas of
   the valley. The mountain pass opens after helping enough villagers, revealing
   a final challenge that requires mastery of all four seasons.

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