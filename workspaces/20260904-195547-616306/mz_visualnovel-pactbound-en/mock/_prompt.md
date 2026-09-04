# Pactbound

Build **Pactbound**, a summoner pact-choice visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a summoner walking a road lined with spirits and monsters, and each one
offers the same dangerous bargain: a pact. Bind it and gain its power, but carry
its price and its loyalties; refuse it and stay clean but weaker; deceive it and
risk what comes due later. Pactbound is a **choice-driven visual novel** where
the player meets a procession of would-be familiars and decides which to bind,
and the **collection of pacts they carry becomes who they are** — shaping which
factions trust them, which paths open, and how the journey ends.

The fantasy is **defining yourself by the bargains you make**. The heart of the
loop is **meet, weigh, bind or break** — encountering a spirit with its own
nature and cost, judging what a pact with it would make of you, and committing
to a bargain the story remembers. A summoner bound to gentle hearth-spirits
walks a different road than one who collected demons, and the writing should make
those allegiances felt. It should play like an atmospheric journey with real
stakes and genuinely different endings, not a linear tour with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player sets out as a
   summoner and is introduced to the road ahead and the bargain at the heart of
   the world, presented as illustrated scenes with characters and narration.
2. **Spirits with Their Own Nature** — Along the way the player meets a variety
   of would-be familiars — a loyal hearth-spirit, a proud beast, a whispering
   demon, and others — each with its own voice, temperament, the power it
   offers, and the price it asks. Encounters feel like meeting distinct
   characters, not picking from an identical list.
3. **Bind, Refuse, or Deceive** — At each spirit the player makes a real choice:
   seal a pact and take on its power and its loyalties, refuse and stay
   unbound, or strike a false bargain with consequences down the line. The
   decision is deliberate and clearly registered, and the player can see what
   they have bound to themselves.
4. **Pacts That Define You** — The pacts the player carries are **remembered and
   accumulate into an identity**: which factions and spirits trust or revile the
   player, which options and dialogue open up, and which later encounters and
   endings become reachable all depend on the company they keep. A choice made
   early should visibly shape a scene much later.
5. **A Journey That Ends Many Ways** — The road resolves in one of several
   genuinely different endings — crowned among monsters, a champion of the
   unbound, a betrayer alone, or a peacemaker between worlds — each reachable
   through the pacts and choices the player made, and shown as an authored,
   styled conclusion that names what they became. The player can set out again
   to bind a different fate.

## Vibe Gaming Quality Bar

The gameplay, logic, and acceptance anchors above take priority over this
presentation contract. Do not rewrite or remove the core mechanics above; use
these rules to turn the same brief into a playable Vibe Gaming vertical slice.

- **Play first, polish second:** establish start, core input, state changes,
  success/failure, and replay before adding visual polish or effects.
- **Choose the smallest sufficient stack**:
  - `HTML5 Canvas 2D + Vanilla JS` for 2D rule-driven games;
  - `DOM + CSS + Vanilla JS` for card, dialogue, menu, and information-heavy games;
  - `pure SVG + CSS animation + Vanilla JS` for icons, diagrams, and geometric motion;
  - `PhaserJS` for continuous collision, cameras, particles, or arcade physics;
  - `Three.js + WebGL` for 3D or spatial camera experiences;
  - native `WebGPU` only when large-scale GPU parallelism or a custom GPU pipeline is genuinely required;
  - Canvas, DOM, CSS, and SVG may be mixed when each layer has a clear responsibility.
    Do not add complexity for technology spectacle.
- **Keep rules independent:** `game_logic.js` is the single source of truth and
  exposes `createGame(opts)` and `advance(game, input, dt)`. Rendering reads state;
  it must not maintain a second hidden rules system.
- **Make every frame explainable:** inputs map to explicit actions, actions
  produce observable state changes, and invalid input, edge cases, resource
  depletion, damage, victory, and failure are visible.
- **Vibe is not decoration:** use at least two feedback channels (animation,
  motion, scale, particles, audio, HUD, or camera) for important actions without
  obscuring the goal or reducing readability.
- **Mobile first:** pointer targets are at least 44×44 CSS px, touch and mouse
  both work, hover is never required, and 390×844, 360×800, 430×932, and
  1280×800 have no horizontal scrolling or overlapping controls.
- **Determinism and tests:** seed random content; verify the core rule, outcome
  conditions, restart/restoration, input boundaries, and at least one error state.
  Do not treat a screenshot or visible label as proof of functionality.
- **Originality and compliance:** use original names, characters, graphics,
  audio, and levels, or explicitly licensed assets. Do not copy trademarks,
  characters, text, artwork, music, level data, or source code.

Finish by reporting actual file paths, launch and test commands/results, key
screenshots, known limitations, stack tradeoffs, and original-asset provenance.

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