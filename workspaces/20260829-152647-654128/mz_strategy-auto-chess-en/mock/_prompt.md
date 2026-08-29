# Auto Chess

Build **Auto Chess**, an **auto-battler draft-and-position strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

Eight players enter a tournament where the battlefield fights itself. Between
rounds the player drafts units from a shared shop, places them on a grid board,
and watches them clash automatically against an opponent's formation. The
strategy is entirely in the draft and the positioning: which units to buy, when
to level up for more board slots, how to arrange front-line tanks and back-line
damage dealers, and which synergy traits to chase. Gold management is the
heartbeat — rerolling the shop costs gold, saving gold earns interest, and
going broke at the wrong moment means fielding a weaker army than everyone else.
Elimination rounds whittle the field until one player remains.

## What the Player Experiences

The player opens to a lobby screen showing eight portraits (one human, seven
AI). Each round begins with a preparation phase: a shop offers five random
units, the player buys with gold, drags units onto a grid board, and arranges
their formation. Combining three copies of the same unit upgrades it to a
stronger star level with a visible transformation.

Units belong to classes and origins that grant synergy bonuses when enough of
the same trait are fielded — the synergy tracker shows active and upcoming
bonuses. The player must decide between a focused synergy build and grabbing
individually powerful units.

When the timer expires, the combat phase begins. Units auto-attack, cast
abilities, and fall until one side is eliminated. The losing player takes
damage to their health pool based on surviving enemy units. Between rounds the
player sees a scoreboard of all eight competitors and their health.

The economy rewards patience: unspent gold earns interest each round, but
falling behind in power means taking heavy damage. The tension is always
between spending now to survive and saving to spike later.

The game ends when the player is eliminated or is the last one standing. A
styled result screen shows final placement and key stats.

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