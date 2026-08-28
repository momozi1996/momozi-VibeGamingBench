# Ink Trail

Build **Ink Trail**, a platformer where the player leaves a trail that becomes
solid platform after a delay as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

An ink spirit dashes through empty voids, leaving behind a wet trail of ink
that solidifies into walkable platforms after a short delay. The spirit has
limited ink — once the reservoir empties, no more trail is created until
reaching an ink well refill. The core puzzle: plan a path through empty space
such that the trail you leave behind creates the platforms you need to reach
the exit. Sometimes you must double back to stand on your own trail. Sometimes
you must draw a bridge mid-jump and land on it as it solidifies. Ink wells are
sparse, forcing efficient routing. Thirty-six levels across six worlds
introduce wind that displaces wet ink, erasers that dissolve trails, color-coded
ink that only solidifies near matching surfaces, and timed ink that fades after
seconds.

## What the Player Experiences

A title screen shows ink dripping into the game name. A world-select grid shows
six worlds of six levels each.

The player moves and jumps normally. While moving, ink trails behind the
character as a visible wet line. After a 1-second delay, the wet ink hardens
into a solid platform with a satisfying visual pop. An ink meter shows remaining
supply — when empty, movement leaves no trail. Ink wells scattered in levels
refill the meter.

Early levels teach basic trail-platforming: cross a gap by running through air
and doubling back onto your solidified trail. Later levels add complexity: wind
pushes wet ink sideways before it hardens, erasers delete sections of trail,
and timed ink fades after a few seconds requiring speed. Each level has a
three-star rating based on ink efficiency. A level-complete screen shows ink
used, time, and stars earned.

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
