# Open-World Bounty

Build a **2D open-world bounty hunter game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a lone hunter roaming a lawless frontier, picking contracts off a
weathered quest board and tracking dangerous marks across hostile terrain. The
fantasy is **pursuit under uncertainty** -- each bounty is a commitment to
venture deeper into unfamiliar ground, and the interesting tension is that the
hunter must read the landscape, manage limited resources, and choose when to
engage versus when to retreat. The pressure comes from escalating target
difficulty, dwindling supplies, and the knowledge that a failed hunt means
walking back empty-handed. The risk is always that the next mark fights harder
than expected, or that the hunter spent too much on an easy bounty and has
nothing left for the real threat.

## What the Player Experiences

1. **Title and Entry** -- A gritty, western-fantasy title screen sets the tone.
   The player hits start and arrives in a frontier town -- a hub with a tavern,
   a quest board, and a handful of NPCs who sell gear or patch wounds.

2. **Picking a Contract** -- The quest board displays available bounties, each
   with a target portrait, a difficulty rating, and a gold reward. The player
   reads the cards, weighs risk against payout, and commits to a mark. The
   chosen bounty becomes the active hunt, and the world shifts focus toward
   tracking.

3. **The Hunt** -- A compass or directional marker guides the player out of
   town and into the wilds. The world has multiple distinct regions -- forest
   hideouts, bandit camps, rocky canyons -- and the target waits somewhere
   inside, patrolling or lying in ambush. The journey itself is part of the
   experience: terrain changes, ambient threats, and the growing distance from
   safety.

4. **Confrontation** -- Finding the target triggers combat. The hunter has
   multiple attack options and must read the target's behavior to survive.
   Targets fight back with visible aggression; health bars deplete on both
   sides. Different marks demand different tactics -- one is fast and evasive,
   another is armored and punishing.

5. **Claiming the Reward** -- Returning to town after a successful hunt
   triggers a payout sequence. Gold is added to the purse, the bounty card is
   struck from the board, and the hunter can spend earnings on better gear or
   harder contracts. The loop resets with new marks and higher stakes.

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