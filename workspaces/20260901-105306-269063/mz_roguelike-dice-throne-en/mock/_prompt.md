# Dice Throne

Build **Dice Throne**, a dice-rolling roguelike with reroll mechanics and
equipment that modifies die faces as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

A warrior battles through a dungeon using dice as their combat system. Each
turn the player rolls a set of dice, then chooses which to keep and which to
reroll (up to two rerolls). Die faces map to abilities: swords deal damage,
shields block, hearts heal, and skulls trigger special attacks. The twist:
equipment found in the dungeon physically modifies die faces — a flame sword
replaces one sword face with a fire-sword that deals double damage, enchanted
armor adds a shield face to a die. The enemy rolls visible dice too, creating
a transparent contest where both sides see what is coming. Building a set of
dice with synergistic faces is the meta-progression within each run.

## What the Player Experiences

A title screen shows dice tumbling with glowing face icons. Starting a run
gives the player 5 standard dice (each with sword, sword, shield, heart,
skull, blank faces).

In combat, the player rolls all dice simultaneously with a satisfying tumble
animation. Results land face-up. The player selects dice to keep (they lock in
place) and rerolls the rest — up to two rerolls per turn. After finalizing,
faces activate: swords deal damage to the enemy, shields reduce incoming damage,
hearts heal, skulls trigger a special ability. The enemy then rolls their own
visible dice and resolves similarly.

Between encounters, loot screens offer equipment that modifies die faces —
replacing, upgrading, or adding faces. A map shows branching paths with combat,
elite, shop, and rest nodes. Shops sell face modifications and new dice. The
run ends at a boss with powerful custom dice. Death shows floor reached, best
roll, and equipment collected.

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