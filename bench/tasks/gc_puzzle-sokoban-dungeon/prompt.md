# Sokoban Dungeon

Build **Sokoban Dungeon**, a 2D turn-based crate-pushing dungeon puzzle as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player pushes crates through procedurally
generated dungeon rooms while enemies move simultaneously on each turn,
collecting keys and items to unlock deeper floors.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a turn-based puzzle-roguelike hybrid where every player step
triggers an enemy step. Each dungeon room is a spatial puzzle: crates must be
pushed onto pressure plates to open doors, but enemies patrol the grid and
move toward the player whenever the player moves. The tension comes from the
simultaneous-turn system — pushing a crate takes a turn, during which enemies
close in, so the player must solve spatial puzzles under mounting threat. Keys
unlock new rooms, items provide one-use abilities (freeze enemies, pull crates,
teleport), and procedural room layouts ensure variety. The best version feels
like chess merged with a warehouse puzzle, where every move has tactical
consequences.

## What the Player Experiences

A title screen sets the dungeon tone with stone textures and a clear way to
begin. The player enters a dungeon room where walls, crates, pressure plates,
locked doors, keys, enemies, and the exit staircase are visible on a grid.
Movement is turn-based: arrow keys move one tile, and all enemies move one
tile simultaneously.

Early rooms teach basic pushing: move a crate onto a plate to open a door.
Soon enemies appear that mirror the player's movement timing, forcing the
player to plan push sequences that also avoid or trap threats. Mid-game
introduces multiple crate types (heavy crates need two pushes, ice crates
slide until hitting a wall), keys that unlock color-coded doors, and items
found in chests. Late rooms combine all mechanics in procedurally arranged
layouts where the player must solve the spatial puzzle while managing enemy
positions.

An undo system lets the player rewind turns. Reaching the exit staircase
advances to the next floor. Death from enemy contact offers retry. The
campaign generates increasingly complex floors with more enemies, more crate
types, and tighter spatial constraints.

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

# 推箱子地牢（Sokoban Dungeon）

在 `/workspace/game/` 用 Godot 4 开发 **Sokoban Dungeon**，一个 2D 回合制推箱子
地牢解谜游戏。玩家在程序化生成的地牢房间中推动箱子，而敌人在每个回合同时行动，
玩家需要收集钥匙和道具来解锁更深的楼层。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款回合制解谜与 Roguelike 的混合作品，玩家每走一步都会触发敌人走一步。
每个地牢房间都是一道空间谜题：箱子必须被推到压力板上才能打开门，但敌人会在网格
上巡逻，并在玩家一移动就朝玩家逼近。张力来自同步回合系统——推一次箱子要花一个
回合，而这期间敌人正在合围，所以玩家必须在不断加剧的威胁下解开空间谜题。钥匙
解锁新房间，道具提供一次性能力（冻结敌人、拉动箱子、传送），程序化的房间布局
保证了变化性。最理想的版本会让人感觉像是把国际象棋和仓库搬运谜题融合在一起，
每一步都有战术上的后果。

## 玩家体验流程

标题画面用石质纹理营造出地牢氛围，并给出清晰的开始入口。玩家进入地牢房间后，
能在网格上看到墙壁、箱子、压力板、锁住的门、钥匙、敌人和出口楼梯。移动是回合制
的：方向键移动一格，同时所有敌人也移动一格。

前期房间教基础的推动：把一个箱子推到压力板上以打开一道门。很快就会出现在移动
时机上与玩家镜像同步的敌人，迫使玩家规划出既能推箱子又能躲开或困住威胁的动作
序列。中期引入多种箱子类型（重箱子需要推两次，冰箱子会一直滑到撞墙为止）、
解锁颜色对应门的钥匙，以及从宝箱里找到的道具。后期房间在程序化编排的布局中把
所有机制结合起来，玩家必须一边解空间谜题，一边管理敌人的位置。

撤销系统让玩家可以回退回合。抵达出口楼梯即前往下一层。被敌人碰到而死亡后可以
重试。战役会生成越来越复杂的楼层，敌人更多、箱子类型更多、空间约束更紧。

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

