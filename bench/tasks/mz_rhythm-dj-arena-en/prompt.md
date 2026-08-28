# Rhythm DJ Arena

Build a Rhythm DJ Arena as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Two musical fighters face off on a neon stage, trading rhythmic attacks in a
battle of beats. Each fighter has a note highway; hitting notes charges special
moves that launch across the arena as musical projectiles. The opponent must
dodge or counter with their own charged abilities. The fantasy is a DJ battle
where musical skill translates directly into combat power — perfect combos
unleash devastating bass drops while missed notes leave you vulnerable. Multiple
characters with distinct musical styles and move sets provide variety.

## What the Player Experiences

1. **Title Screen** — A vibrant neon club aesthetic with the game name in
   glowing graffiti-style text, character select and versus mode buttons, and
   animated equalizer bars in the background. No plain HTML grey.
2. **Character Select** — At least 4 playable characters, each with a distinct
   musical theme (electronic, rock, jazz, hip-hop), unique sprite design, and
   different special move sets. Each character's selection shows a preview
   animation and their move list.
3. **Split Highway** — The screen splits: each side has a 3-lane note highway.
   The player hits notes on their side to build a charge meter. The AI opponent
   plays their own highway simultaneously.
4. **Charge and Attack** — When the charge meter fills a threshold, the player
   can spend it to launch a musical attack (bass wave, treble spike, chord
   blast). Attacks travel across the arena toward the opponent. Stronger charges
   (from higher combos) produce more powerful attacks.
5. **Defence and Dodge** — The opponent can dodge attacks by timing a key press
   as the projectile arrives, or absorb hits (losing health). A health bar
   depletes with each successful hit. First to zero loses the round.
6. **Best of Three** — Matches are best-of-3 rounds. Between rounds, a brief
   interlude shows score and lets the tempo increase for the next round.
7. **Arcade Mode** — A ladder of increasingly difficult AI opponents, each with
   faster note patterns and more aggressive attack usage. Defeating all
   opponents shows a character-specific victory screen.

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
