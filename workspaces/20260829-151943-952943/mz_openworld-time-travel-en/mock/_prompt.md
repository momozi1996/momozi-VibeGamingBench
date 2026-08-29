# Open-World Time Travel

Build a **2D open-world time-travel game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player discovers a time-travel device and explores the same open-world
location across multiple distinct eras — a lush ancient past, a bustling
industrial present, and a desolate high-tech future. Actions in one era ripple
forward and alter the landscape, inhabitants, and available paths in later eras.
The fantasy is **temporal cause and effect**: the player reads the world, makes
deliberate changes in the past, then jumps forward to witness consequences
unfold. Tension comes from the butterfly effect — a small act of kindness or
destruction cascades across centuries — and from paradox: the world resists
contradictions, and the player must think carefully about what they change and
when. The game should feel mind-bending and interconnected, like a puzzle box
made of history.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a "Begin Journey"
   or "Play" button, and a temporal backdrop (overlapping landscapes bleeding
   into each other, clock gears, aurora). No naked HTML 引擎 grey.
2. **Three Eras** — The same geographical region rendered in three visually
   distinct time periods: an ancient wilderness with warm saturated greens, an
   industrial cityscape with muted greys and oranges, and a ruined future with
   cold blues and purples. The player walks freely in each era and recognises
   landmarks that persist across time.
3. **Time Travel** — The player activates a time-travel device to jump between
   eras. The transition plays a visible effect and the destination era loads
   with the player at the corresponding map coordinates, preserving spatial
   continuity.
4. **Butterfly Effect** — Actions in an earlier era alter later eras in visible,
   gameplay-meaningful ways. Multiple causal chains exist: planting something in
   the past changes the landscape in the future, destroying infrastructure
   reshapes routes, befriending NPCs leaves legacies for their descendants.
5. **Paradox Detection** — The game prevents or punishes paradoxical actions.
   Attempting to destroy something your future self depends on triggers warnings
   and instability until the paradox is resolved.
6. **Cross-Era Quests and NPCs** — Each era has unique NPCs whose quests span
   multiple time periods. Completing cross-era objectives unlocks new
   destinations or upgrades the time device.
7. **Temporal Inventory** — Items have era compatibility. Some survive time
   travel while others decay. The inventory communicates which items are stable
   and which will not survive the next jump.

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