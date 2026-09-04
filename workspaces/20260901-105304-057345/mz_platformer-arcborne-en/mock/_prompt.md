# Arcborne

Build **Arcborne**, a 2D **grappling-hook swing-momentum platformer** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a time-attack about chaining pendulum swings across deadly
terrain, releasing at the perfect instant to soar, and hooking again before
gravity wins.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Fly, don't walk. The player is an acrobat who crosses chasms by firing a
grappling hook, swinging on the line, and releasing at the apex to launch into a
soaring arc -- then hooking again to chain momentum across the course. The
fantasy is momentum mastery: gravity, swing arcs, and well-timed releases
compound into speed, and the difference between a clumsy crawl and a flowing
chain of perfect swings is visceral. One clean run of linked swings feels
glorious; one mistimed release drops you into the spikes.

The pressure comes from the clock. Every course is a time-attack where the
player reads terrain, picks anchor points, commits to a swing, and decides the
exact frame to let go. Multiple hook modes add tactical depth -- sometimes you
need raw pendulum momentum, sometimes a direct yank to reposition -- and the
worlds themselves bend the rules of motion so mastery in one biome doesn't
guarantee mastery in the next.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen that
   establishes the acrobatic, high-velocity tone. Starting a run drops them into
   the first world with a visible clock already ticking.

2. **Swing and Chain** -- The core sensation is physical: fire a hook at an
   overhead anchor, feel gravity pull the arc, build speed at the bottom of the
   pendulum, and release to fling forward. A fresh hook mid-flight chains one
   swing into the next without touching the ground. The player shapes each swing
   -- pumping, reeling, steering -- so skilled play looks fluid and fast while
   beginners flail and recover.

3. **Multiple Hook Modes** -- The player discovers they have more than one kind
   of hook. A swing line carries pendulum momentum; a pull line yanks them
   straight to an anchor for tight climbs or recoveries. Switching between modes
   becomes second nature as the terrain demands it.

4. **Worlds that Change the Rules** -- The journey carries the player through
   escalating worlds with distinct environments. Each world introduces its own
   anchor types, hazards, and an environmental modifier that alters how swinging
   feels -- gusts that shove mid-arc, conveyors that drag on the ground, low
   gravity that stretches every launch into a long glide. The player must adapt
   their timing and technique to each new set of physics.

5. **Danger and Recovery** -- Pits, spikes, blades, and moving hazards punish
   mistimed releases. Hitting a hazard or falling sends the player back to a
   checkpoint with clear feedback. The course is forgiving enough to learn but
   punishing enough that a clean run feels earned.

6. **Resolution** -- Reaching the goal ends the course with a result showing
   time and medal. The player can retry for a better time or advance to the next
   course. The full loop -- title, play, result, retry or advance -- flows
   without restarting the application.

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