# Rhythm Garden

Build a Rhythm Garden as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A whimsical garden overworld connects a collection of eight or more timing
minigames, each themed around a different garden activity — watering flowers to
a beat, swatting bugs in rhythm, conducting a bird choir, bouncing seeds into
pots with timed taps. Each minigame teaches a different rhythmic skill (steady
pulse, syncopation, polyrhythm, call-and-response). Mastering individual games
unlocks a final "Remix" stage that weaves all mechanics together into one
climactic performance. The fantasy is a musical gardener tending a world that
blooms in response to rhythmic mastery.

## What the Player Experiences

1. **Title Screen** — A pastel garden scene with the game name in a playful
   hand-drawn font, flowers swaying to a gentle beat, and a "Play" button
   shaped like a watering can. No plain HTML grey.
2. **Garden Hub** — An overworld map showing garden plots, each representing a
   minigame. Completed games bloom with flowers; locked ones show wilted buds.
   The player clicks a plot to enter its minigame.
3. **Minigame Variety** — At least 8 distinct minigames, each with unique
   visuals and a different timing mechanic:
   - Tap to the beat (steady quarter notes)
   - Hold and release (sustained timing)
   - Call and response (echo a pattern)
   - Syncopation (off-beat hits)
   - Polyrhythm (two simultaneous patterns)
   - Speed ramp (accelerating tempo)
   - Pattern memory (repeat increasingly long sequences)
   - Free-form (improvise within a groove)
4. **Scoring** — Each minigame scores accuracy as a star rating (1-3 stars).
   Visual feedback during play shows timing quality with particle bursts for
   perfect hits and wilting effects for misses.
5. **Progression** — Earning stars unlocks later minigames. The garden visibly
   grows and blooms as the player progresses. New flowers, butterflies, and
   decorations appear with each milestone.
6. **Final Remix** — After completing all 8 minigames, a final challenge
   combines mechanics from multiple games into one extended performance. The
   remix transitions between styles every few measures.
7. **Results and Gallery** — A gallery screen shows total stars, best scores per
   minigame, and the fully-bloomed garden as a reward illustration.

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