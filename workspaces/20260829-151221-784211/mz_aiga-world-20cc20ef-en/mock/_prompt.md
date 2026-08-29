# Legacy of the Eight Limbs

Build a complete, playable **3D action combat game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

A young martial artist trains across hidden Bangkok sites, investigates a missing master, and defends the city from threats ordinary people cannot see.

## World Parameters

Treat this as an original adaptation of a **urban-fantasy** shared world with **medium** scope and a **gritty** tone. Do not reproduce commercial characters, names, lore, logos, or protected visual designs.

## Required Playable Systems

1. **System 1** - Explore at least three connected locations adapted from Legacy of the Eight Limbs, each with a landmark, local objective, hazard, and unlockable route.
2. **System 2** - Build a responsive combat loop with directional attacks, defense or dodge timing, enemy telegraphs, stamina or ability limits, and readable hit states.
3. **System 3** - Introduce distinct characters or factions whose schedules, trust, hostility, and available help respond to player behavior.
4. **System 4** - Track health, stamina or focus, ability recovery, enemy pressure, and the consequences of mercy, aggression, or collateral damage.
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

Strong combat silhouettes, readable anticipation, restrained hit flashes, authored arenas, and impact animation that never hides hazards.

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