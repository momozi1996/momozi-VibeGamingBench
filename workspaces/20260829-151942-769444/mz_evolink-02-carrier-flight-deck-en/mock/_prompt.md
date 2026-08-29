# Carrier Flight-Deck Command

Build a complete, playable **3D simulation game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

A playable carrier-deck simulation asks the player to marshal aircraft, manage launch timing, and recover a returning plane safely.

## Required Playable Systems

1. **System 1** - Navigate a detailed carrier deck with orbit and first-person camera modes and clear spatial scale.
2. **System 2** - Direct deck crew markers and taxi aircraft through conflict-free staging positions.
3. **System 3** - Execute one complete launch sequence involving preparation, catapult timing, and safe deck clearance.
4. **System 4** - Recover an incoming aircraft by aligning the deck state, arresting zone, and weather window.
5. **System 5** - Provide at least three functionally distinct content variations that change timing, route choice, resource use, or risk rather than only labels and colors.
6. **System 6** - Use a three-stage arc that teaches the core interaction, combines systems under pressure, and ends in a complete win, loss, or scored completion loop.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

A coherent operational world with legible actors and machines, animated flows, state-driven color, and dense but organized management information.

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