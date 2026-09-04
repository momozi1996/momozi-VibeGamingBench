# Chess Variant

Build **Chess Variant**, a **tactical chess game with cooldowns and terrain** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

Classic chess pieces gain special abilities on cooldown timers, and the board
itself becomes terrain — some tiles heal, some damage, some block movement.
The result is a game that rewards chess intuition but demands new tactical
thinking: a knight's fork matters less when the bishop can teleport every four
turns, and controlling the healing fountain tile can swing an endgame. A
campaign mode unlocks new pieces and abilities level by level, teaching the
player each mechanic before combining them into complex puzzles. The tone is
medieval-fantasy: stone boards, glowing runes, and pieces that feel like
enchanted warriors.

## What the Player Experiences

From the title screen the player enters a campaign map with sequential levels.
Each level is a chess puzzle or skirmish on a themed board with specific terrain
tiles and piece rosters. Early levels teach one mechanic at a time — a piece
with a dash ability, a tile that blocks, a cooldown that must be tracked.

During play the board shows terrain overlays on specific tiles: green for
healing, red for damage, grey for impassable. Pieces move by standard chess
rules but each also has a unique ability (charge, shield, teleport, area
attack) shown as a button with a cooldown counter. Using an ability consumes
the turn and starts the cooldown.

The AI opponent uses the same rules and abilities. Capturing the enemy king
wins; losing yours loses. The campaign escalates by introducing new piece types
with new abilities and more complex terrain layouts. Completing a level unlocks
the next and sometimes adds a new piece to the player's roster for future
levels.

A styled result screen shows victory or defeat with the option to retry or
advance.

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