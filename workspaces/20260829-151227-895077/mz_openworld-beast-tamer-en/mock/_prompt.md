# Open-World Beast Tamer

Build an **Open-World Beast Tamer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player roams diverse biomes — jungle, tundra, desert, swamp — finding and
taming wild creatures with unique abilities. The fantasy is building a bond with
powerful beasts and using their skills to solve environmental puzzles and reach
new areas. Tension comes from the taming process itself: each creature requires
a different approach (stealth, bait, rhythm), and failed attempts spook the beast.
Tamed creatures evolve through use, gaining new forms and abilities.

## What the Player Experiences

1. **Title Screen** — A vibrant title showing the game name with creature
   silhouettes in various biomes. A play button starts the adventure.
2. **Biome Exploration** — The player walks freely across interconnected biomes,
   each with distinct terrain, colour palette, and ambient creatures. Biome
   boundaries are visually clear.
3. **Creature Discovery** — Wild creatures roam each biome with visible behaviour
   patterns. A bestiary silhouette hints at undiscovered species. Each creature
   has a unique sprite and idle animation.
4. **Taming** — Approaching a creature triggers a taming mini-game: the player
   must match a pattern (timing clicks, offering correct bait, or sneaking close
   without startling). Success adds the creature to the party.
5. **Creature Abilities** — Each tamed creature has a unique ability: fire breath
   melts ice barriers, a burrower digs through soft ground, a flyer carries the
   player over gaps. The player switches active creature to solve puzzles.
6. **Environmental Puzzles** — Blocked paths require specific creature abilities.
   A frozen river needs fire, a chasm needs flight, a sealed cave needs brute
   strength.
7. **Evolution** — Using a creature in puzzles and exploration fills an experience
   gauge. When full, the creature evolves into a stronger form with enhanced
   abilities and a new sprite.

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