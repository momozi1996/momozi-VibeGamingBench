# The Winter Clause

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A winter survival mystery inside and around a sprawling family estate. A will-reading locks the heirs in during an unnatural freeze, and the player must explore the house, manage heat, observe family routines, and uncover which clause controls the weather.

## Required Playable Systems

1. **System 1** - Explore a multi-floor mansion, greenhouse, frozen grounds, service tunnels, and weather-vane tower with unlockable shortcuts.
2. **System 2** - Manage room temperature by operating boilers, vents, fireplaces, shutters, and power circuits while fuel remains limited.
3. **System 3** - Observe and question family members whose schedules, alliances, and access permissions change after each discovered clause.
4. **System 4** - Solve inheritance puzzles using portraits, keys, legal documents, mechanical locks, and environmental temperature states.
5. **System 5** - Survive escalating cold effects such as frozen doors, brittle floors, blackouts, and blizzard exposure during exterior trips.
6. **System 6** - Reach the weather-vane mechanism and enforce, reinterpret, or destroy the final clause, producing different family outcomes.

## Progression

Recovered clauses and repaired heating zones expand safe exploration time, reveal hidden wings, and grant leverage in family negotiations.

## Art Direction

A snowbound gothic manor with warm candle interiors, icy blue encroachment, brass heating machinery, stained glass, and wind-driven snow effects.

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
