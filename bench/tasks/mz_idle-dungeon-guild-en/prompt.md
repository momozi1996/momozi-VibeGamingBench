# Idle Dungeon Guild

Build an **Idle Dungeon Guild** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player runs an adventurer's guild, sending heroes on automated dungeon quests
that yield loot and experience. The fantasy is the guild master: recruiting heroes,
equipping them with found gear, and watching them grow from novices to legends.
The idle loop sends parties into dungeons continuously; the player's decisions
shape party composition, equipment allocation, and guild upgrades. Prestige
retires the current generation of heroes and starts a new one with inherited
guild reputation bonuses.

## What the Player Experiences

1. **Title Screen** — A guild hall interior with a quest board and hero
   silhouettes, the game name in fantasy serif font, and a play button styled
   as a wax-sealed letter.
2. **Guild Hall** — The main view shows the guild hall with hero roster, quest
   board, equipment rack, and a reputation meter. Heroes mill about when not on
   quests.
3. **Hero Recruitment** — The player recruits heroes from a pool. Each hero has a
   class (warrior, mage, rogue, healer), stats, and a level. Heroes have distinct
   sprites per class.
4. **Quest Dispatch** — The quest board shows available dungeons with difficulty,
   duration, and reward preview. The player assigns a party (1-4 heroes) and
   sends them. A progress bar shows quest completion over time.
5. **Auto-Combat Results** — When a quest completes, a results screen shows loot
   found, experience gained, and any injuries. Heroes level up automatically.
   Better dungeons yield rarer loot.
6. **Equipment & Loot** — Found gear (weapons, armour, accessories) is assigned
   to heroes from the equipment rack. Better gear improves stats and enables
   harder dungeons. A comparison tooltip shows stat changes.
7. **Prestige (New Generation)** — When guild reputation maxes out, the player
   can prestige: retire all heroes, keep equipment and guild upgrades, and start
   with a new generation that levels faster. Each generation reaches higher
   dungeon tiers.

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
