# Aether Deck Duel

Build a complete, playable **2D card strategy game** as
a polished browser vertical slice from a **top down** viewpoint.

## Core Vision

A fantasy card duel connects drawing, mana, targeting, status resolution, deck construction, and deterministic turn phases.

## Required Playable Systems

1. **System 1** - Draw, select, target, and play cards through clear turn phases and valid-action checks.
2. **System 2** - Resolve attack, defense, damage-over-time, buff, and debuff effects in deterministic order.
3. **System 3** - Manage mana, hand limits, discard, draw pile, and hoverable card details.
4. **System 4** - Build or edit a deck between battles and complete a full opponent, victory, defeat, and rematch loop.
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

Readable cards, deliberate table composition, expressive state changes, clear targeting, and satisfying draw, play, and resolve animation.

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
