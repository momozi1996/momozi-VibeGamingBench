# Rule Rewrite

Build **Rule Rewrite**, a 2D grid-based word-block puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player pushes word-blocks around a tile grid to form
sentences that rewrite the rules of the level, transforming what objects do and
how the world behaves.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a spatial logic puzzle where the level itself is made of language.
Nouns, verbs, and properties exist as pushable blocks on the same grid as the
objects they describe. Forming a sentence like "WALL IS STOP" makes walls solid;
breaking that sentence by pushing a word away makes walls passable. The player
character is not fixed either — "YOU" is a property that can be reassigned to
any noun. The tension comes from the recursive nature of the rules: every move
can redefine what is dangerous, what is the goal, and what the player even
controls. The best version feels like a logic puzzle wrapped in a language game,
where each level teaches a new interaction between familiar English words.

## What the Player Experiences

A title screen introduces the game with stylized word-block imagery and a clear
way to begin. The player enters a grid where objects (walls, flags, skulls,
keys) coexist with word-blocks (nouns like WALL, FLAG; verbs like IS, HAS;
properties like STOP, WIN, PUSH, DEFEAT, YOU). Moving with arrow keys pushes
word-blocks and objects alike, one tile at a time.

Early levels teach the basics: push "FLAG IS WIN" together to make the flag the
goal, then walk into it. Soon the player discovers they can break rules apart,
reassign properties, and even change which object they control. Mid-game levels
introduce conditional chains, multiple rule sentences active simultaneously, and
objects that transform when rules change. Late levels demand planning several
moves ahead, where breaking one rule to form another creates cascading state
changes across the board.

An undo system lets the player step back freely. Level completion celebrates
with a styled screen and advances to the next puzzle. The campaign has 20+
levels with escalating complexity, grouped into worlds that each introduce a
new word or mechanic.

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