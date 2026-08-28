# Strategy: Beast Clash

Build a **single-lane real-time animal-war strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

Two animal kingdoms clash across a single contested lane. The player commands
one side, spending food to send creatures marching toward the enemy den while
the opponent does the same. Every kill feeds growth, growth unlocks evolution,
and evolution turns a trickle of small critters into a roaring tide of apex
predators. The tension lives in the economy: food is scarce, creatures cost
real resources, and the wrong spend at the wrong moment hands the lane to the
enemy. The tone is lively but fierce — a sunlit savanna-and-jungle frontier
where war escalates from scurrying critters to towering, screen-shaking beasts.

## What the Player Experiences

From the title screen the player picks a kingdom — each feels like a real
faction with its own animals, identity, and fighting temperament, so the choice
is a strategy decision, not a skin swap.

The battle unfolds on a side-scrolling lane between two dens. Food ticks up
over time and the player spends it to send creatures out of their den. Each
creature marches on its own toward the enemy, clashing with whatever it meets
and pushing the front line back and forth. The player never pilots a creature
directly; the strategy is about when to spend, which creature to send, when to
invest in gatherers for more food, and when to save up for evolution.

Creatures come in distinct roles — sturdy blockers that hold the front, ranged
strikers that punish from behind, and gatherers that keep the economy flowing.
The best armies use cooperation: blockers absorb hits while ranged beasts deal
damage safely and gatherers sustain the pressure. The enemy fields its own mix
and grows more dangerous over time, so a static plan loses.

As skirmishes are won, a growth track fills. Reaching thresholds evolves the
kingdom into a new era, unlocking larger, fiercer creatures and visibly
upgrading the den. A later-era beast plainly outclasses an opening-era critter
and expands tactics rather than simply replacing everything before it.

Throughout the battle the player reads the war at a glance — food, evolution
progress, and the health of each den. Victory comes when the enemy den is
destroyed; defeat when the player's own den falls. Each ending lands on a
styled result screen that makes the outcome unmistakable and lets the player
fight again without restarting the application.

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
