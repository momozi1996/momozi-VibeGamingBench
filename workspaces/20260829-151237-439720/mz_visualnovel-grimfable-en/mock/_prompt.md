# Grim Fable

Build **Grim Fable**, a branching dark-fairytale visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You step into fairy tales you think you already know — but the woods are darker
than you remember, the kind are not always good, and the wicked may have their
reasons. Grim Fable is a **choice-driven visual novel** where the player relives
familiar storybook tales as their protagonist, yet the choices on offer were
never in the original telling. What looks like a bedtime story hides an uneasy
truth, and the player's decisions decide which version of that truth comes to
pass.

The fantasy is **rewriting a story you assume you know**. The game should turn
the player's own expectations into the trap: a beloved tale opens the familiar
way, then forks toward outcomes the fairy tale never allowed. The heart of the
loop is **read, examine, weigh, decide** — taking in a richly written scene,
looking closely at what the illustration is hiding, sizing up who and what to
trust, and committing to a choice that the story remembers and pays off later.
It should feel like turning the pages of a haunted picture book where text,
portraits, backdrops, and choice menus all belong to the same authored world.
This is a polished, atmospheric storybook with real stakes and genuinely
different endings, not a linear text dump with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player begins the tale and
   is eased into a familiar fairy-tale premise, presented as an illustrated
   storybook scene with characters, narration, and a clear sense of who they
   are and where they stand.
2. **Reading & Examining the Scene** — The story unfolds through paced dialogue
   and narration over illustrated backdrops, but the scene is not just read — it
   invites investigation. Props, details of the setting, and the characters
   present can hide narration, clues, or secrets the player would otherwise
   miss, so the comforting tale's darker underside is something the player
   uncovers, not just something told to them.
3. **Clues That Add Up** — What the player examines and learns is **gathered and
   remembered**: a blood-flecked knife noticed on a table, a confession teased
   out of a character, a detail that contradicts the storybook version. These
   discoveries accumulate into the player's understanding and unlock or color
   the choices and revelations that follow, rewarding a curious player who looks
   closely over one who rushes ahead.
4. **Meaningful Choices** — At key moments the player is offered choices that
   the original story never gave them — whom to trust, what to reveal, which
   path to take through the wood. Choices are deliberate decisions with stakes,
   not cosmetic flavor; what the player has uncovered shapes which options are
   available and what they mean, and the game makes clear that a decision has
   been made and registered.
5. **Consequences That Stick** — Earlier choices are remembered and shape what
   comes later: which characters confide in the player, what truths surface,
   and which doors close. The player should feel the story bending around their
   decisions rather than running on rails, and recurring tales or returning
   characters should reflect what the player did before.
6. **Divergent Endings** — The tale resolves in one of several genuinely
   different endings — a subversion of the happy ending, a grim reckoning, a
   hidden truth uncovered, or a quiet escape — each reachable through different
   choices and clearly tied to how the player played. The ending is an authored,
   styled conclusion that names what the player's path brought about, and the
   player can begin again to seek a different one.

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