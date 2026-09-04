# Word Spell

Build **Word Spell**, a word-forming spell-casting roguelike with letter tiles
and encounters as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A wizard battles through a dungeon by casting spells formed from letter tiles.
Each turn the player has a hand of letter tiles and must form a word — longer
words deal more damage, and specific letter combinations trigger elemental
effects (words containing "fire" deal burn damage, "ice" freezes, "heal"
restores health). Between encounters the player collects new letter tiles,
upgrades existing ones (a golden "E" scores double), and removes weak letters
from their pool. Enemies have visible health and telegraph attacks with a
countdown. The tension is vocabulary under pressure: finding the longest,
most synergistic word from a random hand before the enemy strikes.

## What the Player Experiences

A title screen shows letter tiles arranged into a spell effect. Starting a run
gives the player a starting pool of 20 common letter tiles.

In combat, 7 tiles are drawn from the pool. The player drags tiles onto a
spelling bar to form a word, then casts it. Valid words deal damage proportional
to length (3 letters = weak, 7 letters = devastating). Special letter combos
trigger bonus effects shown as elemental icons. Invalid words fizzle and waste
the turn. After casting, the enemy attacks (damage shown in advance as a
countdown number).

Between encounters, a reward screen offers new tiles (including rare consonants
and vowels with bonus effects), tile upgrades, or tile removal. A map shows
branching paths with combat nodes, rest nodes (heal), and shop nodes (buy/sell
tiles). The run ends at a boss with high health requiring multiple strong words.
Death shows a score based on floor reached and longest word cast.

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