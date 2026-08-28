# Solarline Rally

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A solar-system racing adventure built around route choice rather than a single closed track. The player pilots a modular racer between orbital gates, balances heat and fuel, encounters rivals, and decides how much danger or compromise is acceptable to reach the final line.

## Required Playable Systems

1. **System 1** - Drive or fly a responsive 3D racer across at least three planetary regions with drifting, boost, braking, jumps, and checkpoint validation.
2. **System 2** - Choose branching routes on a navigable system map, trading distance against storms, gravity wells, tolls, and repair opportunities.
3. **System 3** - Manage fuel, battery, hull, and engine heat; overboosting must create visible performance loss and possible breakdown.
4. **System 4** - Race distinct rivals with recognizable vehicles and tactics, including drafting, blocking, shortcuts, and opportunistic rescues.
5. **System 5** - Collect sponsors, upgrades, and route intelligence through optional events that create meaningful mechanical tradeoffs.
6. **System 6** - Complete a multi-leg championship with standings, stage results, rival consequences, and at least two final outcomes.

## Progression

Between legs, players install mutually exclusive modules that alter handling, efficiency, durability, scanning, or boost behavior.

## Art Direction

Bright retro-futurist motorsport with saturated planetary skies, holographic gates, heat trails, modular vehicles, and readable cosmic route graphics.

## HTML Submission Format

Deliver a self-contained 3D browser game in two files:

- `index.html` - the complete playable presentation, rendered with Three.js.
- `game_logic.js` - the deterministic state and rules layer, exporting
  `createGame(opts)` and `advance(game, input, dt)`.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Use procedural geometry, shaders, particles, generated
audio, and CSS; do not fetch external images, models, video, or audio at runtime.
Three.js may be loaded from its official CDN. Any additional library explicitly
required by this task may also be loaded from a pinned CDN URL.

Support keyboard controls and the pointer. Touch or device-sensor controls may be
added where appropriate, but must have a desktop fallback. Keep the main game
readable at 1280x720. Include a styled title screen, short in-game guidance, pause
or restart controls, a complete win/loss or completion loop, and visible feedback
for every important action. This must feel like a polished vertical slice rather
than a passive scene or disconnected technical demo.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.