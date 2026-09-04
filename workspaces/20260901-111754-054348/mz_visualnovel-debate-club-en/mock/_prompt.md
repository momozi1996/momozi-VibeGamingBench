# Debate Club

Build **Debate Club**, a **debate and contradiction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a student investigator who must expose lies in formal debates by
firing evidence at contradictory statements. Suspects make claims during
structured arguments, and the player must identify which statement contradicts
collected evidence, then present the right proof at the right moment. The
tension is timing and precision: statements scroll past, the window to object
is brief, and wrong objections damage the player's reputation score. Multiple
suspects across multiple debate rounds build toward identifying the true
culprit. The tone is academic-thriller: school halls, formal podiums, sharp
dialogue, and the rush of catching someone in a lie.

## What the Player Experiences

From the title screen the player enters an investigation phase. They explore
locations (classroom, library, courtyard) clicking hotspots to gather evidence
cards — each card has a fact, a source, and a relevance tag. Evidence
collection is the preparation for the debate.

The debate phase is the core gameplay. Suspects take turns making statements
displayed as scrolling text panels. The player listens (reads) and watches for
contradictions — a statement that conflicts with collected evidence. When they
spot one, they select the matching evidence card and fire it as a "truth
bullet" at the contradicting statement.

A correct hit triggers a dramatic break sequence: the statement shatters, the
suspect falters, and new information is revealed. An incorrect hit costs
reputation points — lose too many and the debate is lost. After breaking a
contradiction, the debate advances to a new phase with harder claims.

Multiple debate rounds across different suspects build the case. The final
round requires the player to identify the culprit from the accumulated
evidence. A styled result screen shows the verdict, reputation score, and
evidence accuracy.

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