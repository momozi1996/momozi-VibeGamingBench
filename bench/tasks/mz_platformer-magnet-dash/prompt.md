# Magnet Dash

Build **Magnet Dash**, a platformer with magnetic attract/repel mechanics and
momentum traversal as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

A magnetized robot navigates industrial chambers by attracting toward or
repelling away from metal surfaces scattered throughout each level. Holding
attract pulls the robot toward the nearest metal anchor, building speed as it
approaches. Releasing at the right moment converts that pull into ballistic
momentum. Repel pushes the robot away explosively, launching it across gaps or
up shafts. The interplay between attract and repel creates a swinging,
slingshotting movement vocabulary that feels like controlled chaos. Thirty
levels across three zones introduce increasingly complex magnetic puzzles,
and three boss encounters require using magnetic mechanics offensively —
deflecting projectiles or pulling shields away from enemies.

## What the Player Experiences

A title screen shows the robot suspended between two magnets. A zone-select
menu shows three zones of ten levels each, plus a boss at each zone's end.

In gameplay, metal surfaces glow with a distinct color. Holding the attract
button pulls the robot toward the nearest metal surface — the closer it gets,
the faster it accelerates. Releasing converts momentum into free flight.
Pressing repel near a metal surface launches the robot away at high speed.
Levels require chaining these moves to cross gaps, ascend shafts, and avoid
hazards like electric fields and crushers.

Boss fights take place in arenas with metal anchors. Bosses fire projectiles
that can be magnetically deflected, or have metal armor plates that can be
ripped away with attract. Defeating a boss unlocks the next zone. A completion
screen shows time, collectibles gathered, and a style rating based on momentum
chains.

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

# 磁力冲刺（Magnet Dash）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Magnet Dash**，一款带磁力吸引/排斥机制与动量位移的平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一个被磁化的机器人靠吸附向或排斥离每个关卡中散布的金属表面来穿越工业厂房。按住吸引会把机器人拉向最近的金属锚点，并在接近过程中积攒速度。在恰当时机松手就把这股拉力转化为抛射式的动量。排斥会把机器人爆发式地推开，让它横越间隙或沿竖井上冲。吸引与排斥之间的相互作用造就出一套摆荡、弹射般的移动语汇，玩起来像是可控的混乱。三个区域共三十个关卡会引入越来越复杂的磁力谜题，而三场 Boss 战则要求把磁力机制用于进攻——弹开抛射物，或把护盾从敌人身上拉走。

## 玩家体验流程

标题画面显示机器人悬在两块磁铁之间。一个区域选择菜单展示三个区域，每个区域十个关卡，外加每个区域末尾的一场 Boss 战。

进入游玩后，金属表面会以一种醒目的颜色发光。按住吸引键会把机器人拉向最近的金属表面——距离越近，加速越快。松手则把动量转化为自由飞行。在金属表面附近按下排斥会把机器人高速弹开。关卡要求串联这些动作来跨越间隙、攀升竖井，并躲开电场和碾压机之类的危险物。

Boss 战发生在布有金属锚点的竞技场里。Boss 会发射可被磁力弹开的抛射物，或是身上带有能被吸引撕下的金属装甲板。击败 Boss 会解锁下一个区域。完成画面显示时间、收集到的收集品，以及一个基于动量串联的风格评级。

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

