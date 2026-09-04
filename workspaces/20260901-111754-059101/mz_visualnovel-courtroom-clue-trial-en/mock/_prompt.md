# Courtroom Clue Trial

Build **Courtroom Clue Trial**, a compact **courtroom deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player is a junior advocate trying to expose a false account during a
dramatic trial. Each testimony line is a small puzzle: the witness says something
that sounds plausible, but one piece of evidence in the player's folder proves it
wrong. The tension comes from choosing when to press, what to present, and how
many mistakes the judge will tolerate before the case collapses. A wrong
accusation costs credibility; too many losses end in mistrial. The fantasy is
reading people, catching lies, and turning a courtroom on a single well-timed
objection.

## What the Player Experiences

The player opens to a case-file title screen that sets the tone: a courtroom
seal, a case number, the weight of a pending trial. Starting the case brings a
brief that lays out the charge, the suspect, and the evidence folder. Then the
witness takes the stand. Their testimony scrolls statement by statement, and the
player can press for more detail or advance to the next line. At any point the
player can open the evidence tray, inspect cards with facts like timestamps,
fingerprints, or locations, and present one against the current statement. A
correct match triggers an objection sequence: the witness falters, the testimony
updates, and the case shifts. A wrong match draws a penalty from the judge.
After the first contradiction breaks, a second layer emerges: a rebuttal, a new
clue, an alibi that does not quite hold. The player must navigate this deeper
puzzle to reach a verdict. Success means a styled victory with case-closed
fanfare. Failure means a mistrial screen with the option to retry. Both outcomes
feel like endings, not error states.

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