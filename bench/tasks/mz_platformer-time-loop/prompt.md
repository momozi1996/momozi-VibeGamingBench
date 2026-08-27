# Time Loop

Build **Time Loop**, a 30-second time loop platformer where past-self replays
help solve puzzles as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

Each level is a 30-second loop. When the timer expires, time rewinds and the
player starts again — but a ghost of the previous loop replays simultaneously,
interacting with the world. The ghost can hold switches, distract enemies, or
stand on pressure plates while the current player tackles other objectives.
Multiple loops layer: loop 1's ghost holds a door open, loop 2's ghost stands
on a platform to create a bridge, and in loop 3 the player finally reaches the
exit using both ghosts' contributions. The puzzle is temporal coordination —
planning what each loop-self needs to do and when, so that all versions
cooperate across time. Twenty-four levels across four chapters escalate from
single-ghost puzzles to four-loop orchestrations.

## What the Player Experiences

A title screen shows overlapping clock hands and ghost silhouettes. A chapter
menu reveals four chapters of six levels each.

Entering a level starts a 30-second countdown. The player runs, jumps, and
interacts with switches and objects. When the timer hits zero, the screen
flashes and rewinds — the player restarts at the spawn point, but a translucent
ghost replays exactly what they did in the previous loop. The ghost physically
interacts with the world: it presses buttons, holds doors, and blocks lasers.

The player can layer up to four loops. A timeline bar at the top shows all
active ghosts and their current positions in the 30-second window. Reaching the
exit crystal with all required switches held (by ghosts or player) completes
the level. A reset button clears all ghosts to start fresh. Level-complete
shows loops used and time of exit within the final loop.

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

# 时间循环（Time Loop）

在 `/workspace/game/` 用 Godot 4 开发 **Time Loop**，一款 30 秒时间循环平台跳跃游戏，过去自己的重放会帮助解开谜题。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

每个关卡都是一段 30 秒的循环。计时器归零时，时间倒回，玩家重新开始——但上一次循环的幽灵会同时重放，并与世界发生交互。幽灵可以按住开关、引开敌人，或站在压力板上，而当前的玩家则去处理别的目标。多重循环层层叠加：第 1 次循环的幽灵按住一道门，第 2 次循环的幽灵站在一个平台上搭出一座桥，而在第 3 次循环中玩家终于借助两个幽灵的贡献抵达出口。谜题在于时间上的协调——规划每一个循环中的自己需要在何时做什么，好让所有版本跨越时间通力合作。四个章节共二十四个关卡，从单幽灵谜题一路升级到四重循环的编排。

## 玩家体验流程

标题画面显示交叠的时钟指针和幽灵剪影。一个章节菜单展示四个章节，每个章节六个关卡。

进入关卡会启动一段 30 秒倒计时。玩家奔跑、跳跃，并与开关和物件交互。计时器归零时，屏幕闪光并倒回——玩家在出生点重新开始，但一个半透明的幽灵会精确重放他们在上一次循环中所做的一切。幽灵在物理上与世界交互：它会按下按钮、按住门，并挡住激光。

玩家最多可以叠加四重循环。顶部的一条时间轴显示所有活动幽灵及其在这 30 秒窗口中的当前位置。在所有必需的开关都被按住（由幽灵或玩家）的情况下抵达出口水晶即完成关卡。一个重置按钮会清除所有幽灵以重新开始。关卡完成时显示所用的循环数以及在最后一次循环中抵达出口的时间。

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

