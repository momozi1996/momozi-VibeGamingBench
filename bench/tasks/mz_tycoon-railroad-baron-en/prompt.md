# Railroad Baron

Build **Railroad Baron**, a **railroad empire tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player lays rail tracks across a map of cities, buys trains, and profits
from cargo demand. Each city produces and consumes different goods — connecting
a lumber town to a construction city creates a profitable route, but only if
the track is efficient and the train has capacity. Terrain drives costs:
mountains require expensive tunnels, rivers need bridges, and flat plains are
cheap but long. A competitor AI builds its own network, racing to claim the
most lucrative routes. The tension is capital allocation: every mile of track
is an investment that only pays off once trains run, and overbuilding before
revenue flows means bankruptcy. The tone is industrial-era ambition: steam,
iron, and the romance of connecting a frontier.

## What the Player Experiences

From the title screen the player starts a new map. The view shows a top-down
terrain map with cities marked by icons showing their goods (lumber, grain,
ore, manufactured goods). The player lays track by clicking city-to-city,
paying costs that vary by terrain crossed.

Once two cities are connected, the player buys a train and assigns it to the
route. Trains move automatically along tracks, picking up goods at one city
and delivering to another. Revenue depends on distance, cargo value, and
demand — delivering goods a city needs pays well; delivering surplus pays
poorly.

The player expands by connecting more cities, upgrading tracks for speed,
buying faster trains, and reading the demand map to find profitable routes.
A competitor AI builds its own network and competes for the same demand — if
they connect a route first, the player must find alternatives.

Money management is critical: track costs are upfront, train purchases are
large, and revenue trickles in over time. Taking on debt accelerates growth
but interest compounds. The game ends after a set number of years; the player
with the highest net worth wins. A styled result screen shows network maps,
revenue history, and final ranking.

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
