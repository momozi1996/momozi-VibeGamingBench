# Open-World Seasons Witch

Build an **Open-World Seasons Witch** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a witch who controls the seasons in a small valley, shifting between
spring, summer, autumn, and winter to solve problems and help villagers. The
fantasy is elemental mastery: freezing a river to cross it, blooming flowers to
attract bees for honey, melting snow to reveal buried items, or withering vines
blocking a path. Tension comes from villager requests that require specific
seasonal combinations and potion ingredients that only grow in certain seasons.
Each season transforms the entire world visually and mechanically.

## What the Player Experiences

1. **Title Screen** — A four-panel title showing the same valley in each season,
   with the game name in flowing script. A play button surrounded by seasonal
   icons.
2. **The Valley** — The player moves freely through a valley with a village,
   forest, lake, mountain path, and farmland. The entire world changes appearance
   based on the active season.
3. **Season Switching** — The player can cast a season spell to change the world.
   A radial menu shows four seasons; selecting one triggers a visual transition
   that transforms terrain, water, vegetation, and sky colour.
4. **World Reactions** — Each season has mechanical effects: winter freezes water
   and reveals ice caves; spring grows plants and fills rivers; summer dries
   swamps and ripens fruit; autumn drops leaves revealing hidden paths and
   weakens wooden structures.
5. **Villager Quests** — NPCs in the village request help that requires seasonal
   manipulation: a farmer needs rain (spring) then sun (summer) for crops; a
   builder needs frozen lake (winter) to transport stone; a healer needs autumn
   mushrooms.
6. **Potion Brewing** — Ingredients gathered in different seasons combine into
   potions at the witch's cottage. Potions grant abilities: speed boost, barrier
   shield, creature charm. A recipe book tracks discovered combinations.
7. **Progression** — Completing quests earns reputation and unlocks new areas of
   the valley. The mountain pass opens after helping enough villagers, revealing
   a final challenge that requires mastery of all four seasons.

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