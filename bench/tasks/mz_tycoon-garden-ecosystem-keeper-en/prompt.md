# Garden Ecosystem Keeper

Build **Garden Ecosystem Keeper**, a compact **ecosystem gardening management
game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player tends a small restoration garden where every tile is part of a living
web. Plants compete for moisture and light, pollinators follow bloom corridors,
pests exploit monoculture, and weather shifts the whole balance overnight. The
core tension is stewardship under scarcity: limited actions per turn, finite
water, unpredictable seasons, and biodiversity goals that punish brute-force
planting. A thriving garden is one the player composed, not one they clicked
into existence.

The tone is gentle but systemic — readable beds, seed packets, pollinator
trails, pest warnings, seasonal color shifts, and clear biodiversity meters.
The garden should feel alive and authored, not a raw grid of colored squares.

## What the Player Experiences

The player opens to a garden restoration scene and chooses a plot to tend. The
first planting is simple: a few seed types, moist soil, calm weather. Plants
grow visibly over turns, and the player learns the rhythm of water, wait,
harvest.

Soon the ecosystem asserts itself. A pollinator visits one flower bed but
ignores another. A pest cluster appears near a monoculture row. Companion
planting hints emerge — herbs near tomatoes deter aphids, wildflowers draw
bees toward fruit trees. The player starts composing beds rather than filling
them.

Weather and seasons raise the stakes. A dry spell forces triage: which beds
get the last water? An early frost threatens unprotected seedlings. A rainy
season floods low tiles but lets the pond habitat flourish. The player adapts
their plan each turn, balancing short-term survival against long-term
biodiversity targets.

Late game, the garden is a dense web of interactions. The player manages
pollinator corridors, pest barriers, moisture zones, and seasonal rotations.
When the restoration goal is met — a target biodiversity score, a bloom
festival, or a full habitat chain — the result screen reflects the garden's
health and composition. Failure shows what collapsed and why, inviting a
different strategy next time.

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
