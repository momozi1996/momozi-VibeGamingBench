# Robot Factory

Build **Robot Factory**, a **robot programming arena strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player programs robot behaviors using simple if/then rules, deploys them
into a grid arena, and watches them execute simultaneously against an
opponent's robots. The strategy is entirely in the programming phase: once
robots are deployed, they act on their own according to their instruction sets.
A robot might be told "if enemy adjacent, attack; if health low, retreat; else
advance." The tension is that both sides reveal their programs at the same
time, creating emergent interactions that reward prediction and counter-play.
The tone is retro-futuristic: chunky robots on a factory floor, sparks flying,
gears grinding.

## What the Player Experiences

From the title screen the player enters the workshop. Here they build robots
by assigning behavior rules from a visual list. Each robot has three to five
instruction slots, and each slot is an if/then pair: a condition (enemy in
range, health below threshold, ally nearby) and an action (move forward,
attack, turn, heal, wait). Rules execute top to bottom each turn.

After programming, the player positions robots on their half of a grid arena.
Different robot chassis have different stats — heavy bots have more HP but
fewer instruction slots, light bots move faster but break easily, support bots
can heal adjacent allies.

When both sides are ready, the battle plays out turn by turn with simultaneous
execution. Each turn, every robot evaluates its rules and acts. The player
watches their programming logic play out — sometimes brilliantly, sometimes
hilariously wrong. The round ends when one side's robots are all destroyed.

A campaign of escalating challenges teaches mechanics one at a time, and a
skirmish mode lets the player test builds against AI opponents. The result
screen shows battle replay highlights and robot performance stats.

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