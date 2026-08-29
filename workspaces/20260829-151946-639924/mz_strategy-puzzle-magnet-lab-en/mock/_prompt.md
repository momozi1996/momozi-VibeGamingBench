# Puzzle Magnet Lab

Build **Puzzle Magnet Lab**, a 2D grid-based magnetic puzzle mini-game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player manipulates polarity to push and pull
magnetic objects through a laboratory, solving spatial puzzles to guide an
energy core to the exit.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a turn-based spatial logic puzzle built on one central rule:
opposite polarities attract, same polarities repel. Every level is a closed
system of magnets, metal crates, gates, and hazards where the player must
reason about chain reactions before committing a move. The tension comes from
irreversibility and cascading consequences: flipping a polarity switch might
solve one gate while slamming a crate into a hazard. The best version feels
like a miniature physics sandbox wrapped in clean laboratory aesthetics, where
each puzzle teaches a new interaction between familiar magnetic rules.

## What the Player Experiences

A title screen sets the laboratory tone with magnetic imagery and a clear way
to begin. The player enters a grid-based puzzle chamber where walls, floor
tiles, magnetic crates, polarity indicators, switches, gates, and an exit are
all readable at a glance. Movement is deliberate, one tile at a time, and the
grid enforces strict spatial reasoning.

Early puzzles teach the basics: push a same-polarity crate out of the way, or
pull an opposite-polarity block onto a pressure plate to open a gate. As the
player progresses, levels layer mechanics together. A polarity-swap switch
inverts the player's field, turning a repulsion problem into an attraction
opportunity. Hazard tiles punish careless moves. Multi-step sequences demand
planning several moves ahead, where an early push sets up a later pull across
the room.

An undo or reset option keeps frustration in check. When the core reaches the
exit, a completion screen celebrates the solve and offers the next challenge.
Failure states are clear and recoverable. The arc moves from simple single-crate
rooms to intricate multi-gate chambers that require the full toolkit of push,
pull, swap, and sequencing.

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