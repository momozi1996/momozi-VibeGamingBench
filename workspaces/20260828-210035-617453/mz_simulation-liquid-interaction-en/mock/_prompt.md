# Liquid Interaction Lab

Build a complete, playable **3D simulation game** as a polished browser vertical slice.

## Core Vision

A playable real-time particle-fluid laboratory centered on a sphere of roughly ten thousand particles. The player repels and attracts the fluid to complete shape, containment, and energy challenges while learning how velocity and force alter the system.

## Required Playable Systems

1. **System 1** - Simulate approximately 10,000 particles through GPGPU or an equivalent GPU texture technique, with a graceful lower-count fallback.
2. **System 2** - Use pointer movement as a repulsive force and pointer press as an attractive force, with radius and strength controlled by readable UI.
3. **System 3** - Map particle color continuously from cool to warm based on velocity and show force direction, center of mass, and turbulence feedback.
4. **System 4** - Provide playable challenge modes for forming target silhouettes, moving fluid through rings, containing an unstable core, and restoring equilibrium.
5. **System 5** - Track stability, escaped particles, energy use, target accuracy, and elapsed time, with reset and slow-motion experimentation controls.
6. **System 6** - Maintain smooth interaction and clear input response under load, automatically adjusting quality without changing game-state rules.

## Progression

Completing experiments unlocks multi-source force fields, vortices, obstacles, viscosity presets, and more demanding target shapes.

## Art Direction

An elegant black laboratory void with luminous fluid color gradients, subtle grids, glass target volumes, and precise scientific UI.

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