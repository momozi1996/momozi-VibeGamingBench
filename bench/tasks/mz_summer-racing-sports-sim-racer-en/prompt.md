# Sim Racer

Build a complete, playable **3D racing and sports game** as a polished
browser vertical slice, presented from a **first person** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Physics simulation with tire model, Vehicle setup editor, Race weekend structure, and Multiplayer with anti-cheat and steward system. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Physics simulation with tire model**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Vehicle setup editor**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Race weekend structure**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Multiplayer with anti-cheat and steward system**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Physics model with tire temperature and wear; Aerodynamic downforce simulation; Vehicle setup editor with help system; Track grip evolution and rubber buildup; Dynamic weather with grip changes; Race weekend structure (practice, qualifying, race); Pit stop and strategy system; Driver rating and incident point system.
6. **Playable breadth and outcome**: Include a complete event with practice or setup, at least three competitors or challenge tiers, rule-valid scoring, escalating pressure, final standings, and replay.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Strong speed and trajectory cues, readable competitors, clear field markings, dynamic cameras, and replay-worthy finish, collision, and scoring moments.

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
