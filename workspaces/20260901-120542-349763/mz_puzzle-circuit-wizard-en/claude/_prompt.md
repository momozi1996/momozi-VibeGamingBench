# Circuit Wizard

Build **Circuit Wizard**, a 2D logic-circuit puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places and connects logic gates (AND, OR, NOT,
XOR) on a board to route signals from inputs to outputs, solving increasingly
complex signal-routing challenges across a campaign.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a digital logic puzzle where the player builds circuits from
discrete components. Each level provides fixed input signals (on/off or
patterned) and requires specific output signals. The player places gates from
a toolbox onto a grid board and draws wires between them to create the correct
logic path. The tension comes from spatial constraints (limited board space,
wire crossing rules) and logical complexity (multi-bit signals, timing
sequences, feedback loops). The best version feels like being an engineer
with a soldering iron, where each completed circuit produces a satisfying
cascade of signals lighting up from input to output.

## What the Player Experiences

A title screen sets the electronic workshop tone with circuit imagery and a
clear way to begin. The player enters a puzzle board where input terminals
(left side), output terminals (right side), and an empty grid workspace are
visible. A toolbox shows available gate types with quantities.

Early levels teach individual gates: connect an input through a NOT gate to
invert the signal, or wire two inputs through an AND gate. Soon levels require
multi-gate chains where the player must decompose a complex boolean expression
into a physical circuit. Mid-game introduces XOR gates, multi-bit buses,
signal splitters, and delay elements that add timing constraints. Late levels
present real-world-inspired challenges: build an adder, construct a
multiplexer, or create a latch with feedback.

Signals flow visually through wires when the player activates the test button.
Correct outputs light up green; incorrect ones flash red with the expected
value shown. A completion screen celebrates the solve and shows gate count
efficiency. The campaign progresses through themed chapters: basic logic,
arithmetic circuits, memory circuits, and challenge rounds.

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