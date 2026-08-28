# Dungeon Master

Build **Dungeon Master**, a **dungeon management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is the villain: dig rooms in the earth, fill them with traps and
monsters, and watch greedy heroes stumble in to be defeated. But monsters are
not free — they need gold to recruit, food to keep happy, and rooms that suit
their nature. Heroes arrive in waves of increasing strength, and each one that
escapes spreads word of an easy dungeon, attracting tougher adventurers. The
tension is economic: gold comes from defeated heroes' loot, but spending it all
on offense leaves nothing for creature comforts, and unhappy monsters desert.
The fantasy is running an evil enterprise where the product is doom and the
customers are uninvited.

## What the Player Experiences

From the title screen the player starts a new dungeon. The view shows a
cross-section of earth. The player digs rooms by spending gold, creating a
layout of corridors and chambers. Each room can be designated: treasure rooms
lure heroes deeper, trap rooms damage them, barracks house monsters, and
hatcheries produce food.

Monsters are recruited from a roster — each type has a gold cost, preferred
room type, and combat strength. Placing monsters in rooms they like keeps
morale high; cramming them into unsuitable spaces makes them grumpy and
eventually causes desertion. The creature happiness meter is always visible.

Heroes arrive periodically, entering from the surface and navigating toward
treasure. They fight monsters, trigger traps, and either die (dropping loot)
or escape. Escaped heroes increase the dungeon's fame, attracting stronger
parties next wave. The player must balance dungeon depth, trap density, and
monster strength against the escalating threat.

The game tracks gold, creature count, and waves survived. A styled result
screen shows dungeon statistics when the dungeon heart is destroyed by heroes
or a wave milestone is reached.

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
