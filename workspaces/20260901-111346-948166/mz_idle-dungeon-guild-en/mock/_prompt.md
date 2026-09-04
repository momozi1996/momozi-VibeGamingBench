# Idle Dungeon Guild

Build an **Idle Dungeon Guild** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player runs an adventurer's guild, sending heroes on automated dungeon quests
that yield loot and experience. The fantasy is the guild master: recruiting heroes,
equipping them with found gear, and watching them grow from novices to legends.
The idle loop sends parties into dungeons continuously; the player's decisions
shape party composition, equipment allocation, and guild upgrades. Prestige
retires the current generation of heroes and starts a new one with inherited
guild reputation bonuses.

## What the Player Experiences

1. **Title Screen** — A guild hall interior with a quest board and hero
   silhouettes, the game name in fantasy serif font, and a play button styled
   as a wax-sealed letter.
2. **Guild Hall** — The main view shows the guild hall with hero roster, quest
   board, equipment rack, and a reputation meter. Heroes mill about when not on
   quests.
3. **Hero Recruitment** — The player recruits heroes from a pool. Each hero has a
   class (warrior, mage, rogue, healer), stats, and a level. Heroes have distinct
   sprites per class.
4. **Quest Dispatch** — The quest board shows available dungeons with difficulty,
   duration, and reward preview. The player assigns a party (1-4 heroes) and
   sends them. A progress bar shows quest completion over time.
5. **Auto-Combat Results** — When a quest completes, a results screen shows loot
   found, experience gained, and any injuries. Heroes level up automatically.
   Better dungeons yield rarer loot.
6. **Equipment & Loot** — Found gear (weapons, armour, accessories) is assigned
   to heroes from the equipment rack. Better gear improves stats and enables
   harder dungeons. A comparison tooltip shows stat changes.
7. **Prestige (New Generation)** — When guild reputation maxes out, the player
   can prestige: retire all heroes, keep equipment and guild upgrades, and start
   with a new generation that levels faster. Each generation reaches higher
   dungeon tiers.

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