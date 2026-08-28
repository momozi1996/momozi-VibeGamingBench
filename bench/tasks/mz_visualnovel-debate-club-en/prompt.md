# Debate Club

Build **Debate Club**, a **debate and contradiction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a student investigator who must expose lies in formal debates by
firing evidence at contradictory statements. Suspects make claims during
structured arguments, and the player must identify which statement contradicts
collected evidence, then present the right proof at the right moment. The
tension is timing and precision: statements scroll past, the window to object
is brief, and wrong objections damage the player's reputation score. Multiple
suspects across multiple debate rounds build toward identifying the true
culprit. The tone is academic-thriller: school halls, formal podiums, sharp
dialogue, and the rush of catching someone in a lie.

## What the Player Experiences

From the title screen the player enters an investigation phase. They explore
locations (classroom, library, courtyard) clicking hotspots to gather evidence
cards — each card has a fact, a source, and a relevance tag. Evidence
collection is the preparation for the debate.

The debate phase is the core gameplay. Suspects take turns making statements
displayed as scrolling text panels. The player listens (reads) and watches for
contradictions — a statement that conflicts with collected evidence. When they
spot one, they select the matching evidence card and fire it as a "truth
bullet" at the contradicting statement.

A correct hit triggers a dramatic break sequence: the statement shatters, the
suspect falters, and new information is revealed. An incorrect hit costs
reputation points — lose too many and the debate is lost. After breaking a
contradiction, the debate advances to a new phase with harder claims.

Multiple debate rounds across different suspects build the case. The final
round requires the player to identify the culprit from the accumulated
evidence. A styled result screen shows the verdict, reputation score, and
evidence accuracy.

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
