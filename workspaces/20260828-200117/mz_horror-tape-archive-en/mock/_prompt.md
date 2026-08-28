# Horror Tape Archive

Build a **Horror Tape Archive** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player reviews surveillance tapes from a facility, scrubbing through footage
to find and timestamp anomalies. The fantasy is forensic dread: watching mundane
footage knowing something is wrong, catching the moment a shadow moves on its
own or a figure appears where none should be. Tension comes from a sanity meter
that drains as anomalies are witnessed, and from the growing realisation that
the tapes are watching back. Each correctly timestamped anomaly advances the
investigation but costs mental stability.

## What the Player Experiences

1. **Title Screen** — A VHS-styled title with tracking lines, the game name in
   monospace font, and a play button styled as a tape deck control.
2. **The Archive Room** — A desk with a CRT monitor, a tape shelf, a clipboard
   for notes, and a sanity gauge. The room is dimly lit with a single desk lamp.
3. **Tape Selection** — The player chooses from multiple labelled tapes on the
   shelf. Each tape covers a different camera location: hallway, lab, storage,
   courtyard. Tapes have different lengths and anomaly counts.
4. **Footage Review** — The monitor shows grainy surveillance footage. The player
   can play, pause, rewind, and fast-forward. A timestamp counter runs in the
   corner. The footage shows mostly normal activity with subtle anomalies hidden
   within.
5. **Anomaly Detection** — When the player spots something wrong (a shadow moving
   against the light, an object disappearing, a figure in the background), they
   pause and click "Mark Anomaly" with the current timestamp. Correct marks earn
   investigation points; false marks cost sanity.
6. **Sanity Meter** — Watching anomalies drains sanity. Low sanity causes visual
   corruption: the archive room distorts, phantom sounds play, and false
   anomalies appear in the footage to trick the player. At zero sanity, the
   session ends.
7. **Investigation Progress** — Correctly marked anomalies fill a case board,
   connecting events across tapes. Completing connections unlocks new tapes and
   reveals the facility's secret. The final tape shows what happened to the
   previous archivist.

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