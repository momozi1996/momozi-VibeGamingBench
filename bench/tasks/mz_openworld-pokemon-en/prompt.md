# Open World: WildRealm

Build a **creature-capture open-world RPG** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a vibrant open world, stumbles upon wild creatures in tall
grass, and engages them in turn-based battles -- capturing, training, and
growing a personal squad. The interesting tension is resource management across
encounters: every capture ball spent, every HP lost, and every skill cooldown
used is a commitment that carries forward until the player finds a healer. The
pressure escalates as the player ventures further from town into tougher
territory, and the payoff is discovering a rare creature or finally defeating
the gym leader to unlock the next region. The game should feel **bright,
adventurous, and nostalgic** -- think creature-taming meets *A Short Hike* at
a smaller scale.

## What the Player Experiences

1. **Title and Entry** -- A charming title screen sets the tone with the game
   name, a scenic background, and a clear start button. The player hits start
   and arrives in a small town -- a hub with a healer, a trainer NPC, and a
   path leading into the wilds.

2. **Open-World Exploration** -- The player walks freely across a large map
   with at least three visually distinct regions: grassy fields, a small town,
   and a locked area beyond a natural barrier. Tall grass signals danger:
   stepping into it has a chance to trigger a wild creature encounter. The
   world reads clearly at a glance -- each region has its own terrain, palette,
   and props.

3. **Encounter and Battle** -- A brief transition effect whisks the player into
   a turn-based combat scene. The player sees both combatants with HP bars,
   levels, and skill buttons. Attacking triggers visible motion and animated HP
   depletion. The player can also throw a capture ball (visible arc, shake
   animation, success/failure feedback) or flee. Wild creatures vary in species
   and level.

4. **Growth and Progression** -- Defeating opponents yields experience; the
   creature levels up with visible feedback when enough XP accumulates. The
   player's squad grows stronger over time, and captured creatures join the
   roster.

5. **NPC Interaction** -- In town, a trainer challenges the player to a forced
   battle, and a healer restores the squad. Dialog appears in a styled speech
   panel. Defeating the gym leader awards a badge that unlocks the previously
   blocked region, opening new territory to explore.

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
