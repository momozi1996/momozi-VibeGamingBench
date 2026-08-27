# Roguelike: Relic Pinball

Build **Relic Pinball**, a compact **pinball / brick-breaker roguelite** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: an original, polished vertical slice about
navigating a cursed mechanical table one chamber at a time, breaking target
banks, triggering arcane mechanisms, and collecting relics that visibly mutate
the ball's behavior across an escalating run.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is exploring a cursed mechanical table one chamber at a time. Each
chamber is a live pinball board fused with brick-breaker structure: target rows,
bumpers, switches, lanes, gates, spinners, and special blocks create readable
goals while the ball remains fast and physical. The tension lives in flipper
timing and relic synergy — every launch is a gamble, every save a small
triumph, and every relic choice reshapes how the ball interacts with the world.
A ball might split on contact, burn through cracked bricks, curve toward metal
targets, leave scoring echoes, charge bumpers on pass-through, or orbit after
paddle hits. The tone is arcane arcade machine: brass rails, glass reflections,
carved stone bricks, luminous relic icons, bright impact sparks, and snappy
flipper feedback.

## What the Player Experiences

From the title screen the player sees a styled pinball-table motif with at
least one relic or magical ball identity hinting at what lies ahead.

The run drops the player into a live table. A ball launches into a bounded
playfield and the player works left and right flippers to keep it alive,
threading it through bumpers, lanes, and brick banks. Every collision feels
different — bumpers kick the ball away, bricks crack and shatter, switches
light up lanes, spinners charge multipliers, and portals warp the ball across
the board. The table is not a passive backdrop; it reacts.

Clearing enough targets or triggering the right mechanisms opens a relic
choice. The player picks from several relics, each with a name, icon, and
concise rule. The chosen relic immediately changes how the next chamber plays —
the ball splits, pierces, magnetizes, or leaves fire trails. The active relic
row persists and stacks, so the run builds toward a strange loadout that no
two attempts share.

Chambers grow harder: new layouts, tighter drains, armored targets, hazard
bumpers, and eventually a boss table whose special rule demands more than
reflexes. Victory or defeat lands on a styled result screen that lets the
player try again without restarting the application.

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

# Roguelike：遗物弹珠台（Roguelike: Relic Pinball）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Relic Pinball**——一款小巧的**弹珠台 /
打砖块 Roguelite**：一个原创、打磨精良的纵向切片，讲述在一座被诅咒的机械台面上
一间一间地推进，击破目标砖阵、触发奥术机构，并收集能在不断升级的一轮之中肉眼
可见地改变弹球行为的遗物。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片
放到 itch.io 页面或 Steam 上。

## 核心构想

玩家正在一间一间地探索一座被诅咒的机械台面。每一间都是一块活生生的弹珠台，
融合了打砖块的结构：目标行、弹垒、开关、通道、闸门、旋转器和特殊砖块共同构成
清晰可读的目标，而弹球始终保持高速与实体感。张力来自挡板时机与遗物协同——每一次
发球都是一场赌博，每一次救球都是一场小小的胜利，而每一次遗物选择都会重塑弹球与
世界互动的方式。弹球可能在接触时分裂、烧穿裂纹砖、朝金属目标弯曲、留下计分回声、
在穿过时给弹垒充能，或在被挡板击中后进入环绕轨道。整体调性是奥术街机机台：
黄铜导轨、玻璃反光、雕纹石砖、发光的遗物图标、明亮的撞击火花，以及干脆利落的
挡板反馈。

## 玩家体验流程

从标题画面开始，玩家看到一幅有设计感的弹珠台意象，其中至少有一件遗物或一种魔法
弹球的身份，暗示着接下来会发生什么。

这一轮把玩家投进一块活的台面。弹球被发射进一片有界的场地，玩家操作左右挡板让它
存活下去，把它穿过弹垒、通道和砖阵。每一次碰撞的感觉都不一样——弹垒把球弹开，
砖块开裂并碎散，开关点亮通道，旋转器为倍率充能，传送门把球扭送到台面另一处。
台面不是被动的背景板；它会回应。

清掉足够多的目标、或触发正确的机构，就会开启一次遗物选择。玩家从若干遗物中挑选
一件，每件都有名称、图标和一条简明规则。所选遗物会立刻改变下一间的玩法——弹球
会分裂、穿透、磁吸，或者拖出火焰尾迹。已激活的遗物栏会持续保留并叠加，因此这
一轮会朝着一套没有两次尝试会相同的奇特配置堆积。

各间越来越难：新的布局、更窄的漏球口、装甲目标、危险弹垒，最终是一块特殊规则
要求远超反应力的 Boss 台面。胜利或失败都落到一个有设计感的结算画面上，让玩家
无需重启应用程序即可再来一次。

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

