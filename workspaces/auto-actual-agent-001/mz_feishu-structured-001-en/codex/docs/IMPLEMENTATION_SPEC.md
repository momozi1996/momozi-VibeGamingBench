# Traditional Pixel Turn-Based RPG — Implementation Spec (One Page)

## Core Loop
- Title -> Onboarding -> Explore (Playing) -> Random Encounter -> Battle -> Win/Lose -> Explore or Defeat -> Floor Exit -> Next Floor -> Final Boss -> Victory/Result -> Restart/Restore.
- Deterministic seeded RNG (Mulberry32) across logic; all randoms pulled from game.rng().
- Immediate feedback: movement tick sound + camera nudge; damage numbers; color flashes; SFX via WebAudio (UI only) + HUD updates.

## States (State Machine)
- : Inputs: Start, Load. Transitions: Start -> ; Load -> .
- : Shows controls/tutorial; Input: Confirm ->  (floor 1). Exit: give small potion + simple sword.
- : Inputs: Move (up/down/left/right), Interact, Menu, Pause. Exit conditions: encounter check -> ; at stairs (interact) -> go next  floor; meet NPC (interact) -> dialog branch flag; open chest -> loot; HP<=0 -> .
- : Inputs: Resume, Save, Quit. Transitions: Resume -> ; Quit -> .
- : Turn-based. Player turn actions: Attack (physical), Skill (Fire, Shield), Item (use potion), Run. Enemy acts after player or first when faster. Exit: enemy HP<=0 ->  (with rewards) or final boss -> ; player HP<=0 -> .
- : Show summary, score, time, floors cleared. Inputs: Restart -> .
- : Show summary. Inputs: Restart -> .
- : Load snapshot into current state (usually ), then continue.

## Combat
- Stats: HP, MP, ATK, DEF, SPD, LVL, EXP. Equipment: weapon, armor; Inventory list; Items stack.
- Skills: Fire (mp 5, magic dmg = ATK*0.5+10, ignores 50% DEF), Shield (mp 4, buff +DEF for 5 turns); Debuff: Poison (chance from enemy), 3 turns, 4 dmg per turn.
- Turn order by SPD; status effects tick at each round start; Damage variance small (±10%) via RNG.
- Damage numbers pop; flash tint on hit; shake.

## World/Progression
- Floors: 1–3 (phases escalate). Procedural dungeon per floor via drunkard-walk ensuring connectivity. Place: player spawn, stairs, 1 NPC (floor 1), 3–6 chests, 6–10 enemy spawn candidates.
- Encounters: step counter + encounter rate ramp; enemy tier per floor; floor 3 has final boss room near stairs.
- Branch: Help NPC (accept quest) -> grant one-time heal + +score, else get small gold only; branch influences score and NPC state text.

## HUD & Input
- HUD fixed: HP/MP bars, LVL/EXP, Objective text, Floor, Score, Branch flag, Mini-map viewport, Current phase.
- Keyboard: Arrows/WASD move; Space interact/confirm; Enter confirm; I inventory menu; Esc pause; 1–4 battle choices.
- Pointer: click/tap large menu buttons (>=44px) and battle targets; click on-grid to set movement intent (discrete step).

## Save/Load
- LocalStorage under key : JSON snapshot of game state (seed + RNG state + full game object). Game logic exposes pure object; UI handles storage.

## Audio/Art
- Pixel palette: low-saturation 16-bit-ish; All sprites are Canvas rectangles, lines, circles; particles for hits/chests.
- SFX synthesized via WebAudio oscillators (square/triangle/noise) with short envelopes.

## Determinism & Tests
-  is pure/deterministic; no DOM access; consumes at most one queued command per call; dt used for animation timers but rules only change at command/turn boundaries.
- Provide 12+ rule/state tests in Node; 5 end-to-end logic flows simulating complete runs including final boss victory.

## Directory
- , ,  (runner + tests),  (flows),  (this spec), .

## Constraints & Tradeoffs
- Keep rendering simple; prioritize readability and closed-loop completeness over elaborate art.
- E2E use logic-only “equivalent” flows due to headless environment; UI is exercised in browser manually; SFX muted until user gesture.
