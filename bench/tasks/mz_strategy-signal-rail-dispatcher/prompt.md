# Signal Rail Dispatcher

Build **Signal Rail Dispatcher**, a compact 2D railway signal and routing
management game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It
is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

The player is a lone dispatcher in a cramped signal box, watching colored
trains crawl across a schematic board and making split-second routing calls
that ripple forward in time. Every switch flip commits a path; every red signal
buys thinking room at the cost of punctuality. The fantasy is **quiet mastery
under mounting pressure** — a timetable that starts gentle, then stacks
conflicting services until the board is a web of near-misses and the player
must think several moves ahead to keep everything flowing. The best version
feels like a control-room puzzle where one wrong toggle cascades into delay,
and a clean shift feels earned.

## What the Player Experiences

1. **The Shift Begins** — A styled title screen sets the tone of a railway
   control room. The player starts a shift and sees a compact track diagram
   with stations, sidings, signals, and switchable junctions laid out like a
   schematic map.
2. **Reading the Board** — Trains appear at entry points and crawl along the
   tracks. Each train has a visible identity — color, service type, destination
   — and the timetable or HUD tells the player where it needs to go and when.
   Signals glow red or green; switches show which way they are set.
3. **Routing Decisions** — The player clicks signals to hold or release trains,
   and flips switches to redirect paths. A released train follows the set route
   until it hits the next red signal or reaches its destination. The challenge
   is sequencing: two trains cannot safely share a section, and letting one
   through means another waits.
4. **Escalation** — The shift intensifies. More trains arrive, express services
   demand priority, delays compound, and blocked sections force creative
   rerouting. Conflict warnings or occupancy lights tell the player when a
   collision is imminent.
5. **Resolution** — The shift ends with a result screen reporting punctuality,
   incidents avoided or caused, and overall performance. The player can retry
   or return to the title without restarting the application.

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

# 信号铁路调度员（Signal Rail Dispatcher）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Signal Rail Dispatcher**，一款小而精的 2D 铁路信号与路线管理游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一间狭小信号楼里的独任调度员，看着彩色列车在示意图板上缓缓爬行，做出会在时间上一路涟漪扩散的瞬时排线决定。每一次道岔扳动都锁定一条路径；每一个红灯都以准点率为代价换来思考的余地。核心幻想是**在不断累积的压力下静默地掌控全局**——时刻表起初温和，随后把互相冲突的班次层层堆叠，直到图板变成一张险象环生的网，玩家必须提前想好几步才能让一切保持流动。最理想的版本感觉像一道控制室谜题：一次错误的切换就会连锁成延误，而一个干净利落的班次则来之不易。

## 玩家体验流程

1. **班次开始** —— 一个精心设计的标题画面定下铁路控制室的基调。玩家开始一个班次，看到一张紧凑的轨道示意图，其中车站、侧线、信号机与可切换的道岔像示意地图一样铺陈开来。
2. **读懂图板** —— 列车在入口点出现并沿轨道缓行。每列车都有可见的身份标识——颜色、班次类型、目的地——而时刻表或 HUD 会告诉玩家它需要去哪里、何时抵达。信号机亮红或亮绿；道岔显示当前扳向哪一侧。
3. **排线决策** —— 玩家点击信号机来扣停或放行列车，并扳动道岔以改变路径。被放行的列车会沿着已设定的路线行驶，直到遇上下一个红灯或抵达目的地。挑战在于排序：两列车无法安全共用同一区段，放行一列就意味着另一列必须等待。
4. **难度升级** —— 班次逐渐吃紧。更多列车到达，特快班次要求优先权，延误层层累积，被占用的区段迫使玩家创造性地改线。冲突警告或占用指示灯会在碰撞即将发生时提醒玩家。
5. **收尾结算** —— 班次以一个结算画面结束，报告准点率、避免或造成的事故，以及整体表现。玩家可以重试或返回标题画面，无需重启应用程序。

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

