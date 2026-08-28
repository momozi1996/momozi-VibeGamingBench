# Enchanted Block Path

Build a complete, playable **2D puzzle game** as
a polished browser vertical slice from a **top down** viewpoint.

## Core Vision

A dreamlike forest puzzle about dragging constrained blocks to reconnect paths and awaken energy nodes in few moves.

## Required Playable Systems

1. **System 1** - Drag blocks with grid snapping, collision, movement limits, and clear invalid-action feedback.
2. **System 2** - Detect connected paths and energy-node activation from the actual board state.
3. **System 3** - Track moves and time, compare against a target solution, and support undo, hint, and reset.
4. **System 4** - Provide at least three layouts with distinct constraints and persistent level progress.
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

A calm and precise visual language with distinct state colors, clean spatial grouping, smooth transformations, and no obscured puzzle information.

## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use HTML Canvas 2D or Three.js/WebGL for the playable presentation.
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
