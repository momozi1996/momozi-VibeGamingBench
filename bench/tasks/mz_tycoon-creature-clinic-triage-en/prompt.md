# Creature Clinic Triage

Build **Creature Clinic Triage**, a compact **creature-care clinic simulation**
as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player runs a tiny fantasy veterinary clinic during a busy shift. Creatures
arrive faster than they can be treated, each carrying visible ailments that hint
at what they need. The core tension is triage under pressure: which patient do
you attend first, where do you send them, and what happens to the ones still
waiting? Correct reads and smart routing keep the clinic humming and build
reputation; mistakes, delays, or mismatches cost health and trust.

The tone is warm but operational. The clinic floor should feel alive with
queuing creatures, busy stations, and clear feedback when things go right or
wrong. Avoid spreadsheet aesthetics; make it feel like a working fantasy
infirmary.

## What the Player Experiences

The player opens to a themed clinic entrance and begins a shift. Patients start
filing in, each a distinct creature with visible symptoms and an urgency
indicator. Early arrivals are straightforward — one clear ailment, one obvious
destination. The player learns the rhythm: inspect, decide, route.

As the shift continues, the queue grows. New creature types appear with
unfamiliar or combined symptoms. Stations fill up or run low on supplies.
The player must now prioritize: stabilize the critical case or clear the easy
ones to free capacity? A wrong routing wastes time and worsens the patient.
Ignoring urgency lets conditions deteriorate.

Late in the shift, pressure peaks — emergencies, compound cases, resource
scarcity. The player juggles capacity against urgency, making rapid imperfect
decisions. When the shift ends, a results summary reflects how well they
managed: creatures healed, creatures lost, reputation earned, and whether
they unlocked harder shifts or upgrades.

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
