# Wall Dancer

Build **Wall Dancer**, a precision platformer with wall-climb and dash mechanics
as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A nimble climber ascends through crystalline caverns one screen at a time,
clinging to walls, launching off with a directional dash, and threading through
spike-lined corridors that demand pixel-perfect timing. The game is built around
two verbs: cling and dash. Clinging to a wall lets the player slide slowly
downward while scanning the room for the next safe surface. Dashing consumes a
single charge that resets on landing or wall-grab, creating a rhythm of
commit-recover-commit that makes every room feel like a tiny puzzle solved
through muscle memory. Five chapters introduce new hazards — wind currents,
crumbling walls, moving spikes, gravity flips, and timed gates — each layering
complexity without changing the core two-verb vocabulary.

## What the Player Experiences

A title screen presents the game name and a chapter-select option (locked until
cleared). Pressing Start drops the player into Chapter 1, Room 1.

Each room fills exactly one screen. The player character clings to walls on
contact, sliding slowly downward. Pressing jump while clinging launches away
from the wall. Pressing dash mid-air sends the character in the aimed direction
at high speed, consuming the dash charge. Landing on ground or grabbing another
wall restores the charge. Spikes, pits, and moving hazards kill instantly,
respawning the player at the room entrance with no loading screen.

Clearing a room scrolls the camera to the next. Each chapter contains 8-12
rooms culminating in a final room that combines all chapter hazards. Completing
a chapter returns to the hub with the next chapter unlocked. A death counter
and best-time tracker per chapter encourage mastery replays.

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

# 壁舞者（Wall Dancer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Wall Dancer**，一款带贴墙攀爬与冲刺机制的精确操作平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名灵巧的攀登者一屏一屏地向上穿越水晶洞窟，贴附墙面、用一次定向冲刺弹射出去，并穿过要求像素级精确时机的尖刺走廊。游戏围绕两个动词构建：贴附与冲刺。贴附在墙上让玩家缓慢下滑，同时扫视房间寻找下一处安全表面。冲刺消耗单次充能，充能会在着地或抓墙时重置，由此形成一种"投入—恢复—再投入"的节奏，让每个房间都像一道靠肌肉记忆解开的小谜题。五个章节陆续引入新的危险物——气流、崩塌的墙、移动的尖刺、重力翻转和限时门——每一样都在不改变核心双动词语汇的前提下叠加复杂度。

## 玩家体验流程

标题画面呈现游戏名和一个章节选择选项（通关前锁定）。按下开始把玩家投入第 1 章第 1 房。

每个房间正好占满一屏。玩家角色接触即贴附到墙上，缓慢向下滑动。贴附时按跳跃会从墙面弹开。在空中按冲刺会让角色朝瞄准的方向高速射出，并消耗掉冲刺充能。落到地面或抓住另一面墙会恢复充能。尖刺、陷坑和移动危险物会立刻致死，玩家会在房间入口重生，没有加载画面。

清掉一个房间后，摄像机滚动到下一个。每个章节包含 8-12 个房间，以一个综合了本章全部危险物的最终房间收尾。完成一个章节会返回枢纽，并解锁下一章。每个章节的死亡计数器和最佳时间记录鼓励玩家为求精通而反复重玩。

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

