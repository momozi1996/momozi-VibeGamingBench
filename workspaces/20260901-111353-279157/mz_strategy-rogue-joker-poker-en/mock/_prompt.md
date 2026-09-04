# Rogue Joker Poker

Build **Rogue Joker Poker**, a compact **poker-hand roguelite score-chaser** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player builds a scoring engine from poker
hands, strange jokers, and shop upgrades to beat escalating blind targets in a
single high-stakes run.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player sits at a surreal felt table trying to beat a rising sequence of
score targets using nothing but poker hands and a growing roster of bizarre
jokers. Every round is a readable tactical choice: which cards to hold, which
to discard, when to spend a hand versus fishing for a better combination, and
how the current joker lineup warps the value of a flush, straight, pair, or
high-card play. The pressure comes from limited hands and discards per round,
escalating blind targets, and boss rules that twist the scoring math. The tone
is **sleek, strange, casino-arcade, and score-hungry**: felt tables, neon chips,
animated cards, odd joker portraits, compact tooltips, and clear score math
should make the game feel designed rather than assembled from default controls.

Do not clone a named commercial game's exact UI, art, copy, card names, or
iconography. Use original terminology, jokers, rules, palette, and screen
composition while preserving the broad genre fantasy of poker scoring plus
roguelite modifiers.

## What the Player Experiences

The run opens on a styled title screen that sets the casino-arcade mood and
invites the player to begin. Once started, the player faces a sequence of
blinds with rising score targets. Each round deals a hand of cards showing
rank, suit, and selection state. The player studies the hand, selects cards to
form a poker combination, and either plays them to score or discards unwanted
cards to draw replacements, burning limited resources either way.

When a hand is played, the scoring moment unfolds visibly: the poker hand type
is identified, base chips and multiplier are calculated, and then each active
joker fires in sequence, visibly altering the math. The score animates toward
the blind target. The player watches the joker row like a machine, learning
which combinations trigger which bonuses.

Between blinds, a shop offers new jokers, deck modifications, and upgrades.
Purchases reshape the scoring engine for future rounds. The run escalates
through small blinds, big blinds, and boss blinds. Boss rounds introduce
special rules that force the player to rethink hand evaluation: a disabled
suit, a discard tax, a hand-size cap, or a reversed joker.

Victory means beating the final target. Defeat means running out of hands
below a blind. Either way, a styled result screen offers retry or return to
title.

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