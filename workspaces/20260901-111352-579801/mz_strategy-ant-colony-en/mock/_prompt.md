# Ant Colony

Build **Ant Colony**, a **top-down ant colony management strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player commands an ant colony from above, directing workers to dig tunnels,
gather food, tend larvae, and defend against invaders. The colony is a living
organism: ants need roles assigned, tunnels need planning for efficient flow,
and the food stockpile determines how many mouths can be fed. The tension comes
from competing priorities — every ant digging is an ant not foraging, every
tunnel extended is a new front to defend. Seasons change the surface: summer
brings abundant food but also predators; winter cuts supply lines and forces
the colony to survive on reserves. The fantasy is being the invisible mind of
the hive, orchestrating thousands of tiny decisions into a thriving
underground civilization.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
cross-section of earth with the surface above and soil below. The queen sits
in a starting chamber and the player directs initial workers to dig outward.

Digging creates tunnels and chambers. The player designates chamber roles:
nurseries hatch eggs faster, food stores prevent spoilage, barracks train
soldiers. Workers are assigned roles by dragging them to task zones — foragers
go to the surface, diggers extend tunnels, nurses tend larvae, soldiers patrol
entrances.

Food appears on the surface as scattered resources. Foragers carry it back
along tunnel routes — shorter, wider paths mean faster delivery. The colony
grows as the queen produces eggs that hatch into new ants, but each ant
consumes food daily. Overexpansion without food income starves the colony.

Threats arrive periodically: rival insects invade through tunnel entrances,
rain floods shallow tunnels, and winter freezes surface food. The player must
balance growth against defense and plan tunnel depth for flood resistance.

The game tracks colony population and days survived. A styled result screen
shows colony statistics when the queen dies or a survival milestone is reached.

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