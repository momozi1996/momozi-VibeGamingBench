# Roguelike: Wildwood

Build a **node-map forest-exploration roguelike with turn-based combat** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The fantasy is reading a dangerous forest. Every fork in the trail is a bet
placed with incomplete information: claw marks on a trunk, smoke curling above
the canopy, a glint of metal in the undergrowth. The player pushes deeper not
because the path is safe but because the clues make the risk feel knowable. When
a beast appears, combat is deliberate and positional — a small kit of skills
spent against creatures that each punish a different mistake. Health never
refills for free, so every scratch from three clearings ago still matters at the
final gate. Death is permanent for the run, but not for the player: banked gold
and a dwindling supply of entry tickets give each expedition weight without
making failure a dead end. The tone is hushed and watchful — dappled light,
distant howls, the crackle of a campfire earned by surviving one more node.

## What the Player Experiences

The player begins at a trailhead camp that remembers them between sessions —
tickets, gold, and whatever lasting advantages they have earned are all visible
here. Entering the forest costs a ticket, so the decision to set out already
carries stakes.

Once inside, the run unfolds as a branching map of trail nodes stretching deeper
into the wood. Nodes are not fully revealed; instead the map offers partial
evidence — tracks, smoke, glitter, disturbed brush — that lets the player weigh
risk against their current health, gold, and depth. Committing to a node strips
away the mystery: it might be a beast, a chest, a campfire, a trader, a trap, or
something worse.

Combat is turn-based and skill-driven. The hero carries several distinct
abilities that cost a resource, and different beasts demand different responses —
a fast wolf, an armored bear, a venomous serpent. Lingering conditions like
poison or bleed play out over multiple turns, rewarding the player who reads the
threat and plans ahead.

Between fights the player collects relics and gear that reshape how the hero
fights, not just refill health. Growth within a run is tangible: new buttons, new
options, new ways to handle what the forest throws next.

A run ends in victory — reaching the heart of the wood and overcoming its
guardian — or in death, which sends the player back to camp minus a ticket but
richer in banked gold. Progress persists across sessions, so quitting and
returning picks up the same hoard and the same slow accumulation of power.

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

# 中文版提示词

# Roguelike：荒林（Roguelike: Wildwood）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款**带回合制战斗的节点地图森林探索
Roguelike**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当
足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

游戏的幻想核心是读懂一片危险的森林。小径上的每一个岔口都是一场在信息不完整的
情况下押下的赌注：树干上的爪痕、林冠上方盘绕的烟、灌木丛中一闪的金属光。玩家
之所以继续深入，不是因为路是安全的，而是因为那些线索让风险显得可以估量。当野兽
出现时，战斗是审慎且讲究位置的——一小套技能被花在各自惩罚不同失误的生物身上。
生命值从不会免费回满，所以三片林间空地之前挨的每一道擦伤，到最终之门时依然要紧。
死亡对这一轮是永久的，但对玩家不是：存入的金币和数量渐减的入场券，让每次远征
都有分量，同时又不让失败变成死路。整体调性是压低声息、时刻警觉的——斑驳的光影、
远处的嚎叫、以及靠多熬过一个节点换来的营火噼啪声。

## 玩家体验流程

玩家从一处小径起点营地开始，这里会在多次游玩之间记住他——入场券、金币，以及他
挣得的所有持久优势都在这里一目了然。进入森林要花掉一张入场券，所以出发这个决定
本身就已带有筹码。

一旦进入，这一轮就以一张不断向林中深处延伸的小径节点分支地图展开。节点不会被
完全揭示；地图只提供局部证据——足迹、烟、微光、被扰动的灌木——让玩家在当前的生命值、
金币和深度之间权衡风险。选定一个节点会剥去它的神秘：那可能是一头野兽、一只箱子、
一处营火、一名商人、一个陷阱，也可能是更糟的东西。

战斗是回合制且以技能驱动的。英雄拥有若干各不相同、需要消耗一种资源的能力，而不同
的野兽要求不同的应对——迅捷的狼、披甲的熊、含毒的蛇。中毒或流血这类持续状态会在
多个回合内逐步发作，奖励那些读懂威胁并提前规划的玩家。

战斗之间，玩家收集遗物和装备，它们会重塑英雄的战斗方式，而不只是回满生命值。
一轮之内的成长是可触摸的：新的按钮、新的选项、应对森林下一次抛来之物的新方式。

一轮的结局是胜利——抵达林之心并战胜它的守卫者——或是死亡，死亡会把玩家送回营地，
少了一张入场券，但存入的金币更丰厚。进展在多次游玩之间持续保留，因此退出再回来
时，接手的还是同一份积蓄和同一条缓慢累积力量的道路。

## 提交格式（HTML）

交付物 **两个文件**：

- `index.html` —— 双击即开的单文件页面, 走 CDN 引入 `three.js`
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  **不允许** `npm install` / 构建工具 / Python 服务器。普通笔记本 3 秒内必须渲染出来。
- `game_logic.js` —— 纯逻辑层 `createGame(opts)` / `advance(game, input, dt)`,
  由 `index.html` import。规范参考 `bench/references/tg1/game_logic.js`。

约束：
- 全部资产程序化生成(颜色、立方体、球体), 不运行时外取图像/音频。
- 键盘输入 `WASD + 空格 + Enter + ESC`。
- `index.html` 不发生运行时 `fetch/XHR`; 除 three.js 外不引入别的 CDN。
- 体量：`game_logic.js ≤ 220 行`, `index.html ≤ 120 KB`。

