# Roguelike: Wildwood

Build a **node-map forest-exploration roguelike with turn-based combat** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The fantasy is reading a dangerous forest. Every fork in the trail is a bet
placed with incomplete information: claw marks on a trunk, smoke curling above
the canopy, a glint of metal in the undergrowth. The player pushes deeper not
because the path is safe but because the clues make the risk feel knowable. When
a beast appears, combat is deliberate and positional — a small kit of skills
spent against creatures that each punish a different mistake. Health never
refills for free, so every scratch from three clearings ago still matters at the
final gate. Death is permanent for the run, but not for the player: banked gold
and a dwindling supply of entry tickets give each expedition weight without
making failure a dead end. The tone is hushed and watchful — dappled light,
distant howls, the crackle of a campfire earned by surviving one more node.

## What the Player Experiences

The player begins at a trailhead camp that remembers them between sessions —
tickets, gold, and whatever lasting advantages they have earned are all visible
here. Entering the forest costs a ticket, so the decision to set out already
carries stakes.

Once inside, the run unfolds as a branching map of trail nodes stretching deeper
into the wood. Nodes are not fully revealed; instead the map offers partial
evidence — tracks, smoke, glitter, disturbed brush — that lets the player weigh
risk against their current health, gold, and depth. Committing to a node strips
away the mystery: it might be a beast, a chest, a campfire, a trader, a trap, or
something worse.

Combat is turn-based and skill-driven. The hero carries several distinct
abilities that cost a resource, and different beasts demand different responses —
a fast wolf, an armored bear, a venomous serpent. Lingering conditions like
poison or bleed play out over multiple turns, rewarding the player who reads the
threat and plans ahead.

Between fights the player collects relics and gear that reshape how the hero
fights, not just refill health. Growth within a run is tangible: new buttons, new
options, new ways to handle what the forest throws next.

A run ends in victory — reaching the heart of the wood and overcoming its
guardian — or in death, which sends the player back to camp minus a ticket but
richer in banked gold. Progress persists across sessions, so quitting and
returning picks up the same hoard and the same slow accumulation of power.

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