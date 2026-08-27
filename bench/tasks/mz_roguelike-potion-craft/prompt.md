# Potion Craft

Build **Potion Craft**, a potion-brewing roguelike with ingredient maps and
recipe discovery as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

An alchemist navigates a procedural ingredient map, gathering herbs, minerals,
and essences to brew potions that fulfill customer orders. Brewing is a
navigation puzzle on an alchemy map — the player steers a mixing cursor through
ingredient space, and the path taken determines the potion's properties. Each
customer wants a specific potion type (healing, fire resistance, invisibility)
and the alchemist must discover recipes by experimentation, then reproduce them
reliably. Between days the shop earns reputation that unlocks rarer ingredients
and harder customers. Failing too many orders loses reputation until the shop
closes. Each run is a fresh start with a new ingredient layout to discover.

## What the Player Experiences

A title screen shows bubbling cauldrons and potion bottles. Starting a run
opens the shop on Day 1 with three customer orders visible.

The brewing screen shows an alchemy map — a 2D space with ingredient nodes
connected by paths. The player navigates a cursor from the center outward,
passing through ingredient zones that add properties to the brew. Reaching a
recipe zone and bottling creates a potion of that type. The map is partially
hidden and revealed through exploration.

Customers arrive with orders (icons showing desired potion type). Fulfilling
an order earns gold and reputation. Gold buys map reveals, better tools (faster
navigation, wider paths), and ingredient restocks. Each day brings new
customers with harder requests. After a set number of days, a final evaluation
scores the run based on reputation, gold earned, and recipes discovered. Losing
all reputation ends the run early.

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

# 魔药工艺（Potion Craft）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Potion Craft**——一款带材料地图和配方探索的
炼药 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当
足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位炼金术士在程序化生成的材料地图上探索，采集草药、矿物和精华，酿造药水来满足
顾客订单。酿造本身是炼金地图上的一道导航谜题——玩家操纵一个搅拌光标穿过材料空间，
而走过的路径决定了药水的属性。每位顾客想要某种特定类型的药水（治疗、抗火、隐身），
炼金术士必须通过试验发现配方，然后稳定地复现出来。营业日之间，店铺积累声望，
解锁更稀有的材料和更难应付的顾客。失败的订单太多就会掉声望，直到店铺关门。
每一轮都是全新开始，等待发现一套新的材料布局。

## 玩家体验流程

标题画面展示咕嘟冒泡的坩埚和药水瓶。开始一轮后，店铺在第 1 天开门，三份顾客
订单清晰可见。

酿造画面展示一张炼金地图——一片由路径连接材料节点的 2D 空间。玩家把光标从中心
向外导航，穿过为药剂添加属性的材料区域。抵达某个配方区域并装瓶，就得到该类型的
药水。地图部分隐藏，通过探索逐步揭示。

顾客带着订单到来（图标显示想要的药水类型）。完成订单可获得金币和声望。金币可用
于购买地图揭示、更好的工具（导航更快、路径更宽）和材料补货。每一天都会带来提出
更难要求的新顾客。经过设定的天数后，一次最终评估依据声望、赚到的金币和发现的
配方为这一轮打分。声望全部失去则会提前结束这一轮。

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

