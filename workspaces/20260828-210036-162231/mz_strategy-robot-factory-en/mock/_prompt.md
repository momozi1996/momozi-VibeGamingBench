# Robot Factory

Build **Robot Factory**, a **robot programming arena strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player programs robot behaviors using simple if/then rules, deploys them
into a grid arena, and watches them execute simultaneously against an
opponent's robots. The strategy is entirely in the programming phase: once
robots are deployed, they act on their own according to their instruction sets.
A robot might be told "if enemy adjacent, attack; if health low, retreat; else
advance." The tension is that both sides reveal their programs at the same
time, creating emergent interactions that reward prediction and counter-play.
The tone is retro-futuristic: chunky robots on a factory floor, sparks flying,
gears grinding.

## What the Player Experiences

From the title screen the player enters the workshop. Here they build robots
by assigning behavior rules from a visual list. Each robot has three to five
instruction slots, and each slot is an if/then pair: a condition (enemy in
range, health below threshold, ally nearby) and an action (move forward,
attack, turn, heal, wait). Rules execute top to bottom each turn.

After programming, the player positions robots on their half of a grid arena.
Different robot chassis have different stats — heavy bots have more HP but
fewer instruction slots, light bots move faster but break easily, support bots
can heal adjacent allies.

When both sides are ready, the battle plays out turn by turn with simultaneous
execution. Each turn, every robot evaluates its rules and acts. The player
watches their programming logic play out — sometimes brilliantly, sometimes
hilariously wrong. The round ends when one side's robots are all destroyed.

A campaign of escalating challenges teaches mechanics one at a time, and a
skirmish mode lets the player test builds against AI opponents. The result
screen shows battle replay highlights and robot performance stats.

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