# Lantern Keeper of the Drifting Isles

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A traversal and restoration game across floating islands whose guiding lanterns are going dark. The player pilots a small glider between moving landmasses, relights a navigation network, and keeps isolated communities connected through dangerous weather.

## Required Playable Systems

1. **System 1** - Glide, climb, and dock across at least five drifting islands whose relative positions and reachable routes change over time.
2. **System 2** - Repair and relight lantern towers through hands-on mechanisms involving lenses, fuel, alignment, and timed ignition sequences.
3. **System 3** - Use the illuminated network for navigation: active beams reveal safe wind lanes, hidden islands, and emergency routes.
4. **System 4** - Gather fuel and repair materials through exploration, delivery jobs, and environmental traversal challenges.
5. **System 5** - Protect lanterns from storms and airborne creatures using steering, temporary shields, signal flares, and rapid maintenance.
6. **System 6** - Restore a full route across the archipelago and complete a final storm crossing that reflects which communities were connected.

## Progression

Upgraded glider wings, fuel tanks, lenses, and weather instruments expand range and allow access to higher, faster-moving islands.

## Art Direction

Hopeful sky-fantasy with painterly clouds, warm lantern gold, cool storm fronts, miniature island ecosystems, and elegant wind-stream visualization.

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