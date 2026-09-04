# Keepsake

Build **Keepsake**, a quiet memory-reconstruction visual novel about sorting a
late person's belongings, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

Someone has died, and you have been asked to sort through what they left behind.
A faded photograph, a folded letter, a worn ring, a diary with a torn-out
page — each object holds a fragment of a life, and they do not give up their
meaning in order. Keepsake is a **choice-driven visual novel of reconstruction**
where the player examines the keepsakes of a stranger and, piece by piece and
out of sequence, assembles the story of who this person really was — and the
quiet secret time had buried with them.

The fantasy is **piecing together a life from the things it left behind**. The
heart of the loop is **examine, remember, connect, understand** — turning a
keepsake over, hearing the memory it stirs, and fitting it against what you have
already found until a hidden shape emerges. The order the player chooses, and
how they come to read an ambiguous choice the dead made, shape the
understanding they arrive at. It should feel like a slow, tender, melancholy
piece with real emotional weight and more than one way to understand a life, not
a single linear obituary read start to finish.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player is given their
   task — a room, a box, a life's worth of objects to sort — established as a
   quiet illustrated scene with narration that sets the mood and the absence at
   its center.
2. **Examining the Keepsakes** — The player chooses which object to take up,
   in whatever order they like, and each keepsake is examined as an illustrated
   item with the memory or fragment of the past it reveals. The room of
   belongings is something the player works through at their own pace, not a
   fixed slideshow.
3. **Fragments That Connect** — Each examined keepsake adds a remembered
   fragment to what the player knows, and fragments fit against one another:
   a date on a letter explains a photograph, an object's absence answers an
   earlier question. The player feels a life assembling out of order, and what
   they have already found colors how the next piece reads.
4. **A Choice of Understanding** — As the picture comes together the player
   reaches moments of interpretation — how to read an ambiguous decision the
   dead person made, what to believe about a secret, whether to judge or
   forgive. These choices are deliberate and remembered, and what the player has
   uncovered shapes which understandings are even available.
5. **More Than One Way to Remember** — The piece resolves into one of several
   genuinely different closing understandings — a life redeemed, a secret kept
   in kindness, a quiet grief, a truth that recasts everything — each reached
   through which fragments the player found and how they chose to read them,
   and shown as an authored, styled conclusion that names the understanding they
   came to. The player can begin again and arrive somewhere else.

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