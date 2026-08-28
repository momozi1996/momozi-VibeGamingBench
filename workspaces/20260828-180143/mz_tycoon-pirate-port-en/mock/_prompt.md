# Pirate Port

Build **Pirate Port**, a **pirate haven management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player builds a hidden pirate port on a tropical island, attracting crews
with taverns and docks, sending them on raids for plunder, and defending
against the royal navy when notoriety grows too high. The economy loops through
three currencies: gold from raids funds buildings, reputation attracts better
crews, and notoriety draws navy attention. The tension is that the most
profitable actions raise notoriety fastest, forcing the player to balance
aggression against defense preparation. The tone is swashbuckling Caribbean:
palm trees, rickety docks, rum barrels, and cannon smoke.

## What the Player Experiences

From the title screen the player starts a new port. The view shows a coastal
island with a grid for building. The player constructs docks to berth ships,
taverns to attract pirate crews, warehouses to store plunder, and defenses
(walls, cannons, watchtowers) to repel navy raids.

Pirate crews arrive based on the port's reputation. Each crew has a ship type,
combat strength, and upkeep cost. The player sends crews on raids by selecting
a target from a map of trade routes — richer targets yield more gold but raise
notoriety higher. Raids play out automatically with a result summary.

Gold funds expansion: better docks attract larger ships, upgraded taverns keep
crews happy, and a shipyard allows repairing and upgrading vessels. Crew morale
depends on tavern quality, raid success, and pay.

When notoriety reaches thresholds, the navy attacks. Navy raids are tower-
defense encounters where the port's cannons and walls must hold against
incoming warships. Surviving a raid lowers notoriety slightly; failing means
losing buildings and crews.

The game tracks gold, fleet size, and raids completed. A styled result screen
shows port statistics when the port falls or reaches a prosperity milestone.

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