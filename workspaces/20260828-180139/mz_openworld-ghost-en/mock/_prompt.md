# Open-World Ghost Hunting

Build a **2D open-world ghost hunting game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores haunted locations across an open-world town, using
specialised equipment to detect, track, and capture ghosts. The game feels
**atmospheric, tense, and investigative** -- think *Phasmophobia* meets
*A Short Hike* at a smaller scale. The art style must be **coherent and
dark-atmospheric**: muted palettes, fog overlays, flickering light sources,
and readable sprites against shadowy backgrounds.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen with a
   spooky backdrop (foggy graveyard, flickering lantern, silhouette of a house)
   and a "Begin Hunt" or "Play" button. Starting drops them into the open-world
   town hub.

2. **The Haunted World** -- The player walks freely across an open-world town
   with at least four visually distinct haunted locations: an abandoned mansion
   (dark, broken windows, overgrown garden), a haunted forest (twisted trees,
   fog, glowing eyes), an old lighthouse (coastal, waves, creaking wood), and a
   derelict hospital (corridors, flickering lights, wheelchairs). Each location
   has its own atmosphere and ghost type.

3. **Detection Equipment** -- The player carries at least three tools: an EMF
   reader (beep frequency increases near ghosts), a thermal camera (shows cold
   spots as blue overlays), and a spirit box (captures ghost voices as text).
   Each tool has distinct visual and audio feedback. Ghosts are invisible
   without equipment -- the tools are the only way to find them.

4. **Ghost Types and Evidence** -- At least four distinct ghost types with
   unique behaviours: poltergeist (throws objects), wraith (freezing breath,
   walks through walls), banshee (screams before attacking), and shade (hides
   in darkness, afraid of light). Each type leaves specific evidence that the
   player must collect and cross-reference on an evidence board to identify it.

5. **The Hunt Phase** -- When enough evidence is collected, the ghost becomes
   aggressive: lights flicker, the environment distorts, and a hunt timer
   counts down. The player must use defensive items (crucifix, salt circle,
   flashlight) to survive and capture the ghost before time runs out.

6. **Sanity and Pressure** -- A sanity meter drops in darkness, when seeing
   ghost activity, or when alone too long. Low sanity causes hallucinations
   (false readings, fake shadows) and makes the ghost more aggressive. Light
   sources and safe rooms restore sanity, creating a push-pull between
   investigation and self-preservation.

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