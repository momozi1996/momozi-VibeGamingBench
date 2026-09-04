# Open-World Submarine

Build an **Open-World Submarine** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player pilots a submarine through a vast deep ocean, using sonar to navigate
the darkness and discover sunken wrecks, underwater caves, and strange creatures.
The fantasy is the thrill of the abyss: descending into crushing depths where
light fades and pressure mounts, finding treasures no one else has reached.
Tension comes from oxygen management, hull pressure limits, and the unknown
shapes that appear on sonar. Salvaged treasures fund upgrades that let the
submarine dive deeper.

## What the Player Experiences

1. **Title Screen** — A dark oceanic title with the game name in glowing
   bioluminescent lettering, bubbles rising, and a play button.
2. **The Ocean** — The player pilots the submarine freely in a large 2D ocean
   cross-section. Depth increases downward with visible pressure zones marked by
   colour shifts from light blue to deep navy to black.
3. **Sonar** — Visibility is limited. The player pings sonar to reveal terrain,
   wrecks, and creatures in a radius. Sonar pulses are visible as expanding
   rings. Passive sonar shows moving contacts as blips.
4. **Exploration** — Sunken ships, underwater caves, and coral formations dot the
   ocean. The player docks with wrecks to salvage cargo, enters caves to find
   rare minerals, and photographs creatures for research bounties.
5. **Oxygen** — A constantly depleting oxygen meter forces the player to surface
   periodically or find air pockets in caves. Running out causes a blackout and
   forced ascent with cargo loss.
6. **Depth Pressure** — Descending past the submarine's rated depth causes hull
   stress. A hull integrity meter drops; if it reaches zero, the sub implodes.
   Upgrades increase depth rating.
7. **Upgrades** — Salvage funds better hull plating (deeper dives), larger oxygen
   tanks, improved sonar range, cargo hold expansion, and a headlight for
   visibility without sonar.

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