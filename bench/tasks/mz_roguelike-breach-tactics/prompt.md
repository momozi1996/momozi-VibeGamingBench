# Breach Tactics

Build **Breach Tactics**, a tactics roguelike on a small grid with visible enemy
intents as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A squad of three mechs defends a city grid from waves of alien invaders. The
twist: every enemy telegraphs its next move before the player acts, turning
each turn into a spatial puzzle of displacement, blocking, and sacrifice. The
grid is small (8x8) and buildings occupy tiles that must be protected — if too
many are destroyed, the timeline is lost. Between battles the player earns
reactor cores to upgrade mech abilities or unlock new pilots with passive
traits. A timeline-reset mechanic gives the player a limited number of full
turn undos per battle, allowing recovery from catastrophic mistakes. Four
islands of escalating difficulty each culminate in a boss encounter with unique
grid mechanics.

## What the Player Experiences

A title screen shows mechs dropping onto a grid. An island-select map shows
four islands with branching mission paths.

Each mission places the mech squad on a grid with buildings and spawning
enemies. Before the player moves, every enemy displays its intended action:
attack direction, movement target, or spawn location. The player moves each
mech and uses one ability per mech — push, shoot, shield, repair, or special.
After all mechs act, enemies execute their telegraphed moves simultaneously.

Protecting buildings is the priority — each destroyed building reduces a
structural integrity bar. Losing all integrity fails the mission. Timeline
resets (limited per battle) rewind one full turn. Between missions, upgrade
screens offer new weapons, pilot abilities, and reactor power allocation.
Completing an island unlocks the next. A final victory screen shows missions
completed, buildings saved, and resets used.

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

# 突破战术（Breach Tactics）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Breach Tactics**——一款在小型网格上进行、
敌人意图完全可见的战术 Roguelike。这不是原型，而是一个**完整、可发布的微型
游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一支由三台机甲组成的小队保卫城市网格，抵御一波又一波异星入侵者。妙处在于：每个
敌人都会在玩家行动之前预告自己的下一步，让每个回合都变成一道关于位移、阻挡与
牺牲的空间谜题。网格很小（8x8），建筑占据着必须保护的格子——若被摧毁的建筑过多，
时间线就宣告失守。战斗之间，玩家赚取反应堆核心，用来升级机甲能力或解锁带被动
特质的新驾驶员。时间线重置机制给玩家每场战斗有限次数的整回合撤销，让灾难性失误
还有挽回余地。四座难度递增的岛屿各自以一场拥有独特网格机制的 Boss 战收尾。

## 玩家体验流程

标题画面展示机甲降落到网格上。岛屿选择地图展示四座岛屿以及分支任务路线。

每场任务把机甲小队放在一片有建筑和不断刷出的敌人的网格上。在玩家移动之前，每个
敌人都会显示自己打算做的事：攻击方向、移动目标或刷出位置。玩家移动每台机甲，
并让每台机甲使用一个能力——推击、射击、护盾、修复或特殊技。所有机甲行动完毕后，
敌人同时执行它们预告过的行动。

保护建筑是首要任务——每栋建筑被毁都会削减一条结构完整度条。完整度耗尽即任务
失败。时间线重置（每场战斗次数有限）可以回退一整个回合。任务之间的升级画面提供
新武器、驾驶员能力和反应堆功率分配。完成一座岛屿即解锁下一座。最终的胜利画面
展示完成的任务数、保住的建筑数和使用过的重置次数。

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

