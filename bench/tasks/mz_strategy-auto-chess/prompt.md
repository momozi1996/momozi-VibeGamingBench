# Auto Chess

Build **Auto Chess**, an **auto-battler draft-and-position strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

Eight players enter a tournament where the battlefield fights itself. Between
rounds the player drafts units from a shared shop, places them on a grid board,
and watches them clash automatically against an opponent's formation. The
strategy is entirely in the draft and the positioning: which units to buy, when
to level up for more board slots, how to arrange front-line tanks and back-line
damage dealers, and which synergy traits to chase. Gold management is the
heartbeat — rerolling the shop costs gold, saving gold earns interest, and
going broke at the wrong moment means fielding a weaker army than everyone else.
Elimination rounds whittle the field until one player remains.

## What the Player Experiences

The player opens to a lobby screen showing eight portraits (one human, seven
AI). Each round begins with a preparation phase: a shop offers five random
units, the player buys with gold, drags units onto a grid board, and arranges
their formation. Combining three copies of the same unit upgrades it to a
stronger star level with a visible transformation.

Units belong to classes and origins that grant synergy bonuses when enough of
the same trait are fielded — the synergy tracker shows active and upcoming
bonuses. The player must decide between a focused synergy build and grabbing
individually powerful units.

When the timer expires, the combat phase begins. Units auto-attack, cast
abilities, and fall until one side is eliminated. The losing player takes
damage to their health pool based on surviving enemy units. Between rounds the
player sees a scoreboard of all eight competitors and their health.

The economy rewards patience: unspent gold earns interest each round, but
falling behind in power means taking heavy damage. The tension is always
between spending now to survive and saving to spike later.

The game ends when the player is eliminated or is the last one standing. A
styled result screen shows final placement and key stats.

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

# 自走棋（Auto Chess）

在 `/workspace/game/` 用 Godot 4 开发 **Auto Chess**，一款**自动战斗抽卡与站位策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

八名玩家进入一场由战场自行厮杀的锦标赛。回合之间，玩家从共享商店中抽选单位，把它们摆在格状棋盘上，然后看它们自动对阵对手的阵型。策略完全在于抽选与站位：买哪些单位、何时升级以获得更多棋盘格位、如何编排前排坦克与后排输出、以及要追求哪些协同特质。金币管理是这一切的心跳——刷新商店要花金币，攒金币能吃利息，而在错误的时机破产就意味着你的军队比所有人都弱。淘汰赛不断削减参赛者，直到只剩一名玩家。

## 玩家体验流程

玩家一开始看到的是大厅画面，上面有八个头像（一名人类、七名 AI）。每一回合以准备阶段开始：商店提供五个随机单位，玩家用金币购买，把单位拖到格状棋盘上，并编排阵型。将同一单位的三个副本合并可以把它升级到更强的星级，并伴有可见的形态变化。

单位归属于不同职业与种族，当场上同一特质的单位数量足够时便会授予协同加成——协同追踪器会显示已激活与即将激活的加成。玩家必须在专注的协同体系与抓取单体强力单位之间做出取舍。

计时器归零时，战斗阶段开始。单位自动攻击、施放技能、相继倒下，直到一方被全歼。落败的玩家会根据存活的敌方单位数量损失生命值。回合之间，玩家可以看到全部八名参赛者及其生命值的积分榜。

经济奖励耐心：未花完的金币每回合都会产生利息，但战力落后就意味着承受重创。张力始终存在于"现在花钱求生存"与"攒钱以求后期爆发"之间。

当玩家被淘汰或成为最后的幸存者时，游戏结束。一个精心设计的结算画面会展示最终排名与关键数据。

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

