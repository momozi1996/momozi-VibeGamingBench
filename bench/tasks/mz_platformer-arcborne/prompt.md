# Arcborne

Build **Arcborne**, a 2D **grappling-hook swing-momentum platformer** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a time-attack about chaining pendulum swings across deadly
terrain, releasing at the perfect instant to soar, and hooking again before
gravity wins.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Fly, don't walk. The player is an acrobat who crosses chasms by firing a
grappling hook, swinging on the line, and releasing at the apex to launch into a
soaring arc -- then hooking again to chain momentum across the course. The
fantasy is momentum mastery: gravity, swing arcs, and well-timed releases
compound into speed, and the difference between a clumsy crawl and a flowing
chain of perfect swings is visceral. One clean run of linked swings feels
glorious; one mistimed release drops you into the spikes.

The pressure comes from the clock. Every course is a time-attack where the
player reads terrain, picks anchor points, commits to a swing, and decides the
exact frame to let go. Multiple hook modes add tactical depth -- sometimes you
need raw pendulum momentum, sometimes a direct yank to reposition -- and the
worlds themselves bend the rules of motion so mastery in one biome doesn't
guarantee mastery in the next.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen that
   establishes the acrobatic, high-velocity tone. Starting a run drops them into
   the first world with a visible clock already ticking.

2. **Swing and Chain** -- The core sensation is physical: fire a hook at an
   overhead anchor, feel gravity pull the arc, build speed at the bottom of the
   pendulum, and release to fling forward. A fresh hook mid-flight chains one
   swing into the next without touching the ground. The player shapes each swing
   -- pumping, reeling, steering -- so skilled play looks fluid and fast while
   beginners flail and recover.

3. **Multiple Hook Modes** -- The player discovers they have more than one kind
   of hook. A swing line carries pendulum momentum; a pull line yanks them
   straight to an anchor for tight climbs or recoveries. Switching between modes
   becomes second nature as the terrain demands it.

4. **Worlds that Change the Rules** -- The journey carries the player through
   escalating worlds with distinct environments. Each world introduces its own
   anchor types, hazards, and an environmental modifier that alters how swinging
   feels -- gusts that shove mid-arc, conveyors that drag on the ground, low
   gravity that stretches every launch into a long glide. The player must adapt
   their timing and technique to each new set of physics.

5. **Danger and Recovery** -- Pits, spikes, blades, and moving hazards punish
   mistimed releases. Hitting a hazard or falling sends the player back to a
   checkpoint with clear feedback. The course is forgiving enough to learn but
   punishing enough that a clean run feels earned.

6. **Resolution** -- Reaching the goal ends the course with a result showing
   time and medal. The player can retry for a better time or advance to the next
   course. The full loop -- title, play, result, retry or advance -- flows
   without restarting the application.

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

# 弧行者（Arcborne）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Arcborne**，一款 2D **钩索摆荡动量平台跳跃游戏**：这是一场计时挑战，玩家要在致命地形之上串联钟摆式摆荡，在完美的瞬间脱手腾空，并在重力占上风之前再次抛出钩索。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

要飞，不要走。玩家扮演一名杂技高手，靠发射钩索、吊在绳上摆荡、并在最高点脱手弹射出一道腾空弧线来跨越深渊——随后再次抛钩，把动量在整条赛道上串联起来。这里的幻想是掌控动量：重力、摆荡弧线和精准掐时的脱手会层层叠加成速度，而笨拙地爬行与流畅串联的完美摆荡之间的差别是可以切身感受到的。一次干净的连续摆荡跑完全程令人畅快无比；一次脱手失误就会把你摔进尖刺。

压力来自时钟。每条赛道都是一场计时挑战，玩家要读地形、挑锚点、决心投入一次摆荡，并判断究竟在哪一帧松手。多种钩索模式带来战术深度——有时你需要纯粹的钟摆动量，有时需要一次直接的拉拽来重新占位——而各个世界本身还会扭曲运动规则，所以在一个生态区中的熟练并不保证在下一个中同样游刃有余。

## 玩家体验流程

1. **标题与入场** —— 玩家进入一个经过设计的标题画面，它确立了杂技般的高速调性。开始一轮游戏后，玩家被投入第一个世界，时钟已经在可见地走动。

2. **摆荡与串联** —— 核心体感是物理性的：朝头顶的锚点发射钩索，感受重力拉出弧线，在钟摆底部积攒速度，然后脱手向前抛射。飞行途中重新抛出的钩索能把一次摆荡接进下一次，全程不落地。玩家还能塑形每一次摆荡——助推、收绳、转向——因此高手的操作看上去流畅迅捷，而新手则手忙脚乱、疲于补救。

3. **多种钩索模式** —— 玩家会发现自己拥有不止一种钩索。摆荡索承载钟摆动量；牵引索则把自己直接拽向锚点，用于贴身攀爬或紧急补救。随着地形提出要求，模式切换会变成本能。

4. **改写规则的世界** —— 旅程带领玩家穿过一个个难度递增、环境各异的世界。每个世界都会引入自己的锚点类型、危险物，以及一种改变摆荡手感的环境修正——弧线中途推挤你的阵风、在地面上拖拽你的传送带、把每次弹射拉长成一段滑翔的低重力。玩家必须针对每套新物理规则调整自己的时机与技巧。

5. **危险与补救** —— 陷坑、尖刺、刀刃和移动危险物会惩罚脱手失误。撞上危险物或坠落会把玩家送回检查点，并给出明确反馈。赛道足够宽容以供学习，但也足够严苛，让一次干净通关显得来之不易。

6. **收束** —— 抵达终点结束本条赛道，并弹出显示用时与奖牌的结算。玩家可以重试以刷新更好的时间，或是推进到下一条赛道。完整的循环——标题、游玩、结算、重试或推进——全程无需重启应用。

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

