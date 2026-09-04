# Rhythm DJ Arena

Build a Rhythm DJ Arena as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Two musical fighters face off on a neon stage, trading rhythmic attacks in a
battle of beats. Each fighter has a note highway; hitting notes charges special
moves that launch across the arena as musical projectiles. The opponent must
dodge or counter with their own charged abilities. The fantasy is a DJ battle
where musical skill translates directly into combat power — perfect combos
unleash devastating bass drops while missed notes leave you vulnerable. Multiple
characters with distinct musical styles and move sets provide variety.

## What the Player Experiences

1. **Title Screen** — A vibrant neon club aesthetic with the game name in
   glowing graffiti-style text, character select and versus mode buttons, and
   animated equalizer bars in the background. No plain HTML grey.
2. **Character Select** — At least 4 playable characters, each with a distinct
   musical theme (electronic, rock, jazz, hip-hop), unique sprite design, and
   different special move sets. Each character's selection shows a preview
   animation and their move list.
3. **Split Highway** — The screen splits: each side has a 3-lane note highway.
   The player hits notes on their side to build a charge meter. The AI opponent
   plays their own highway simultaneously.
4. **Charge and Attack** — When the charge meter fills a threshold, the player
   can spend it to launch a musical attack (bass wave, treble spike, chord
   blast). Attacks travel across the arena toward the opponent. Stronger charges
   (from higher combos) produce more powerful attacks.
5. **Defence and Dodge** — The opponent can dodge attacks by timing a key press
   as the projectile arrives, or absorb hits (losing health). A health bar
   depletes with each successful hit. First to zero loses the round.
6. **Best of Three** — Matches are best-of-3 rounds. Between rounds, a brief
   interlude shows score and lets the tempo increase for the next round.
7. **Arcade Mode** — A ladder of increasingly difficult AI opponents, each with
   faster note patterns and more aggressive attack usage. Defeating all
   opponents shows a character-specific victory screen.

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