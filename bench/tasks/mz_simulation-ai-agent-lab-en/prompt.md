# AI Agent Evolution Lab

Build a complete, playable **3D simulation game** as a polished browser vertical slice.

## Core Vision

A controlled 3D behavioral sandbox inside a transparent glass habitat. Several autonomous agents sense resources, hazards, temperature, and gravity; the player changes the environment and runs scored experiments to observe adaptation rather than watching random motion.

## Required Playable Systems

1. **System 1** - Simulate multiple autonomous agents with visible goals, sensing range, energy, memory, and behavior-state transitions such as explore, seek, avoid, rest, and cooperate.
2. **System 2** - Let players adjust temperature, gravity magnitude and direction, resource density, hazard level, and time scale with responsive controls.
3. **System 3** - Click an agent to inspect its current perception, target, energy, recent decisions, and trajectory, highlighting sensed objects in the habitat.
4. **System 4** - Display live charts for entropy, population energy, movement diversity, collisions, resource use, and agent-state distribution.
5. **System 5** - Provide repeatable experiment scenarios with hypotheses and success conditions, plus seeded reset and side-by-side result comparison.
6. **System 6** - Make environmental changes visibly affect trajectories and group behavior without instantly teleporting or directly scripting agents.

## Progression

Completed experiments unlock new sensors, agent traits, environment presets, and more complex multi-variable research objectives.

## Art Direction

A clean scientific glass-box diorama with soft laboratory lighting, distinct agent colors, translucent sensor cones, plotted trajectories, and precise dashboard graphics.

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
