# Cardgame Poker Roguelike

Build a Cardgame Poker Roguelike as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A roguelike scoring game built on poker hand evaluation. The player is dealt
cards and must form poker hands (pairs, straights, flushes) to score points
against escalating blind targets. The twist: collectible Joker cards modify
scoring rules in wild ways — one might triple the value of all hearts, another
might make every pair count as a full house. Between rounds, a shop sells new
Jokers, card enhancements, and consumable items. The fantasy is discovering
absurd scoring combos that turn a humble pair of twos into a million-point
hand. Fail to meet the blind and the run ends.

## What the Player Experiences

1. **Title Screen** — A casino-noir aesthetic with the game name in gold
   embossed lettering on green felt, animated card shuffling in the background,
   and New Run / Stats buttons. No plain HTML grey.
2. **The Hand** — The player is dealt 8 cards from a standard deck. They select
   up to 5 cards to form a poker hand and submit it for scoring. Remaining
   cards can be discarded and redrawn (limited discards per round).
3. **Scoring** — Each hand type has a base chip value and multiplier (e.g.,
   Pair = 10 chips x2, Flush = 35 chips x4). Jokers and enhancements modify
   these values. The score animates with each modifier applied sequentially,
   building dramatic tension.
4. **Blinds** — Each round has a target score (the blind). Small Blind, Big
   Blind, and Boss Blind escalate. The player has multiple hands per round to
   meet the target. Failing to reach the blind ends the run.
5. **Joker Cards** — Up to 5 Joker slots. Each Joker has a unique rule-bending
   effect with illustrated art and a description. Jokers are purchased from
   the shop or earned from Boss Blinds. Synergies between Jokers create
   exponential scoring potential.
6. **Shop** — Between rounds, spend earned money on new Jokers, card
   enhancements (foil, holographic, polychrome — each with scoring bonuses),
   vouchers (permanent upgrades), or booster packs (new playing cards).
7. **Boss Blinds** — Special blinds with debuff conditions (e.g., "all clubs
   are face-down", "no discards this round", "first hand played is
   debuffed"). The player must adapt their strategy to the boss condition.

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