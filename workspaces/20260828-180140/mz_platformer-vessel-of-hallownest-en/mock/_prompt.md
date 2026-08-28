# Vessel of Hallownest

Build a **2D atmospheric metroidvania platform-action game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A silent bug knight descends into a ruined underground kingdom, armed only with
a nail and the will to press deeper. The fantasy is exploration under pressure:
every room might hold a new threat or a shortcut home, and the player is always
weighing aggression against survival. Combat is fast and punishing — each slash
refills the soul that fuels healing, so standing still means dying slowly. The
interesting tension is that the resource loop forces engagement: you heal by
fighting, but fighting risks the health you are trying to recover. Progression
gates the world behind abilities earned in earlier zones, rewarding mastery with
access rather than numbers. The tone is somber, desolate, and beautifully
tragic — cold underground ruins, glowing particles drifting through silence, and
the quiet weight of a kingdom that fell long ago.

## What the Player Experiences

A melancholic title screen greets the player with the game name and a lone
knight silhouette before they choose to begin or continue a saved journey.

The Kingdom Map appears — a network of named stages stretching downward, each
locked until the one before it falls. The player selects the first open stage
and drops in. Inside, the world is a continuous side-scrolling corridor of
connected rooms: platforms jut from cavern walls, thorn pits line the floor, and
infected husks patrol ledges. Movement feels tight and responsive — the knight
accelerates smoothly, jumps with a satisfying arc, clings to walls, and dashes
through gaps that demand precision.

Combat is immediate and visceral. Slashing an enemy staggers it, sprays geo
currency, and fills the soul meter. Taking a hit costs a mask of health and
triggers a brief flash of invincibility. When masks run low the player faces the
core dilemma: hold still to channel soul into healing — vulnerable, exposed — or
press forward and hope the next kill refills enough to survive. Enemies guard
room exits behind soul-barriers that lift only when every husk in the chamber is
dead.

Deeper rooms demand wall-clings and dashes to cross chasms the knight cannot
simply jump. Reaching the far end of a stage triggers a checkpoint that saves
progress and unlocks the next zone on the map. Death is costly — all carried geo
drops at the point of failure and the knight returns to the map to try again.

The final stage is a boss chamber: a large creature with telegraphed attack
patterns that test everything the player has learned. Victory crowns the run;
defeat sends the knight back with nothing but knowledge.

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