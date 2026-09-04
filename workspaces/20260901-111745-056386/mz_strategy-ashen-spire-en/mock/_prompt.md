# Strategy: Ashen Spire

Build **Ashen Spire**, a compact **dark-fantasy roguelike deckbuilding card
battler** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is climbing a cursed tower one floor at a time with nothing but a
thin deck of cards and whatever you scavenge along the way. Each combat is a
small tactical puzzle: energy is scarce, the enemy telegraphs its next move, and
every card played reshapes the odds for the rest of the run. The interesting
tension is that the deck is both your weapon and your liability -- adding
powerful cards dilutes consistency, while staying lean means fewer answers to
escalating threats. The pressure comes from reading enemy intent, rationing
energy across attack and defense, and gambling on which reward cards will pay off
three fights from now. The risk is always that one greedy pick or one misread
intent leaves you one hit from death with no block in hand.

## What the Player Experiences

The player arrives at a dark, atmospheric title screen that sets the tone of a
grim tower ascent. Starting a run reveals a branching route map -- a web of
nodes stretching upward toward a final confrontation, with forks that force the
player to choose which dangers to face and which to skip.

Entering a combat node drops the player into a turn-based card duel. A small
hand is drawn, energy refills, and the enemy displays what it intends to do next
turn. The player spends energy playing cards -- strikes that chip away at the
enemy, guards that raise a shield, and stranger tactical effects that poison,
burn, draw extra cards, or bend the rules. When the hand is spent or the player
is satisfied, ending the turn lets the enemy act, then a fresh hand is drawn and
the cycle repeats.

Winning a fight offers a choice of new cards to weave into the deck, each with
its own identity and cost. The map updates, the player picks the next node, and
the deck grows richer and riskier with every floor. Different encounters reveal
different pixel monsters with distinct silhouettes and behaviors, so no two
climbs feel identical.

The run resolves at the top: defeat the boss and a styled victory screen
celebrates the climb, or fall to zero health anywhere along the way and a defeat
screen marks how far you got. Either way, the player can retry or return to the
title without restarting the application.

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