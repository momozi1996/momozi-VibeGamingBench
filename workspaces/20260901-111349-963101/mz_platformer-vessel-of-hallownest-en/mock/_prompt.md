# Vessel of Hallownest

Build a **2D atmospheric metroidvania platform-action game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A silent bug knight descends into a ruined underground kingdom, armed only with
a nail and the will to press deeper. The fantasy is exploration under pressure:
every room might hold a new threat or a shortcut home, and the player is always
weighing aggression against survival. Combat is fast and punishing — each slash
refills the soul that fuels healing, so standing still means dying slowly. The
interesting tension is that the resource loop forces engagement: you heal by
fighting, but fighting risks the health you are trying to recover. Progression
gates the world behind abilities earned in earlier zones, rewarding mastery with
access rather than numbers. The tone is somber, desolate, and beautifully
tragic — cold underground ruins, glowing particles drifting through silence, and
the quiet weight of a kingdom that fell long ago.

## What the Player Experiences

A melancholic title screen greets the player with the game name and a lone
knight silhouette before they choose to begin or continue a saved journey.

The Kingdom Map appears — a network of named stages stretching downward, each
locked until the one before it falls. The player selects the first open stage
and drops in. Inside, the world is a continuous side-scrolling corridor of
connected rooms: platforms jut from cavern walls, thorn pits line the floor, and
infected husks patrol ledges. Movement feels tight and responsive — the knight
accelerates smoothly, jumps with a satisfying arc, clings to walls, and dashes
through gaps that demand precision.

Combat is immediate and visceral. Slashing an enemy staggers it, sprays geo
currency, and fills the soul meter. Taking a hit costs a mask of health and
triggers a brief flash of invincibility. When masks run low the player faces the
core dilemma: hold still to channel soul into healing — vulnerable, exposed — or
press forward and hope the next kill refills enough to survive. Enemies guard
room exits behind soul-barriers that lift only when every husk in the chamber is
dead.

Deeper rooms demand wall-clings and dashes to cross chasms the knight cannot
simply jump. Reaching the far end of a stage triggers a checkpoint that saves
progress and unlocks the next zone on the map. Death is costly — all carried geo
drops at the point of failure and the knight returns to the map to try again.

The final stage is a boss chamber: a large creature with telegraphed attack
patterns that test everything the player has learned. Victory crowns the run;
defeat sends the knight back with nothing but knowledge.

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