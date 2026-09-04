# Cardgame Autobattler

Build a Cardgame Autobattler as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A draft-and-watch autobattler where the player recruits creatures from a shared
shop each round, arranges them on a board, and watches them fight automatically
against an opponent's team. Strategy lives entirely in the draft phase: which
creatures to buy, when to level up for stronger units, and how to build
synergies between tribal tags. Creatures of the same tribe buff each other —
stack enough Beasts and they gain attack; fill a row with Undead and they
resurrect once. An 8-player elimination format (simulated against AI) creates
escalating pressure as the field narrows. The fantasy is assembling a dream
team from random offerings and watching your synergy engine demolish the
opposition.

## What the Player Experiences

1. **Title Screen** — A tavern interior with the game name on a wooden sign
   above the bar, creature silhouettes seated at tables, and a "Find Match"
   button styled as a tavern door. No plain HTML grey.
2. **Shop Phase** — Each round, a shop displays 3-5 random creatures for
   purchase. The player buys creatures (spending gold), places them on a
   bench or directly onto the board (limited slots). Selling creatures
   refunds partial gold. A timer counts down to the fight phase.
3. **Board Arrangement** — The player's board has a front row and back row.
   Positioning matters: front-row creatures are attacked first; back-row
   creatures with ranged attacks stay safe longer. Drag-and-drop placement.
4. **Auto Combat** — When the timer expires, the player's board fights an
   opponent's board automatically. Creatures attack in order, targeting the
   nearest enemy. Abilities trigger based on conditions (on-attack, on-death,
   start-of-combat). The fight plays out with attack animations and health
   bars depleting.
5. **Tribal Synergies** — At least 5 tribes (Beast, Undead, Mech, Dragon,
   Elemental). Having 2/4/6 of a tribe activates escalating bonuses shown in
   a synergy tracker panel. Synergies are the primary strategic axis.
6. **Economy** — Gold income increases each round. Winning streaks and losing
   streaks both grant bonus gold. Interest accrues on saved gold (1 gold per
   10 saved). Levelling up costs gold but increases shop quality and board
   size.
7. **Elimination** — The player starts with a health pool. Losing a round
   costs health proportional to surviving enemy creatures. Last player
   standing wins. A placement screen shows final ranking.

## Vibe Gaming Quality Bar

The gameplay, logic, and acceptance anchors above take priority over this
presentation contract. Do not rewrite or remove the core mechanics above; use
these rules to turn the same brief into a playable Vibe Gaming vertical slice.

- **Play first, polish second:** establish start, core input, state changes,
  success/failure, and replay before adding visual polish or effects.
- **Choose the smallest sufficient stack**:
  - `HTML5 Canvas 2D + Vanilla JS` for 2D rule-driven games;
  - `DOM + CSS + Vanilla JS` for card, dialogue, menu, and information-heavy games;
  - `pure SVG + CSS animation + Vanilla JS` for icons, diagrams, and geometric motion;
  - `PhaserJS` for continuous collision, cameras, particles, or arcade physics;
  - `Three.js + WebGL` for 3D or spatial camera experiences;
  - native `WebGPU` only when large-scale GPU parallelism or a custom GPU pipeline is genuinely required;
  - Canvas, DOM, CSS, and SVG may be mixed when each layer has a clear responsibility.
    Do not add complexity for technology spectacle.
- **Keep rules independent:** `game_logic.js` is the single source of truth and
  exposes `createGame(opts)` and `advance(game, input, dt)`. Rendering reads state;
  it must not maintain a second hidden rules system.
- **Make every frame explainable:** inputs map to explicit actions, actions
  produce observable state changes, and invalid input, edge cases, resource
  depletion, damage, victory, and failure are visible.
- **Vibe is not decoration:** use at least two feedback channels (animation,
  motion, scale, particles, audio, HUD, or camera) for important actions without
  obscuring the goal or reducing readability.
- **Mobile first:** pointer targets are at least 44×44 CSS px, touch and mouse
  both work, hover is never required, and 390×844, 360×800, 430×932, and
  1280×800 have no horizontal scrolling or overlapping controls.
- **Determinism and tests:** seed random content; verify the core rule, outcome
  conditions, restart/restoration, input boundaries, and at least one error state.
  Do not treat a screenshot or visible label as proof of functionality.
- **Originality and compliance:** use original names, characters, graphics,
  audio, and levels, or explicitly licensed assets. Do not copy trademarks,
  characters, text, artwork, music, level data, or source code.

Finish by reporting actual file paths, launch and test commands/results, key
screenshots, known limitations, stack tradeoffs, and original-asset provenance.

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
