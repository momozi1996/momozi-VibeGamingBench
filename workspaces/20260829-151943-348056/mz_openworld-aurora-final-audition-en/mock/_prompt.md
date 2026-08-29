# Final Audition at Aurora Studio

Build a complete, playable **3D open-world adventure game** as a polished browser vertical slice.

## Core Vision

A supernatural exploration game set across an abandoned film studio. The player is an actor summoned for one final audition and must traverse connected sound stages where unfinished scenes replay themselves and the studio evaluates every performance.

## Required Playable Systems

1. **System 1** - Explore a studio backlot with at least three themed stages, backstage corridors, prop storage, and unlockable shortcuts.
2. **System 2** - Perform interactive audition scenes by hitting movement, dialogue, lighting, and camera marks in the correct dramatic sequence.
3. **System 3** - Manipulate rotating sets, spotlights, curtains, and practical effects to reveal paths and appease or provoke the studio presence.
4. **System 4** - Meet spectral cast members with distinct motives and recover production notes that alter scene objectives.
5. **System 5** - Track composure and audience approval; mistakes should distort sets, summon hazards, or rewrite the current scene.
6. **System 6** - Complete a final live take that combines previous mechanics and branches according to the roles and truths the player accepted.

## Progression

Successful takes earn role tokens that unlock new stage controls, costumes with abilities, and access to the sealed director's wing.

## Art Direction

Decaying golden-age cinema with dusty spotlights, velvet reds, monochrome projections, painted backdrops, and theatrical supernatural transitions.

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