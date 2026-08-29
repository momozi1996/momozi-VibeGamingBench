# Arcane Academy

Build **Arcane Academy**, a magic-school stat-raising visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a first-year at a school of magic, and a term is short. There is never
enough time to master everything, so what you choose to study — elemental
sorcery, runecraft, alchemy, the tempting forbidden arts — slowly shapes the
mage you become. Arcane Academy is a **stat-raising visual novel**: between
story beats the player spends limited time and effort training different
disciplines, and the magician they grow into decides how classmates and
mentors treat them, which paths open, and how the term ends.

The fantasy is **becoming someone through the choices of a single term**. The
heart of the loop is **plan, train, live the consequences** — deciding where to
invest scarce time, watching abilities rise, and then meeting story moments
where who you have become matters as much as what you say. A student who poured
everything into forbidden magic walks a different road than a diligent
runescribe, and the writing should make that growth felt. It should play like a
warm, atmospheric school story with real stakes and genuinely different
outcomes, not a linear tour with a single ending.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player arrives at the
   academy and is introduced to the term ahead, the disciplines they might
   study, and the classmates and mentors around them, presented as illustrated
   scenes with characters and narration.
2. **Planning the Term** — Across the term the player repeatedly decides how to
   spend limited time and energy, choosing which magical disciplines to train.
   Time is scarce, so investing in one pursuit means neglecting another, and the
   player feels the weight of the trade-off.
3. **Growth That Shows** — Training visibly raises the player's abilities, and
   that progress is something the player can read and care about. The mage they
   are building takes shape over the term rather than staying fixed.
4. **Story Beats That Test You** — Between training, authored story scenes
   unfold — a rivalry, a mentor's offer, a forbidden temptation, a crisis at the
   school — where the player makes meaningful choices. What the player has
   trained matters here: some options, lines, or events are only available to a
   mage who built the right strengths, so growth and choice intertwine.
5. **A Term That Ends in Many Ways** — The term resolves in one of several
   genuinely different endings — honored graduate, fallen to the forbidden arts,
   expelled in disgrace, or the keeper of a hidden truth — each reachable
   through how the player trained and chose, and shown as an authored, styled
   conclusion that names what they became. The player can begin a new term to
   grow into someone else.

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