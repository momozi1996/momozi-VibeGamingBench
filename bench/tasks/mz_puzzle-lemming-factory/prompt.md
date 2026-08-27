# Lemming Factory

Build **Lemming Factory**, a 2D creature-guiding puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player assigns jobs to a stream of marching factory
workers — diggers, builders, blockers, climbers — to guide them safely from
an entrance hatch to an exit door, saving a required quota each level.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a real-time puzzle about indirect control. Creatures march
autonomously in a straight line, turning at walls, falling off ledges, and
walking into hazards unless the player intervenes. The player cannot move
creatures directly but can click on individual workers to assign them a job
from a limited toolbar. Each job transforms the creature's behavior: diggers
carve downward through terrain, builders construct diagonal staircases, blockers
become impassable walls that redirect traffic, and climbers scale vertical
surfaces. The tension comes from limited job supplies, time pressure as
creatures march toward danger, and the spatial reasoning needed to route a
crowd through complex terrain. The best version feels like conducting an
orchestra of tiny workers where every assignment ripples through the crowd's
path.

## What the Player Experiences

A title screen sets the factory tone with marching creature silhouettes and a
clear way to begin. The player enters a level where terrain, hazards (pits,
saws, lava), an entrance hatch, and an exit door are visible. A toolbar shows
available jobs with remaining counts. The hatch opens and creatures begin
marching out at a steady rate.

Early levels teach one job at a time: assign a digger to carve through a floor,
or a builder to bridge a gap. Soon levels require combining jobs — a blocker
redirects traffic while a digger opens an alternate path. Mid-game introduces
climbers for vertical navigation, floaters for safe falls, and bombers for
emergency terrain removal. Each level specifies a save quota; losing too many
creatures to hazards means failure.

The player can adjust release rate and pause to plan. When enough creatures
reach the exit, a results screen shows the save percentage and offers the next
challenge. The campaign has levels grouped into difficulty tiers, each
introducing new terrain types and job combinations.

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

# 旅鼠工厂（Lemming Factory）

在 `/workspace/game/` 用 Godot 4 开发 **Lemming Factory**，一个 2D 生物引导解谜
游戏。玩家给一队不停行进的工厂工人分配职业——挖掘工、建造工、阻挡工、攀爬工
——引导它们从入口舱门安全走到出口大门，并在每关救下规定的配额。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款关于间接控制的实时解谜游戏。生物会自主地沿直线行进，碰墙转身，从平台
边缘掉落，若玩家不干预就会一头撞进危险中。玩家无法直接移动生物，但可以点击
某个工人，从数量有限的工具栏中给它分配一个职业。每个职业都会改变该生物的行为：
挖掘工向下凿穿地形，建造工搭出斜向阶梯，阻挡工变成不可通行的墙来改变人流走向，
攀爬工则能攀上垂直表面。张力来自职业名额有限、生物不断向危险行进带来的时间压力，
以及把一大群生物疏导穿过复杂地形所需的空间推理。最理想的版本会让人感觉像在
指挥一支小工人组成的交响乐团，每一次分配都会在人群的路线上层层扩散。

## 玩家体验流程

标题画面用行进中的生物剪影营造出工厂氛围，并给出清晰的开始入口。玩家进入关卡后
能看到地形、危险物（深坑、锯片、岩浆）、入口舱门和出口大门。工具栏显示可用职业
及其剩余数量。舱门打开，生物开始以稳定的速率涌出。

前期关卡一次只教一个职业：派一个挖掘工凿穿地板，或派一个建造工架桥跨过缝隙。
很快，关卡就会要求组合使用职业——用阻挡工改变人流方向，同时让挖掘工打开另一条
通路。中期引入用于垂直移动的攀爬工、用于安全降落的漂浮工，以及用于紧急清除地形
的爆破工。每关都规定一个救援配额；被危险物害死的生物太多就算失败。

玩家可以调整放出速率，也可以暂停来做规划。当足够多的生物抵达出口时，结算画面
展示救援百分比，并给出下一个挑战。战役中的关卡按难度层级分组，每一层级都引入
新的地形类型和职业组合。

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

