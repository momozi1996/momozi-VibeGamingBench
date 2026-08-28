# Voxel Tower Defense

Build a complete, playable **3D strategy game** as a polished browser vertical slice.

## Core Vision

A bright voxel tower-defense game on a miniature island. Players place and upgrade towers while enemies use A* to route around terrain and legal obstacles, creating a tactical relationship between construction and path shape.

## Required Playable Systems

1. **System 1** - Allow pointer-based tower placement on a voxel grid with ghost previews, range indicators, cost checks, smoke particles, and a landing bounce.
2. **System 2** - Move enemies with A* pathfinding from spawn to base, recalculating legal routes after placement and rejecting constructions that fully block the path.
3. **System 3** - Implement at least three tower types with distinct targeting, laser or projectile behavior, damage roles, cooldowns, and upgrade branches.
4. **System 4** - Run multiple waves with several enemy types, escalating stats, rewards, base health, victory, defeat, pause, and speed controls.
5. **System 5** - Add destructible or changing terrain, branching lanes, and tactical tiles that influence range, speed, or damage.
6. **System 6** - Create volumetric-looking hit and death explosions, readable health feedback, economy UI, and a complete results/retry flow.

## Progression

New islands introduce route constraints, tower synergies, enemy resistances, and persistent unlock choices across a short campaign.

## Art Direction

A polished pastel voxel diorama with lush terrain, toy-like towers and enemies, crisp laser lines, chunky smoke, and colorful volumetric explosions.

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
