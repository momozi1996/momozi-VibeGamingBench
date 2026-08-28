# Transit Web

Build **Transit Web**, a 2D transit network simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is designing a city's transit network from scratch, connecting
stations with colored lines and watching passengers flow through the system like
blood through veins. The interesting tension is resource scarcity: the player has
limited lines, carriages, and tunnels to serve a city that keeps growing. New
stations appear over time with different shapes representing passenger
destinations, and overcrowded stations eventually fail, ending the game. Every
line placement is a commitment — rerouting wastes precious time while passengers
pile up. The elegance of the solution matters: a well-designed network handles
growth gracefully while a tangled mess collapses under its own complexity.

## What the Player Experiences

The player opens to a minimalist city-map title screen, then begins with a small
map showing 3 stations of different shapes (circle, triangle, square). The player
draws a line connecting two or more stations by clicking them in sequence. Tiny
passenger icons appear at stations, each shaped to indicate their destination
type. Passengers board trains that travel along lines and disembark at matching
stations.

As time passes new stations appear across the map. The player receives periodic
resource grants: new lines, extra carriages (increasing line capacity), or
tunnels (allowing river crossings). Stations that accumulate too many waiting
passengers flash warnings and eventually overflow, ending the run. The player
can reroute lines at any time but must manage the transition. Different map
layouts offer varied challenges — river cities, island chains, sprawling
suburbs. A run-end screen shows days survived, passengers delivered, and
network efficiency stats.

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