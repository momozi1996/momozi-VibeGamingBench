# Sports Boxing Gym

Build a **Sports Boxing Gym** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a boxer rising through the ranks, reading opponent tells, timing
dodges and counters, and managing stamina across multi-round bouts. The fantasy
is the sweet science: not brute force but pattern recognition, knowing when to
slip a jab and answer with a hook. Tension comes from stamina — every punch
thrown and every dodge costs energy, and a tired boxer drops their guard. Between
fights, training mini-games improve stats and unlock new techniques.

## What the Player Experiences

1. **Title Screen** — A boxing ring under spotlights with the game name in bold
   block letters, a play button styled as a bell.
2. **Career Menu** — The player sees their boxer's stats, upcoming opponent, and
   training options. A fight card shows the next bout with the opponent's
   silhouette and record.
3. **Training** — Before each fight, the player completes training mini-games:
   heavy bag (timing combos), speed bag (rhythm clicking), jump rope (pattern
   matching). Training improves power, speed, or stamina stats.
4. **The Fight** — Side-view boxing with two fighters. The opponent telegraphs
   attacks with visible tells (shoulder dip, foot shift, glove pull-back). The
   player must read the tell and respond: dodge high/low, block, or counter.
5. **Punch Mechanics** — The player throws jabs, hooks, and uppercuts with
   different keys. Each punch type has different speed, power, and stamina cost.
   Combos (sequences of punches) deal bonus damage.
6. **Stamina System** — A stamina bar depletes with every action. Low stamina
   slows punches and weakens blocks. Between rounds, stamina partially recovers.
   The player must pace themselves across rounds.
7. **Career Progression** — Winning fights advances rank. Opponents get harder
   with faster tells and more varied patterns. Reaching the championship requires
   mastering all defensive techniques.

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