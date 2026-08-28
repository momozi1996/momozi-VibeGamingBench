# News Editor

Build **News Editor**, a 2D newspaper management simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a scrappy newspaper, deciding which stories to chase,
which reporters to assign, and whether to prioritize speed or accuracy in a
media landscape where both reputation and revenue matter. The interesting tension
is the fact-check tradeoff: publishing fast captures readers and ad revenue but
risks printing errors that damage credibility; thorough fact-checking produces
reliable journalism but competitors scoop you and readers drift away. Reporters
have specialties and reliability ratings, stories have complexity and time
sensitivity, and the player must match resources to opportunities while keeping
the lights on.

## What the Player Experiences

The player opens to a newsroom title screen with a printing press motif, then
enters the editor's desk view. The main screen shows today's story leads in an
inbox, the current edition layout, reporter assignments, and financial status.
Story leads arrive throughout the day with topic, complexity, time sensitivity,
and potential impact ratings.

The player assigns reporters to stories, choosing between fast coverage (higher
error risk) and deep investigation (slower but more accurate). Completed stories
are placed in the edition layout — front page, inside, or buried. Publishing
triggers reader response: accurate scoops boost reputation and subscriptions;
errors trigger corrections that cost credibility. Revenue comes from
subscriptions and advertisers (who care about readership numbers). Between
editions the player can hire/fire reporters, invest in fact-checking tools, or
expand coverage areas. The campaign spans 20+ editions with escalating story
complexity, competitor pressure, and financial targets. An edition summary shows
stories published, accuracy rate, readership change, and profit/loss.

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