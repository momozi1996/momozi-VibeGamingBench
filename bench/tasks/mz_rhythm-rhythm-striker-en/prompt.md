# Rhythm Striker

Build a complete, playable **3D rhythm-action game** as a polished browser vertical slice.

## Core Vision

A minimal 3D rhythm game inside an endless emissive tunnel. Geometric targets arrive on musical beats; accurate key strikes shatter them into physical debris while the tunnel, materials, and camera react to synthesized audio.

## Required Playable Systems

1. **System 1** - Spawn geometric beat targets in multiple lanes and judge key input with Perfect, Good, and Miss timing windows tied to a deterministic chart.
2. **System 2** - Use Web Audio API synthesis and an analyser so emissive materials, tunnel segments, and camera impulses respond to current frequency bands.
3. **System 3** - Shatter successful targets into velocity-aware physical fragments while misses pass the player and cause a distinct tunnel distortion.
4. **System 4** - Implement combo, multiplier, score, health, song progress, pause, retry, and a results screen with timing breakdown.
5. **System 5** - Provide at least three charts or difficulty modes with distinct rhythms, speeds, lane patterns, and visual identities.
6. **System 6** - Keep timing readable despite bloom, camera motion, debris, and audio-reactive effects; accessibility settings must reduce shake and flash.

## Progression

Clearing charts unlocks denser patterns, hold targets, alternating strike directions, and cosmetic tunnel themes without compromising deterministic timing.

## Art Direction

A restrained neon tunnel with black negative space, strong lane colors, emissive geometry, frequency-reactive surfaces, and crisp impact typography.

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
