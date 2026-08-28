# Tycoon: Village Farm

Build a **2D village-farm tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player inherits a small plot of land and turns it into a living farm through
daily ritual. The fantasy is cozy accumulation — waking each morning to tend
crops that grew overnight, selling the harvest for just enough gold to plant
something new, and watching the homestead slowly fill with colour and life. The
interesting tension is that every day is finite: stamina runs out before
ambition does, so the player must choose which chores matter most right now.
The pressure is gentle but real — skip watering and crops stall, overextend and
tomorrow starts hungry. The risk is never catastrophic, just the quiet cost of
a wasted day. Over many mornings the farm transforms from bare dirt into a
thriving patchwork, and the satisfaction is entirely earned one tile at a time.

## What the Player Experiences

The player opens a saved farm or starts fresh and sees their homestead — a
fenced plot of tillable earth, a farmhouse, a shop, and water glinting at the
edge. Early mornings are simple: till a few squares, drop seeds, water them,
and head inside to sleep. Each action visibly marks the land and costs a sliver
of the day's energy.

As gold accumulates the player diversifies — new seed types with longer growth
but bigger payoffs, a fishing spot for side income, maybe an expanded field.
The daily loop stays the same but the decisions inside it deepen: which crops
to prioritize, when to harvest versus when to water the next batch, whether to
spend the last stamina fishing or saving it for tomorrow's planting.

Crops grow only overnight, so sleeping is the punctuation that gives each day
meaning. The morning reveal — seeing sprouts advance a stage, mature plants
ready to pick — is the hook that pulls the player into one more day. Progress
is banked at bedtime, so a returning player wakes to the same farm, the same
season of growth, and the same quiet momentum.

The art direction is warm, sunlit, cartoon-pastoral — greens, ochres, soft
wood — never naked HTML 引擎 grey. The tone is gentle and unhurried, the opposite
of a twitch game.

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