# News Editor

Build **News Editor**, a 2D newspaper management simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a scrappy newspaper, deciding which stories to chase,
which reporters to assign, and whether to prioritize speed or accuracy in a
media landscape where both reputation and revenue matter. The interesting tension
is the fact-check tradeoff: publishing fast captures readers and ad revenue but
risks printing errors that damage credibility; thorough fact-checking produces
reliable journalism but competitors scoop you and readers drift away. Reporters
have specialties and reliability ratings, stories have complexity and time
sensitivity, and the player must match resources to opportunities while keeping
the lights on.

## What the Player Experiences

The player opens to a newsroom title screen with a printing press motif, then
enters the editor's desk view. The main screen shows today's story leads in an
inbox, the current edition layout, reporter assignments, and financial status.
Story leads arrive throughout the day with topic, complexity, time sensitivity,
and potential impact ratings.

The player assigns reporters to stories, choosing between fast coverage (higher
error risk) and deep investigation (slower but more accurate). Completed stories
are placed in the edition layout — front page, inside, or buried. Publishing
triggers reader response: accurate scoops boost reputation and subscriptions;
errors trigger corrections that cost credibility. Revenue comes from
subscriptions and advertisers (who care about readership numbers). Between
editions the player can hire/fire reporters, invest in fact-checking tools, or
expand coverage areas. The campaign spans 20+ editions with escalating story
complexity, competitor pressure, and financial targets. An edition summary shows
stories published, accuracy rate, readership change, and profit/loss.

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