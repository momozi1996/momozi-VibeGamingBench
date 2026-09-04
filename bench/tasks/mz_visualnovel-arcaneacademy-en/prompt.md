# Arcane Academy

Build **Arcane Academy**, a magic-school stat-raising visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a first-year at a school of magic, and a term is short. There is never
enough time to master everything, so what you choose to study — elemental
sorcery, runecraft, alchemy, the tempting forbidden arts — slowly shapes the
mage you become. Arcane Academy is a **stat-raising visual novel**: between
story beats the player spends limited time and effort training different
disciplines, and the magician they grow into decides how classmates and
mentors treat them, which paths open, and how the term ends.

The fantasy is **becoming someone through the choices of a single term**. The
heart of the loop is **plan, train, live the consequences** — deciding where to
invest scarce time, watching abilities rise, and then meeting story moments
where who you have become matters as much as what you say. A student who poured
everything into forbidden magic walks a different road than a diligent
runescribe, and the writing should make that growth felt. It should play like a
warm, atmospheric school story with real stakes and genuinely different
outcomes, not a linear tour with a single ending.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player arrives at the
   academy and is introduced to the term ahead, the disciplines they might
   study, and the classmates and mentors around them, presented as illustrated
   scenes with characters and narration.
2. **Planning the Term** — Across the term the player repeatedly decides how to
   spend limited time and energy, choosing which magical disciplines to train.
   Time is scarce, so investing in one pursuit means neglecting another, and the
   player feels the weight of the trade-off.
3. **Growth That Shows** — Training visibly raises the player's abilities, and
   that progress is something the player can read and care about. The mage they
   are building takes shape over the term rather than staying fixed.
4. **Story Beats That Test You** — Between training, authored story scenes
   unfold — a rivalry, a mentor's offer, a forbidden temptation, a crisis at the
   school — where the player makes meaningful choices. What the player has
   trained matters here: some options, lines, or events are only available to a
   mage who built the right strengths, so growth and choice intertwine.
5. **A Term That Ends in Many Ways** — The term resolves in one of several
   genuinely different endings — honored graduate, fallen to the forbidden arts,
   expelled in disgrace, or the keeper of a hidden truth — each reachable
   through how the player trained and chose, and shown as an authored, styled
   conclusion that names what they became. The player can begin a new term to
   grow into someone else.

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
