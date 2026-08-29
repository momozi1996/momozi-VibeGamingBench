# Idle Spell Tower

Build an **Idle Spell Tower** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds a wizard's tower that generates mana passively, researches
spells, and automates magical casting for ever-increasing power. The fantasy is
arcane accumulation: watching mana flow from crystal to crystal, spells firing
automatically at targets, and the tower growing taller with each prestige cycle.
The idle loop generates mana continuously; the player's decisions shape which
spells to research and how to allocate mana between offence, defence, and
growth. Prestige collapses the tower and rebuilds it higher with better
foundations.

## What the Player Experiences

1. **Title Screen** — A tall wizard tower against a starry sky with magical
   particles flowing upward, the game name in arcane script, and a play button
   glowing with mana.
2. **Tower View** — A vertical tower cross-section showing floors. Each floor
   has a function: mana generators, spell labs, crystal storage, automated
   casters. The tower grows as floors are added.
3. **Mana Generation** — Base mana ticks up automatically. Mana generators on
   each floor contribute to the rate. The player can click a crystal to manually
   generate bursts. A large mana counter dominates the UI.
4. **Spell Research** — A research tree shows available spells. Each spell costs
   mana and time to research. Researched spells can be assigned to auto-casters
   or cast manually for immediate effect.
5. **Automated Casting** — Auto-caster floors fire spells at targets (monsters
   approaching the tower base) without player input. Each caster has a rate and
   spell assignment. Defeating monsters yields mana crystals.
6. **Tower Growth** — Spending mana builds new floors, each with a specific
   function. Higher floors generate more mana but cost exponentially more. The
   tower visually grows taller.
7. **Prestige** — When the tower reaches maximum height, the player can collapse
   it (prestige). The tower resets to one floor but gains a permanent height
   multiplier, faster mana generation, and access to higher-tier spells. Each
   rebuild reaches greater heights faster.

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