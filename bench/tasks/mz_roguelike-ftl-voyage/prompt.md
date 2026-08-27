# FTL Voyage

Build **FTL Voyage**, a spaceship management roguelike with crew and sector
navigation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A small starship flees through procedurally generated sectors toward a final
confrontation, managing crew, fuel, scrap, and ship systems along the way. Each
sector is a node map of encounters — hostile ships, traders, distress signals,
asteroid fields, and empty space. Combat is a real-time-with-pause system where
the player assigns crew to ship systems (weapons, shields, engines, medbay),
targets enemy rooms, and manages power distribution as systems take damage and
fires break out. Between jumps, scrap funds repairs and upgrades. Fuel limits
how many nodes can be visited before the sector exit must be reached. The final
sector pits the ship against a powerful flagship in a multi-phase battle that
tests every system the player has invested in.

## What the Player Experiences

A title screen shows the ship silhouette against a star field. Starting a run
presents a ship layout with rooms, three crew members, and starting resources.

The sector map shows connected nodes with partial information — icons hint at
combat, shops, or events. Jumping to a node costs fuel and triggers an
encounter. Combat shows both ships in cross-section: the player drags crew
between rooms, powers systems on/off, and fires weapons at targeted enemy rooms.
Damage breaches hulls, starts fires, and injures crew. Winning yields scrap.

Shops sell weapons, augments, crew, and fuel. Events present narrative choices
with risk/reward outcomes. Reaching the sector exit advances to the next sector
with harder encounters. After several sectors, the flagship battle begins — a
multi-phase fight with unique mechanics. Victory shows a run summary; defeat
shows how far the player reached.

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

# FTL 航程（FTL Voyage）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **FTL Voyage**——一款带船员管理和星区导航的
飞船经营 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一艘小型星舰穿越程序化生成的星区一路逃亡，奔向最终对决，途中要管理船员、燃料、
废料和舰船系统。每个星区都是一张由遭遇构成的节点地图——敌对舰船、商人、遇险
信号、小行星带和空无一物的太空。战斗采用实时+暂停系统，玩家把船员分配到各个
舰船系统（武器、护盾、引擎、医疗舱），瞄准敌舰的房间，并在系统受损、火势蔓延时
调度功率分配。跃迁之间，废料用于维修和升级。燃料限制了在必须抵达星区出口之前
能访问多少节点。最终星区让飞船对上一艘强大的旗舰，展开多阶段战斗，考验玩家
投资过的每一个系统。

## 玩家体验流程

标题画面展示星空背景下的飞船剪影。开始一轮后，呈现一张带房间的舰船布局图、
三名船员和初始资源。

星区地图展示相互连接的节点，信息只是局部的——图标暗示着战斗、商店或事件。跃迁
到某个节点会消耗燃料并触发一场遭遇。战斗以剖面图形式展示双方飞船：玩家在房间
之间拖动船员，开关系统供电，并向选定的敌舰房间开火。伤害会击穿船体、引发火灾、
伤及船员。取胜可获得废料。

商店出售武器、增强装置、船员和燃料。事件给出带风险/回报结果的叙事选择。抵达
星区出口即前往下一个遭遇更艰难的星区。经过若干星区后，旗舰战开始——一场带独特
机制的多阶段战斗。胜利展示本轮总结；失败则展示玩家走到了多远。

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

