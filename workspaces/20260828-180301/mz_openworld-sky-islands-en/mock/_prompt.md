# Open-World Sky Islands

Build an **Open-World Sky Islands** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player glides between floating islands suspended in an endless sky, exploring
mini-dungeons, collecting wind crystals, and defeating boss guardians to unlock
new regions. The fantasy is weightless freedom: leaping from island edges, riding
wind currents, and discovering hidden platforms in the clouds. Tension comes from
the glide mechanic — stamina depletes mid-air, and falling into the void means
restarting from the last island. Wind crystals extend glide range and unlock
powerful abilities.

## What the Player Experiences

1. **Title Screen** — A bright, airy title with the game name floating among
   clouds and distant islands. A play button shaped like a wind crystal.
2. **Island Hub** — The player starts on a central island with paths leading to
   launch points. Distant islands are visible, some shrouded in mist until
   unlocked.
3. **Gliding** — The player jumps from edges and glides using a stamina-based
   wing mechanic. Wind currents (visible as particle streams) boost altitude.
   Stamina depletes during flight; landing on any surface restores it.
4. **Mini-Dungeons** — Each island contains a small dungeon with platforming
   challenges, enemies, and a wind crystal reward. Dungeons have themed hazards:
   fire jets, moving platforms, spike traps.
5. **Wind Crystals** — Collectible crystals that serve as both currency and power
   source. Spending crystals unlocks abilities: dash, double-jump, updraft
   creation. A crystal counter is always visible.
6. **Boss Guardians** — Larger islands have boss encounters. Each boss has
   attack patterns the player must learn and dodge. Defeating a boss unlocks
   access to a new cluster of islands.
7. **Progression** — The world is divided into island clusters. Each cluster has
   a distinct visual theme (forest islands, crystal islands, volcanic islands)
   and progressively harder challenges.

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