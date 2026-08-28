# Vector Corporation: The Endless Office

Build a complete, playable **3D open-world adventure game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

An invisible office worker tries to terminate a contract and escape an impossible corporate building using camouflage and a reality-bending stapler.

## World Parameters

Treat this as an original adaptation of a **surrealism** shared world with **large** scope and a **surreal** tone. Do not reproduce commercial characters, names, lore, logos, or protected visual designs.

## Required Playable Systems

1. **System 1** - Explore at least three connected locations adapted from Vector Corporation: The Endless Office, each with a landmark, local objective, hazard, and unlockable route.
2. **System 2** - Combine traversal, local jobs, environmental interaction, and spontaneous events so each district offers a different way to make progress.
3. **System 3** - Introduce distinct characters or factions whose schedules, trust, hostility, and available help respond to player behavior.
4. **System 4** - Track route access, local danger, favors, supplies, attention, and district state while optional events compete with the main objective.
5. **System 5** - Persist discoveries, relationships, altered locations, depleted resources, and unresolved consequences throughout the run.
6. **System 6** - Conclude with a mastery objective or confrontation that combines traversal, the primary challenge, relationships, and accumulated world state.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

Distinct district identities, visible traversal routes, authored landmarks, reactive inhabitants, and world changes that remain visible after choices.

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
