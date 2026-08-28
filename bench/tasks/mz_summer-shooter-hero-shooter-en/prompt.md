# Hero Shooter

Build a complete, playable **3D shooter game** as a polished
browser vertical slice, presented from a **first person** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Hero selection and roster system, Ability and cooldown system, Objective-based match modes, and Team role system. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Hero selection and roster system**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Ability and cooldown system**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Objective-based match modes**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Team role system**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Hero roster with per-hero weapon, abilities, and stats; Cooldown and ultimate charge system; Role system: tank, damage, support; Control point ownership and capture progress system; Payload escort movement and blocking system; Respawn wave timer; Hero select screen with team composition view; Match replay and stat summary.
6. **Playable breadth and outcome**: Provide at least three enemy archetypes, weapon or ability tradeoffs, escalating waves or spaces, readable damage and ammunition state, and a final objective with victory, defeat, and retry.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Readable targets and projectiles, disciplined muzzle and impact effects, strong cover silhouettes, useful depth cues, and camera treatment that supports aiming.

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
