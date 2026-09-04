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

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. Use HTML Canvas 2D or Three.js/WebGL for the playable presentation.
- `game_logic.js` - the deterministic state and rules layer. Use a classic script
  and expose `createGame(opts)` and `advance(game, input, dt)`; an optional
  `render(gameState, renderCtx)` hook may be exposed.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Assets must be generated at runtime with no network
requests: procedural geometry, Canvas2D-drawn textures encoded as `data:` URIs,
offscreen-canvas particle sprites, Web Audio API synthesized sound, shaders,
post-processing, and CSS are all allowed and encouraged. Do not embed or fetch
external image, model, video, or audio files at runtime. Three.js may be loaded
from its pinned official CDN; if post-processing is used, pin the matching
`examples/jsm/postprocessing/*` modules to the same Three.js version.

Interaction scheme (both): Support both keyboard and pointer controls: use keyboard for movement or actions and the pointer for spatial selection, menus, or targeting.
Keep the complete play area and HUD readable at 1280x720. Include a clear start
flow, concise in-game guidance, pause and restart controls, a complete win/loss
or scored outcome loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest` for external URLs; only
the pinned Three.js CDN above is allowed. Keep `index.html` at or below 400 KB.
The `game_logic.js` line count is advisory and is not a BUILD-gate failure.

### Logic and rendering scaffold

```html
<script src="./game_logic.js"></script>
<script>
  const { createGame, advance, render } = window.GameLogic;
  const game = createGame({});
  // The loop calls advance; render(game, { THREE, scene, ... }) is optional.
</script>
```

```javascript
(function (root) {
  function createGame(opts) { return { phase: "title", score: 0 }; }
  function advance(game, input, dt) { return game; }
  function render(gameState, renderCtx) { /* optional visual hook */ }
  const api = { createGame, advance, render };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` must be pure and must not access DOM or Three.js objects. The optional
`render()` hook is called by the main loop and may map state to scenes, materials,
particles, and post-processing.