# Cardgame Spire Descent

Build a Cardgame Spire Descent as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A deckbuilder roguelike where the player ascends a spire floor by floor,
fighting enemies with a deck of cards that grows and evolves through drafting
choices. Each combat is a tactical puzzle: play attack cards to deal damage,
skill cards to gain block, and power cards for lasting buffs — all constrained
by a per-turn energy budget. Between fights, the player drafts new cards from
a reward selection, visits shops, and collects relics that bend the rules.
Three distinct character classes with different starting decks and card pools
ensure replayability. The fantasy is crafting a broken combo engine that
trivializes the final boss — if you survive long enough to assemble it.

## What the Player Experiences

1. **Title Screen** — A dark tower silhouette against a stormy sky with the
   game name in ornate fantasy lettering, and New Run / Continue buttons. No
   plain HTML 引擎 grey.
2. **Class Select** — Three character classes (Warrior, Rogue, Mage) each with
   a unique portrait, starting deck description, and signature mechanic
   (Warrior: strength scaling; Rogue: shiv generation; Mage: orb channelling).
3. **Map Navigation** — A branching path map showing the current act. Nodes
   represent combat encounters, elite fights, shops, rest sites, and events.
   The player chooses their path through the act, balancing risk and reward.
4. **Card Combat** — Turn-based battles. The player draws 5 cards per turn,
   has 3 energy to spend, and plays cards to attack or defend. Enemies show
   their intent (attack amount, buff, debuff) so the player can plan. Health
   persists between fights.
5. **Card Rewards** — After combat, choose 1 of 3 cards to add to the deck.
   Cards have rarities (Common, Uncommon, Rare) with distinct border colours.
   The player can skip the reward to keep the deck lean.
6. **Relics** — Passive items that modify rules (e.g., "gain 1 energy per
   turn", "draw 2 extra cards on turn 1"). Relics display in a bar at the top
   of the screen with tooltip descriptions. Elite enemies always drop a relic.
7. **Three Acts** — The run spans 3 acts, each with a boss at the end. Bosses
   have unique mechanics and multi-phase patterns. Defeating the final boss
   wins the run with a victory screen showing stats.

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