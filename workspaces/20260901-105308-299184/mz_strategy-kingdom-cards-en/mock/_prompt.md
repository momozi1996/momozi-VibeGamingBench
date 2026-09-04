# Kingdom Cards

Build **Kingdom Cards**, a **card-driven kingdom management strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A small kingdom is governed entirely through cards. Each turn the player draws
a hand and plays cards to build structures, recruit soldiers, gather resources,
or launch attacks against rival lords. The deck starts bloated with weak cards;
smart play thins it, replacing chaff with powerful upgrades. Diplomacy cards
let the player negotiate truces or betray allies, adding a social layer to the
engine-building. The tension is that every card played is a card not saved for
defense, and the rivals do not wait. The tone is parchment-and-ink medieval:
cards look like royal decrees, the kingdom is a growing map of holdings, and
war is declared with a wax seal.

## What the Player Experiences

From the title screen the player starts a new campaign. The kingdom begins as
a single castle on a map with rival territories visible. Each turn the player
draws five cards from their deck and plays up to three. Build cards add
structures to the map (farms for food, barracks for troops, markets for gold).
Recruit cards add soldiers. Attack cards send armies against a rival's
territory. Diplomacy cards open negotiations.

After playing, unplayed cards can be trashed to thin the deck, or kept for
next turn's draw. New cards are gained by building specific structures or
winning battles — each acquisition is a permanent deck change.

Rivals take their turns simultaneously, expanding and attacking. The map
updates to show territory changes. Losing all territories ends the game in
defeat; controlling the entire map wins. The player must balance building
economy cards for long-term growth against military cards for immediate
survival.

A styled result screen shows the campaign outcome with territory history and
offers a new game.

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