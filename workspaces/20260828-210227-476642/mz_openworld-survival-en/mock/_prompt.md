# Open-World Survival

Build a **2D open-world survival game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player awakens alone in a wilderness and must gather resources, craft tools,
build shelter, and survive the night. The fantasy is **self-reliance under
pressure** -- every decision matters because daylight is finite, hunger is
constant, and the world turns hostile after dark. The interesting tension is
choosing what to prioritize: food now or tools for later, exploration or
fortification, risk or safety. Temperature drops, visibility shrinks, and
survival depends on preparation. The art style should feel **earthy, raw, and
immersive** -- think *Don't Starve* meets *A Short Hike* at a smaller scale.

## What the Player Experiences

1. **Title Screen** -- A stylised opening with the game name, a play button, and
   a wilderness backdrop (forest, campsite, or mountain vista). No naked HTML 引擎
   grey.

2. **The Wilderness** -- The player spawns in an open-world map with multiple
   visually distinct biomes: grassy plains, dense forest, and rocky terrain or
   water. The player moves freely in 8 directions across a large explorable
   space.

3. **Resource Gathering** -- Scattered across the map are interactable resources:
   trees for wood, stone outcrops for stone, and berry bushes for food. The
   player approaches a resource and interacts to gather it, with visible feedback
   (animation, particle effect, or resource disappearing).

4. **Survival Metrics** -- Status bars are always visible (hunger, thirst, or
   temperature). They drain over time. When a bar hits critical levels, the
   player suffers consequences: slowed movement, screen vignette, health loss, or
   other visible penalties.

5. **Crafting** -- A crafting panel shows available recipes that consume gathered
   materials. Recipes produce useful items: a campfire for warmth, a shelter for
   protection, an axe for faster gathering. The player sees what they can and
   cannot afford to build.

6. **Building and Placement** -- Crafted structures can be placed into the world
   as persistent objects. A campfire provides warmth and light. A shelter
   restores health or blocks environmental damage. Placement has clear visual
   indicators.

7. **Day-Night Cycle** -- Time passes automatically. Day is bright and safe.
   Night darkens the map, shrinks visibility, and accelerates survival drain.
   Being near a campfire at night extends the player's safe radius. Surviving a
   full day-night cycle is the minimal success condition.

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