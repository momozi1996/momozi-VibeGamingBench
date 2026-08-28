# Cozy Harbor Delivery

Build **Cozy Harbor Delivery**, a 2D top-down delivery routing mini-game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A small courier boat putters through a sun-dappled harbor, weaving between
islands and buoys to ferry parcels from pickup crates to waiting dock customers.
The tension lives in the routing: multiple orders tick down simultaneously, each
with a different destination and urgency, and the harbor is just tangled enough
that the player cannot serve everyone on a straight line. Choosing which parcel
to grab first, which customer to disappoint, and when to risk a tight shortcut
between moored hulls is the entire decision space. Between shifts the player
reinvests earnings into speed, cargo capacity, or route hints, shaping how the
next shift feels. The tone is warm and unhurried on the surface but quietly
demanding underneath — a cozy logistics puzzle wrapped in watercolor docks and
bobbing boats.

## What the Player Experiences

A styled title screen sets the mood: the game name, a harbor map illustration,
and a courier boat identity greet the player before they press Start.

The shift begins on a top-down harbor map alive with water lanes, wooden docks,
rocky islands, painted buoys, and waiting customers. The player steers the boat
smoothly through the water, feeling it slow near obstacles and bounce off island
edges. Picking up a crate changes the boat's silhouette or HUD loadout,
confirming what is aboard and where it needs to go.

Orders stack up on the screen — each with a destination marker and a countdown.
Some are leisurely, others flash urgent. The player threads routes, drops
parcels at matching customers, and watches coins or reputation tick upward with
each successful delivery. Miss a timer and the customer frowns away. A day timer
or shift meter counts down the round, escalating the pressure as remaining
orders pile up.

When the shift ends, a result screen tallies deliveries, earnings, and a
performance rating. Between shifts an upgrade or planning screen offers choices
that change the next run — faster engine, bigger hold, better route hints. The
loop invites one more shift, then one more after that.

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