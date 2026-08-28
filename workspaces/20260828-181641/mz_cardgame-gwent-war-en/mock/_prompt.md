# Cardgame Gwent War

Build a Cardgame Gwent War as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A row-based card battle game where bluffing is as important as card strength.
Each player places unit cards into one of three combat rows (melee, ranged,
siege), and the side with the higher total strength at round's end wins. But
matches are best-of-three — winning a round early by dumping your hand leaves
you empty for the next. The core tension is knowing when to push and when to
pass, baiting the opponent into overcommitting. Multiple faction decks with
unique abilities and a campaign of escalating AI opponents provide depth. The
fantasy is the poker-face moment of passing with a slim lead, daring the
opponent to waste cards chasing it.

## What the Player Experiences

1. **Title Screen** — A medieval war-table aesthetic with the game name in
   iron-forged lettering, faction banners flanking the sides, and Campaign /
   Quick Match / Deck Builder buttons. No plain HTML grey.
2. **Deck Builder** — At least 3 factions (Northern Realms, Monsters, Elves)
   each with 15+ unique cards. The player builds a deck of exactly 25 cards
   from their chosen faction plus neutral cards. Each card shows art, strength
   value, row placement, and any special ability.
3. **The Board** — Three rows per side (melee/ranged/siege) displayed
   horizontally. Cards are played from hand into their designated row. Total
   strength per row and overall total are shown. The opponent's rows mirror
   above.
4. **Turn Structure** — Players alternate playing one card or passing. Once
   both pass, the round ends. The side with higher total strength wins the
   round. Best of 3 rounds wins the match. A round tracker shows current
   standing.
5. **Bluffing and Passing** — The player can pass at any time, locking in their
   current strength. The opponent must then decide whether to keep playing
   cards (wasting resources for future rounds) or also pass. This creates
   rich mind-game dynamics.
6. **Special Abilities** — Cards have abilities: Spy (played on opponent's side
   but draws 2 cards), Medic (resurrects a card from discard), Weather (reduces
   all cards in a row to 1 strength), Commander's Horn (doubles a row's
   strength), Decoy (returns a played card to hand). Each ability has a
   distinct visual effect.
7. **Campaign** — A series of AI opponents with increasing difficulty and
   unique deck strategies. Winning matches earns new cards for the player's
   collection. A world map shows progression through the campaign.

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