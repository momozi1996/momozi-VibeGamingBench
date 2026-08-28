# Dread Wings

Build **Dread Wings**, a **one-button endless flyer** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a dark cyberpunk score-chaser where a fragile metallic bird
fights gravity through an infinite corridor of industrial hazards.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player fights physics with a single input. Every tap buys a moment of lift
against relentless downward pull, threading the bird through narrow gaps that
demand precise timing and rhythm. The tension comes from the gap between what
the player sees coming and what their reflexes can execute -- each successful
pass raises the stakes because the score is now worth protecting. Death is
instant, retry is instant, and the "just one more try" loop is the entire
product. The world is a dark industrial wasteland: neon-lit pipes, smog, and
a distant ruined skyline scrolling beneath a crimson sky.

## What the Player Experiences

The player opens to a moody title screen showing their all-time best score and
a clear way to launch. Once they begin, the bird hovers in place, waiting for
the first tap. The moment input arrives, gravity takes hold and the corridor
begins scrolling. Each tap fires an upward impulse that fights the bird's
falling arc, creating a rhythmic bobbing flight path. Paired hazards scroll in
from the right with randomized vertical placement but a consistent gap size,
demanding constant micro-adjustments. Passing a hazard pair ticks the score
upward. Over time the challenge escalates -- faster scrolling, tighter margins,
or new hazard presentations keep the player adapting. Contact with any surface
ends the run immediately: the world freezes, a result panel reveals the final
score and whether a new record was set, and a single button drops the player
back to the ready state without restarting the executable. The high score
persists between sessions.

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