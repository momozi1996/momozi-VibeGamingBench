# Idle Ant Empire

Build an **Idle Ant Empire** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds an ant colony from a single queen, assigning workers to tasks,
unlocking new ant types, and growing exponentially through prestige resets. The
fantasy is watching a tiny empire scale to absurd proportions: from gathering
crumbs to harvesting entire gardens, from a handful of workers to millions. The
idle loop runs continuously — ants gather resources even when the player is not
clicking. Tension comes from resource allocation decisions and seasonal challenges
that threaten the colony.

## What the Player Experiences

1. **Title Screen** — A cross-section of underground tunnels with ants marching,
   the game name in earthy brown font, and a play button styled as a leaf.
2. **Colony View** — A side-view ant colony with visible chambers: nursery, food
   storage, queen's chamber, and tunnels connecting them. Ants visibly move
   between chambers carrying resources.
3. **Worker Assignment** — The player assigns ants to roles: gatherers (collect
   food), builders (dig new chambers), soldiers (defend), and nurses (hatch eggs).
   Sliders or buttons control allocation. Production rates update in real-time.
4. **Resource Generation** — Food accumulates automatically based on gatherer
   count. The player can click to manually boost gathering. Resources fund new
   chambers, ant hatching, and upgrades.
5. **Ant Types** — Unlockable ant types with special abilities: leaf-cutters
   (bonus food), fire ants (defence), flying ants (exploration), and mega-ants
   (10x production). Each type has a distinct sprite.
6. **Prestige System** — When the colony reaches a threshold size, the player can
   prestige: reset the colony but gain permanent multipliers (queen fertility,
   gathering speed, defence strength). Each prestige makes the next run faster.
7. **Seasonal Challenges** — Periodic events threaten the colony: rain floods
   tunnels (need builders), predators attack (need soldiers), winter reduces food
   (need stockpiles). Surviving challenges grants bonus resources.

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