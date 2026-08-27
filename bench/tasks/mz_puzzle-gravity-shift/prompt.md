# Gravity Shift

Build **Gravity Shift**, a 2D gravity-rotation puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player rotates the direction of gravity to guide a
ball through obstacle-filled chambers to an exit, using destructible terrain
and chain reactions to clear paths.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a physics puzzle built on directional gravity. The player cannot
move the ball directly but can rotate gravity in 90-degree increments (down,
left, up, right), causing everything in the chamber to fall in the new
direction. The tension comes from planning gravity sequences: rotating right
sends the ball sliding into a wall, but also drops a boulder onto a
destructible platform, opening a path for the next rotation. Chain reactions
emerge naturally — explosive crates detonate on impact, crumbling blocks
break after one landing, and weighted objects trigger pressure switches as
they settle. The best version feels like orchestrating a Rube Goldberg machine
where gravity itself is the only tool.

## What the Player Experiences

A title screen sets the tone with floating geometry and directional arrows.
The player enters a chamber where the ball, exit portal, walls, platforms,
hazards, and special objects are visible. Gravity direction indicators show
the current pull. The player presses arrow keys or buttons to rotate gravity.

Early chambers teach basic rotation: shift gravity right to roll the ball
toward the exit. Soon obstacles require multi-step sequences — rotate down
to drop through a gap, then left to slide past spikes. Mid-game introduces
destructible terrain (crumbling blocks that break on second impact, explosive
crates that blast nearby walls), weighted objects that trigger switches, and
conveyor surfaces that add lateral movement during falls. Late chambers
demand precise rotation sequences where each gravity shift triggers a chain
reaction that reshapes the level geometry.

An undo system lets the player rewind gravity shifts. Reaching the exit
portal completes the chamber with a celebration screen. Death from hazards
offers instant retry. The campaign progresses through themed worlds with
escalating physics complexity.

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

# 重力翻转（Gravity Shift）

在 `/workspace/game/` 用 Godot 4 开发 **Gravity Shift**，一个 2D 重力旋转解谜
游戏。玩家旋转重力方向，引导一颗球穿过布满障碍的试验室抵达出口，并利用可破坏
地形与连锁反应清出通路。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款建立在方向性重力之上的物理解谜游戏。玩家无法直接移动小球，但可以按
90 度为单位旋转重力（下、左、上、右），让试验室里的一切都朝新方向坠落。张力
来自对重力序列的规划：向右旋转会让球滑撞到墙上，但同时也会把一块巨石砸到可破坏
的平台上，为下一次旋转打开通路。连锁反应会自然涌现——爆炸箱子受撞即引爆，
易碎方块落地一次后碎裂，有重量的物体在落定时会踩下压力开关。最理想的版本会让人
感觉像在编排一台鲁布·戈德堡机械，而重力本身是唯一的工具。

## 玩家体验流程

标题画面用漂浮的几何体和方向箭头营造氛围。玩家进入试验室后，能看到小球、出口
传送门、墙壁、平台、危险物和特殊物件。重力方向指示器显示当前的牵引方向。玩家
按方向键或按钮来旋转重力。

前期试验室教基础旋转：把重力转向右侧，让球滚向出口。很快，障碍就会要求多步序列
——先向下旋转穿过一道缝隙，再向左滑过尖刺。中期引入可破坏地形（第二次受撞才
碎裂的易碎方块、能炸开附近墙壁的爆炸箱子）、可触发开关的有重量物体，以及在坠落
过程中附加横向位移的传送带表面。后期试验室要求精确的旋转序列，每一次重力翻转
都会触发一场重塑关卡地形的连锁反应。

撤销系统让玩家可以回退重力翻转操作。抵达出口传送门即完成该试验室，并弹出庆祝
画面。被危险物害死后可以立即重试。战役按主题世界推进，物理复杂度层层升级。

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

