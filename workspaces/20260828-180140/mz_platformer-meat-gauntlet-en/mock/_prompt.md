# Meat Gauntlet

Build **Meat Gauntlet**, a die-and-retry speed platformer with saw blades and
replay ghosts as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A tiny square of meat hurls itself through rooms bristling with spinning saw
blades, retracting spikes, and crumbling ledges. Death is instant and restart
is instantaneous — the loop is attempt, die, learn, attempt again until the
room clicks. After clearing a room, a ghost of the successful run replays
alongside the next attempt, turning past mastery into a visible companion. Fifty
compact levels across five worlds escalate from simple jumps to frame-tight
gauntlets that demand wall-slides, mid-air direction changes, and split-second
timing. The game celebrates speed: each level tracks completion time and a
global death counter reminds the player how far they have come.

## What the Player Experiences

A punchy title screen shows the game name, a level-select grid (unlocked
progressively), and a death counter. Selecting a level drops the player in
instantly.

Each level is a single screen. The meat character runs and jumps with tight,
responsive controls. Saw blades spin in fixed or patrolled paths. Spikes
retract and extend on timers. Crumbling platforms vanish after contact. Touching
any hazard kills instantly — the screen flashes, and the player respawns at the
start within a fraction of a second.

On clearing a level, the completion time displays and a ghost recording is
saved. Re-entering the level shows the ghost replaying the best run as a
translucent afterimage. Clearing all levels in a world unlocks the next world
with new hazard types. A results screen per world shows times and death counts.

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