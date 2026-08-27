# Racing Terrain Climb

Build a Racing Terrain Climb as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A side-scrolling physics vehicle game where the player drives over rugged
terrain, managing momentum and fuel to reach the farthest distance possible.
The vehicle bounces, tilts, and flips over hills and valleys — too much
throttle on a steep incline flips you backward; too little and you stall on
the slope. Fuel is limited and refilled at checkpoints, creating tension between
speed and conservation. Earned coins buy vehicle upgrades (engine power,
suspension, fuel capacity) and new vehicle types, each with different physics
properties. The fantasy is conquering impossible terrain through smart driving
and incremental improvement.

## What the Player Experiences

1. **Title Screen** — A rugged outdoor scene with the game name in bold blocky
   letters, a vehicle silhouette mid-jump against a sunset sky, and Play/Garage
   buttons. No plain Godot grey.
2. **Stage Select** — Multiple terrain environments (countryside hills, moon
   surface, arctic ice, desert dunes) each with distinct physics properties
   (friction, gravity). Stages unlock by reaching distance milestones.
3. **Driving Physics** — The vehicle has realistic 2D physics: wheels grip
   terrain, the chassis tilts with slope angle, and momentum carries over
   crests. The player controls gas (right) and brake (left), plus tilt
   (up/down) to adjust the vehicle's angle mid-air.
4. **Fuel Management** — A fuel gauge depletes as the player drives. Running
   out stops the vehicle. Fuel canisters appear along the route at intervals.
   The tension between driving fast (burning fuel) and conserving creates
   meaningful decisions.
5. **Coins and Distance** — Coins scatter along the terrain and award currency.
   Distance is tracked as a high score. Each run ends when fuel runs out or
   the vehicle is destroyed (landing on the roof).
6. **Garage/Upgrades** — Between runs, the player spends coins on upgrades:
   engine power, fuel capacity, suspension stiffness, tyre grip. At least 3
   different vehicle types (jeep, motorcycle, monster truck) with visibly
   different sprites and handling characteristics.
7. **Distance Records** — A persistent leaderboard shows best distance per
   stage. Beating a personal record triggers a celebration effect.

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

# 越野爬坡竞速（Racing Terrain Climb）

在 `/workspace/game/` 用 Godot 4 开发一个越野爬坡竞速游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款横向卷轴物理载具游戏，玩家驾车翻越崎岖地形，管理动量与燃油以抵达尽可能远的
距离。载具会在山丘与谷地上弹跳、倾斜、翻滚——在陡坡上油门给太猛会向后翻车；
给太小则会在坡上熄火停住。燃油有限，在检查点补充，从而在速度与节省之间制造出
张力。赚到的金币可以购买载具升级（引擎功率、悬挂、油箱容量）和新的载具类型，
每种都有不同的物理属性。这里的幻想是通过聪明的驾驶和一点点的改良，征服不可能的
地形。

## 玩家体验流程

1. **标题画面** —— 一幕粗粝的户外场景，游戏名称采用粗厚的方块字母，一辆载具的
   剪影在夕阳天空前腾空跃起，另有"开始"/"车库"按钮。不要出现 Godot 的裸灰色。
2. **关卡选择** —— 多种地形环境（乡间丘陵、月球表面、极地冰原、沙漠沙丘），
   每种都有独特的物理属性（摩擦力、重力）。关卡通过达到距离里程碑来解锁。
3. **驾驶物理** —— 载具具有真实的 2D 物理：车轮抓紧地形，底盘随坡度角度倾斜，
   动量会越过坡顶延续下去。玩家控制油门（右方向键）和刹车（左方向键），外加
   倾斜（上/下方向键）以在空中调整载具角度。
4. **燃油管理** —— 油量表随玩家行驶而下降。耗尽后载具会停下。燃油罐会间隔地
   出现在路线沿途。在开快（烧油）与省油之间的张力，造就了有意义的决策。
5. **金币与距离** —— 金币散布在地形沿途，收集可获得货币。距离作为最高分被记录。
   每一轮在燃油耗尽或载具被毁（车顶着地）时结束。
6. **车库/升级** —— 在两轮之间，玩家花金币购买升级：引擎功率、油箱容量、
   悬挂硬度、轮胎抓地力。至少有 3 种不同的载具类型（吉普车、摩托车、
   怪兽卡车），拥有明显不同的精灵图和操控特性。
7. **距离记录** —— 一个持久化的排行榜显示每个关卡的最远距离。打破个人记录会
   触发一段庆祝特效。

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

