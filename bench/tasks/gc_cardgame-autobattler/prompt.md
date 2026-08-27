# Cardgame Autobattler

Build a Cardgame Autobattler as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A draft-and-watch autobattler where the player recruits creatures from a shared
shop each round, arranges them on a board, and watches them fight automatically
against an opponent's team. Strategy lives entirely in the draft phase: which
creatures to buy, when to level up for stronger units, and how to build
synergies between tribal tags. Creatures of the same tribe buff each other —
stack enough Beasts and they gain attack; fill a row with Undead and they
resurrect once. An 8-player elimination format (simulated against AI) creates
escalating pressure as the field narrows. The fantasy is assembling a dream
team from random offerings and watching your synergy engine demolish the
opposition.

## What the Player Experiences

1. **Title Screen** — A tavern interior with the game name on a wooden sign
   above the bar, creature silhouettes seated at tables, and a "Find Match"
   button styled as a tavern door. No plain Godot grey.
2. **Shop Phase** — Each round, a shop displays 3-5 random creatures for
   purchase. The player buys creatures (spending gold), places them on a
   bench or directly onto the board (limited slots). Selling creatures
   refunds partial gold. A timer counts down to the fight phase.
3. **Board Arrangement** — The player's board has a front row and back row.
   Positioning matters: front-row creatures are attacked first; back-row
   creatures with ranged attacks stay safe longer. Drag-and-drop placement.
4. **Auto Combat** — When the timer expires, the player's board fights an
   opponent's board automatically. Creatures attack in order, targeting the
   nearest enemy. Abilities trigger based on conditions (on-attack, on-death,
   start-of-combat). The fight plays out with attack animations and health
   bars depleting.
5. **Tribal Synergies** — At least 5 tribes (Beast, Undead, Mech, Dragon,
   Elemental). Having 2/4/6 of a tribe activates escalating bonuses shown in
   a synergy tracker panel. Synergies are the primary strategic axis.
6. **Economy** — Gold income increases each round. Winning streaks and losing
   streaks both grant bonus gold. Interest accrues on saved gold (1 gold per
   10 saved). Levelling up costs gold but increases shop quality and board
   size.
7. **Elimination** — The player starts with a health pool. Losing a round
   costs health proportional to surviving enemy creatures. Last player
   standing wins. A placement screen shows final ranking.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server, no Godot.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Same pattern as `bench/references/tg1/game_logic.js`.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.

# 中文版提示词

# 卡牌自动战斗（Cardgame Autobattler）

在 `/workspace/game/` 用 Godot 4 开发一个卡牌自动战斗游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款"抽选后观战"的自动战斗游戏：玩家每一轮从共享商店招募生物，把它们布置在棋盘
上，然后看它们自动对抗敌方队伍。策略完全存在于抽选阶段：买哪些生物、何时升级
以获得更强的单位、以及如何在部族标签之间构建协同。同一部族的生物会互相增益——
攒够足够多的野兽就能获得攻击力加成；用亡灵填满一排，它们就能复活一次。8 人淘汰
赛制（对 AI 模拟）会随着场上人数收窄而制造出层层升级的压力。这份幻想在于：从
随机的供给中拼出一支梦之队，然后看着你的协同引擎摧枯拉朽地击溃对手。

## 玩家体验流程

1. **标题画面** —— 一间酒馆内景，游戏名写在吧台上方的木制招牌上，生物剪影坐在
   桌旁，还有一个做成酒馆门样式的"寻找对战"按钮。不要出现 Godot 默认的纯灰。
2. **商店阶段** —— 每一轮，商店展示 3-5 个随机生物供购买。玩家花金币买下生物，
   把它们放到备战席或直接放上棋盘（槽位有限）。出售生物会返还部分金币。一个
   计时器倒数至战斗阶段。
3. **棋盘布置** —— 玩家的棋盘分为前排和后排。站位很关键：前排生物会先被攻击；
   拥有远程攻击的后排生物能更久地保持安全。采用拖放摆放。
4. **自动战斗** —— 计时器归零时，玩家的棋盘会自动与对手的棋盘交战。生物按顺序
   攻击，以最近的敌人为目标。能力会根据条件触发（攻击时、死亡时、战斗开始时）。
   战斗过程伴有攻击动画和不断消减的血条。
5. **部族协同** —— 至少 5 个部族（野兽、亡灵、机械、巨龙、元素）。凑齐某部族
   2/4/6 个会激活层层升级的加成，并在协同追踪面板中展示。协同是最主要的策略轴。
6. **经济** —— 金币收入每轮递增。连胜和连败都会给予额外金币。存下的金币会产生
   利息（每存 10 金币得 1 金币）。升级需要花金币，但会提升商店品质和棋盘容量。
7. **淘汰** —— 玩家从一份生命值池开始。输掉一轮会按存活敌方生物数量按比例扣除
   生命值。最后存活的玩家获胜。排名画面展示最终名次。

## 提交格式（HTML）

交付物 **两个文件**：

- `index.html` —— 双击即开的单文件页面, 走 CDN 引入 `three.js`
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  **不允许** `npm install` / 构建工具 / Python 服务器 / Godot。普通笔记本 3 秒内必须渲染出来。
- `game_logic.js` —— 纯逻辑层 `createGame(opts)` / `advance(game, input, dt)`,
  由 `index.html` import。规范参考 `bench/references/tg1/game_logic.js`。

约束：
- 全部资产程序化生成(颜色、立方体、球体), 不运行时外取图像/音频。
- 键盘输入 `WASD + 空格 + Enter + ESC`。
- `index.html` 不发生运行时 `fetch/XHR`; 除 three.js 外不引入别的 CDN。
- 体量：`game_logic.js ≤ 220 行`, `index.html ≤ 120 KB`。

