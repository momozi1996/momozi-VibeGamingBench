# Stealth: Shadow Courier

Build **Shadow Courier**, a compact **top-down stealth infiltration game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The fantasy is being a lone courier who survives not by fighting but by reading
the room -- memorizing patrol rhythms, threading gaps in overlapping vision
cones, and choosing the exact moment to slip through a door or kill the lights.
The interesting tension is that every objective changes the player's exposure:
picking up the key means crossing a lit corridor, stealing the document means
lingering in the most guarded room, and reaching the exit means retracing ground
where patrols have shifted. The pressure comes from the gap between what the
player can see (cone arcs, shadow pools, locked routes) and what they must risk
to advance. One miscalculated step collapses the whole plan into alarm bells and
closing nets.

## What the Player Experiences

The player arrives at a dark, atmospheric title screen that establishes the
covert tone -- the game name, a shadowy facility silhouette, and a way to begin.

A brief mission briefing sets the stakes: an archive holds a sealed document,
guards patrol the corridors, and the courier must get in, steal it, and get out
unseen.

Control begins in a top-down facility map. The courier moves smoothly through
rooms and corridors, hugging walls and cover objects. Guards walk visible patrol
routes, their vision cones sweeping ahead of them like searchlights. The player
reads the timing, waits for a gap, and slips past -- or finds another way
around.

Deeper in, a locked door blocks the direct path. The player hunts for a key or
credential, picks it up, and sees the HUD confirm possession. A light switch or
fuse box offers a different kind of power: flipping it plunges a section into
darkness, shrinking guard awareness and opening shadow routes that were
previously exposed.

The document sits in the most dangerous room. Stealing it updates the mission
state and shifts the objective to escape. The player retraces or finds a new
route to the exit, now aware that patrol timing has changed or alert levels have
risen.

Getting spotted triggers escalation -- a warning state, then capture if the
courier lingers. Reaching the exit with the document produces a styled success
screen; getting caught produces a failure screen. Either way, retry and
return-to-title controls keep the player in the loop without restarting the
application.

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
