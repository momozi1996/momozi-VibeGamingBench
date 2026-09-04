# Horror Tape Archive

Build a **Horror Tape Archive** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player reviews surveillance tapes from a facility, scrubbing through footage
to find and timestamp anomalies. The fantasy is forensic dread: watching mundane
footage knowing something is wrong, catching the moment a shadow moves on its
own or a figure appears where none should be. Tension comes from a sanity meter
that drains as anomalies are witnessed, and from the growing realisation that
the tapes are watching back. Each correctly timestamped anomaly advances the
investigation but costs mental stability.

## What the Player Experiences

1. **Title Screen** — A VHS-styled title with tracking lines, the game name in
   monospace font, and a play button styled as a tape deck control.
2. **The Archive Room** — A desk with a CRT monitor, a tape shelf, a clipboard
   for notes, and a sanity gauge. The room is dimly lit with a single desk lamp.
3. **Tape Selection** — The player chooses from multiple labelled tapes on the
   shelf. Each tape covers a different camera location: hallway, lab, storage,
   courtyard. Tapes have different lengths and anomaly counts.
4. **Footage Review** — The monitor shows grainy surveillance footage. The player
   can play, pause, rewind, and fast-forward. A timestamp counter runs in the
   corner. The footage shows mostly normal activity with subtle anomalies hidden
   within.
5. **Anomaly Detection** — When the player spots something wrong (a shadow moving
   against the light, an object disappearing, a figure in the background), they
   pause and click "Mark Anomaly" with the current timestamp. Correct marks earn
   investigation points; false marks cost sanity.
6. **Sanity Meter** — Watching anomalies drains sanity. Low sanity causes visual
   corruption: the archive room distorts, phantom sounds play, and false
   anomalies appear in the footage to trick the player. At zero sanity, the
   session ends.
7. **Investigation Progress** — Correctly marked anomalies fill a case board,
   connecting events across tapes. Completing connections unlocks new tapes and
   reveals the facility's secret. The final tape shows what happened to the
   previous archivist.

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