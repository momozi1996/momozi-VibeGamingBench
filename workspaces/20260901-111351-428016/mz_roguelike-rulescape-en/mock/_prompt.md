# Roguelike: Rulescape

Build **Rulescape**, a top-down **rules-horror roguelike survival game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a polished vertical slice where the player
navigates haunted public spaces, deciphers unstable rules, and escapes before
the site consumes them.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being trapped inside a place that was once ordinary -- a
hospital, a school, a subway station -- now governed by rules that shift,
corrupt, and lie. Survival depends on reading the environment, deducing which
rules are real, and acting before time runs out. The pressure comes from an
advancing timetable that changes what is safe, anomalies whose behavior is
tied to the local mystery, and the knowledge that obeying the wrong rule is as
deadly as breaking the right one. Each site is a story before it is a level:
its rooms, props, clues, and escape condition should feel like one connected
mystery, not a generic dungeon with swapped textures. The tone is frightening,
bloody, investigative, and oppressive.

## What the Player Experiences

1. **Title and Survivor Choice** -- The player arrives at a dark, themed title screen and selects a survivor from a small roster. Each survivor brings a different tool or instinct that changes how the player reads danger and interacts with the site.
2. **Entering the Site** -- The run drops the player into a top-down anomaly site -- a real-feeling place with rooms, corridors, locked doors, scattered props, and environmental storytelling. The site has its own name, visual identity, local mystery, and set of posted rules that the player can inspect in-world.
3. **The Timetable** -- A visible clock or schedule advances during exploration. When it reaches authored thresholds the site's rhythm changes: new areas unlock, anomalies shift behavior, rules become more dangerous, or an escape window opens.
4. **Exploration and Deduction** -- The player moves through the site, searches objects for clues and items, reads rules (some incomplete, misleading, or corrupted), and pieces together what is actually true. Anomalies appear as spatial threats tied to the site's rules; the player responds by fleeing, hiding, using items, or obeying the correct rule -- wrong choices cost health, sanity, or time.
5. **Resolution** -- Victory comes from satisfying the site's escape condition; defeat comes from a fatal anomaly encounter, rule violation, or resource collapse. The result screen explains what rule, clue, or decision sealed the outcome.

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