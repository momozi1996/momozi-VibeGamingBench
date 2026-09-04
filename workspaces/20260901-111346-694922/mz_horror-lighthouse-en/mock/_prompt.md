# Horror Lighthouse

Build a **Horror Lighthouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a lighthouse keeper during an endless storm, maintaining the light
to guide ships safely past the rocks while something in the water tries to lure
them onto the shore. The fantasy is lonely duty against cosmic dread: the beam
is the only thing between sailors and death, but keeping it lit attracts the
attention of what lurks below. Tension comes from fuel management, mechanical
breakdowns, and the creature's escalating attempts to extinguish the light or
drive the keeper mad.

## What the Player Experiences

1. **Title Screen** — A stormy coastal scene with a lighthouse beam sweeping
   through rain, the game name in weathered serif font, and a play button.
2. **The Lighthouse** — A cross-section view showing multiple floors: the lamp
   room at top, living quarters in the middle, fuel storage at the bottom, and
   the dock outside. The player moves between floors.
3. **Light Maintenance** — The lamp burns fuel and occasionally malfunctions. The
   player must refuel from storage below, clean the lens when spray coats it,
   and repair the rotation mechanism when it jams. If the light goes out, ships
   crash.
4. **Ship Guidance** — Ships appear on the dark ocean as distant lights. The
   player must keep the beam rotating to warn them of rocks. Successfully guided
   ships pass safely; crashed ships add wreckage and guilt.
5. **Fuel Management** — Fuel is limited. Supply boats come periodically but the
   storm delays them. The player must ration fuel, choosing between full
   brightness (safe but drains fast) and dim mode (conserves fuel but ships may
   not see it).
6. **The Creature** — Something in the water interferes: tentacles reach for the
   dock, bioluminescent lures mimic ship lights to confuse the keeper, and
   whispers try to convince the player to extinguish the lamp. The player must
   resist and repair damage.
7. **Escalation** — Each night the storm worsens, fuel becomes scarcer, and the
   creature grows bolder. The final night requires the player to keep the light
   burning through a direct assault while guiding the last ship to safety.

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