# Auto-Combat Survivors

Build a complete, playable **2D action and fighting game** as a polished
browser vertical slice, presented from a **top down** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Auto-attack weapon system, XP gem collection and level-up screen, Enemy horde spawner with timeline, and Passive item and upgrade system. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Auto-attack weapon system**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - XP gem collection and level-up screen**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Enemy horde spawner with timeline**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Passive item and upgrade system**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Auto-attack weapon system with configurable targeting; XP gem drop and attraction radius system; Level-up upgrade selection screen (pause, pick 1 of 3); Enemy spawn timeline with minute-by-minute escalation; Passive item system with stat modifications; Weapon evolution system (max level weapon + specific passive = evolved weapon); 30-minute run timer with final boss at end; Gold and treasure chest drop system.
6. **Playable breadth and outcome**: Include at least three opponents or fighter archetypes, escalating encounters, defensive and offensive choices, and a final match or boss with victory, defeat, and rematch states.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Bold combat silhouettes, readable hit flashes, strong anticipation poses, impact particles, and arenas whose hazards remain legible during fast motion.

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

Support keyboard and pointer input, with gamepad or touch added where appropriate.
Keep the complete play area and HUD readable at 1280x720. Include a styled start
flow, concise in-game guidance, pause and restart controls, a complete outcome
loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.