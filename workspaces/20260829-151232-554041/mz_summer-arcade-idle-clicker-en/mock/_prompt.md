# Idle Clicker

Build a complete, playable **2D arcade and casual game** as a polished
browser vertical slice, presented from a **front facing** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on Click handler and resource counter, Generator and cost-scaling system, Idle and offline earnings, and Prestige and permanent bonuses. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - Click handler and resource counter**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - Generator and cost-scaling system**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - Idle and offline earnings**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - Prestige and permanent bonuses**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: Click handler granting the primary resource; Resource counter with large-number formatting (K, M, B, e-notation); Generator tiers with per-second production; Cost-scaling curve per generator (geometric growth); Upgrade system: output multipliers and cost reducers; Idle and offline earnings calculation on resume; Prestige reset granting a permanent multiplier currency; Achievement system with milestone bonuses.
6. **Playable breadth and outcome**: Provide a short session with escalating pace, score and combo logic, at least three challenge patterns, a high-score result, and an immediate replay flow.

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

Immediate arcade readability, energetic motion, saturated accents against a restrained background, and celebratory score and combo feedback.

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