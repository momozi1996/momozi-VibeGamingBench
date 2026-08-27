# Sports Skateboard Park

Build a **Sports Skateboard Park** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player skates through parks performing trick combos for high scores, unlocking
new tricks and building custom parks. The fantasy is flow state: chaining grinds
into flips into manuals in one unbroken combo, watching the score multiplier
climb. Tension comes from the landing — mistiming a trick means a bail that
resets the combo. Career goals push the player to master specific tricks and
achieve target scores in themed parks.

## What the Player Experiences

1. **Title Screen** — A graffiti-styled title with the game name in spray-paint
   font over a half-pipe silhouette. A play button shaped like a wheel.
2. **Park Selection** — Multiple parks with different layouts: a street course
   (rails, stairs, ledges), a vert ramp (half-pipes, bowls), and a mega park
   (all elements combined). Each unlocks progressively.
3. **Skating** — The player moves left/right with momentum physics. Speed builds
   on downhill, drains on uphill. The skater has smooth rolling animation and
   responds to terrain.
4. **Trick System** — Button combinations trigger tricks: flip tricks (tap keys),
   grind tricks (press near rails), grab tricks (hold in air). Each trick has a
   name that pops up on screen. Tricks chain into combos with a visible
   multiplier.
5. **Score Multiplier** — Linking tricks without touching ground or bailing
   increases the multiplier. Landing cleanly banks the score; bailing loses the
   current combo. A combo meter shows current chain length and potential score.
6. **Career Goals** — Each park has specific challenges: "Score 10,000 in one
   combo", "Land a kickflip to grind", "Complete a full pipe rotation". Completing
   goals unlocks new tricks and parks.
7. **Park Editor** — The player can place ramps, rails, and obstacles to create
   custom parks. Placed elements snap to a grid. Custom parks are playable
   immediately.

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

# 滑板公园（Sports Skateboard Park）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**滑板公园**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在各个公园里滑行，做出特技连击来刷高分，解锁新特技并搭建自定义公园。
这里的幻想是"心流状态"：在一段不间断的连击中把磨轨串进翻板、再串进平衡滑行，
看着分数倍率一路攀升。张力来自落地——一个特技没掐准时机就意味着一次摔车，
连击随之清零。生涯目标推动玩家去精通特定的特技，并在主题公园里达成目标分数。

## 玩家体验流程

1. **标题画面** —— 一个涂鸦风格的标题，游戏名称采用喷漆字体，压在一个半管的
   剪影之上。一个轮子形状的开始按钮。
2. **公园选择** —— 多个布局各异的公园：街式场地（栏杆、台阶、边沿）、垂直坡道
   （半管、碗池），以及一个综合公园（所有元素合而为一）。它们逐步解锁。
3. **滑行** —— 玩家用左/右移动，带有动量物理。速度在下坡时积攒，在上坡时流失。
   滑手拥有流畅的滚动动画，并会对地形做出反应。
4. **特技系统** —— 按键组合触发特技：翻板特技（轻按按键）、磨轨特技（靠近栏杆
   时按下）、抓板特技（在空中按住）。每个特技都有一个名字弹出在屏幕上。特技可以
   串成连击，并带有可见的倍率。
5. **分数倍率** —— 在不触地、不摔车的前提下把特技连起来，倍率就会提升。干净
   落地会把分数入袋；摔车则丢掉当前连击。一个连击计量条显示当前的连接长度和
   潜在得分。
6. **生涯目标** —— 每个公园都有特定挑战："在一次连击中得到 10,000 分"、
   "落成一个 kickflip 接磨轨"、"完成一次全管旋转"。完成目标可解锁新的特技和
   公园。
7. **公园编辑器** —— 玩家可以摆放坡道、栏杆和障碍物来创建自定义公园。摆放的
   元素会吸附到网格上。自定义公园可立即游玩。

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

