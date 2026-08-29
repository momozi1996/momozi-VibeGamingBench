# Action: Void Harvest

Build **Void Harvest**, a compact **survivor-like auto-attacking arena game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A fragile hero is dropped into an expanding hostile void where survival depends
on threading through swarms, harvesting the energy they leave behind, and
evolving into a strange weapon system before the arena overwhelms them. The
tension lives in the upgrade economy: each level-up reshapes how the run plays,
but the void does not wait — enemies grow denser, faster, and stranger with
every passing second. The player never fires manually; positioning and upgrade
choices are the only levers. The identity should feel cosmic and original —
void insects, rust alchemy, signal flares, magnetic rail bursts, tether drones,
shard mines — not a reskin of familiar vampire-hunter rosters.

## What the Player Experiences

From a styled title screen the player picks a hero from a small roster of
original characters, each with a distinct portrait, starting weapon, and
passive that makes the choice feel like a strategy decision.

The arena begins immediately: enemies pour in from the edges and the hero's
weapons fire on their own while the player weaves through gaps with the
keyboard. Defeated enemies scatter XP shards that pull toward the hero,
filling a level meter that interrupts the action with a choice of three
upgrades — a new weapon, a stat boost, or a weapon evolution. Each pick
visibly changes the run: more projectiles, wider arcs, new attack patterns
orbiting the hero.

Time pushes the run through a visible difficulty ladder. Early swarms give way
to mixed enemy roles — chargers, ranged attackers, splitters, shield bearers —
and eventually an elite or boss-like threat whose mechanic forces repositioning
rather than simply tanking damage. The run resolves in victory or defeat on a
styled result screen with retry and return-to-title options.

Throughout, the combat HUD keeps the player oriented: HP, XP bar, survival
timer, and a weapon loadout strip showing what the hero has become.

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