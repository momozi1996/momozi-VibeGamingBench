# Rhythm Conductor

Build a Rhythm Conductor as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a battlefield conductor issuing rhythmic commands to a squad of
warriors. Each command — march, attack, defend, charge — must be tapped in a
specific rhythm pattern. Nail the timing and your troops execute with power and
precision; fumble it and they stumble into disarray. Enemies advance in waves,
and the player must read the battlefield and choose the right command at the
right tempo. Between battles, the squad levels up and unlocks new command
patterns with more complex rhythms.

## What the Player Experiences

1. **Title Screen** — A war-drum themed menu with the game name in bold
   military-style lettering, a campaign button, and marching silhouettes in
   the background. No plain HTML grey.
2. **Command Input** — The bottom of the screen shows a rhythm bar. The player
   taps 4-beat patterns (e.g., tap-tap-hold-tap for "Attack") in time with a
   metronome pulse. Visual feedback shows timing accuracy per beat.
3. **Squad Response** — When a command is executed successfully, the squad
   performs the action with a power level proportional to timing accuracy.
   Perfect timing triggers a "Fever" version with bonus effects (extra damage,
   wider shield, faster march).
4. **Enemy Waves** — Enemies march from the right in formation. Different enemy
   types require different counter-strategies: shielded foes need the "Charge"
   command to break through; archers need "Defend" to block volleys; swarms
   need "Attack" for area damage.
5. **Battlefield View** — A side-scrolling battlefield shows the player's squad
   on the left and enemies on the right. Units animate their actions in sync
   with the rhythm. Health bars float above each unit group.
6. **Upgrades** — Between missions, the player spends earned resources to
   upgrade unit types (stronger attacks, faster movement) or unlock new command
   patterns (a 6-beat "Rally" that heals, a syncopated "Ambush" for critical
   hits).
7. **Boss Encounters** — Boss enemies have their own rhythm patterns that
   interfere with the player's commands. The player must maintain their own
   tempo while adapting to the boss's disruption beats.

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