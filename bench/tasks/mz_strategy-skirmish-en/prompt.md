# Strategy: Skirmish

Build a **dark-fantasy tactical skirmish** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player commands a small, outnumbered squad through desperate grid-based
battles where every move is a commitment and every loss is permanent for the
fight. The fantasy is **grim tactical survival** — a handful of specialists
against a tide of enemies, where positioning is life and a single misread costs
a unit you cannot replace mid-battle. The tone channels *Into the Breach* meets
*Darkest Dungeon* at a smaller scale: limited palette, high contrast, tense
decisions. The best version makes the player feel like a cornered general
finding the one sequence of moves that turns impossible odds into a narrow
victory.

## What the Player Experiences

A moody title screen sets the dark-fantasy tone immediately. The player begins
and receives a brief tactical briefing — the squad's objective, the threat
ahead, the stakes — before the grid appears.

The battle is turn-based and deliberate. The player selects a unit, sees its
limited movement range light up on the grid, and commits it to a position.
Enemies are visible, aggressive, and numerous — the squad is always
outnumbered. After the player spends their actions, an End Turn command hands
control to the enemy, which advances with purpose: flanking, closing distance,
attacking when in range. Then control returns and the cycle repeats.

Combat is lethal and readable. Attacks require proximity or a clear range
indicator, reduce persistent HP, and kill. Dead units vanish from the board and
stop blocking or threatening. The player's squad members are specialists —
different movement ranges, attack patterns, HP pools, or abilities — so
choosing who moves where and who attacks what is the core decision space.

The battlefield itself adds tactical texture: terrain obstacles funnel movement,
hazards punish careless positioning, or objectives create time pressure beyond
simple elimination. Multiple battle layouts keep the experience from feeling
solved after one fight.

Victory comes from eliminating all enemies; defeat from losing the squad. Either
outcome lands on a styled result screen showing what happened, and the player
can retry or return to the title without relaunching. The entire arc — title,
briefing, battle, result — flows as one continuous authored experience.

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
