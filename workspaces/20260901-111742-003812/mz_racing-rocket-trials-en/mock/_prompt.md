# Racing Rocket Trials

Build a Racing Rocket Trials as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A physics-based motorcycle obstacle course where precision throttle control and
body lean are everything. The rider navigates increasingly absurd ramps, loops,
seesaws, and explosive barrels across 20+ hand-crafted levels. Crashing is
spectacular — the rider ragdolls on impact, tumbling across the course in a
darkly comic display. The challenge is surgical: feathering the throttle to
climb a near-vertical wall, leaning back to clear a gap, or threading between
swinging hazards. Checkpoints are generous but the clock is merciless — medals
reward speed and flawless runs.

## What the Player Experiences

1. **Title Screen** — A grungy industrial backdrop with the game name in
   stencil-style bold font, a motorcycle silhouette mid-wheelie, and
   Play/Level Select buttons. No plain HTML grey.
2. **Level Select** — A grid of 20+ levels organized into 4 difficulty tiers
   (Easy/Medium/Hard/Extreme). Each shows medal status, best time, and a small
   preview. Levels unlock sequentially within each tier.
3. **Motorcycle Physics** — The bike has realistic 2D physics: two wheels with
   suspension, a rider body that leans. Throttle (right key) accelerates the
   rear wheel; brake (left key) slows it. Up/down keys lean the rider
   forward/backward, shifting the centre of gravity.
4. **Obstacle Variety** — Levels feature ramps, loops, seesaws, swinging
   pendulums, explosive barrels, crumbling platforms, moving platforms, and
   steep inclines. Each obstacle type has distinct visual design and physics
   interaction.
5. **Ragdoll Crash** — When the rider's body hits an obstacle or the ground at
   a bad angle, they ragdoll off the bike. The crash plays out with physics-
   driven limb movement. A "Fault" counter increments and the player respawns
   at the last checkpoint.
6. **Checkpoints** — Flags or markers placed throughout each level. Reaching
   one saves progress. The timer continues running. Fewer faults and faster
   times earn better medals.
7. **Medal and Star System** — Each level awards Gold/Silver/Bronze based on
   completion time. A "Flawless" star is awarded for zero-fault completions.
   Total medals and stars unlock later difficulty tiers.

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

Interaction scheme (keyboard-first): Use arrows or WASD plus clear Space, Enter, and Escape actions; add pointer input where it naturally improves aiming or menus.
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