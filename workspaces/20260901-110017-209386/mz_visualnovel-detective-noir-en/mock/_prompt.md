# Detective Noir

Build **Detective Noir**, a **detective deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A private investigator works cases in a rain-soaked city, examining crime
scenes, interviewing suspects, and piecing together who did what, when, and
why on a deduction board. Each case is a self-contained mystery with physical
evidence, witness statements, and a web of connections that the player must
untangle. The tension is cognitive: all the clues are available, but connecting
them correctly requires careful reading and logical elimination. Wrong
accusations waste credibility and lock out information. The tone is classic
noir: shadows, trench coats, jazz undertones, and morally grey characters who
all have something to hide.

## What the Player Experiences

From the title screen the player selects a case from a case board. Each case
opens with a crime scene — a location rendered in noir style with interactive
hotspots. Clicking hotspots reveals evidence: a bloodstain, a torn letter, a
misplaced object. Each piece of evidence is added to the player's notebook
with its details.

The player then visits locations to interview suspects and witnesses. Each
character has dialogue that reveals information — some truthful, some
misleading. The player can press on statements to probe deeper, sometimes
unlocking new evidence or contradictions.

The deduction board is the core puzzle interface: the player connects evidence
to suspects, timelines, and motives by dragging links between cards. When
enough connections are made, the player can make an accusation — selecting
who, what weapon, and when. A correct accusation solves the case with a
dramatic reveal sequence. An incorrect one costs credibility points; too many
wrong guesses and the case goes cold.

Multiple cases are available with different difficulty levels. A styled result
screen shows the case outcome, evidence found, and deduction accuracy.

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