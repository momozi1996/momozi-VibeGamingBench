# The 3D Terminal

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

A command-driven 3D puzzle adventure inside a floating cyberpunk terminal. Typed commands alter the surrounding simulation: launching machines, routing energy, moving platforms, decoding matrices, and triggering dramatic spatial feedback.

## Required Playable Systems

1. **System 1** - Implement a real command parser with history, help, autocomplete or suggestions, arguments, aliases, and clear unknown-command handling.
2. **System 2** - Connect commands to visible 3D systems such as launching a rocket, opening sectors, rotating code matrices, routing power, and moving a drone.
3. **System 3** - Build multi-step missions where players inspect state, infer valid commands, combine arguments, and observe persistent consequences.
4. **System 4** - Use strong feedback: successful commands animate the world, launches create procedural smoke, and invalid commands shake or glitch the space.
5. **System 5** - Provide discoverable logs, hidden commands, optional objectives, command documentation, and at least three linked mission chapters.
6. **System 6** - Track objective state, terminal access level, errors, discovered commands, and completion, with restart and safe recovery from bad input.

## Progression

Completing missions raises terminal access, unlocks new command namespaces, and exposes more of the surrounding 3D machine.

## Art Direction

A black-void cyberpunk command chamber with glass terminal planes, magenta/cyan matrices, volumetric smoke, emissive machinery, and controlled glitch effects.

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
