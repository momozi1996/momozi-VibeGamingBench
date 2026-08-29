# Academy of Forgotten Students

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A magical campus mystery where students are being erased from records and memory. The player freely explores halls, towers, gardens, and sealed archives, preserving unstable memories before the academy rewrites itself around each disappearance.

## Required Playable Systems

1. **System 1** - Explore at least four connected campus zones with day/night schedules, moving stairways, secret doors, and student routines.
2. **System 2** - Use a memory lens to reveal erased people, reconstruct shared moments, and pin unstable memories before they dissolve.
3. **System 3** - Cross-reference portraits, attendance ledgers, dorm objects, and witness recollections in a searchable archive interface.
4. **System 4** - Build trust with rival student groups whose memories conflict and whose cooperation opens different investigation routes.
5. **System 5** - Avoid or confront corrective magical entities that alter corridors and remove collected evidence when the player is detected.
6. **System 6** - Identify the erasure mechanism and choose whom or what to restore in a final ritual with multiple campus-wide outcomes.

## Progression

Preserved memories strengthen the lens, reveal deeper historical layers, and unlock spells for stabilizing spaces and protecting evidence.

## Art Direction

Whimsical gothic academia with luminous ink, moving portraits, moonlit courtyards, impossible staircases, and dissolving paper-particle memory effects.

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