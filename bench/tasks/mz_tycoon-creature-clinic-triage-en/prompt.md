# Creature Clinic Triage

Build **Creature Clinic Triage**, a compact **creature-care clinic simulation**
as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player runs a tiny fantasy veterinary clinic during a busy shift. Creatures
arrive faster than they can be treated, each carrying visible ailments that hint
at what they need. The core tension is triage under pressure: which patient do
you attend first, where do you send them, and what happens to the ones still
waiting? Correct reads and smart routing keep the clinic humming and build
reputation; mistakes, delays, or mismatches cost health and trust.

The tone is warm but operational. The clinic floor should feel alive with
queuing creatures, busy stations, and clear feedback when things go right or
wrong. Avoid spreadsheet aesthetics; make it feel like a working fantasy
infirmary.

## What the Player Experiences

The player opens to a themed clinic entrance and begins a shift. Patients start
filing in, each a distinct creature with visible symptoms and an urgency
indicator. Early arrivals are straightforward — one clear ailment, one obvious
destination. The player learns the rhythm: inspect, decide, route.

As the shift continues, the queue grows. New creature types appear with
unfamiliar or combined symptoms. Stations fill up or run low on supplies.
The player must now prioritize: stabilize the critical case or clear the easy
ones to free capacity? A wrong routing wastes time and worsens the patient.
Ignoring urgency lets conditions deteriorate.

Late in the shift, pressure peaks — emergencies, compound cases, resource
scarcity. The player juggles capacity against urgency, making rapid imperfect
decisions. When the shift ends, a results summary reflects how well they
managed: creatures healed, creatures lost, reputation earned, and whether
they unlocked harder shifts or upgrades.

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
