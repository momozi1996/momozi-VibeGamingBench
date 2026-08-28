# Strategy: Ashen Spire

Build **Ashen Spire**, a compact **dark-fantasy roguelike deckbuilding card
battler** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is climbing a cursed tower one floor at a time with nothing but a
thin deck of cards and whatever you scavenge along the way. Each combat is a
small tactical puzzle: energy is scarce, the enemy telegraphs its next move, and
every card played reshapes the odds for the rest of the run. The interesting
tension is that the deck is both your weapon and your liability -- adding
powerful cards dilutes consistency, while staying lean means fewer answers to
escalating threats. The pressure comes from reading enemy intent, rationing
energy across attack and defense, and gambling on which reward cards will pay off
three fights from now. The risk is always that one greedy pick or one misread
intent leaves you one hit from death with no block in hand.

## What the Player Experiences

The player arrives at a dark, atmospheric title screen that sets the tone of a
grim tower ascent. Starting a run reveals a branching route map -- a web of
nodes stretching upward toward a final confrontation, with forks that force the
player to choose which dangers to face and which to skip.

Entering a combat node drops the player into a turn-based card duel. A small
hand is drawn, energy refills, and the enemy displays what it intends to do next
turn. The player spends energy playing cards -- strikes that chip away at the
enemy, guards that raise a shield, and stranger tactical effects that poison,
burn, draw extra cards, or bend the rules. When the hand is spent or the player
is satisfied, ending the turn lets the enemy act, then a fresh hand is drawn and
the cycle repeats.

Winning a fight offers a choice of new cards to weave into the deck, each with
its own identity and cost. The map updates, the player picks the next node, and
the deck grows richer and riskier with every floor. Different encounters reveal
different pixel monsters with distinct silhouettes and behaviors, so no two
climbs feel identical.

The run resolves at the top: defeat the boss and a styled victory screen
celebrates the climb, or fall to zero health anywhere along the way and a defeat
screen marks how far you got. Either way, the player can retry or return to the
title without restarting the application.

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