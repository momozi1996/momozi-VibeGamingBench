# Idle Spell Tower

Build an **Idle Spell Tower** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds a wizard's tower that generates mana passively, researches
spells, and automates magical casting for ever-increasing power. The fantasy is
arcane accumulation: watching mana flow from crystal to crystal, spells firing
automatically at targets, and the tower growing taller with each prestige cycle.
The idle loop generates mana continuously; the player's decisions shape which
spells to research and how to allocate mana between offence, defence, and
growth. Prestige collapses the tower and rebuilds it higher with better
foundations.

## What the Player Experiences

1. **Title Screen** — A tall wizard tower against a starry sky with magical
   particles flowing upward, the game name in arcane script, and a play button
   glowing with mana.
2. **Tower View** — A vertical tower cross-section showing floors. Each floor
   has a function: mana generators, spell labs, crystal storage, automated
   casters. The tower grows as floors are added.
3. **Mana Generation** — Base mana ticks up automatically. Mana generators on
   each floor contribute to the rate. The player can click a crystal to manually
   generate bursts. A large mana counter dominates the UI.
4. **Spell Research** — A research tree shows available spells. Each spell costs
   mana and time to research. Researched spells can be assigned to auto-casters
   or cast manually for immediate effect.
5. **Automated Casting** — Auto-caster floors fire spells at targets (monsters
   approaching the tower base) without player input. Each caster has a rate and
   spell assignment. Defeating monsters yields mana crystals.
6. **Tower Growth** — Spending mana builds new floors, each with a specific
   function. Higher floors generate more mana but cost exponentially more. The
   tower visually grows taller.
7. **Prestige** — When the tower reaches maximum height, the player can collapse
   it (prestige). The tower resets to one floor but gains a permanent height
   multiplier, faster mana generation, and access to higher-tier spells. Each
   rebuild reaches greater heights faster.

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