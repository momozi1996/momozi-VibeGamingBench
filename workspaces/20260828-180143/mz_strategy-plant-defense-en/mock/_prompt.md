# Plant Defense

Build **Plant Defense**, a **lane-based tower defense strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A garden grid stands between a homestead and waves of encroaching creatures.
The player plants defenders on a multi-lane lawn, spending sunlight that must
be actively collected. Each plant type fills a tactical role — some shoot, some
block, some generate economy — and the creatures come in varieties that punish
a one-note defense. The tension is resource scarcity: sunlight arrives slowly,
plants cost real economy, and a misplaced defender means a lane falls before
reinforcements grow. An adventure map connects levels with escalating challenge
and new plant unlocks, giving the player a reason to master each tool before
the next threat arrives.

## What the Player Experiences

From the title screen the player enters an adventure map showing a trail of
levels. Selecting a level shows the upcoming creature types and lets the player
pick a loadout of plant defenders from their unlocked roster.

The level plays on a grid of lanes. Sunlight drops periodically and the player
clicks to collect it, building a resource pool. Plants are dragged from a
toolbar onto empty grid cells, each costing sunlight. Shooters fire
projectiles down their lane, walls absorb hits, and sun-producers accelerate
the economy. Creatures march from the right edge in waves, each lane
independent.

Creature variety forces adaptation: armored types shrug off weak shots, fast
types outrun slow-firing plants, and flying types bypass ground walls. Later
levels introduce night conditions where sun production drops, forcing the
player to rely on alternative economy plants.

A level is won when all waves are defeated; lost when any creature reaches the
left edge. Victory unlocks the next map node and sometimes a new plant type.
The result screen shows stars earned and the map updates visibly.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Same pattern as `bench/references/tg1/game_logic.js`.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.