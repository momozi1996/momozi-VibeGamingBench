# Music Label

Build **Music Label**, a **music label management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player runs an independent music label, signing artists, producing albums,
marketing releases, and scheduling tours. Each artist has a genre, talent
level, morale, and fanbase that grow or shrink based on management decisions.
The market shifts — genres trend up and down, and timing a release to ride a
wave multiplies sales. The tension is resource allocation: studio time is
limited, marketing budgets are finite, and pushing an artist too hard burns
them out. The tone is creative-industry drama: recording studios, chart
battles, and the thrill of a breakout hit.

## What the Player Experiences

From the title screen the player starts a new label. The main view shows the
label dashboard: signed artists, upcoming releases, financial summary, and
genre trend charts. Time advances week by week.

Artists are scouted from a pool — each has a genre, talent rating, and
personality traits that affect studio behavior. Signing costs an advance and
commits to producing their album. In the studio, the player allocates
production weeks and chooses a producer style (polished, raw, experimental)
that affects album quality and genre fit.

Marketing is a budget allocation: spend on social media, radio, press, or
touring. Each channel reaches different audiences and has diminishing returns.
Timing matters — releasing during a genre's peak trend multiplies exposure.

Tours generate revenue and grow fanbases but cost money upfront and drain
artist morale. An exhausted artist produces worse albums and may leave the
label. The player must balance exploitation against artist care.

Revenue comes from album sales, streaming royalties, tour profits, and
merchandise. Expenses include studio rent, staff salaries, advances, and
marketing. The game tracks label reputation, total revenue, and chart
positions. A styled result screen shows label achievements each quarter.

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