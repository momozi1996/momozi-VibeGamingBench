# Spelunk Depths

Build **Spelunk Depths**, a procedural platformer roguelike with physics objects
and shopkeepers as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

An explorer descends through procedurally generated cave floors, using ropes,
bombs, and whatever objects are at hand to navigate traps, defeat creatures, and
collect treasure. Every object in the world has physics — pots can be thrown at
enemies, rocks tumble when supports are destroyed, and explosions chain through
destructible terrain. Shopkeepers sell items on certain floors but turn hostile
if the player steals. A ghost timer activates after lingering too long on any
floor, creating an invincible pursuer that forces forward progress. Shortcuts
unlock after meeting specific conditions, allowing experienced players to skip
early floors. Death is permanent and sends the player back to the surface with
nothing but knowledge.

## What the Player Experiences

A title screen shows the cave entrance with depth markers. Starting a run
places the explorer at floor 1 with basic equipment: 4 ropes and 4 bombs.

Each floor is a procedurally generated platformer level with an exit at the
bottom. The explorer runs, jumps, whips enemies, throws ropes upward to create
climbable lines, and places bombs to blast through terrain. Pots, crates, and
skulls can be picked up and thrown. Traps include arrow traps, spike pits, and
crush blocks. Enemies patrol with simple AI.

Shops appear every few floors with items for sale — buying requires gold
collected from gems and chests. Stealing triggers shopkeeper aggression for the
rest of the run. After 3 minutes on a floor, a ghost spawns and chases the
player relentlessly. Every 5 floors the environment theme changes. Death shows
a summary of depth reached, gold collected, and enemies defeated.

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

# 洞穴深渊（Spelunk Depths）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Spelunk Depths**——一款带物理物件和店主的
程序化平台跳跃 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位探险家向下穿越程序化生成的洞穴层，利用绳索、炸弹以及手边任何物件来通过陷阱、
击败生物、收集宝藏。世界里的每一个物件都有物理——罐子可以砸向敌人，支撑被破坏后
岩石会滚落，爆炸会在可破坏地形中连锁传播。店主在某些层出售道具，但如果玩家偷东西
就会转为敌对。在任意一层逗留过久会激活幽灵计时器，产生一个无敌的追猎者，迫使玩家
持续向前推进。满足特定条件后会解锁捷径，让老练的玩家跳过前面的层。死亡是永久的，
会把玩家送回地表，除了经验之外一无所有。

## 玩家体验流程

标题画面展示带深度标记的洞穴入口。开始一轮时，探险家出现在第 1 层，携带基础装备：
4 条绳索和 4 枚炸弹。

每一层都是一个程序化生成的平台跳跃关卡，底部有一个出口。探险家奔跑、跳跃、用鞭子
抽打敌人、向上抛出绳索造出可攀爬的绳线，并放置炸弹炸穿地形。罐子、木箱和骷髅可以
被捡起投掷。陷阱包括弓箭陷阱、尖刺坑和压碎方块。敌人以简单 AI 巡逻。

商店每隔几层出现一次，摆出待售道具——购买需要从宝石和箱子中收集来的金币。偷窃会
在这一轮的余下时间里触发店主的敌意。在一层停留 3 分钟后，一个幽灵会刷出并不停
追赶玩家。每 5 层环境主题变换一次。死亡时展示抵达深度、收集金币和击败敌人数的总结。

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

