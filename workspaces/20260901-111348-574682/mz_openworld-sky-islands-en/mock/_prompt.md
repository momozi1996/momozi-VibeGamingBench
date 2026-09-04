# Open-World Sky Islands

Build an **Open-World Sky Islands** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player glides between floating islands suspended in an endless sky, exploring
mini-dungeons, collecting wind crystals, and defeating boss guardians to unlock
new regions. The fantasy is weightless freedom: leaping from island edges, riding
wind currents, and discovering hidden platforms in the clouds. Tension comes from
the glide mechanic — stamina depletes mid-air, and falling into the void means
restarting from the last island. Wind crystals extend glide range and unlock
powerful abilities.

## What the Player Experiences

1. **Title Screen** — A bright, airy title with the game name floating among
   clouds and distant islands. A play button shaped like a wind crystal.
2. **Island Hub** — The player starts on a central island with paths leading to
   launch points. Distant islands are visible, some shrouded in mist until
   unlocked.
3. **Gliding** — The player jumps from edges and glides using a stamina-based
   wing mechanic. Wind currents (visible as particle streams) boost altitude.
   Stamina depletes during flight; landing on any surface restores it.
4. **Mini-Dungeons** — Each island contains a small dungeon with platforming
   challenges, enemies, and a wind crystal reward. Dungeons have themed hazards:
   fire jets, moving platforms, spike traps.
5. **Wind Crystals** — Collectible crystals that serve as both currency and power
   source. Spending crystals unlocks abilities: dash, double-jump, updraft
   creation. A crystal counter is always visible.
6. **Boss Guardians** — Larger islands have boss encounters. Each boss has
   attack patterns the player must learn and dodge. Defeating a boss unlocks
   access to a new cluster of islands.
7. **Progression** — The world is divided into island clusters. Each cluster has
   a distinct visual theme (forest islands, crystal islands, volcanic islands)
   and progressively harder challenges.

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