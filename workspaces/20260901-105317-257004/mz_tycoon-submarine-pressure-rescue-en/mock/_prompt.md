# Submarine Pressure Rescue

Build **Submarine Pressure Rescue**, a compact **submarine damage-control and
rescue simulation** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

The player commands a battered rescue sub sinking toward crush depth. Water
pours through breached compartments, pressure climbs, oxygen bleeds out, and
the power grid can only feed so many systems at once. Every order is a tradeoff:
seal a bulkhead to slow flooding but trap a crewmate, reroute power to pumps
but lose sonar, send the engineer to patch a hull breach while the med bay goes
unattended. The fantasy is desperate, competent leadership under impossible
constraints — keeping a dying vessel alive long enough to reach the rescue
beacon and bring survivors home.

The tone is tense industrial survival: dark hull cross-sections, warning lights,
blue sonar sweeps, valve icons, crew markers, and clear alarm feedback.

## What the Player Experiences

The player opens to a styled submarine rescue title screen with hull silhouette
and emergency signal. A mission briefing introduces the objective, crew roster,
and initial damage state.

Once the mission begins, the player sees the sub's compartment layout with
water levels, pressure gauges, oxygen, and power routing. Early damage is
manageable — a single leak, one crew member to assign. The player learns the
rhythm: identify the threat, assign crew, watch the repair progress, check
the sonar for distance to the beacon.

As the mission continues, failures cascade. A second compartment breaches while
the first is still being pumped. Power drops and the player must choose which
systems stay online. Oxygen falls in sealed sections. Crew members get trapped
or injured. The sonar shows the beacon getting closer, but new hazards appear
on the route.

In the final stretch, everything is failing simultaneously. The player makes
rapid imperfect calls — sacrifice a compartment to save the rest, burn the last
power reserve on pumps, hope the hull holds. Reaching the beacon and
stabilizing the vessel shows rescue success. Hull collapse, oxygen depletion,
or failed evacuation shows defeat. Both outcomes are styled and navigable.

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

Interaction scheme (pointer-first): Use click, hover, drag, or selection as the primary controls; add keyboard shortcuts only where they are natural.
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