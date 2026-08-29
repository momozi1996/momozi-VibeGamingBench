# Spy Handler

Build **Spy Handler**, a **spy operations management visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a handler running field agents from a command desk, receiving
messages, making real-time decisions, and managing multiple simultaneous
operations. Information is unreliable — agents may be compromised, intel may
be planted, and time pressure forces decisions before full clarity. The player
reads incoming transmissions, chooses responses from limited options, and lives
with consequences that cascade across operations. The tension is information
management under pressure: too many threads, not enough time, and the constant
question of who to trust. The tone is cold-war espionage: encrypted messages,
dossier files, red pins on maps, and the weight of lives hanging on a single
reply.

## What the Player Experiences

From the title screen the player enters the operations room — a desk with a
message terminal, a map with agent positions, and dossier files. Time advances
in real-time (acceleratable) and messages arrive from field agents.

Each message presents a situation: an agent reports a target sighting, requests
extraction, warns of a tail, or asks for instructions. The player reads the
message and selects a response from two to four options. Responses have
consequences: sending backup costs resources, ordering an agent to proceed
risks their safety, and waiting may cause the window to close.

Multiple operations run simultaneously. While handling one agent's crisis,
another's message arrives. The player must triage — some situations are urgent,
others can wait. A priority system helps but does not eliminate the pressure.

Information reliability is the core challenge. Some messages contain
disinformation from compromised agents. The player must cross-reference
reports, check agent trust ratings, and sometimes sacrifice an operation to
protect the network. Trust ratings update based on whether agent intel proves
accurate.

Operations conclude with success or failure. A styled result screen shows
mission outcomes, agent status (safe, captured, turned), and overall
intelligence gathered.

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