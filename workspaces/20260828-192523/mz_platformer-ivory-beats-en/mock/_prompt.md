# Ivory Beats

Build **Ivory Beats**, a 2D vertical rhythm-reaction arcade game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A relentless cascade of dark tiles rushes down a stark monochrome grid, and the
player must shatter each one at the exact moment it crosses the strike line.
The tension is pure reaction speed married to lane-switching rhythm: four lanes
mean four possible targets every beat, and a single mistap or missed tile ends
the run instantly. The game rewards flow state — that trance where fingers move
faster than conscious thought and the score counter blurs upward. Between
attempts the player chases personal bests across multiple modes that each twist
the pressure differently: race to clear a target count, survive an ever-
accelerating scroll, or maximize hits within a countdown. The aesthetic is
sleek modernist minimalism — a crisp black-and-white grid punctuated by neon
feedback flashes whenever a tile shatters.

## What the Player Experiences

A clean title screen presents the game name and a mode-select menu showing
personal-best scores loaded from a save file. The player picks a challenge mode
and lands on a frozen four-lane grid with a pulsing prompt inviting the first
tap.

The moment the player acts, tiles begin scrolling. Dark tiles descend one per
row, each in a random lane, and the player hammers lane keys or clicks to
destroy the lowest active tile before it escapes the bottom. Every successful
hit vaporizes the tile with a neon flash, nudges the score, and pulls the next
row into position. The rhythm builds — slow and approachable at first, then
quickening until fingers blur.

A wrong-lane tap or an escaped tile triggers instant defeat: the board locks,
the faulted tile flashes red with a screen shake, and a results panel slides
over the frozen grid. The panel shows the run's score against the saved best,
updates the record if beaten, and offers an instant retry that resets the board
without relaunching.

Each mode reshapes the pressure: one races to clear a fixed tile count against
the clock, another accelerates the scroll every few successful hits until the
player breaks, and a third imposes a tight countdown where every tile counts.
The loop is short, punchy, and endlessly replayable.

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