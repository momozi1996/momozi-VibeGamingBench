# Neon Gravity Marble Run

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

A tactile 3D neon marble labyrinth controlled by keyboard tilt or device orientation. Real gravity, collisions, moving geometry, and momentum are the puzzle; the player learns to bank, brake, and redirect the ball through increasingly dangerous transparent courses.

## Required Playable Systems

1. **System 1** - Simulate the marble with Cannon.js, including gravity, rolling acceleration, restitution, friction, ramps, rails, and physically credible collisions.
2. **System 2** - Support arrow-key tilt and device orientation with calibration, sensitivity control, and an always-available desktop fallback.
3. **System 3** - Create collision feedback with camera impulse, sparks, sound, and Vibration API on supported devices without making input unreadable.
4. **System 4** - Provide at least three courses with checkpoints, moving platforms, launch pads, narrow rails, hazards, collectibles, and finish gates.
5. **System 5** - Track time, falls, checkpoint progress, best run, and optional pickups, with quick recovery after leaving the course.
6. **System 6** - Use speed-sensitive trails or postprocessing to communicate motion blur and increasing danger at high velocity.

## Progression

Later courses introduce stronger gravity, rotating frames, polarity zones, and branching risk/reward routes while preserving deterministic resets.

## Art Direction

A dark synthwave void with translucent emissive tracks, contrasting hazard colors, luminous particles, glossy marbles, and restrained bloom.

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