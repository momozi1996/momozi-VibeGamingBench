# The Last Reservoir

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A drought-management exploration game around the final functioning reservoir. The player travels between settlements, inspects infrastructure, and returns to a council chamber to allocate water before climate events turn political compromise into physical survival.

## Required Playable Systems

1. **System 1** - Explore the reservoir basin and at least four connected districts, inspecting pumps, canals, wells, farms, and damaged treatment equipment.
2. **System 2** - Operate a physical water-control board with valves and allocation sliders that visibly redirect animated flow through the 3D map.
3. **System 3** - Balance reservoir volume, contamination, pressure, and district demand across a changing multi-day forecast.
4. **System 4** - Negotiate with factions whose needs and trust change based on inspections, promises, shortages, and previous allocations.
5. **System 5** - Respond to fires, pipe failures, dust storms, and illegal tapping through timed field missions and emergency rerouting.
6. **System 6** - Finish with a council vote and final drought event whose playable outcome reflects both infrastructure and social legitimacy.

## Progression

Repairs and negotiated agreements unlock efficient infrastructure, better forecasts, and new allocation options while permanently changing district resilience.

## Art Direction

A sun-bleached low-poly basin with cracked earth, turquoise flow overlays, weathered civic machinery, heat haze, and urgent red emergency lighting.

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