# Rhythm Note Highway

Build a Rhythm Note Highway as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Notes cascade down a multi-lane highway toward a judgement line at the bottom
of the screen. The player must press the matching lane key precisely as each
note crosses the line. Accuracy builds a combo multiplier that amplifies the
score; misses break the streak and drain a life bar. The fantasy is performing
a concert — nailing every note in a flow state while the background stage
lights react to your accuracy. A full campaign of procedurally-timed songs
provides hours of escalating challenge.

## What the Player Experiences

1. **Title Screen** — A neon-lit stage backdrop with the game name in a bold
   stylized font, a campaign button, and a free-play button. No plain grey.
2. **Song Select** — A scrollable list of at least 10 songs with difficulty
   ratings (Easy/Medium/Hard), best scores, and completion grades (S/A/B/C/F).
   Songs unlock sequentially through the campaign.
3. **The Highway** — 4 lanes with colour-coded note gems falling toward a
   judgement bar. The player presses D/F/J/K (or arrow keys) to hit notes.
   Timing windows: Perfect, Great, Good, Miss — each with distinct visual
   feedback (burst, glow, shake).
4. **Combo System** — A combo counter increments on consecutive hits. The
   multiplier (x2, x4, x8) scales score. Breaking combo resets the counter
   with a visible shatter effect.
5. **Life Bar** — Misses drain health. If health hits zero, the song fails
   with a game-over screen showing stats. Perfects restore a small amount.
6. **Hold Notes and Slides** — Some notes require holding the key for their
   duration (a trailing tail). Others slide across lanes, requiring the player
   to follow with their finger position.
7. **Results Screen** — After each song: total score, max combo, accuracy
   percentage, grade, and a breakdown of Perfect/Great/Good/Miss counts.
   New high scores trigger a celebration animation.

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
