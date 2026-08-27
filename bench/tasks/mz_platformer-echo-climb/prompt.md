# Echo Climb

Build **Echo Climb**, a tower-climbing platformer where past runs become ghost
platforms as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A climber ascends an impossibly tall tower, but the tower is mostly empty air.
The trick: every failed attempt leaves behind a ghost that replays the run, and
the ghost's body becomes a solid platform for future attempts. The first run
might reach only a few ledges before falling. The second run can stand on the
ghost of the first to reach higher. Each attempt layers another ghost into the
tower, gradually building a scaffold of past selves that makes previously
impossible heights reachable. The player decides when to sacrifice a run to
create a useful stepping stone versus when to push for maximum height. A
persistent best-height marker and ghost count track progress across sessions.

## What the Player Experiences

A title screen shows the tower stretching upward with ghost silhouettes
visible. Starting a run places the player at the tower base.

The climber can run, jump, and wall-slide. The tower has sparse fixed platforms
but large vertical gaps that seem impassable. When the player falls or quits,
the run is recorded as a ghost. On the next attempt, all previous ghosts replay
simultaneously — their bodies are semi-transparent but physically solid. The
player can stand on ghosts, use them as moving platforms, or ride them upward.

A height meter shows current altitude and best-ever altitude. Every five
attempts the player can choose to "solidify" one ghost into a permanent
platform (it stops replaying and becomes a fixed ledge). The game saves ghost
data between sessions. Reaching milestone heights unlocks cosmetic trail
effects for the climber.

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

# 回声攀登（Echo Climb）

在 `/workspace/game/` 用 Godot 4 开发 **Echo Climb**，一款把过去的每一轮变成幽灵平台的爬塔平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名攀登者向上攀爬一座高不可攀的塔，但塔里大部分都是空气。诀窍在于：每一次失败的尝试都会留下一个重放该轮过程的幽灵，而幽灵的身体会成为后续尝试可以踩踏的实体平台。第一轮可能只够到几处岩架就摔了下来。第二轮就能站在第一轮的幽灵身上爬得更高。每次尝试都往塔里叠加一个幽灵，逐步搭起一座由过去的自己组成的脚手架，让此前不可能的高度变得可及。玩家要决定何时牺牲一轮去制造一块有用的垫脚石，何时全力冲击最大高度。一个持久保存的最佳高度标记和幽灵计数会跨会话记录进度。

## 玩家体验流程

标题画面显示那座向上延伸的塔，其中可见幽灵的剪影。开始一轮会把玩家放在塔基处。

攀登者可以奔跑、跳跃和贴墙下滑。塔里有稀疏的固定平台，但纵向间隙巨大、看似无法逾越。当玩家坠落或退出时，这一轮会被记录为一个幽灵。在下一次尝试中，所有此前的幽灵会同时重放——它们的身体半透明，但在物理上是实体的。玩家可以站在幽灵上、把它们当作移动平台，或是搭着它们向上。

一个高度计显示当前高度和历史最佳高度。每五次尝试，玩家可以选择把一个幽灵"固化"成永久平台（它会停止重放，变成一处固定岩架）。游戏在多次会话之间保存幽灵数据。抵达里程碑高度会为攀登者解锁装饰性的拖尾特效。

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

