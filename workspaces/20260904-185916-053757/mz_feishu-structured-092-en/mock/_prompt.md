# science fiction universe

You are a senior Vibe Gaming designer, gameplay engineer, interaction designer,
and QA engineer. Turn the evidence below into a **complete, runnable, testable,
replayable original browser game**, not a static demo or a visual-only mockup.

## Task Identity

- Benchmark family: action game
- Task dimension: 2D
- Required technology: Canvas, planet drawing, starship, space battle
- Source: Feishu “Prompt Catalog” · 直接1 · source index 92

## Original Gameplay Brief (Semantically Immutable)

> Create a fully playable browser game vertical slice around the "Sci-Fi Universe Demo". This is an original implementation driven by the question type and must use or reasonably explain the following technical constraints: Canvas, Planet Drawing, Starship, Space Combat. Please convert the question type into a clear core loop, player input, state changes, success and failure conditions; it must not stop at static display, and must be able to start, play, settle and replay.

This brief is the gameplay and logic anchor. You may reduce content quantity for
a browser vertical slice, but must not delete, replace, or weaken its core inputs,
rules, states, goals, failure conditions, or technology constraints. If the brief
only supplies a type and technology seed, explicitly state your assumptions and
build the smallest complete same-family loop; do not pretend hidden rules were
provided.

## Vibe Gaming Implementation Requirements

1. Start by writing a one-page implementation specification, then create files,
   run the page, and execute tests; do not stop at a plan.
2. Convert the brief into a verifiable state machine: title, onboarding, playing,
   pause, failure, victory/result, restart, and restoration. Each state needs
   inputs, transitions, exit conditions, and visible feedback.
3. Build a clear loop: start -> understand objective -> perform the main action ->
   immediate feedback -> resource/progress update -> success or failure -> next,
   retry, or title.
4. Implement at least three escalating phases: teach the core action, combine it
   with pressure, and finish with a synthesis scenario. If the source brief states
   a level count, preserve it where practical.
5. Give every important action at least two feedback channels (motion, scale,
   particles, color, sound, HUD, or camera). Invalid input, damage, failure,
   success, and persistent state changes must be distinguishable.
6. Keep the HUD minimal but stable. Show objective, critical resources, selection,
   progress, danger, timer/score, and current phase; never rely on color alone.
7. Make primary interactions clear for one hand/keyboard use; pointer targets must
   be at least 44x44 CSS px, and mouse/touch input must not depend on hover.
8. Use original names, procedural artwork, original audio, or explicitly licensed
   assets. Do not copy trademarks, characters, narrative text, artwork, music,
   sound effects, level data, servers, or reverse-engineered code.
9. Use localStorage for settings, best scores, and permitted progress. Do not upload
   personal data, connect real payments or ads, or create an unreviewed multiplayer service.

## HTML Submission Contract

Deliver two files: `index.html` and `game_logic.js`. Use Canvas, planet drawing, starship, space battle for the
2D presentation when appropriate, but keep the rules layer independent
from DOM, Canvas, WebGL, or WebGPU rendering.

The page must open without a build step and expose meaningful interaction within
three seconds. Do not request external images, models, video, or audio at runtime.
Procedural geometry, Canvas2D, SVG, CSS, Web Audio, shaders, pinned libraries, and
`data:` URIs are allowed. If a CDN is used, pin an official library version.

Interaction scheme (keyboard-first): Use keyboard input as the primary control with arrows or WASD plus clear Space, Enter, and Escape actions; add pointer input where natural.
Keep the play area and HUD readable at 1280x720 and avoid horizontal overflow or
unreachable controls at 390x844, 360x800, and 430x932. Include title, playing,
pause, failure/victory, restart, and state-restoration flows.

`index.html` owns presentation and input. `game_logic.js` owns deterministic rules
and exposes:

```javascript
(function (root) {
  function createGame(opts) { return { phase: "title", score: 0 }; }
  function advance(game, input, dt) { return game; }
  const api = { createGame, advance };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` must not access DOM or rendering objects. Random content must be
reproducible from a seed.


## Acceptance Criteria

- First meaningful interaction within three seconds; the core loop is understandable within 60 seconds.
- No overlap, horizontal scrolling, clipped text, or unreachable controls at
  390x844, 360x800, 430x932, and 1280x800.
- `game_logic.js` loads directly in Node; `createGame({seed})` and
  `advance(game, input, dt)` run deterministically and do not depend on the DOM.
- Provide at least 12 meaningful rule/state tests and five Playwright or equivalent
  end-to-end flows.
- README documents startup, gameplay, states, tests, directory structure, technical
  tradeoffs, and differences from the original brief.
- Finish by reporting actual file paths, launch commands, test results, screenshot
  paths, known limitations, and original-asset provenance.