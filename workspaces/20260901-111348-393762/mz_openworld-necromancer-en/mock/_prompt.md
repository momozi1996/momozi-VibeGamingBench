# Open-World Necromancer

Build an **Open-World Necromancer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a necromancer wandering a dark fantasy world, raising the dead from
fallen enemies to build an ever-growing undead army. The fantasy is forbidden
power: every battlefield becomes a recruitment ground, every graveyard a goldmine.
Tension comes from hero NPCs who hunt you — paladins, witch-hunters, and
adventuring parties that grow stronger as your infamy rises. You must conquer
territory, fortify positions with undead garrisons, and choose which minions to
raise based on the corpses available.

## What the Player Experiences

1. **Title Screen** — A dark, atmospheric title with the game name in gothic
   lettering over a misty graveyard scene. A play button pulses with eerie light.
2. **The World** — The player moves freely across a dark open world with villages,
   graveyards, forests, and ruined keeps. Each area has different enemy types and
   corpse quality.
3. **Combat** — Enemies (guards, militia, wildlife) attack on sight. The player
   has a dark magic attack and commands their undead minions to fight. Combat is
   real-time with simple click-to-attack and ability hotkeys.
4. **Raising the Dead** — After enemies fall, their corpses remain on the ground.
   The player channels a raise spell on corpses to add them to their army. Different
   corpse types yield different undead: skeleton warriors, zombie brutes, spectral
   archers.
5. **Army Management** — A minion panel shows the current army composition, health,
   and count. The player can dismiss weak undead to make room for stronger ones.
   Army size is capped by the player's necromantic power level.
6. **Territory Conquest** — Capturing a village or keep turns it into a dark
   stronghold. Garrisoned undead defend it. Conquered territory generates soul
   energy over time.
7. **Hero Hunters** — As infamy grows, hero NPCs spawn and hunt the player. They
   are powerful, have unique abilities, and require strategy to defeat. Defeating
   them yields elite corpses.

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