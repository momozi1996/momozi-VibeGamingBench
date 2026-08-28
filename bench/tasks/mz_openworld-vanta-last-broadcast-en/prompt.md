# Last Broadcast from Vanta

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A lonely space-exploration campaign across a small star system. The player pilots a salvage vessel toward a dead colony's repeating emergency signal while storms, failing systems, and contradictory recordings turn navigation into a survival mystery.

## Required Playable Systems

1. **System 1** - Pilot a ship across a navigable star map with manual thrust, docking, scanning, and at least three explorable orbital locations.
2. **System 2** - Tune a multi-band receiver to isolate fragments of the Vanta broadcast while interference and false echoes obscure the correct signal.
3. **System 3** - Manage hull, power, fuel, and heat by rerouting ship systems during radiation storms and debris encounters.
4. **System 4** - Recover logs and physical evidence from derelicts, then arrange them on a timeline that changes the meaning of the final message.
5. **System 5** - Include hazards and optional rescues that force tradeoffs between mission progress, crew safety, and dwindling resources.
6. **System 6** - Reach Vanta and complete one of several playable approaches to the beacon, with different discoveries and endings.

## Progression

Recovered components improve engines, scanner precision, and power capacity, enabling access to harsher regions and deeper signal layers.

## Art Direction

Hard-sci-fi solitude: dark planetary silhouettes, instrument-lit interiors, volumetric signal waves, electrical arcs, and pale emergency beacons.

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
