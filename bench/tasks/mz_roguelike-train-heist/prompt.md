# Train Heist

Build **Train Heist**, a procedural train-car roguelike with car-by-car
encounters as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A bandit boards the caboose of a procedurally generated train and must fight
forward car by car to reach the engine before the train arrives at the station.
Each car is a self-contained encounter: a passenger car with civilians to rob,
a guard car with armed defenders, a cargo car with locked safes to crack, a
dining car with cover-based shootouts, or a mail car with time-locked vaults.
The bandit carries limited ammo and health, spending both as they push forward.
Loot from earlier cars funds purchases at a black-market car that appears
mid-train. A turn counter represents distance to the station — if it hits zero
before reaching the engine, the heist fails. Each run generates a new train
with different car sequences and lengths.

## What the Player Experiences

A title screen shows a steam train silhouette against a sunset. Starting a run
shows the full train in side-view with car types partially visible (some
hidden).

The player enters the caboose and encounters the first car's challenge. Combat
is turn-based with cover mechanics — the bandit and enemies take positions
behind furniture and exchange fire. Ammo is limited and must be looted from
fallen guards. Passenger cars offer robbery choices: intimidate for quick cash
or search thoroughly for better loot but risk alerting guards ahead.

A progress bar shows position along the train and turns remaining. The black-
market car offers health kits, ammo, special weapons, and disguises. Reaching
the engine triggers a boss fight against the conductor. Victory shows total
loot, cars cleared, and turns remaining. Failure (health zero or time out)
shows how far along the train the bandit reached.

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

# 列车劫案（Train Heist）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Train Heist**——一款逐节车厢展开遭遇的
程序化列车车厢 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名匪徒登上一列程序化生成的列车的尾车，必须一节一节向前打，在列车到站之前抵达
车头。每节车厢都是一场自成一体的遭遇：载着可供抢劫的平民的客车厢、有武装守卫的
警卫车厢、有待撬保险柜的货运车厢、以掩体为核心展开枪战的餐车，或者有定时锁金库的
邮政车厢。匪徒携带的弹药和生命值都有限，一路向前推进就是在消耗这两样。前面车厢
的战利品，可以在列车中段出现的黑市车厢里用于采购。一个回合计数器代表到站的距离
——若它在抵达车头之前归零，这次劫案就失败了。每一轮都会生成一列车厢序列和长度
各不相同的新列车。

## 玩家体验流程

标题画面展示夕阳映衬下的蒸汽列车剪影。开始一轮后，展示整列列车的侧视图，车厢
类型部分可见（有些隐藏）。

玩家进入尾车，遭遇第一节车厢的挑战。战斗是回合制并带有掩体机制——匪徒和敌人各自
在家具后面占据位置并交火。弹药有限，必须从倒下的守卫身上搜刮。客车厢提供抢劫
选择：恫吓以快速拿钱，或者仔细搜查以获得更好的战利品，但要承担惊动前方守卫的风险。

一条进度条显示在列车上的位置和剩余回合数。黑市车厢提供医疗包、弹药、特殊武器和
伪装。抵达车头会触发一场对抗列车长的 Boss 战。胜利展示总战利品、清空的车厢数和
剩余回合数。失败（生命值归零或时间耗尽）则展示匪徒在这列车上走到了多远。

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

