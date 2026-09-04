# Racing Trick Runner

Build a Racing Trick Runner as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

An endless downhill runner where the player carves through procedurally varied
terrain, launching off ramps to perform aerial tricks that boost speed and
score. The slope never ends — the challenge is how far you can go before
crashing. Weather shifts from sunshine to blizzard, day cycles to night, and
the terrain grows steeper and more treacherous. Tricks are the key to survival:
they refill a boost meter that lets you power through flat sections. Unlockable
characters with different trick styles and visual flair provide long-term goals.

## What the Player Experiences

1. **Title Screen** — A snowy mountain vista with the game name in a frosty
   stylized font, a silhouetted rider mid-backflip, and Play/Collection
   buttons. No plain HTML grey.
2. **The Run** — Side-scrolling endless descent. The character automatically
   moves downhill; the player controls jump timing, trick execution, and
   landing angle. Terrain scrolls with parallax mountain backgrounds.
3. **Trick System** — While airborne, the player inputs trick commands (flip,
   spin, grab) using directional keys. Each trick has a point value and a
   time cost. Landing cleanly after a trick awards points and refills boost.
   Landing badly (wrong angle) causes a stumble that costs speed.
4. **Boost Mechanic** — A boost meter fills from successful tricks. Activating
   boost increases speed dramatically with a visual trail effect. Boost is
   essential for clearing flat sections and gaps.
5. **Weather and Day/Night** — Conditions change during a run: clear skies
   transition to fog (reduced visibility), then snow (slippery terrain), then
   blizzard (both). Day fades to night with reduced visibility. Each condition
   affects gameplay and visuals distinctly.
6. **Obstacles and Terrain** — Rocks, trees, and crevasses appear as obstacles.
   The terrain varies between smooth slopes, mogul fields, cliff drops, and
   ramp sequences. Hitting an obstacle ends the run.
7. **Character Collection** — At least 5 unlockable characters earned by
   reaching distance milestones or score targets. Each has a unique sprite,
   trick animation style, and one special ability (higher jumps, longer boost,
   extra hit point).

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