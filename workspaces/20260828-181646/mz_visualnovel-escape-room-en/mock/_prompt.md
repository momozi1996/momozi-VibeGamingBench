# Escape Room

Build **Escape Room**, a **narrative escape room visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player wakes in a locked room with no memory of how they got there. Each
room is a self-contained puzzle box: examine objects, combine items, decode
ciphers, and find the exit. But this is also a narrative — choices made during
escape sequences branch the story, revealing different truths about why the
player is trapped. Multiple rooms connect into a larger mystery, and reaching
the true ending requires solving all rooms and making specific narrative
choices. The tension is dual: the intellectual satisfaction of puzzle-solving
layered with the narrative dread of discovering what is really happening. The
tone is atmospheric suspense: dim lighting, cryptic notes, and the ticking
pressure of confinement.

## What the Player Experiences

From the title screen the player enters the first room. The view shows a
first-person-style room illustration with interactive hotspots — drawers,
paintings, locks, scattered objects. Clicking hotspots examines them, sometimes
adding items to an inventory bar.

Items can be combined (key + lock, cipher + coded message) or used on hotspots.
Each room has a sequence of puzzles that gate progress: solving one reveals the
next. Puzzles include pattern matching, code deciphering, hidden object
finding, and logic deduction.

Between puzzle segments, narrative moments present dialogue choices that affect
the story branch. The player might find a note that reveals a character's
motive, and their response determines which version of events they believe —
affecting which rooms unlock next and which ending they reach.

Multiple rooms form a sequence, each harder than the last. The true ending
requires completing all rooms and making specific deduction choices. Other
endings are valid but incomplete — the player knows they missed something.

A styled result screen shows escape time, puzzles solved, and which ending
was reached, with a hint about paths not taken.

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