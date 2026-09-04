# Rhythm Note Highway

Build a Rhythm Note Highway as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Notes cascade down a multi-lane highway toward a judgement line at the bottom
of the screen. The player must press the matching lane key precisely as each
note crosses the line. Accuracy builds a combo multiplier that amplifies the
score; misses break the streak and drain a life bar. The fantasy is performing
a concert — nailing every note in a flow state while the background stage
lights react to your accuracy. A full campaign of procedurally-timed songs
provides hours of escalating challenge.

## What the Player Experiences

1. **Title Screen** — A neon-lit stage backdrop with the game name in a bold
   stylized font, a campaign button, and a free-play button. No plain grey.
2. **Song Select** — A scrollable list of at least 10 songs with difficulty
   ratings (Easy/Medium/Hard), best scores, and completion grades (S/A/B/C/F).
   Songs unlock sequentially through the campaign.
3. **The Highway** — 4 lanes with colour-coded note gems falling toward a
   judgement bar. The player presses D/F/J/K (or arrow keys) to hit notes.
   Timing windows: Perfect, Great, Good, Miss — each with distinct visual
   feedback (burst, glow, shake).
4. **Combo System** — A combo counter increments on consecutive hits. The
   multiplier (x2, x4, x8) scales score. Breaking combo resets the counter
   with a visible shatter effect.
5. **Life Bar** — Misses drain health. If health hits zero, the song fails
   with a game-over screen showing stats. Perfects restore a small amount.
6. **Hold Notes and Slides** — Some notes require holding the key for their
   duration (a trailing tail). Others slide across lanes, requiring the player
   to follow with their finger position.
7. **Results Screen** — After each song: total score, max combo, accuracy
   percentage, grade, and a breakdown of Perfect/Great/Good/Miss counts.
   New high scores trigger a celebration animation.

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