# Rhythm Beat Dungeon

Build a Rhythm Beat Dungeon as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player descends through a grid-based dungeon where every action — moving,
attacking, dodging — must land on the beat of a persistent rhythm track. Miss
the beat and you stumble; hit it perfectly and your strikes deal bonus damage.
Enemies telegraph their attacks in rhythmic patterns the player must read and
counter. The fantasy is a warrior-dancer weaving through danger with musical
precision, collecting loot that changes their combat style, and facing bosses
whose attack patterns form complex polyrhythms.

## What the Player Experiences

1. **Title Screen** — A styled menu with the game name pulsing to a beat,
   a play button, and a dark dungeon backdrop with flickering torchlight. No
   plain HTML 引擎 grey.
2. **The Beat** — A persistent rhythm indicator (bouncing icon, pulsing border,
   or metronome bar) shows the current beat. The player taps movement or attack
   keys in time with this pulse. Perfect timing flashes gold; early/late shows
   a different colour.
3. **Grid Movement** — The dungeon is a tile-based grid. Each beat, the player
   can move one tile in any cardinal direction or stay and attack. Moving off-
   beat causes a stumble animation and wastes the turn.
4. **Enemies** — Multiple enemy types with distinct rhythm patterns: a skeleton
   that attacks every 2 beats, a slime that moves on off-beats, a wraith that
   teleports every 4 beats. Each telegraphs with a visual wind-up.
5. **Combat** — Attacking on-beat deals full damage with a satisfying hit flash.
   Off-beat attacks deal reduced damage. Enemies drop gold and occasional
   equipment (weapons that change attack range or pattern).
6. **Loot and Progression** — Between floors, a shop lets the player spend gold
   on health potions, new weapons (spear hits 2 tiles, dagger attacks twice per
   beat), or armour. Equipment visibly changes the player sprite.
7. **Boss Fights** — Each dungeon section ends with a boss whose attacks form
   a complex multi-beat pattern. The boss telegraphs with a unique visual
   sequence the player must memorize and dodge rhythmically.

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