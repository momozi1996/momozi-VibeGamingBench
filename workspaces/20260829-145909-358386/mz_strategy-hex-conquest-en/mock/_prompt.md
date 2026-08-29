# Hex Conquest

Build **Hex Conquest**, a **turn-based hex-grid conquest strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

Two factions clash over a hex-tiled continent shrouded in fog. Each turn the
player spends income from captured cities to recruit units, moves armies across
terrain that shapes every engagement, and pushes the fog back tile by tile. The
tension lives in incomplete information: the enemy builds behind the fog, and
every advance risks stumbling into a prepared defense. Victory demands balancing
expansion for income against consolidation for defense, reading the map's
chokepoints, and timing a decisive strike before the opponent's economy
outpaces yours.

## What the Player Experiences

From the title screen the player picks a faction — each has a distinct roster
and economic bonus that shapes early strategy. The map generates with cities,
forests, mountains, and plains on a hex grid, fog covering everything beyond
the player's starting territory.

Each turn has clear phases: collect income from owned cities, recruit units at
cities, move units across hexes, and attack adjacent enemies. Terrain matters —
forests slow movement, mountains block it, rivers cost extra to cross. Units
have types: infantry hold ground cheaply, cavalry strike fast, and siege units
crack fortified cities.

Fog lifts only around the player's units, so scouting is a real investment.
The AI opponent expands, builds, and attacks with its own strategy. Capturing
a city flips its income to the conqueror and pushes the front line forward.

The game ends when one faction controls all cities or destroys the enemy's last
unit. A styled result screen shows the outcome with territory statistics and
offers a rematch.

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