# Gladiator Arena

Build **Gladiator Arena**, a **gladiator arena management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player owns a gladiatorial arena in a fantasy-Roman setting, recruiting
fighters, training them, scheduling bouts, and upgrading the arena to attract
bigger crowds and richer sponsors. Each gladiator has stats, a fighting style,
and a personality — some are crowd favorites who draw spectators, others are
efficient killers who win but bore the audience. The tension is between
spectacle and survival: the crowd wants blood and drama, but dead gladiators
are expensive to replace. Betting adds a layer of risk-reward: the player can
wager on their own fighters for extra gold, but upsets happen. The tone is
sand-and-steel grandeur: roaring crowds, clashing weapons, and the drama of
the arena floor.

## What the Player Experiences

From the title screen the player starts a new arena season. The main view
shows the arena compound: training grounds, barracks, the arena floor, and a
management office. Time advances day by day toward scheduled fight nights.

Gladiators are recruited from a slave market or free-fighter pool — each has
combat stats (strength, speed, defense), a weapon preference, and a crowd
appeal rating. Training improves stats over days but costs food and trainer
fees. The player assigns training regimens: strength drills, sparring, or
showmanship practice.

Fight nights are scheduled on the calendar. The player picks matchups from
their roster against visiting challengers or rival arena fighters. During
fights, gladiators battle automatically based on their stats and style — the
player watches but cannot intervene. Crowd excitement builds with dramatic
moments (near-deaths, comebacks, finishing moves).

Revenue comes from ticket sales (based on crowd size), sponsor deals (based on
arena prestige), and betting winnings. Expenses include gladiator upkeep,
training costs, arena maintenance, and medical bills for injured fighters.

The game tracks gold, arena prestige, and season wins. A styled result screen
shows season statistics and champion gladiator highlights.

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