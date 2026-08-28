# Infernal Loot Hunt

Build a complete, playable **3D role-playing game** as a polished
browser vertical slice, presented from a **isometric** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Isometric click-to-move combat, Color-coded item rarity system, Procedural dungeon generation, and Class and skill system. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Isometric click-to-move combat**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Color-coded item rarity system**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Procedural dungeon generation**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Class and skill system**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Click-to-move with ability hotbar (6-8 active skills); Color-coded item rarity: common, magic, rare, legendary, set, mythic; Randomized affix system: items roll random stat bonuses; Procedural dungeon tile generation with handcrafted tile sets; Class system with skill trees and passive nodes; Endgame rift/map system with escalating difficulty tiers; Elite monster modifiers: extra health, reflects damage, teleports; Inventory grid with item comparison tooltips.
6. **Playable breadth and outcome**: Include at least three encounter types, meaningful build or party choices, resources and status effects, progression between encounters, and a final objective with more than one viable strategy.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

A cohesive world identity, readable party and enemy roles, expressive abilities, layered locations, and progression changes that are visible on characters and equipment.

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

Support keyboard and pointer input, with gamepad or touch added where appropriate.
Keep the complete play area and HUD readable at 1280x720. Include a styled start
flow, concise in-game guidance, pause and restart controls, a complete outcome
loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.
