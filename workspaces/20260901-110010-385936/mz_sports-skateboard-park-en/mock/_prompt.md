# Sports Skateboard Park

Build a **Sports Skateboard Park** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player skates through parks performing trick combos for high scores, unlocking
new tricks and building custom parks. The fantasy is flow state: chaining grinds
into flips into manuals in one unbroken combo, watching the score multiplier
climb. Tension comes from the landing — mistiming a trick means a bail that
resets the combo. Career goals push the player to master specific tricks and
achieve target scores in themed parks.

## What the Player Experiences

1. **Title Screen** — A graffiti-styled title with the game name in spray-paint
   font over a half-pipe silhouette. A play button shaped like a wheel.
2. **Park Selection** — Multiple parks with different layouts: a street course
   (rails, stairs, ledges), a vert ramp (half-pipes, bowls), and a mega park
   (all elements combined). Each unlocks progressively.
3. **Skating** — The player moves left/right with momentum physics. Speed builds
   on downhill, drains on uphill. The skater has smooth rolling animation and
   responds to terrain.
4. **Trick System** — Button combinations trigger tricks: flip tricks (tap keys),
   grind tricks (press near rails), grab tricks (hold in air). Each trick has a
   name that pops up on screen. Tricks chain into combos with a visible
   multiplier.
5. **Score Multiplier** — Linking tricks without touching ground or bailing
   increases the multiplier. Landing cleanly banks the score; bailing loses the
   current combo. A combo meter shows current chain length and potential score.
6. **Career Goals** — Each park has specific challenges: "Score 10,000 in one
   combo", "Land a kickflip to grind", "Complete a full pipe rotation". Completing
   goals unlocks new tricks and parks.
7. **Park Editor** — The player can place ramps, rails, and obstacles to create
   custom parks. Placed elements snap to a grid. Custom parks are playable
   immediately.

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