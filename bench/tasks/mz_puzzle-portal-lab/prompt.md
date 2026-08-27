# Portal Lab

Build **Portal Lab**, a 2D portal-placement puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places entry and exit portals on designated
wall surfaces to redirect lasers, launch objects, and transport themselves
through test chambers, using momentum conservation and spatial reasoning.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a spatial puzzle built on linked teleportation. Each test chamber
has walls, floors, laser emitters, targets, weighted cubes, buttons, and a
locked exit. The player can place two portal endpoints on valid surfaces;
anything entering one emerges from the other with conserved momentum and
direction. The tension comes from chaining portals with physics: drop a cube
from height through a floor portal to launch it horizontally from a wall
portal onto a distant button, or redirect a laser through multiple portal
bounces to hit a sensor. The best version feels like bending space itself,
where each chamber is an "aha" moment of seeing how two linked holes solve
an impossible geometry.

## What the Player Experiences

A title screen sets the laboratory tone with portal imagery and a clean
scientific aesthetic. The player enters a test chamber where walls, laser
emitters, targets, cubes, buttons, and the exit door are visible. Valid portal
surfaces are subtly highlighted.

Early chambers teach basic portal use: place two portals to walk through a
wall, or redirect a single laser to a target. Soon chambers require momentum
tricks — falling through a floor portal to gain speed and launching from a
wall portal to cross a gap. Mid-game introduces weighted cubes that must be
portaled onto pressure plates, laser grids requiring multiple redirections,
and timed sequences where portals must be repositioned mid-puzzle. Late
chambers combine all mechanics: redirect lasers, launch cubes, and navigate
the player through a single interconnected portal network.

Placing a portal shows a preview of where it will link. Objects passing through
portals have visible trajectory trails. When all targets are activated, the
exit unlocks. A completion screen shows the chamber number and offers the next
challenge. The campaign progresses through increasingly complex test chambers.

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

# 传送门实验室（Portal Lab）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Portal Lab**，一个 2D 传送门摆放解谜游戏。
玩家在指定的墙面上放置入口与出口传送门，借助动量守恒和空间推理来折射激光、
弹射物体，并把自己送过一间间试验室。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款建立在成对传送之上的空间解谜游戏。每间试验室都有墙壁、地板、激光发射器、
标靶、配重方块、按钮和一道锁住的出口。玩家可以在有效表面上放置两个传送门端点；
任何进入其中一个的东西都会从另一个出来，动量与方向都被保留。张力来自把传送门
与物理串联起来：让方块从高处落入地面传送门，从墙面传送门横向弹射出去砸中远处的
按钮；或者让激光经过多次传送门折射后命中传感器。最理想的版本会让人感觉空间本身
被折弯了，每一间试验室都是一个"啊哈"时刻——你忽然看清两个相连的洞如何解开一道
不可能的几何难题。

## 玩家体验流程

标题画面用传送门意象和干净的科研美学营造出实验室氛围。玩家进入试验室后，能看到
墙壁、激光发射器、标靶、方块、按钮和出口门。有效的传送门表面被以不显眼的方式
高亮出来。

前期试验室教基础的传送门用法：放两个传送门穿过一堵墙，或把一束激光折射到标靶上。
很快，试验室就会要求动量技巧——落入地面传送门以获得速度，再从墙面传送门弹射出去
跨越缝隙。中期引入必须靠传送门送上压力板的配重方块、需要多次折射的激光阵列，
以及需要在解谜途中重新摆放传送门的限时序列。后期试验室把所有机制结合起来：在
同一个互相连通的传送门网络中折射激光、弹射方块，并让玩家自己穿行其间。

放置传送门时会预览它将连往何处。穿过传送门的物体带有可见的轨迹尾迹。当所有标靶
都被激活后，出口解锁。完成画面显示试验室编号，并给出下一个挑战。战役会一路推进
到越来越复杂的试验室。

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

