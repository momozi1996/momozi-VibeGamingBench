# Last Signal

Build **Last Signal**, a post-apocalyptic radio visual novel of scarce
resources and hard choices, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

The world has gone quiet, and you keep the night watch over a small radio
station that still has power. Out of the static, survivors call in — hungry,
hunted, frightened, sometimes lying. You answer with the only things you have
left: a thin store of supplies, a failing generator, and your judgment. Last
Signal is a **choice-driven visual novel of triage** where every call asks you
to decide who to help, who to turn away, who to believe — and the resources you
spend and the people you save or abandon decide what the long night makes of
you.

The fantasy is **holding a fragile lifeline together while it runs out**. The
heart of the loop is **listen, weigh, decide, live with it** — taking in a
caller's plea, judging it against what little you can spare, and committing to a
choice that costs something real and is remembered. Generosity may empty your
stores before dawn; caution may save you and damn others. The writing should
make those trade-offs weigh on the player. It should play like a tense,
atmospheric survival drama with real stakes and genuinely different endings, not
a linear script with one outcome.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player takes the night
   watch and is grounded in the station, the dead world outside, and the scarce
   resources they keep, presented as illustrated scenes with narration and a
   sense of place.
2. **Calls Out of the Static** — Survivors reach the player over the radio, each
   a distinct voice with their own situation, plea, and shadow of doubt — a
   family at a roadblock, a stranger who knows too much, a voice that may be
   bait. Calls feel like meeting people, not picking from an identical list.
3. **Decisions That Cost** — For each call the player makes a real choice — send
   supplies, open the door, talk them down, refuse, or probe for the truth — and
   choices visibly spend the player's limited resources (supplies, power, trust,
   or equivalent), so generosity and caution both have a price. The player can
   always see what they have left, and the decision is clearly registered.
4. **A Night That Remembers** — Resources and earlier decisions are carried
   forward and shape what comes later: who calls back, who can still be helped,
   which options remain affordable, and how others come to regard the station.
   Running low changes what the player can do, and a choice made early should
   visibly matter much later in the night.
5. **Many Ways for Dawn to Break** — The night resolves in one of several
   genuinely different endings — a beacon that saved many, a cold survivor who
   outlasted everyone, a station that gave until it had nothing left, or a
   darker truth uncovered — each reachable through how the player spent and
   chose, shown as an authored, styled conclusion that names what the watch
   became. The player can take the watch again to face the night differently.

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
