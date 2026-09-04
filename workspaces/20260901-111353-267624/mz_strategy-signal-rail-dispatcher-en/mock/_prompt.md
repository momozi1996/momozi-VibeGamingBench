# Signal Rail Dispatcher

Build **Signal Rail Dispatcher**, a compact 2D railway signal and routing
management game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

The player is a lone dispatcher in a cramped signal box, watching colored
trains crawl across a schematic board and making split-second routing calls
that ripple forward in time. Every switch flip commits a path; every red signal
buys thinking room at the cost of punctuality. The fantasy is **quiet mastery
under mounting pressure** — a timetable that starts gentle, then stacks
conflicting services until the board is a web of near-misses and the player
must think several moves ahead to keep everything flowing. The best version
feels like a control-room puzzle where one wrong toggle cascades into delay,
and a clean shift feels earned.

## What the Player Experiences

1. **The Shift Begins** — A styled title screen sets the tone of a railway
   control room. The player starts a shift and sees a compact track diagram
   with stations, sidings, signals, and switchable junctions laid out like a
   schematic map.
2. **Reading the Board** — Trains appear at entry points and crawl along the
   tracks. Each train has a visible identity — color, service type, destination
   — and the timetable or HUD tells the player where it needs to go and when.
   Signals glow red or green; switches show which way they are set.
3. **Routing Decisions** — The player clicks signals to hold or release trains,
   and flips switches to redirect paths. A released train follows the set route
   until it hits the next red signal or reaches its destination. The challenge
   is sequencing: two trains cannot safely share a section, and letting one
   through means another waits.
4. **Escalation** — The shift intensifies. More trains arrive, express services
   demand priority, delays compound, and blocked sections force creative
   rerouting. Conflict warnings or occupancy lights tell the player when a
   collision is imminent.
5. **Resolution** — The shift ends with a result screen reporting punctuality,
   incidents avoided or caused, and overall performance. The player can retry
   or return to the title without restarting the application.

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