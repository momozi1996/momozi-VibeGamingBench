# Ink Trail

Build **Ink Trail**, a platformer where the player leaves a trail that becomes
solid platform after a delay as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

An ink spirit dashes through empty voids, leaving behind a wet trail of ink
that solidifies into walkable platforms after a short delay. The spirit has
limited ink — once the reservoir empties, no more trail is created until
reaching an ink well refill. The core puzzle: plan a path through empty space
such that the trail you leave behind creates the platforms you need to reach
the exit. Sometimes you must double back to stand on your own trail. Sometimes
you must draw a bridge mid-jump and land on it as it solidifies. Ink wells are
sparse, forcing efficient routing. Thirty-six levels across six worlds
introduce wind that displaces wet ink, erasers that dissolve trails, color-coded
ink that only solidifies near matching surfaces, and timed ink that fades after
seconds.

## What the Player Experiences

A title screen shows ink dripping into the game name. A world-select grid shows
six worlds of six levels each.

The player moves and jumps normally. While moving, ink trails behind the
character as a visible wet line. After a 1-second delay, the wet ink hardens
into a solid platform with a satisfying visual pop. An ink meter shows remaining
supply — when empty, movement leaves no trail. Ink wells scattered in levels
refill the meter.

Early levels teach basic trail-platforming: cross a gap by running through air
and doubling back onto your solidified trail. Later levels add complexity: wind
pushes wet ink sideways before it hardens, erasers delete sections of trail,
and timed ink fades after a few seconds requiring speed. Each level has a
three-star rating based on ink efficiency. A level-complete screen shows ink
used, time, and stars earned.

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