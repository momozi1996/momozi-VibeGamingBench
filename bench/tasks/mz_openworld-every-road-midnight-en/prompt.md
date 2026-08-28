# Every Road Returns Before Midnight

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A surreal road-loop exploration game. Every route taken across a lonely region folds back toward the same motel before midnight, while landmarks subtly decay and memories persist between loops. The player must map contradictions and break the topology.

## Required Playable Systems

1. **System 1** - Drive and walk through a connected road network with at least four distinct landmarks, branching junctions, and navigable interiors.
2. **System 2** - Run a visible day-to-midnight loop in which roads reconnect differently while selected evidence, map annotations, and player knowledge persist.
3. **System 3** - Let the player place map pins and compare road lengths, signs, shadows, and landmark states to identify impossible connections.
4. **System 4** - Introduce changing hitchhikers, radio broadcasts, weather, and roadside hazards that reveal different clues on later loops.
5. **System 5** - Track vehicle condition, fuel, fatigue, and a distortion meter that changes controls and scenery as midnight approaches.
6. **System 6** - Provide several topology-breaking solutions that require performing a learned route sequence before the final midnight reset.

## Progression

Each verified contradiction unlocks new map tools and memory anchors, allowing more state to persist and exposing deeper routes.

## Art Direction

Dreamlike nocturnal Americana with wet asphalt, sodium lights, analog dashboard glow, impossible horizon folds, and escalating spatial distortion.

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
