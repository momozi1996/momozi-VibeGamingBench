# Dungeon Master

Build **Dungeon Master**, a **dungeon management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is the villain: dig rooms in the earth, fill them with traps and
monsters, and watch greedy heroes stumble in to be defeated. But monsters are
not free — they need gold to recruit, food to keep happy, and rooms that suit
their nature. Heroes arrive in waves of increasing strength, and each one that
escapes spreads word of an easy dungeon, attracting tougher adventurers. The
tension is economic: gold comes from defeated heroes' loot, but spending it all
on offense leaves nothing for creature comforts, and unhappy monsters desert.
The fantasy is running an evil enterprise where the product is doom and the
customers are uninvited.

## What the Player Experiences

From the title screen the player starts a new dungeon. The view shows a
cross-section of earth. The player digs rooms by spending gold, creating a
layout of corridors and chambers. Each room can be designated: treasure rooms
lure heroes deeper, trap rooms damage them, barracks house monsters, and
hatcheries produce food.

Monsters are recruited from a roster — each type has a gold cost, preferred
room type, and combat strength. Placing monsters in rooms they like keeps
morale high; cramming them into unsuitable spaces makes them grumpy and
eventually causes desertion. The creature happiness meter is always visible.

Heroes arrive periodically, entering from the surface and navigating toward
treasure. They fight monsters, trigger traps, and either die (dropping loot)
or escape. Escaped heroes increase the dungeon's fame, attracting stronger
parties next wave. The player must balance dungeon depth, trap density, and
monster strength against the escalating threat.

The game tracks gold, creature count, and waves survived. A styled result
screen shows dungeon statistics when the dungeon heart is destroyed by heroes
or a wave milestone is reached.

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