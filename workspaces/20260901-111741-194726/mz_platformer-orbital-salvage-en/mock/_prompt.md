# Orbital Salvage

Build **Orbital Salvage**, a compact 2D space-salvage physics game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a polished micro-game about piloting a small tug through
orbital debris, latching onto wreckage with a tractor beam, and hauling it back
to a recovery station before fuel runs dry or hazards tear the payload loose.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a salvage pilot working the edge of a debris belt. The tug does
not stop on a dime — it drifts, coasts, and fights momentum every time the
thrusters fire. Attaching a tractor beam to a chunk of wreckage changes
everything: heavier salvage drags the tug off course, volatile pieces threaten
to rupture, and the route back to the station threads between gravity wells,
drifting mines, and radiation arcs. The decision space lives in choosing which
contract to accept, which salvage to grab first, how aggressively to burn fuel,
and whether to risk a shortcut through a hazard corridor for a bigger payout.
Between runs the player reinvests credits into thrust power, beam strength, or
hull plating, shaping how the next contract feels. The tone is tense and
industrial — a blue-collar space job where physics is the real antagonist.

## What the Player Experiences

A styled title screen sets the mood: the game name over a starfield with
drifting debris silhouettes, a tug outline, and a clear way to begin.

The player picks a contract from a board showing salvage type, estimated mass,
payout, and hazard warnings. The tug launches into a 2D orbital field where
inertia is king — tapping thrust accelerates, releasing it lets the ship coast,
and reversing burns fuel fast. Salvage floats among asteroid chunks and hazard
zones. The player maneuvers close, fires the tractor beam, and feels the tug
lurch as the mass latches on. Towing a heavy reactor core is nothing like
dragging a light panel — the ship wallows, turns wide, and fuel burns faster.

Hazards punctuate the route: gravity wells bend the flight path, mines detonate
if clipped, radiation arcs pulse warnings before firing. The player reads the
field, plans a line, and commits — or cuts the beam and abandons the payload to
save the tug. Delivering salvage to the station awards credits and advances the
contract. A result screen tallies earnings, fuel spent, hull damage, and offers
the next contract or a return to title.

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