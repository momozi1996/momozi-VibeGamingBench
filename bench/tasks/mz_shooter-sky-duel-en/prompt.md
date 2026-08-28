# Sky Duel

Build **Sky Duel**, a 2D aerial combat game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a nimble fighter plane through open sky, using momentum
and gravity to outmaneuver waves of enemy aircraft in dogfights that feel like
violent dances. The interesting tension is physics-driven movement: the plane has
thrust, drag, and gravity, so climbing bleeds speed while diving builds it. The
player must manage energy state — trading altitude for velocity and vice versa —
while lining up shots on enemies who exploit the same physics. Customizable plane
parts earned through score milestones let the player tune handling, firepower,
and survivability to match their style.

## What the Player Experiences

The player opens to a hangar title screen showing their current plane loadout,
then launches into a sortie. The plane flies in a 2D side-view sky with
wraparound or bounded edges. Thrust is applied with a button; the plane rotates
with left/right input and is always subject to gravity. Firing sends bullets in
the facing direction. Enemy planes enter in formations, each with distinct
behavior — dive bombers, circling aces, heavy gunships.

Destroying enemies and completing objectives earns score that unlocks new parts
at thresholds: engine upgrades for more thrust, wing shapes for tighter turns,
weapon pods for spread or homing shots, armor plating that adds weight. Between
sorties the player equips parts in the hangar. Boss encounters feature large
aircraft with multiple turrets and attack phases. The campaign spans 6+ sorties
with increasing enemy variety and environmental hazards like storms and flak
towers.

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
