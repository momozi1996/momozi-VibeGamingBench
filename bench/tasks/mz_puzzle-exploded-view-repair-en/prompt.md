# Zero-G Exploded View

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

An interactive 3D inspection and repair puzzle built around the exploded view of a precision drone or camera. The player disassembles the device, examines labeled components, diagnoses faults, and restores the assembly in the correct order.

## Required Playable Systems

1. **System 1** - Drive a smooth exploded-view amount with a slider and mouse wheel, giving component groups distinct spring and damping responses.
2. **System 2** - Support orbit, zoom, hover highlighting, isolation, and pinned 3D labels that remain readable and point to the correct moving part.
3. **System 3** - Create an inspection puzzle where players identify faulty components through visual clues, diagnostic readings, and functional descriptions.
4. **System 4** - Require a valid disassembly and reassembly order with tool selection, dependency checks, snap previews, and invalid-action feedback.
5. **System 5** - Include multiple device modules or fault scenarios involving optics, power, control boards, motors, cooling, and structural parts.
6. **System 6** - Verify the repair with a playable system test and show performance differences based on diagnosis and assembly accuracy.

## Progression

New repair jobs add denser assemblies, subtler faults, calibration steps, and optional efficiency challenges.

## Art Direction

Premium industrial visualization with brushed metal, transparent plastic, rubber, glass optics, studio lighting, crisp outlines, and restrained technical labels.

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
