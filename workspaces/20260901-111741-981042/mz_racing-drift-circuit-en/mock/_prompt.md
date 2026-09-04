# Racing Drift Circuit

Build a Racing Drift Circuit as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A precision time-trial racing game where mastering the drift is everything. The
player pilots a car through tight circuits, initiating controlled drifts around
corners to maintain speed. Each track is a puzzle of racing lines — brake too
early and you lose seconds; drift too wide and you clip the barrier. Ghost
replays of your best run haunt every attempt, pushing you to shave milliseconds.
A medal system (Gold/Silver/Bronze) across 10+ tracks provides clear progression
goals, and the satisfaction of a perfect drift chain through a complex chicane
is the core reward.

## What the Player Experiences

1. **Title Screen** — A dynamic menu with the game name in speed-styled italic
   font, a blurred track in the background with a ghost car drifting past, and
   buttons for Campaign and Time Trial. No plain HTML grey.
2. **Track Select** — A grid of 10+ tracks with preview thumbnails, medal
   status (empty/bronze/silver/gold), and best time displayed. Tracks unlock
   sequentially by earning at least bronze on the previous track.
3. **Driving Feel** — Top-down or angled-top view. The car accelerates smoothly,
   brakes with visible deceleration, and steers with momentum. Holding a drift
   key while turning initiates a drift: the car slides sideways with tyre smoke
   particles trailing behind.
4. **Drift Boost** — Maintaining a drift builds a boost meter. Releasing the
   drift at the right moment grants a speed burst with a visible flame/trail
   effect. Longer drifts yield bigger boosts but risk hitting walls.
5. **Ghost Replay** — A translucent ghost of the player's best lap drives
   alongside them in real time. The ghost is clearly distinguishable (different
   colour, slight transparency) and shows exactly where time is being gained
   or lost.
6. **Medal System** — Each track has Gold/Silver/Bronze time thresholds shown
   before the race. Finishing awards the appropriate medal with a podium
   animation. Medals are tracked on the track select screen.
7. **Track Variety** — Tracks range from simple ovals to complex circuits with
   hairpins, chicanes, elevation changes (visual only), and varying widths.
   Each track has a distinct visual theme (city, desert, forest, night).

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