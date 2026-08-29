# Dig Descent

Build **Dig Descent**, a vertical descent platformer with downward shooting and
combo scoring as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A diver plunges endlessly downward through procedurally assembled shafts,
firing a weapon beneath their feet to destroy blocks, slow their fall, and
chain kills into escalating combos. The gun is both offense and movement tool —
shooting downward provides upward recoil that buys precious milliseconds to
steer around hazards. Gems collected from destroyed blocks fund visits to
mid-run shops where weapon upgrades and health refills await. The deeper the
player descends, the faster the screen scrolls and the denser the hazards
become. Death resets to the surface with nothing carried over except skill.

## What the Player Experiences

A title screen shows the game name, high score, and a Start button. Pressing
Start begins the descent immediately.

The player character falls continuously. Pressing the fire button shoots
downward, destroying soft blocks and nudging the character upward slightly.
Enemies drift across the shaft — shooting them adds to a combo counter that
multiplies gem value. Landing on a platform resets the combo but provides a
safe moment to breathe. Touching spikes, enemies, or the top of the screen
costs health.

Every few depth tiers a shop platform appears with three purchasable upgrades:
weapon spread, fire rate, health refill, or a shield. The player spends
collected gems and continues downward. Procedural generation ensures no two
runs are identical. When health reaches zero, a game-over screen shows depth
reached, gems collected, max combo, and a retry button.

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