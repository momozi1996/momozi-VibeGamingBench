# Shape Shift

Build **Shape Shift**, a puzzle-platformer with three transformable forms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A polymorphic creature navigates chambers by switching between three physical
forms mid-air: a heavy cube that falls fast and activates pressure plates, a
bouncy sphere that ricochets off walls and reaches high places, and a gliding
triangle that floats across wide gaps. Each form has distinct physics — the cube
is dense and grippy, the sphere is elastic and slippery, the triangle is light
and drifty. Puzzles require chaining transformations in sequence: launch as
sphere, shift to triangle mid-arc to glide over spikes, then drop as cube onto
a switch. Forty levels across four worlds teach each form individually before
demanding fluid mid-air combos.

## What the Player Experiences

A title screen shows the three forms orbiting the game name. A world-select
menu reveals four worlds of ten levels each, unlocked sequentially.

World 1 teaches the cube: weight, pressure plates, breaking fragile floors.
World 2 introduces the sphere: bouncing, wall-ricochets, momentum preservation.
World 3 adds the triangle: gliding, updrafts, precision floating. World 4
combines all three with puzzles requiring rapid mid-air switching.

The player presses 1/2/3 or cycles with a button to transform instantly. Each
form change produces a satisfying visual morph and a physics shift the player
feels immediately. Levels contain a goal crystal — reaching it completes the
level. Optional collectible stars reward creative form usage. A level-complete
screen shows time, stars collected, and form-switch count.

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

# 变形切换（Shape Shift）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Shape Shift**，一款带三种可变形态的解谜平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一只多形态生物靠在空中切换三种物理形态来穿越房间：一个下落飞快、能压下压力板的沉重立方体；一个能在墙面上弹射、够到高处的弹性球体；以及一个能飘过宽阔间隙的滑翔三角。每种形态都有截然不同的物理特性——立方体致密且抓地，球体弹性且滑溜，三角轻盈且飘忽。谜题要求按顺序串联变形：以球体弹射出去，在弧线中途切换成三角滑过尖刺，然后化作立方体砸到一个开关上。四个世界共四十个关卡会先分别教授每种形态，再要求流畅的空中连招。

## 玩家体验流程

标题画面显示三种形态围绕游戏名旋转。一个世界选择菜单展示四个世界，每个世界十个关卡，按顺序解锁。

世界 1 教授立方体：重量、压力板、打破易碎地板。世界 2 引入球体：弹跳、墙面弹射、动量保持。世界 3 加入三角：滑翔、上升气流、精确飘移。世界 4 把三者结合，谜题要求在空中快速切换。

玩家按 1/2/3 或用一个按键循环切换来即时变形。每次形态变化都会产生令人满足的视觉变形效果和玩家能立刻感受到的物理变化。关卡中含有一颗目标水晶——碰到它即完成关卡。可选的收集星奖励对形态的创造性运用。关卡完成画面显示时间、收集到的星数和形态切换次数。

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

