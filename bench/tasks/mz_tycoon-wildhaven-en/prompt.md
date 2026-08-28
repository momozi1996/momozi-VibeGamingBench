# Tycoon: Wildhaven

Build a **multi-industry frontier-economy tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a frontier boss carving a thriving outpost from lakeside
wilderness. The fantasy is juggling multiple industries that share one stretch
of land under a turning seasonal clock — pushing one too hard quietly starves
the others, so the real skill is reading cause-and-effect links and hedging
across production chains as the calendar turns. Seasons reshape what pays and
what stalls, weather and wildlife disrupt the best-laid plans, and reinvesting
earnings visibly transforms the camp from a lonely shack into a humming
operation. The tone is warm but demanding: nature is generous and punishing in
equal measure, and coasting is never an option.

## What the Player Experiences

The player opens a saved camp or starts fresh and sees the outpost spread before
them — forest, cleared land, lake, and a simple ledger of cash and season. Early
on, work is hands-on: fell a tree, plant a row, cast a line. Each action
visibly changes the land and feeds a production chain that turns raw nature into
goods into money.

As earnings accumulate the player reinvests — better tools, new buildings,
expanded capacity — and the outpost grows busier and more capable on the map.
The seasonal clock keeps turning: warm months favor crops, cold months freeze
the lake, timber demand shifts, and no single industry pays year-round. The
player learns to hedge, stockpile, and plan ahead.

Disruptions arrive without warning — storms flatten output, animals raid stores
— and the player adapts or absorbs the loss. Over time the deeper game reveals
itself: industries are interdependent, and overexploiting one degrades the
others. Balanced management visibly beats tunnel-vision. Progress is banked to a
save, so a returning player picks up the same outpost, season, and momentum.

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
