# Open-World Sky Islands

Build an **Open-World Sky Islands** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player glides between floating islands suspended in an endless sky, exploring
mini-dungeons, collecting wind crystals, and defeating boss guardians to unlock
new regions. The fantasy is weightless freedom: leaping from island edges, riding
wind currents, and discovering hidden platforms in the clouds. Tension comes from
the glide mechanic — stamina depletes mid-air, and falling into the void means
restarting from the last island. Wind crystals extend glide range and unlock
powerful abilities.

## What the Player Experiences

1. **Title Screen** — A bright, airy title with the game name floating among
   clouds and distant islands. A play button shaped like a wind crystal.
2. **Island Hub** — The player starts on a central island with paths leading to
   launch points. Distant islands are visible, some shrouded in mist until
   unlocked.
3. **Gliding** — The player jumps from edges and glides using a stamina-based
   wing mechanic. Wind currents (visible as particle streams) boost altitude.
   Stamina depletes during flight; landing on any surface restores it.
4. **Mini-Dungeons** — Each island contains a small dungeon with platforming
   challenges, enemies, and a wind crystal reward. Dungeons have themed hazards:
   fire jets, moving platforms, spike traps.
5. **Wind Crystals** — Collectible crystals that serve as both currency and power
   source. Spending crystals unlocks abilities: dash, double-jump, updraft
   creation. A crystal counter is always visible.
6. **Boss Guardians** — Larger islands have boss encounters. Each boss has
   attack patterns the player must learn and dodge. Defeating a boss unlocks
   access to a new cluster of islands.
7. **Progression** — The world is divided into island clusters. Each cluster has
   a distinct visual theme (forest islands, crystal islands, volcanic islands)
   and progressively harder challenges.

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

# 开放世界浮空岛（Open-World Sky Islands）

在 `/workspace/game/` 用 Godot 4 开发一个**开放世界浮空岛（Open-World Sky Islands）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在悬浮于无尽天空中的浮空岛之间滑翔，探索迷你地牢、收集风之结晶，并击败
Boss 守卫以解锁新的区域。这里的幻想是失重般的自由：从岛缘一跃而下，乘着气流
飞行，在云间发现隐藏的平台。张力来自滑翔机制——空中体力会不断消耗，而坠入
虚空意味着从上一座岛重新开始。风之结晶能延长滑翔距离并解锁强力能力。

## 玩家体验流程

1. **标题画面** —— 一个明亮通透的标题，游戏名称漂浮在云朵和远处的岛屿之间。
   开始按钮做成风之结晶的形状。
2. **岛屿枢纽** —— 玩家从一座中央岛出发，岛上的道路通往各个起飞点。远处的
   岛屿可见，其中一些在解锁前笼罩在薄雾中。
3. **滑翔** —— 玩家从岛缘跳出，使用基于体力的翼翅机制滑翔。气流（以粒子流的
   形式可见）能提升高度。飞行时体力持续消耗；落到任何表面上都会恢复体力。
4. **迷你地牢** —— 每座岛都包含一个小型地牢，内有平台跳跃挑战、敌人，以及一枚
   风之结晶作为奖励。地牢有各具主题的危险机关：火焰喷口、移动平台、尖刺陷阱。
5. **风之结晶** —— 可收集的结晶，既是货币也是能量来源。花费结晶可解锁能力：
   冲刺、二段跳、制造上升气流。结晶计数始终可见。
6. **Boss 守卫** —— 较大的岛上有 Boss 战。每个 Boss 都有玩家必须学习并躲避的
   攻击模式。击败一个 Boss 会解锁通往一片新岛群的通路。
7. **进程** —— 世界被划分为若干岛群。每个岛群都有独特的视觉主题（森林岛、
   结晶岛、火山岛），挑战难度逐级提升。

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

