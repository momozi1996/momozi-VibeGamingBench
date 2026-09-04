# Horror Floor 13

Build a **Horror Floor 13** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is an elevator operator in a cursed building where each floor is a
self-contained nightmare. The fantasy is being trapped in service: passengers
request floors, and the player must deliver them — but every floor visited warps
reality further. Tension comes from passenger requests that conflict (some floors
are dangerous, some passengers are not what they seem) and the elevator itself,
which malfunctions as the curse deepens. The building has thirteen floors, and
floor 13 should never be visited.

## What the Player Experiences

1. **Title Screen** — A dark art-deco elevator panel with floor numbers, the game
   name in brass lettering, and a play button styled as the door-close button.
2. **The Elevator** — The main view is the elevator interior: a floor selector
   panel, an indicator showing current floor, doors that open and close, and a
   small window showing the shaft.
3. **Passengers** — NPCs enter and request floors. Each has a distinct appearance
   and demeanour. Some are normal; others are unsettling (wrong number of eyes,
   flickering sprites, speaking backwards). The player must choose whether to
   comply with requests.
4. **Floor Visits** — When doors open on a floor, the player sees a vignette:
   a hotel hallway that stretches infinitely, an office where everyone is frozen,
   a ballroom with no floor. Each floor is a unique horror scene with a brief
   interactive element.
5. **Malfunctions** — The elevator increasingly misbehaves: going to wrong floors,
   lights flickering, buttons rearranging, the indicator spinning. The player
   must adapt and maintain control.
6. **Passenger Consequences** — Delivering passengers to wrong floors or refusing
   requests has consequences: the building grows more hostile, new impossible
   floors appear, and the elevator descends toward floor 13.
7. **Floor 13** — The final floor. Reaching it triggers the climax. What the
   player did with passengers determines the ending. Multiple endings exist based
   on choices made.

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