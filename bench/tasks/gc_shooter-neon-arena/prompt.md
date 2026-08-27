# Neon Arena

Build **Neon Arena**, a twin-stick arena shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being the last pilot standing in a sealed geometric arena as
waves of hostile shapes pour in from every edge. The interesting tension is the
score multiplier: every kill within a short window raises the multiplier, but
taking a single hit resets it to zero. The player must constantly push forward
into danger to keep the chain alive rather than retreating to safety. Bombs
offer a panic button that clears the screen but sacrifice potential multiplier
growth. Multiple arenas with different layouts and hazard placements force the
player to adapt movement patterns rather than memorizing one safe route.

## What the Player Experiences

The player opens to a pulsing title screen with neon wireframe aesthetics, then
selects an arena from a small roster. Gameplay begins immediately: the ship sits
center-screen, one stick (or WASD) moves, the other (or arrow keys) aims and
fires continuously. Enemies spawn at arena edges in escalating waves — small
darts, splitting hexagons, homing diamonds, shielded rings. Each kill adds to a
visible multiplier counter; a timer bar shows how long until the multiplier
decays. Grazing bullets without dying builds a secondary graze bonus.

Between waves a brief upgrade prompt offers weapon mods — wider spread, faster
fire rate, piercing shots, or an extra bomb. The arena itself may shift: walls
retract, hazard zones ignite, or gravity wells appear. Every few waves a boss
shape enters with patterned attacks. Losing all lives shows a final score
breakdown with multiplier stats, highest chain, and arena-specific leaderboard
position.

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

# 霓虹竞技场（Neon Arena）

在 `/workspace/game/` 用 Godot 4 开发 **Neon Arena**，一款双摇杆竞技场射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一座封闭的几何竞技场中当那个活到最后的驾驶员，敌意图形一波波
从每一条边界涌入。有趣的张力来自分数倍率：短时间窗口内的每次击杀都会提高倍率，
但只要挨到一次伤害就会把它清零。玩家必须不断向危险中推进以维持连锁，而不是
退守安全区。炸弹提供了一个能清屏的应急按钮，代价是牺牲潜在的倍率成长。多个
布局与危险物摆放各异的竞技场迫使玩家调整移动模式，而不是背下一条安全路线。

## 玩家体验流程

玩家进入游戏时看到一个带霓虹线框美学、不断脉动的标题画面，然后从一个小型
名单中选择一个竞技场。游戏立刻开始：飞船位于屏幕中央，一根摇杆（或 WASD）
负责移动，另一根（或方向键）负责瞄准并持续开火。敌人在竞技场边缘以逐步升级的
波次生成——小型飞镖、会分裂的六边形、追踪型菱形、带护盾的圆环。每次击杀都会
累加到一个可见的倍率计数器上；一根计时条显示倍率还有多久开始衰减。擦弹而不
死亡会积累一项额外的擦弹奖励。

波次之间会有一个简短的升级提示，提供武器改装——更宽的散射、更快的射速、
穿透弹，或多一枚炸弹。竞技场本身也可能变化：墙壁收回、危险区域点燃，或出现
重力井。每隔几个波次会有一个 Boss 图形带着成形的攻击入场。失去所有生命后会
显示一份最终分数细目，含倍率数据、最高连锁，以及该竞技场专属的排行榜名次。

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

