# Pirate Port

Build **Pirate Port**, a **pirate haven management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player builds a hidden pirate port on a tropical island, attracting crews
with taverns and docks, sending them on raids for plunder, and defending
against the royal navy when notoriety grows too high. The economy loops through
three currencies: gold from raids funds buildings, reputation attracts better
crews, and notoriety draws navy attention. The tension is that the most
profitable actions raise notoriety fastest, forcing the player to balance
aggression against defense preparation. The tone is swashbuckling Caribbean:
palm trees, rickety docks, rum barrels, and cannon smoke.

## What the Player Experiences

From the title screen the player starts a new port. The view shows a coastal
island with a grid for building. The player constructs docks to berth ships,
taverns to attract pirate crews, warehouses to store plunder, and defenses
(walls, cannons, watchtowers) to repel navy raids.

Pirate crews arrive based on the port's reputation. Each crew has a ship type,
combat strength, and upkeep cost. The player sends crews on raids by selecting
a target from a map of trade routes — richer targets yield more gold but raise
notoriety higher. Raids play out automatically with a result summary.

Gold funds expansion: better docks attract larger ships, upgraded taverns keep
crews happy, and a shipyard allows repairing and upgrading vessels. Crew morale
depends on tavern quality, raid success, and pay.

When notoriety reaches thresholds, the navy attacks. Navy raids are tower-
defense encounters where the port's cannons and walls must hold against
incoming warships. Surviving a raid lowers notoriety slightly; failing means
losing buildings and crews.

The game tracks gold, fleet size, and raids completed. A styled result screen
shows port statistics when the port falls or reaches a prosperity milestone.

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