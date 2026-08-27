# Puzzle Magnet Lab

Build **Puzzle Magnet Lab**, a 2D grid-based magnetic puzzle mini-game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player manipulates polarity to push and pull
magnetic objects through a laboratory, solving spatial puzzles to guide an
energy core to the exit.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a turn-based spatial logic puzzle built on one central rule:
opposite polarities attract, same polarities repel. Every level is a closed
system of magnets, metal crates, gates, and hazards where the player must
reason about chain reactions before committing a move. The tension comes from
irreversibility and cascading consequences: flipping a polarity switch might
solve one gate while slamming a crate into a hazard. The best version feels
like a miniature physics sandbox wrapped in clean laboratory aesthetics, where
each puzzle teaches a new interaction between familiar magnetic rules.

## What the Player Experiences

A title screen sets the laboratory tone with magnetic imagery and a clear way
to begin. The player enters a grid-based puzzle chamber where walls, floor
tiles, magnetic crates, polarity indicators, switches, gates, and an exit are
all readable at a glance. Movement is deliberate, one tile at a time, and the
grid enforces strict spatial reasoning.

Early puzzles teach the basics: push a same-polarity crate out of the way, or
pull an opposite-polarity block onto a pressure plate to open a gate. As the
player progresses, levels layer mechanics together. A polarity-swap switch
inverts the player's field, turning a repulsion problem into an attraction
opportunity. Hazard tiles punish careless moves. Multi-step sequences demand
planning several moves ahead, where an early push sets up a later pull across
the room.

An undo or reset option keeps frustration in check. When the core reaches the
exit, a completion screen celebrates the solve and offers the next challenge.
Failure states are clear and recoverable. The arc moves from simple single-crate
rooms to intricate multi-gate chambers that require the full toolkit of push,
pull, swap, and sequencing.

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

# 解谜：磁力实验室（Puzzle Magnet Lab）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Puzzle Magnet Lab**，一款基于 2D 网格的磁力解谜小游戏。玩家通过操纵极性来推拉磁性物体穿过一座实验室，解开空间谜题，把一枚能量核心引导到出口。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款回合制空间逻辑解谜游戏，建立在一条核心规则之上：异极相吸，同极相斥。每个关卡都是一个由磁体、金属箱、闸门与危险物构成的封闭系统，玩家必须在落子之前推演连锁反应。张力来自不可逆性与层层递进的后果：翻转一个极性开关或许解开了一道闸门，却同时把一个箱子撞进了危险物。最理想的版本感觉像一个被干净实验室美学包裹起来的微型物理沙盒，每道谜题都在教你熟悉的磁力规则之间的一种新互动。

## 玩家体验流程

标题画面用磁力意象定下实验室基调，并提供清晰的开始方式。玩家进入一间基于网格的解谜室，其中墙体、地板图块、磁性箱子、极性指示器、开关、闸门与出口都一眼可辨。移动是审慎的，一次一格，而网格强制严格的空间推理。

前期谜题教授基础：把一个同极箱子推开，或把一块异极方块拉到压力板上以打开闸门。随着玩家推进，关卡会把各种机制叠加起来。极性反转开关会反转玩家的磁场，把一道斥力难题变成一次引力机会。危险图块惩罚草率的移动。多步序列要求玩家提前规划好几步，其中前期的一次推动为后期跨房间的一次拉拽做好铺垫。

撤销或重置选项让挫败感保持在可控范围内。当核心到达出口时，一个完成画面为这次解题喝彩，并提供下一项挑战。失败状态清晰且可恢复。整体弧线从简单的单箱房间推进到需要动用推、拉、反转与排序全套工具的复杂多闸门密室。

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

