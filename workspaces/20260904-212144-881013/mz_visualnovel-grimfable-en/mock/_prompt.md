# Grim Fable

Build **Grim Fable**, a branching dark-fairytale visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You step into fairy tales you think you already know — but the woods are darker
than you remember, the kind are not always good, and the wicked may have their
reasons. Grim Fable is a **choice-driven visual novel** where the player relives
familiar storybook tales as their protagonist, yet the choices on offer were
never in the original telling. What looks like a bedtime story hides an uneasy
truth, and the player's decisions decide which version of that truth comes to
pass.

The fantasy is **rewriting a story you assume you know**. The game should turn
the player's own expectations into the trap: a beloved tale opens the familiar
way, then forks toward outcomes the fairy tale never allowed. The heart of the
loop is **read, examine, weigh, decide** — taking in a richly written scene,
looking closely at what the illustration is hiding, sizing up who and what to
trust, and committing to a choice that the story remembers and pays off later.
It should feel like turning the pages of a haunted picture book where text,
portraits, backdrops, and choice menus all belong to the same authored world.
This is a polished, atmospheric storybook with real stakes and genuinely
different endings, not a linear text dump with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player begins the tale and
   is eased into a familiar fairy-tale premise, presented as an illustrated
   storybook scene with characters, narration, and a clear sense of who they
   are and where they stand.
2. **Reading & Examining the Scene** — The story unfolds through paced dialogue
   and narration over illustrated backdrops, but the scene is not just read — it
   invites investigation. Props, details of the setting, and the characters
   present can hide narration, clues, or secrets the player would otherwise
   miss, so the comforting tale's darker underside is something the player
   uncovers, not just something told to them.
3. **Clues That Add Up** — What the player examines and learns is **gathered and
   remembered**: a blood-flecked knife noticed on a table, a confession teased
   out of a character, a detail that contradicts the storybook version. These
   discoveries accumulate into the player's understanding and unlock or color
   the choices and revelations that follow, rewarding a curious player who looks
   closely over one who rushes ahead.
4. **Meaningful Choices** — At key moments the player is offered choices that
   the original story never gave them — whom to trust, what to reveal, which
   path to take through the wood. Choices are deliberate decisions with stakes,
   not cosmetic flavor; what the player has uncovered shapes which options are
   available and what they mean, and the game makes clear that a decision has
   been made and registered.
5. **Consequences That Stick** — Earlier choices are remembered and shape what
   comes later: which characters confide in the player, what truths surface,
   and which doors close. The player should feel the story bending around their
   decisions rather than running on rails, and recurring tales or returning
   characters should reflect what the player did before.
6. **Divergent Endings** — The tale resolves in one of several genuinely
   different endings — a subversion of the happy ending, a grim reckoning, a
   hidden truth uncovered, or a quiet escape — each reachable through different
   choices and clearly tied to how the player played. The ending is an authored,
   styled conclusion that names what the player's path brought about, and the
   player can begin again to seek a different one.

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