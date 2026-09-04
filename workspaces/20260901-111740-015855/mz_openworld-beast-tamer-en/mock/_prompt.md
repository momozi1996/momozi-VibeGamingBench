# Open-World Beast Tamer

Build an **Open-World Beast Tamer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player roams diverse biomes — jungle, tundra, desert, swamp — finding and
taming wild creatures with unique abilities. The fantasy is building a bond with
powerful beasts and using their skills to solve environmental puzzles and reach
new areas. Tension comes from the taming process itself: each creature requires
a different approach (stealth, bait, rhythm), and failed attempts spook the beast.
Tamed creatures evolve through use, gaining new forms and abilities.

## What the Player Experiences

1. **Title Screen** — A vibrant title showing the game name with creature
   silhouettes in various biomes. A play button starts the adventure.
2. **Biome Exploration** — The player walks freely across interconnected biomes,
   each with distinct terrain, colour palette, and ambient creatures. Biome
   boundaries are visually clear.
3. **Creature Discovery** — Wild creatures roam each biome with visible behaviour
   patterns. A bestiary silhouette hints at undiscovered species. Each creature
   has a unique sprite and idle animation.
4. **Taming** — Approaching a creature triggers a taming mini-game: the player
   must match a pattern (timing clicks, offering correct bait, or sneaking close
   without startling). Success adds the creature to the party.
5. **Creature Abilities** — Each tamed creature has a unique ability: fire breath
   melts ice barriers, a burrower digs through soft ground, a flyer carries the
   player over gaps. The player switches active creature to solve puzzles.
6. **Environmental Puzzles** — Blocked paths require specific creature abilities.
   A frozen river needs fire, a chasm needs flight, a sealed cave needs brute
   strength.
7. **Evolution** — Using a creature in puzzles and exploration fills an experience
   gauge. When full, the creature evolves into a stronger form with enhanced
   abilities and a new sprite.

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