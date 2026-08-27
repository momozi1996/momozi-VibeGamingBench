# Cozy Harbor Delivery

Build **Cozy Harbor Delivery**, a 2D top-down delivery routing mini-game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A small courier boat putters through a sun-dappled harbor, weaving between
islands and buoys to ferry parcels from pickup crates to waiting dock customers.
The tension lives in the routing: multiple orders tick down simultaneously, each
with a different destination and urgency, and the harbor is just tangled enough
that the player cannot serve everyone on a straight line. Choosing which parcel
to grab first, which customer to disappoint, and when to risk a tight shortcut
between moored hulls is the entire decision space. Between shifts the player
reinvests earnings into speed, cargo capacity, or route hints, shaping how the
next shift feels. The tone is warm and unhurried on the surface but quietly
demanding underneath — a cozy logistics puzzle wrapped in watercolor docks and
bobbing boats.

## What the Player Experiences

A styled title screen sets the mood: the game name, a harbor map illustration,
and a courier boat identity greet the player before they press Start.

The shift begins on a top-down harbor map alive with water lanes, wooden docks,
rocky islands, painted buoys, and waiting customers. The player steers the boat
smoothly through the water, feeling it slow near obstacles and bounce off island
edges. Picking up a crate changes the boat's silhouette or HUD loadout,
confirming what is aboard and where it needs to go.

Orders stack up on the screen — each with a destination marker and a countdown.
Some are leisurely, others flash urgent. The player threads routes, drops
parcels at matching customers, and watches coins or reputation tick upward with
each successful delivery. Miss a timer and the customer frowns away. A day timer
or shift meter counts down the round, escalating the pressure as remaining
orders pile up.

When the shift ends, a result screen tallies deliveries, earnings, and a
performance rating. Between shifts an upgrade or planning screen offers choices
that change the next run — faster engine, bigger hold, better route hints. The
loop invites one more shift, then one more after that.

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

# 温馨港湾快递（Cozy Harbor Delivery）

在 `/workspace/game/` 用 Godot 4 开发 **Cozy Harbor Delivery**，一款 2D 俯视视角送货路线规划小游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一艘小小的快递船在阳光斑驳的港湾里嗒嗒穿行，在岛屿与浮标之间迂回，把包裹从取货货箱送到码头上等待的客户手中。张力就在于路线规划：多份订单同时倒计时，每一份都有不同的目的地和紧急程度，而港湾的地形恰好错综到玩家无法沿一条直线服务所有人。先抓哪个包裹、让哪位客户失望、以及何时冒险从停泊的船体之间穿一条贴身近道，这就是全部的决策空间。班次之间，玩家把收入重新投入到速度、载货容量或路线提示上，从而塑造下一个班次的手感。整体调性表面温暖悠然，底下却暗含要求——一道被水彩码头和摇曳小船包裹起来的温馨物流谜题。

## 玩家体验流程

一个经过设计的标题画面奠定气氛：游戏名、一幅港湾地图插画，以及一个快递船的身份形象，在玩家按下开始之前迎接他们。

班次从一张俯视港湾地图开始，图上水道、木质码头、岩石岛屿、彩绘浮标和等待中的客户一派生机。玩家平顺地驾船穿行水面，能感觉到它在靠近障碍时减速、在岛缘上弹开。拾取一个货箱会改变船的剪影或 HUD 上的装载信息，确认船上载了什么、要送往何处。

订单在屏幕上层层堆叠——每一份都带有目的地标记和倒计时。有些不慌不忙，有些则闪着紧急提示。玩家串联路线，把包裹投递给对应的客户，看着金币或声望随每次成功送达向上跳动。错过一个计时器，客户就会皱着眉离开。一个日程计时器或班次进度条为本轮倒数，随着未完成订单堆积而不断加压。

班次结束时，结算画面清点送达数、收入和一个表现评级。班次之间的升级或规划画面提供会改变下一轮的选择——更快的引擎、更大的货舱、更好的路线提示。这个循环会诱使玩家再来一班，然后再来一班。

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

