# Open World: WildRealm

Build a **creature-capture open-world RPG** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a vibrant open world, stumbles upon wild creatures in tall
grass, and engages them in turn-based battles -- capturing, training, and
growing a personal squad. The interesting tension is resource management across
encounters: every capture ball spent, every HP lost, and every skill cooldown
used is a commitment that carries forward until the player finds a healer. The
pressure escalates as the player ventures further from town into tougher
territory, and the payoff is discovering a rare creature or finally defeating
the gym leader to unlock the next region. The game should feel **bright,
adventurous, and nostalgic** -- think creature-taming meets *A Short Hike* at
a smaller scale.

## What the Player Experiences

1. **Title and Entry** -- A charming title screen sets the tone with the game
   name, a scenic background, and a clear start button. The player hits start
   and arrives in a small town -- a hub with a healer, a trainer NPC, and a
   path leading into the wilds.

2. **Open-World Exploration** -- The player walks freely across a large map
   with at least three visually distinct regions: grassy fields, a small town,
   and a locked area beyond a natural barrier. Tall grass signals danger:
   stepping into it has a chance to trigger a wild creature encounter. The
   world reads clearly at a glance -- each region has its own terrain, palette,
   and props.

3. **Encounter and Battle** -- A brief transition effect whisks the player into
   a turn-based combat scene. The player sees both combatants with HP bars,
   levels, and skill buttons. Attacking triggers visible motion and animated HP
   depletion. The player can also throw a capture ball (visible arc, shake
   animation, success/failure feedback) or flee. Wild creatures vary in species
   and level.

4. **Growth and Progression** -- Defeating opponents yields experience; the
   creature levels up with visible feedback when enough XP accumulates. The
   player's squad grows stronger over time, and captured creatures join the
   roster.

5. **NPC Interaction** -- In town, a trainer challenges the player to a forced
   battle, and a healer restores the squad. Dialog appears in a styled speech
   panel. Defeating the gym leader awards a badge that unlocks the previously
   blocked region, opening new territory to explore.

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