# Music Label

Build **Music Label**, a **music label management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player runs an independent music label, signing artists, producing albums,
marketing releases, and scheduling tours. Each artist has a genre, talent
level, morale, and fanbase that grow or shrink based on management decisions.
The market shifts — genres trend up and down, and timing a release to ride a
wave multiplies sales. The tension is resource allocation: studio time is
limited, marketing budgets are finite, and pushing an artist too hard burns
them out. The tone is creative-industry drama: recording studios, chart
battles, and the thrill of a breakout hit.

## What the Player Experiences

From the title screen the player starts a new label. The main view shows the
label dashboard: signed artists, upcoming releases, financial summary, and
genre trend charts. Time advances week by week.

Artists are scouted from a pool — each has a genre, talent rating, and
personality traits that affect studio behavior. Signing costs an advance and
commits to producing their album. In the studio, the player allocates
production weeks and chooses a producer style (polished, raw, experimental)
that affects album quality and genre fit.

Marketing is a budget allocation: spend on social media, radio, press, or
touring. Each channel reaches different audiences and has diminishing returns.
Timing matters — releasing during a genre's peak trend multiplies exposure.

Tours generate revenue and grow fanbases but cost money upfront and drain
artist morale. An exhausted artist produces worse albums and may leave the
label. The player must balance exploitation against artist care.

Revenue comes from album sales, streaming royalties, tour profits, and
merchandise. Expenses include studio rent, staff salaries, advances, and
marketing. The game tracks label reputation, total revenue, and chart
positions. A styled result screen shows label achievements each quarter.

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
