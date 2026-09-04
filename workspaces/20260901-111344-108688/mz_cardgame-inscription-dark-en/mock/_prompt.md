# Cardgame Inscription Dark

Build a Cardgame Inscription Dark as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A dark and atmospheric card battle game where creatures are summoned by
sacrificing other creatures. The player places cards on a grid battlefield,
but powerful cards demand blood — weaker creatures must be sacrificed to fuel
stronger summons. Each card bears sigils (passive abilities) that create
emergent interactions: a card with "Airborne" flies over blockers; one with
"Bifurcated Strike" hits two lanes. An overworld map connects encounters with
branching paths, and a creeping meta-narrative unfolds through environmental
storytelling. The fantasy is the unsettling thrill of sacrificing your own
creatures for power, wrapped in a cabin-horror atmosphere.

## What the Player Experiences

1. **Title Screen** — A dimly lit wooden table with the game name scratched
   into the surface in rough lettering, a flickering candle, and a "Begin"
   card the player clicks. No plain HTML grey.
2. **The Table** — Battles take place on a 4-lane grid. The player's row faces
   the opponent's row. Cards are played from hand into lanes. Each card has
   attack power, health, a blood cost, and zero or more sigils.
3. **Sacrifice Mechanic** — To play a card costing 2 blood, the player must
   first sacrifice 2 of their own creatures already on the field. Sacrificed
   creatures die with a visual effect. Free cards (0 cost) serve as sacrifice
   fodder. This creates a constant tension between board presence and power.
4. **Sigils** — At least 8 distinct sigils with unique icons: Airborne (attacks
   directly), Bifurcated Strike (hits adjacent lanes too), Mighty Leap (blocks
   Airborne), Stinky (adjacent enemies lose 1 attack), Unkillable (returns to
   hand on death), Fledgling (evolves after 1 turn), Touch of Death (kills
   anything it damages), Many Lives (has 3 extra lives).
5. **Damage Scale** — A balance scale tips as damage is dealt. When one side
   takes 5 more total damage than the other, that side loses. The scale
   visually tips with each hit, creating tension as it approaches the tipping
   point.
6. **Overworld Map** — Between battles, a branching path map shows nodes:
   card battles, totem poles (add a sigil to a card), campfires (merge two
   cards), and traders (buy/sell cards). The player chooses their route.
7. **Atmosphere** — Dark, muted colour palette. Cards look hand-drawn on
   parchment. The opponent is a shadowy figure whose eyes glow. Ambient
   effects (dust motes, candle flicker) reinforce the unsettling mood.

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