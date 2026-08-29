# Ant Colony

Build **Ant Colony**, a **top-down ant colony management strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player commands an ant colony from above, directing workers to dig tunnels,
gather food, tend larvae, and defend against invaders. The colony is a living
organism: ants need roles assigned, tunnels need planning for efficient flow,
and the food stockpile determines how many mouths can be fed. The tension comes
from competing priorities — every ant digging is an ant not foraging, every
tunnel extended is a new front to defend. Seasons change the surface: summer
brings abundant food but also predators; winter cuts supply lines and forces
the colony to survive on reserves. The fantasy is being the invisible mind of
the hive, orchestrating thousands of tiny decisions into a thriving
underground civilization.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
cross-section of earth with the surface above and soil below. The queen sits
in a starting chamber and the player directs initial workers to dig outward.

Digging creates tunnels and chambers. The player designates chamber roles:
nurseries hatch eggs faster, food stores prevent spoilage, barracks train
soldiers. Workers are assigned roles by dragging them to task zones — foragers
go to the surface, diggers extend tunnels, nurses tend larvae, soldiers patrol
entrances.

Food appears on the surface as scattered resources. Foragers carry it back
along tunnel routes — shorter, wider paths mean faster delivery. The colony
grows as the queen produces eggs that hatch into new ants, but each ant
consumes food daily. Overexpansion without food income starves the colony.

Threats arrive periodically: rival insects invade through tunnel entrances,
rain floods shallow tunnels, and winter freezes surface food. The player must
balance growth against defense and plan tunnel depth for flood resistance.

The game tracks colony population and days survived. A styled result screen
shows colony statistics when the queen dies or a survival milestone is reached.

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