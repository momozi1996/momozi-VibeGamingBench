# Dungeon Shop

Build **Dungeon Shop**, a shopkeeper roguelike where you price items and defend
from thieves as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player runs a dungeon item shop, stocking shelves with weapons, potions,
and armor that adventurers browse and buy. The twist: the player sets prices,
and pricing is the core mechanic. Price too high and adventurers leave empty-
handed. Price too low and profit evaporates. Some customers are thieves who
grab items and bolt for the door — the player must physically chase and tackle
them or deploy traps. Between shopping days, the player ventures into a
procedural dungeon to acquire new stock, fighting monsters with whatever unsold
inventory is on hand. Gold funds shop upgrades: display cases, security
measures, and larger floor space. Each run spans multiple days until the shop
either thrives to a target gold amount or goes bankrupt.

## What the Player Experiences

A title screen shows a cozy shop interior with a sword on display. Starting a
run opens the shop on Day 1 with basic starter inventory.

During the shop phase, adventurers enter and browse. The player drags items
onto shelves and sets prices via a slider. Adventurers have visible budget
indicators and preferences. Satisfied customers pay and leave; overcharged
customers scoff and exit. Thieves grab items and run — the player clicks to
chase or activates pre-placed traps.

During the dungeon phase, the player enters a procedural side-scrolling dungeon
with simple combat, collecting loot to stock the shop. Better dungeon
performance means better inventory. Between days, an upgrade screen offers shop
improvements. The run ends in victory (reaching a gold target) or bankruptcy
(running out of stock and gold). A results screen shows days survived, total
profit, and thieves caught.

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

# 地牢商店（Dungeon Shop）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dungeon Shop**——一款你要给商品定价并
防范小偷的店主 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一间地牢道具店，往货架上摆放武器、药水和护甲，供冒险者浏览购买。妙处
在于：价格由玩家自己设定，而定价就是核心机制。定得太高，冒险者会空手离开；定得
太低，利润就蒸发了。有些顾客是小偷，会抓起商品夺门而出——玩家必须亲自追上去把
他们扑倒，或者布置陷阱。营业日之间，玩家会深入一座程序化生成的地牢补充货源，
用手头任何没卖掉的库存去打怪。金币用于资助商店升级：展示柜、安保措施和更大的
营业面积。每一轮横跨多个营业日，直到商店要么兴旺到目标金币数，要么破产。

## 玩家体验流程

标题画面展示一间温馨的店内景象，一把剑陈列其中。开始一轮后，商店在第 1 天以
基础的初始库存开门。

在营业阶段，冒险者进店浏览。玩家把商品拖到货架上，并用一个滑块设定价格。冒险者
带有可见的预算指示和偏好。满意的顾客付钱离开；被要价过高的顾客会嗤之以鼻然后
走人。小偷会抓起商品就跑——玩家点击进行追捕，或者启动预先布置好的陷阱。

在地牢阶段，玩家进入一座程序化生成的横版卷轴地牢，进行简单战斗并收集战利品来
充实店里的库存。地牢中表现越好，库存就越好。营业日之间，升级画面提供商店改进
项。这一轮以胜利（达到金币目标）或破产（库存与金币双双耗尽）告终。结算画面展示
存活天数、总利润和抓住的小偷数。

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

