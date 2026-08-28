# Open-World Archaeology

Build a **2D open-world archaeology game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).:
an expedition across ancient ruins where the player excavates buried artefacts,
deciphers forgotten inscriptions, and reconstructs lost civilisations one dig
at a time.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Unearth the past. The player is an archaeologist who travels to remote dig
sites, carefully removes layers of earth and stone, and discovers artefacts
that tell the story of vanished cultures. The fantasy is patient revelation:
each brush stroke peels back time, each shard connects to a larger picture, and
the deeper you dig the rarer and more fragile the finds become. One careless
swing of the pickaxe can shatter a legendary relic; one solved inscription can
unlock a hidden chamber no one has entered in millennia.

The pressure comes from the sites themselves. Sandstorms bury progress, floors
collapse underfoot, oxygen runs thin in flooded passages. The player must read
the terrain, choose the right tool, and decide when to push deeper versus when
to retreat and catalogue what they have. A growing museum back at base camp
makes every expedition feel worthwhile -- each new display fills in a gap in
the timeline and unlocks access to the next frontier.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen that
   establishes the mysterious, ancient tone -- torchlit stone, weathered maps,
   sand drifting across glyphs. Starting an expedition drops them into the
   overworld.

2. **Exploration** -- The world stretches across multiple biomes, each hiding
   its own dig sites. Desert temples shimmer under a scorching sun, jungle ruins
   drip with moss and vine, sunken pillars glow beneath turquoise water, and
   mountain tombs sit locked in ice. Walking between sites feels like a journey
   -- the terrain changes, the palette shifts, the ambient mood transforms.

3. **Excavation** -- At a dig site the player switches between tools -- a
   delicate brush for fragile surfaces, a trowel for packed earth, a pickaxe
   for solid rock. Each tool removes material at a different speed and risk.
   Layers peel away visually, revealing colour changes and texture shifts as
   depth increases, until an artefact edge glimmers into view.

4. **Discovery and Cataloguing** -- Unearthed artefacts range from common
   pottery shards to legendary golden idols. Each has a distinct look, a rarity
   tier, and a short historical description. Rare finds are buried deeper and
   demand more careful tool selection. The player feels the thrill of not
   knowing what lies beneath the next layer.

5. **Puzzles and Secrets** -- Some sites hide inscribed tablets or symbol murals
   that gate access to sealed chambers. The player manipulates symbols -- matching,
   rotating, tracing -- until the lock yields and a passage opens with a
   satisfying rumble. Inside waits a guaranteed rare artefact or a new wing of
   ruins to explore.

6. **Museum and Progression** -- Back at base camp, a museum tent displays
   every collected artefact on labelled shelves. Arranging finds by culture or
   era earns research points that unlock improved tools and new dig sites on the
   map. The museum grows from empty shelves to a rich gallery, charting the
   player's journey through history.

7. **Hazards and Tension** -- Each biome threatens the player differently:
   sandstorms obscure vision, jungle floors collapse, underwater oxygen depletes,
   mountain ice triggers avalanches. The player watches a health or safety gauge,
   decides whether to press on or retreat, and scavenges safety gear to push
   further next time.

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