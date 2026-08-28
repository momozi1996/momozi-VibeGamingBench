# Courtroom Clue Trial

Build **Courtroom Clue Trial**, a compact **courtroom deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player is a junior advocate trying to expose a false account during a
dramatic trial. Each testimony line is a small puzzle: the witness says something
that sounds plausible, but one piece of evidence in the player's folder proves it
wrong. The tension comes from choosing when to press, what to present, and how
many mistakes the judge will tolerate before the case collapses. A wrong
accusation costs credibility; too many losses end in mistrial. The fantasy is
reading people, catching lies, and turning a courtroom on a single well-timed
objection.

## What the Player Experiences

The player opens to a case-file title screen that sets the tone: a courtroom
seal, a case number, the weight of a pending trial. Starting the case brings a
brief that lays out the charge, the suspect, and the evidence folder. Then the
witness takes the stand. Their testimony scrolls statement by statement, and the
player can press for more detail or advance to the next line. At any point the
player can open the evidence tray, inspect cards with facts like timestamps,
fingerprints, or locations, and present one against the current statement. A
correct match triggers an objection sequence: the witness falters, the testimony
updates, and the case shifts. A wrong match draws a penalty from the judge.
After the first contradiction breaks, a second layer emerges: a rebuttal, a new
clue, an alibi that does not quite hold. The player must navigate this deeper
puzzle to reach a verdict. Success means a styled victory with case-closed
fanfare. Failure means a mistrial screen with the option to retry. Both outcomes
feel like endings, not error states.

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