# Zoo Keeper

Build **Zoo Keeper**, a **zoo management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player builds and manages a zoo, constructing enclosures for diverse
animals, keeping visitors happy, and pursuing conservation goals. Each animal
species has habitat requirements — size, terrain type, temperature, companions
— and meeting them keeps animals healthy and breeds new ones. Visitors pay
admission and spend at gift shops and food stalls, but they come for the
animals: rare species and well-designed enclosures draw bigger crowds. The
tension is between commercial pressure (visitors want spectacle) and animal
welfare (cramped exhibits stress animals). The tone is bright and educational:
lush habitats, informational plaques, and the joy of seeing animals thrive.

## What the Player Experiences

From the title screen the player starts a new zoo. The view shows a top-down
park grid with an entrance gate. The player builds paths, enclosures, visitor
amenities, and staff buildings.

Enclosures are built by fencing an area and assigning a biome type (savanna,
arctic, jungle, aquatic). Animals are acquired from a catalog — each has a
purchase cost, habitat requirement, and popularity rating. Placing an animal
in a matching habitat keeps it happy; mismatched habitats cause stress shown
by a visible mood indicator.

Visitors enter through the gate, walk paths, view enclosures, and spend money.
Visitor happiness depends on animal variety, enclosure quality, path layout,
and amenity availability. Happy visitors stay longer and spend more.

Breeding is triggered when compatible animals share a well-maintained
enclosure. Baby animals are a major visitor draw and can be kept or traded for
conservation points. Conservation goals (breed endangered species, maintain
genetic diversity) provide bonus objectives beyond pure profit.

Staff (keepers, vets, janitors) must be hired and assigned. The game tracks
money, visitor count, animal welfare score, and conservation progress. A styled
result screen shows zoo statistics at the end of each season.

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