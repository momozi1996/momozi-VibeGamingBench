# Luma and the Lost Rainbow

Build a complete, playable **3D adventure and exploration game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

A silver unicorn recovers a missing rainbow glow by traveling through the woods, helping friends, and restoring color through kindness.

## World Parameters

Treat this as an original adaptation of a **adventure** shared world with **small** scope and a **lighthearted** tone. Do not reproduce commercial characters, names, lore, logos, or protected visual designs.

## Required Playable Systems

1. **System 1** - Explore at least three connected story locations from Luma and the Lost Rainbow with direct movement, inspectable landmarks, and unlockable routes.
2. **System 2** - Solve multiple spatial, sequence, or inventory puzzles whose state is represented in the rules layer.
3. **System 3** - Talk with distinct characters and make choices that alter trust, available help, and later scene objectives.
4. **System 4** - Collect or create meaningful objects that change navigation, puzzle solutions, or character outcomes.
5. **System 5** - Persist discovered facts, relationships, changed locations, and completed favors so later scenes acknowledge earlier actions.
6. **System 6** - Finish a playable final scene that combines exploration, puzzle, and relationship decisions into visibly different outcomes.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

Memorable landmarks, layered routes, environmental storytelling, useful lighting guidance, and distinct interaction states.

## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use Three.js and WebGL for the playable presentation.
- `game_logic.js` - the deterministic state and rules layer, exporting
  `createGame(opts)` and `advance(game, input, dt)`.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Use procedural geometry, generated textures, shaders,
particles, synthesized audio, and CSS. Do not fetch external images, models,
video, or audio at runtime. Three.js may be loaded from its official CDN when
used; pin any permitted library to a specific version.

Support keyboard and pointer input, with touch or gamepad added where appropriate.
Keep the complete play area and HUD readable at 1280x720. Include a styled start
flow, concise in-game guidance, pause and restart controls, a complete outcome
loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.