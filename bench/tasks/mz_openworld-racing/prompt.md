# Open-World Racing

Build a **2D open-world racing game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player drives a vehicle across a large open-world map with multiple
biomes, discovering and racing on scattered tracks. Each track has a unique
layout, terrain type, and time-trial record to beat. Tension comes from
momentum management — braking too late sends you off the road, drifting at
the right moment rewards a speed boost, and each biome demands a different
driving style. The art style should feel **fast, vibrant, and arcade-like** —
think *Burnout* meets *A Short Hike* at a smaller scale.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a play button, and
   a dynamic racing backdrop (speed lines, car silhouette, sunset highway).
   No naked Godot grey.
2. **The World** — The player spawns in an open-world map with at least three
   visually distinct biomes: coastal road, desert canyon, and mountain pass.
   The vehicle can drive freely in all directions, exploring at will.
3. **Scattered Tracks** — Each biome contains at least one race track marked
   by a visible start/finish line and checkpoint gates. Tracks have different
   layouts suited to their terrain: long straights, tight switchbacks, or
   elevation hairpins.
4. **Vehicle Physics** — The vehicle accelerates, brakes, and steers with
   visible momentum. Drifting around corners produces a skid-mark trail and
   a brief speed boost when released. The vehicle sprite visibly tilts when
   turning.
5. **Timer and Records** — A lap timer starts when the player crosses the
   start line and stops at the finish. The HUD shows current lap time, best
   lap time, and a medal ranking (Gold/Silver/Bronze based on time).
6. **Track Unlocking** — Winning a bronze or better medal on one track unlocks
   the next track with a visible unlock animation. The player progresses
   through the world by earning medals.
7. **Speed Feedback** — A speedometer is always visible on the HUD. At high
   speed, the screen edges show a subtle motion-blur or speed-line effect.

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

# 开放世界竞速（Open-World Racing）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界竞速游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶载具穿越一张包含多个生态区的大型开放世界地图，发现散布各处的赛道并
在上面竞速。每条赛道都有独特的布局、地形类型和待打破的计时赛记录。张力来自
动量管理——刹车太晚会冲出路面，在正确的时机漂移则会奖励一次速度提升，而每个
生态区都要求不同的驾驶风格。美术风格应当给人**快速、鲜艳、街机感**的观感——
可以想象成小体量的 *Burnout* 结合 *A Short Hike*。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮，以及一幅
   富有动感的竞速背景（速度线、汽车剪影、日落公路）。不要出现 Godot 的裸灰色。
2. **世界** —— 玩家出生在一张开放世界地图上，其中至少有三个视觉上截然不同的
   生态区：海岸公路、沙漠峡谷和山间隘口。载具可以朝任意方向自由行驶，随意探索。
3. **散布的赛道** —— 每个生态区至少包含一条赛道，由可见的起终点线和检查点门
   标示。赛道拥有与其地形相适应的不同布局：长直道、密集的连续弯，或者带落差的
   发夹弯。
4. **载具物理** —— 载具的加速、刹车和转向都带有可见的动量。绕弯漂移会产生一条
   刹车痕轨迹，并在松开时给予短暂的速度提升。载具精灵图在转向时会明显倾斜。
5. **计时与记录** —— 玩家越过起点线时圈速计时开始，到达终点线时停止。HUD 显示
   当前圈速、最佳圈速，以及一个奖牌等级（依据用时评定金/银/铜）。
6. **赛道解锁** —— 在一条赛道上取得铜牌或更好的成绩会解锁下一条赛道，并伴有
   可见的解锁动画。玩家通过赢取奖牌在世界中推进。
7. **速度反馈** —— HUD 上始终显示一个速度表。高速时，屏幕边缘会呈现细微的
   动态模糊或速度线效果。

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

