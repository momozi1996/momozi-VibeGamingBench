# Pirate Fleet

Build **Pirate Fleet**, a **naval tactics strategy game with wind mechanics** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A fleet of pirate ships navigates a hex-sea where wind direction dictates
everything. Sailing with the wind is fast; tacking against it is slow and
costly. The player commands multiple ship types — nimble sloops, heavy
galleons, boarding frigates — positioning them to exploit wind advantage while
denying it to the enemy. Combat is broadside-based: ships deal damage from
their flanks, so facing matters as much as range. Treasure islands dot the map
as objectives worth fighting over. The tone is golden-age piracy: sun-bleached
sails, cannon smoke, and the creak of timber under fire.

## What the Player Experiences

From the title screen the player selects a scenario or campaign mission. The
map shows a hex-grid sea with islands, shallows, and a wind-direction indicator
that shifts every few turns. The player's fleet starts on one side; the enemy
on the other. Treasure islands sit between them as objectives.

Each turn the player moves ships. Movement cost depends on direction relative
to wind: downwind is cheap, crosswind moderate, upwind expensive. Ships have
limited movement points per turn. After moving, ships with enemies in their
broadside arc can fire cannons — damage depends on range and facing angle.

Ship types serve different roles: sloops scout and flank quickly, galleons
absorb damage and carry heavy guns, and frigates can initiate boarding actions
on adjacent ships for a chance to capture rather than sink. Captured ships join
the player's fleet.

Treasure islands are captured by moving a ship adjacent and holding for one
turn. Controlling islands earns victory points. The scenario ends when one side
reaches the point target or loses all ships. A styled result screen shows the
battle outcome with ships sunk, captured, and treasure claimed.

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

# 海盗舰队（Pirate Fleet）

在 `/workspace/game/` 用 Godot 4 开发 **Pirate Fleet**，一款**带风向机制的海战战术策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一支海盗舰队航行在六边形格的海域上，而风向决定着一切。顺风航行速度飞快；逆风抢风则既慢又费。玩家指挥多种舰船类型——灵巧的单桅帆船、笨重的大帆船、专擅接舷的护卫舰——把它们布置到能利用风势优势的位置，同时不让敌人得到这份优势。战斗以舷炮为核心：舰船从侧舷输出伤害，因此朝向与射程同样重要。宝藏岛屿散布在地图各处，是值得为之一战的目标。基调是海盗黄金时代：被烈日晒白的船帆、炮火硝烟，以及炮击之下船木的吱呀作响。

## 玩家体验流程

玩家从标题画面选择一个场景或战役任务。地图呈现一片六边形格的海域，其中有岛屿、浅滩，以及每隔几回合就会变动的风向指示器。玩家的舰队从一侧出发，敌方在另一侧。宝藏岛屿位于双方之间，是争夺目标。

每回合玩家移动舰船。移动消耗取决于相对风向的方向：顺风便宜，横风中等，逆风昂贵。舰船每回合的移动点数有限。移动之后，若有敌人处在其舷炮射界内，舰船便可开炮——伤害取决于距离与朝向角度。

各舰船类型承担不同职责：单桅帆船快速侦察与包抄，大帆船承受伤害并搭载重型火炮，护卫舰则可对相邻舰船发起接舷战，有机会俘获而非击沉。被俘获的舰船会加入玩家的舰队。

宝藏岛屿的占领方式是把一艘船移动到相邻位置并驻留一个回合。控制岛屿可获得胜利点数。当一方达到点数目标或损失所有舰船时，场景结束。一个精心设计的结算画面会展示战斗结果，包括击沉数、俘获数与获得的宝藏。

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

