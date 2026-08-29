# Festival Committee Disaster

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A comedic open-village management game about staging a major festival while every committee member creates a new crisis. The player runs between venues, schedules activities, solves local incidents, and tries to preserve both the celebration and community trust.

## Required Playable Systems

1. **System 1** - Explore a connected village with at least four festival venues, vendor streets, storage areas, and shortcuts that open during setup.
2. **System 2** - Place stalls, decorations, stages, power lines, and crowd barriers while respecting space, budget, access, and safety constraints.
3. **System 3** - Build a timed event schedule and personally complete short playable activities such as parade routing, cooking, music cues, or fireworks setup.
4. **System 4** - Handle dynamic incidents including weather, missing supplies, animal escapes, performer conflicts, outages, and crowd congestion.
5. **System 5** - Manage committee-member trust, vendor satisfaction, attendance, budget, and safety through visible consequences rather than text-only reports.
6. **System 6** - Run the final festival day from opening to closing ceremony, with success, partial failure, or comic catastrophe states.

## Progression

Completed preparations unlock better equipment and volunteer abilities, while unresolved incidents carry forward and complicate the final day.

## Art Direction

Cheerful handcrafted low-poly village art with colorful bunting, varied stalls, expressive characters, readable crowd flow, and slapstick event effects.

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