# Tycoon: Funfair

Build a **grid-based theme-park management tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The fantasy is turning a bare patch of land into a roaring amusement park that
people love to visit. The player is part architect, part accountant: every path
laid and ride placed shapes how a living crowd moves, spends, and feels. The
interesting tension is that growth feeds on itself — a happy crowd generates the
cash to build more attractions, which draws a bigger crowd — but the snowball
works in reverse too. Neglect paths, gouge prices, or let queues balloon and the
park empties faster than it filled. The pressure comes from balancing ambition
against the crowd's patience: expand too fast and you're broke, too slow and
guests get bored. The risk is always that one bad decision — a dead-end path, a
price hike, a missing amenity — quietly poisons satisfaction before the numbers
catch up.

## What the Player Experiences

The player starts with an empty lot, a gate, and a small pile of cash. The first
minutes are about laying a spine of paths out from the entrance and dropping a
first ride — watching the first handful of guests trickle in and spend money is
the hook. From there the arc is organic growth: earnings fund new rides and
stalls, the crowd swells, and the grid fills with colour and motion.

What the player notices most is the crowd itself — little visitors streaming
along paths, pooling at popular rides, drifting toward food stalls. A well-built
park hums with movement; a badly planned one has lonely corners and bottlenecks.
The satisfaction readout and the cash counter tell the story at a glance, but the
real feedback is visual: a thriving park looks busy and alive.

Pricing is the lever that keeps things interesting even in a mature park. Charge
more and each guest is worth more, but fewer come and they leave sooner. Drop
prices and the gates flood, but margins thin. The player is always tuning this
dial alongside layout decisions — where to put the next ride, whether to upgrade
an existing one into a headline attraction, when to add another food stall to
keep the far side of the park happy.

Over time the lot transforms from a bare grid into a sprawling, bustling
fairground. Progress persists across sessions, so the player returns to the same
park and picks up where they left off. The tone throughout is bright, cheerful,
and colourful — a sunlit carnival of spinning rides and candy colours.

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
