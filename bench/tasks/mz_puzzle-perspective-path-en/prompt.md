# Perspective Path

Build a complete, playable **3D puzzle game** as a polished browser vertical slice.

## Core Vision

An orthographic 3D puzzle game about impossible architecture. The player rotates a sculptural building until separated paths overlap on screen, creating temporary walkable connections for a small character.

## Required Playable Systems

1. **System 1** - Rotate an orthographic camera around a 3D monument with snapped and free-drag controls while preserving stable framing and depth order.
2. **System 2** - Detect screen-space alignment between path endpoints and enable traversal only while geometric and occlusion conditions are valid.
3. **System 3** - Let the player click reachable nodes to move a character along connected routes, blocking invalid moves with clear feedback.
4. **System 4** - Provide at least six escalating puzzles using rotating towers, movable bridges, elevators, switches, occluders, and multiple alignment steps.
5. **System 5** - Include undo, restart, camera reset, selected-node highlighting, optional hints, and deterministic puzzle state.
6. **System 6** - Complete each level by carrying or activating a goal object, then unlock a level-select path through the monument.

## Progression

New chapters introduce layered alignment rules, moving parts, split characters, and simultaneous path conditions while teaching each mechanic visually.

## Art Direction

A calm architectural diorama with clean stone, jewel-like accents, soft shadows, impossible silhouettes, and minimal illustrated UI.

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
