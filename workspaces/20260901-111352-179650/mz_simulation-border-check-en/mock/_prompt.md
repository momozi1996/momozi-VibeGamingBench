# Border Check

Build **Border Check**, a 2D document-inspection simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is working as a border checkpoint inspector in a fictional
authoritarian state, examining travelers' documents against an ever-changing
rulebook while trying to earn enough to keep your family alive. The interesting
tension is moral versus mechanical: the rules say deny this person, but their
story is sympathetic — and every wrong decision costs money your family needs for
heat and medicine. Speed matters because each day has a time limit and pay is
per-person processed, but rushing causes mistakes that trigger citations and
fines. The rules grow more complex each day — new document types, new
contraband checks, new exceptions — until the player is juggling five documents
simultaneously while a queue of desperate faces waits.

## What the Player Experiences

The player opens to a bleak title screen showing the checkpoint booth, then
begins Day 1. The workspace shows a desk surface with an inspection area, a
rulebook panel, and stamps for APPROVE and DENY. Travelers approach one at a
time, presenting documents that slide onto the desk. The player drags documents
around, opens the rulebook to check current rules, compares photo to face,
checks expiration dates, and cross-references permit numbers.

Each day introduces new rules: Day 1 might only require matching names, while
Day 5 requires valid work permits, vaccination records, and weight discrepancy
checks. End-of-day shows earnings, family expenses, and any citations received.
Story events interrupt between days — a guard offers bribes, a rebel asks for
help, family members fall ill. Choices affect the narrative path. The game spans
10+ days with escalating complexity and multiple ending conditions based on
accumulated choices and financial survival.

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