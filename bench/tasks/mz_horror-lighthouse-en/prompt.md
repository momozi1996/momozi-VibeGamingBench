# Horror Lighthouse

Build a **Horror Lighthouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a lighthouse keeper during an endless storm, maintaining the light
to guide ships safely past the rocks while something in the water tries to lure
them onto the shore. The fantasy is lonely duty against cosmic dread: the beam
is the only thing between sailors and death, but keeping it lit attracts the
attention of what lurks below. Tension comes from fuel management, mechanical
breakdowns, and the creature's escalating attempts to extinguish the light or
drive the keeper mad.

## What the Player Experiences

1. **Title Screen** — A stormy coastal scene with a lighthouse beam sweeping
   through rain, the game name in weathered serif font, and a play button.
2. **The Lighthouse** — A cross-section view showing multiple floors: the lamp
   room at top, living quarters in the middle, fuel storage at the bottom, and
   the dock outside. The player moves between floors.
3. **Light Maintenance** — The lamp burns fuel and occasionally malfunctions. The
   player must refuel from storage below, clean the lens when spray coats it,
   and repair the rotation mechanism when it jams. If the light goes out, ships
   crash.
4. **Ship Guidance** — Ships appear on the dark ocean as distant lights. The
   player must keep the beam rotating to warn them of rocks. Successfully guided
   ships pass safely; crashed ships add wreckage and guilt.
5. **Fuel Management** — Fuel is limited. Supply boats come periodically but the
   storm delays them. The player must ration fuel, choosing between full
   brightness (safe but drains fast) and dim mode (conserves fuel but ships may
   not see it).
6. **The Creature** — Something in the water interferes: tentacles reach for the
   dock, bioluminescent lures mimic ship lights to confuse the keeper, and
   whispers try to convince the player to extinguish the lamp. The player must
   resist and repair damage.
7. **Escalation** — Each night the storm worsens, fuel becomes scarcer, and the
   creature grows bolder. The final night requires the player to keep the light
   burning through a direct assault while guiding the last ship to safety.

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
