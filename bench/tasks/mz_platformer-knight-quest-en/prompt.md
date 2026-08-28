# Knight Quest

Build **Knight Quest**, a retro action platformer with melee combat and
sub-weapons as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

An armored knight ventures forth from a peaceful village hub into eight themed
stages — haunted crypt, volcanic forge, frozen peak, sunken temple, sky
fortress, poison swamp, clockwork tower, and shadow throne — each ending in a
boss encounter. The knight wields a primary melee weapon with a satisfying
three-hit combo and collects sub-weapons (throwing axe, boomerang cross, holy
water, dagger) that consume a shared ammo resource. Stages are linear but hide
optional treasure chests behind skill challenges. Between stages the village
hub offers a shop for health upgrades and sub-weapon restocks. The tone is
bright, chunky pixel-art nostalgia with modern responsive controls.

## What the Player Experiences

A title screen shows the game name, the knight's silhouette, and Start/Continue
options. Starting fresh places the player in the village hub — a small
scrolling area with a shop NPC and a stage-select gate showing eight portals
(only the first unlocked initially).

Entering a stage begins a side-scrolling level with platforms, pits, and
enemies. The knight attacks with a melee combo and can use sub-weapons with a
secondary button. Enemies drop gems for the shop and occasional health pickups.
Each stage ends with a boss that has a visible health bar and telegraphed attack
patterns. Defeating the boss unlocks the next stage and returns to the hub.

The shop sells health capacity upgrades, sub-weapon ammo packs, and a damage
boost. Progress is saved between sessions. Completing all eight stages triggers
a victory screen with stats.

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
