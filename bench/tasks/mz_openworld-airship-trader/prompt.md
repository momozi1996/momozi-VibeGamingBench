# Open-World Airship Trader

Build a **2D open-world airship trading game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player pilots an airship through a sky filled with floating islands, each
with its own economy and goods to trade. The fantasy is freedom above the clouds:
charting routes between distant ports, buying low and selling high, upgrading
your vessel with better engines and cargo holds, and fending off sky pirates who
lurk along trade lanes. Tension comes from fuel management, pirate ambushes, and
volatile market prices that shift as you trade.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name over a parallax sky
   backdrop with drifting clouds and distant islands. A play button begins the
   journey.
2. **The Sky Map** — The player flies their airship freely across a large open
   sky. Multiple floating islands are visible, each with a distinct silhouette
   and colour palette. Clouds drift in parallax layers.
3. **Docking** — Approaching an island triggers a docking prompt. Once docked,
   the player enters a trade menu showing local goods, prices, and their cargo
   hold contents.
4. **Trading** — Each island produces certain goods cheaply and demands others at
   premium prices. The player buys cargo, flies to another island, and sells for
   profit. Prices fluctuate over time.
5. **Upgrades** — Profits fund ship upgrades: faster engines, larger cargo hold,
   better fuel efficiency, and hull armour. Upgrades are visible on the ship
   sprite.
6. **Sky Pirates** — Along certain routes, pirate ships appear and chase the
   player. The player can outrun them, fight with a mounted cannon, or pay a
   toll. Combat is real-time with simple projectile shooting.
7. **Fuel & Risk** — The airship consumes fuel while flying. Running out means
   drifting helplessly. Fuel can be bought at islands or found in floating
   crates.

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

# 开放世界飞艇商人（Open-World Airship Trader）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界飞艇贸易游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶一艘飞艇穿行于漂满浮空岛的天空，每座岛都有自己的经济体系和可供
贸易的货物。这里的幻想是云端之上的自由：在遥远港口之间开辟航线，低买高卖，
用更好的引擎和货舱升级自己的船，并击退潜伏在贸易航道上的天空海盗。张力来自
燃料管理、海盗突袭，以及随你贸易而不断波动的市场价格。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，游戏名称叠在带视差滚动的天空背景上，
   云朵飘动，远处可见岛屿。一个开始按钮启程。
2. **天空地图** —— 玩家驾驶飞艇在一片广阔开放的天空中自由飞行。视野中可见
   多座浮空岛，每座都有独特的轮廓与配色。云层以视差层次飘动。
3. **停靠** —— 接近岛屿时触发停靠提示。停靠后，玩家进入贸易菜单，其中显示
   当地货物、价格以及自己货舱中的物品。
4. **贸易** —— 每座岛都会廉价产出某些货物，同时高价求购另一些货物。玩家买入
   货物，飞往另一座岛，卖出获利。价格随时间波动。
5. **升级** —— 利润用于升级飞艇：更快的引擎、更大的货舱、更好的燃料效率以及
   船体装甲。升级会体现在飞艇精灵图上。
6. **天空海盗** —— 在某些航线上会出现海盗船追击玩家。玩家可以甩掉他们、用
   船载火炮迎战，或者交过路费。战斗为实时进行，采用简单的抛射物射击。
7. **燃料与风险** —— 飞艇在飞行时消耗燃料。燃料耗尽意味着只能无助地随风漂流。
   燃料可以在岛上购买，也可以从漂浮的木箱中找到。

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

