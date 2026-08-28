# Dice Throne

Build **Dice Throne**, a dice-rolling roguelike with reroll mechanics and
equipment that modifies die faces as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

A warrior battles through a dungeon using dice as their combat system. Each
turn the player rolls a set of dice, then chooses which to keep and which to
reroll (up to two rerolls). Die faces map to abilities: swords deal damage,
shields block, hearts heal, and skulls trigger special attacks. The twist:
equipment found in the dungeon physically modifies die faces — a flame sword
replaces one sword face with a fire-sword that deals double damage, enchanted
armor adds a shield face to a die. The enemy rolls visible dice too, creating
a transparent contest where both sides see what is coming. Building a set of
dice with synergistic faces is the meta-progression within each run.

## What the Player Experiences

A title screen shows dice tumbling with glowing face icons. Starting a run
gives the player 5 standard dice (each with sword, sword, shield, heart,
skull, blank faces).

In combat, the player rolls all dice simultaneously with a satisfying tumble
animation. Results land face-up. The player selects dice to keep (they lock in
place) and rerolls the rest — up to two rerolls per turn. After finalizing,
faces activate: swords deal damage to the enemy, shields reduce incoming damage,
hearts heal, skulls trigger a special ability. The enemy then rolls their own
visible dice and resolves similarly.

Between encounters, loot screens offer equipment that modifies die faces —
replacing, upgrading, or adding faces. A map shows branching paths with combat,
elite, shop, and rest nodes. Shops sell face modifications and new dice. The
run ends at a boss with powerful custom dice. Death shows floor reached, best
roll, and equipment collected.

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
