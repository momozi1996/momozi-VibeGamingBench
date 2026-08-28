# Roguelike: Relic Pinball

Build **Relic Pinball**, a compact **pinball / brick-breaker roguelite** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: an original, polished vertical slice about
navigating a cursed mechanical table one chamber at a time, breaking target
banks, triggering arcane mechanisms, and collecting relics that visibly mutate
the ball's behavior across an escalating run.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is exploring a cursed mechanical table one chamber at a time. Each
chamber is a live pinball board fused with brick-breaker structure: target rows,
bumpers, switches, lanes, gates, spinners, and special blocks create readable
goals while the ball remains fast and physical. The tension lives in flipper
timing and relic synergy — every launch is a gamble, every save a small
triumph, and every relic choice reshapes how the ball interacts with the world.
A ball might split on contact, burn through cracked bricks, curve toward metal
targets, leave scoring echoes, charge bumpers on pass-through, or orbit after
paddle hits. The tone is arcane arcade machine: brass rails, glass reflections,
carved stone bricks, luminous relic icons, bright impact sparks, and snappy
flipper feedback.

## What the Player Experiences

From the title screen the player sees a styled pinball-table motif with at
least one relic or magical ball identity hinting at what lies ahead.

The run drops the player into a live table. A ball launches into a bounded
playfield and the player works left and right flippers to keep it alive,
threading it through bumpers, lanes, and brick banks. Every collision feels
different — bumpers kick the ball away, bricks crack and shatter, switches
light up lanes, spinners charge multipliers, and portals warp the ball across
the board. The table is not a passive backdrop; it reacts.

Clearing enough targets or triggering the right mechanisms opens a relic
choice. The player picks from several relics, each with a name, icon, and
concise rule. The chosen relic immediately changes how the next chamber plays —
the ball splits, pierces, magnetizes, or leaves fire trails. The active relic
row persists and stacks, so the run builds toward a strange loadout that no
two attempts share.

Chambers grow harder: new layouts, tighter drains, armored targets, hazard
bumpers, and eventually a boss table whose special rule demands more than
reflexes. Victory or defeat lands on a styled result screen that lets the
player try again without restarting the application.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Keep the rules layer independent of DOM and rendering code.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.
