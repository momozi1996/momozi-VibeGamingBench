# The Warp Stranger

Build a complete, playable **3D strategy game** as
a polished browser vertical slice from a **third person** viewpoint.

## Core Vision

A psychic space soldier is stranded in a medieval fantasy realm and builds a reputation through guild quests, alliances, conquests, and unsettling future technology.

## World Parameters

Treat this as an original adaptation of a **high-fantasy** shared world with **huge** scope and a **epic** tone. Do not reproduce commercial characters, names, lore, logos, or protected visual designs.

## Required Playable Systems

1. **System 1** - Explore at least three connected districts or territories from The Warp Stranger, each with distinct opportunities, hazards, and ownership state.
2. **System 2** - Complete jobs through negotiation, trade, tactical conflict, or service to earn reputation with transparent gain and loss rules.
3. **System 3** - Manage at least three factions whose trust, hostility, alliances, and control change after persistent player choices.
4. **System 4** - Balance health, resources, influence, and attention while territory events continue to evolve without waiting for the player.
5. **System 5** - Persist reputation, faction relations, owned or protected locations, depleted resources, and unresolved consequences across the whole run.
6. **System 6** - Reach a playable influence milestone that combines territory, faction, resource, and reputation systems, then support continued play or a scored conclusion.

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

A scan-friendly tactical field, distinct roles, visible ranges and ownership, restrained effects, and information hierarchy for repeated decisions.

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
