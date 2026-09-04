# Strategy: Tower-Defense

Build a **2D Tower-Defense Game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a field commander staring down a map of chokepoints and open
ground, watching a tide of hostiles pour along fixed corridors toward a
vulnerable endpoint. The only tool is a handful of deployable defenders and a
ticking resource clock. The fantasy is **spatial puzzle-solving under escalating
pressure** -- every tile placement is a commitment, every wave ratchets the
stakes, and the interesting tension is that resources spent now on a safe pick
could have been saved for a desperate answer later. The pressure comes from
reading the next wave's composition, choosing where to invest scarce Deployment
Points, and deciding whether to shore up a crumbling lane or gamble on a
high-cost unit that might turn the whole map. The risk is always that one
misread wave or one greedy save leaves the line too thin and enemies pour
through before the next DP tick arrives.

## What the Player Experiences

1. **Title and Campaign Entry** -- A cold, industrial title screen sets the tone.
   The player starts fresh or loads a save, then enters a stage-select map
   showing available missions, each hinting at the enemy composition and
   difficulty ahead.

2. **Deployment Phase** -- Inside a stage the player sees a grid battlefield with
   clearly marked paths, deployable tiles, and a base endpoint. DP ticks upward
   over time. The player drags unit cards from a hand onto legal tiles; each
   placement costs DP and commits a defender to that position. Invalid spots or
   insufficient funds refuse cleanly.

3. **The Assault** -- Enemies surge along the fixed path in discrete waves. Each
   wave is stronger or stranger than the last -- faster scouts, armored brutes,
   flying threats that bypass blockers. Defenders auto-attack within range,
   blockers hold the line, and the player watches HP bars tick down on both
   sides. Deaths remove units from the field; leaks chip away at the base's
   life total.

4. **Escalation and Adaptation** -- Later waves demand answers the opening
   roster cannot provide alone. The player weighs upgrades, repositions
   priorities, and stretches DP across competing needs. The map becomes a living
   puzzle of overlapping ranges and shifting pressure points.

5. **Resolution** -- The final wave breaks against the defense and victory is
   declared, or the base's life hits zero and defeat is acknowledged. Clearing
   a stage marks progress and unlocks the next. The player can retry, return to
   stage select, or quit to title without relaunching.

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