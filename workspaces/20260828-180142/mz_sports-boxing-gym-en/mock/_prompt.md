# Sports Boxing Gym

Build a **Sports Boxing Gym** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a boxer rising through the ranks, reading opponent tells, timing
dodges and counters, and managing stamina across multi-round bouts. The fantasy
is the sweet science: not brute force but pattern recognition, knowing when to
slip a jab and answer with a hook. Tension comes from stamina — every punch
thrown and every dodge costs energy, and a tired boxer drops their guard. Between
fights, training mini-games improve stats and unlock new techniques.

## What the Player Experiences

1. **Title Screen** — A boxing ring under spotlights with the game name in bold
   block letters, a play button styled as a bell.
2. **Career Menu** — The player sees their boxer's stats, upcoming opponent, and
   training options. A fight card shows the next bout with the opponent's
   silhouette and record.
3. **Training** — Before each fight, the player completes training mini-games:
   heavy bag (timing combos), speed bag (rhythm clicking), jump rope (pattern
   matching). Training improves power, speed, or stamina stats.
4. **The Fight** — Side-view boxing with two fighters. The opponent telegraphs
   attacks with visible tells (shoulder dip, foot shift, glove pull-back). The
   player must read the tell and respond: dodge high/low, block, or counter.
5. **Punch Mechanics** — The player throws jabs, hooks, and uppercuts with
   different keys. Each punch type has different speed, power, and stamina cost.
   Combos (sequences of punches) deal bonus damage.
6. **Stamina System** — A stamina bar depletes with every action. Low stamina
   slows punches and weakens blocks. Between rounds, stamina partially recovers.
   The player must pace themselves across rounds.
7. **Career Progression** — Winning fights advances rank. Opponents get harder
   with faster tells and more varied patterns. Reaching the championship requires
   mastering all defensive techniques.

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