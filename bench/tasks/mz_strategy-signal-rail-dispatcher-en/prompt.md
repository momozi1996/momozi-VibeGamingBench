# Signal Rail Dispatcher

Build **Signal Rail Dispatcher**, a compact 2D railway signal and routing
management game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

The player is a lone dispatcher in a cramped signal box, watching colored
trains crawl across a schematic board and making split-second routing calls
that ripple forward in time. Every switch flip commits a path; every red signal
buys thinking room at the cost of punctuality. The fantasy is **quiet mastery
under mounting pressure** — a timetable that starts gentle, then stacks
conflicting services until the board is a web of near-misses and the player
must think several moves ahead to keep everything flowing. The best version
feels like a control-room puzzle where one wrong toggle cascades into delay,
and a clean shift feels earned.

## What the Player Experiences

1. **The Shift Begins** — A styled title screen sets the tone of a railway
   control room. The player starts a shift and sees a compact track diagram
   with stations, sidings, signals, and switchable junctions laid out like a
   schematic map.
2. **Reading the Board** — Trains appear at entry points and crawl along the
   tracks. Each train has a visible identity — color, service type, destination
   — and the timetable or HUD tells the player where it needs to go and when.
   Signals glow red or green; switches show which way they are set.
3. **Routing Decisions** — The player clicks signals to hold or release trains,
   and flips switches to redirect paths. A released train follows the set route
   until it hits the next red signal or reaches its destination. The challenge
   is sequencing: two trains cannot safely share a section, and letting one
   through means another waits.
4. **Escalation** — The shift intensifies. More trains arrive, express services
   demand priority, delays compound, and blocked sections force creative
   rerouting. Conflict warnings or occupancy lights tell the player when a
   collision is imminent.
5. **Resolution** — The shift ends with a result screen reporting punctuality,
   incidents avoided or caused, and overall performance. The player can retry
   or return to the title without restarting the application.

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
