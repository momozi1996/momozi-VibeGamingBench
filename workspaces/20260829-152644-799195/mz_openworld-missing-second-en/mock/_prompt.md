# The Missing Second

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A compact open-city investigation game about a superhero who vanished during one impossible missing second. The player patrols several connected districts, reconstructs frozen incidents, and decides whether the city's celebrated rescue was actually a coordinated cover-up.

## Required Playable Systems

1. **System 1** - Explore at least three connected city districts, move freely between rooftops and streets, and locate temporal anomaly scenes through a scanner.
2. **System 2** - Reconstruct each missing-second scene by rotating a time echo, matching evidence positions, and locking a plausible sequence before the timer expires.
3. **System 3** - Interview witnesses whose testimony changes with trust and discovered evidence, then connect clues on an interactive conspiracy board.
4. **System 4** - Include multiple anomaly types, such as displaced vehicles, duplicated civilians, frozen projectiles, and corrupted security drones.
5. **System 5** - Track public trust and institutional suspicion; accusations, leaked evidence, and reckless scanning must change NPC reactions and available routes.
6. **System 6** - End with a playable confrontation where the player selects and proves one of several theories, producing visibly different city outcomes.

## Progression

Solving district cases upgrades scan range and time-echo control, opens restricted locations, and unlocks increasingly complex reconstructions.

## Art Direction

A rain-slick near-future metropolis with cyan forensic projections, amber street lighting, graphic-novel shadows, and sharp temporal fracture effects.

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