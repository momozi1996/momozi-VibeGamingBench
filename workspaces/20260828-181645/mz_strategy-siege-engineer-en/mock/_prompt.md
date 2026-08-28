# Siege Engineer

Build **Siege Engineer**, a **physics-based siege weapon strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player builds and aims siege weapons to demolish castle fortifications
using realistic projectile physics. Each level presents a castle with walls,
towers, and defenders that must be reduced to rubble within a limited number
of shots. The player chooses weapon type, adjusts angle and power, and fires —
watching the projectile arc through the air and crash into destructible
terrain. The tension is resource scarcity: ammunition is limited, each shot
must count, and the castle's geometry creates puzzles about where to strike
for maximum structural collapse. The tone is medieval engineering: wood and
iron machines, stone dust, and the satisfying crunch of masonry giving way.

## What the Player Experiences

From the title screen the player enters a campaign map of increasingly
fortified castles. Each level shows the target castle on the right and the
player's siege position on the left, with terrain between them.

The player selects from available weapon types: trebuchets for high arcs over
walls, ballistae for flat direct shots, and catapults for medium-range
bombardment. Each weapon has different projectile weight, speed, and blast
radius. The player aims by adjusting angle and power with a drag interface,
seeing a trajectory preview line.

Firing launches the projectile with physics-based flight. On impact, castle
blocks take damage and can crack, crumble, or collapse depending on structural
support — removing a load-bearing wall brings everything above it down. The
player has a limited shot count per level and must destroy enough of the castle
to meet a destruction threshold.

Later levels add wind that shifts projectile paths, armored walls that resist
certain weapon types, and defenders that repair damage between shots. The
campaign escalates from simple walls to complex multi-tower fortresses.

A styled result screen shows destruction percentage, shots used, and stars
earned. Three stars require efficient demolition with minimal shots.

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