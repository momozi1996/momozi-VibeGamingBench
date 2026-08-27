# Pipe Crisis

Build **Pipe Crisis**, a 2D pipe-routing puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places and rotates pipe segments on a grid to
route colored fluids from sources to matching drains before pressure builds
and the system overflows.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a time-pressure spatial puzzle built on fluid routing. Each level
has one or more fluid sources that begin pumping after a countdown. The player
must lay pipe segments from a queue onto a grid, rotating and placing them to
create continuous paths from each source to its matching drain. The tension
comes from the countdown timer and multiple fluid types: red chemicals cannot
mix with blue coolant, green acid dissolves standard pipes, and crossing paths
require special junction pieces. The best version feels like a frantic plumbing
emergency where every second of planning pays off when the fluids start flowing
and the paths light up with color.

## What the Player Experiences

A title screen sets the industrial tone with pipe imagery and pressure gauges.
The player enters a grid-based facility where sources, drains, obstacles, and
empty cells are visible. A pipe queue shows upcoming pieces. The countdown
timer ticks toward flow start.

Early levels teach basic routing: connect one source to one drain with simple
straight and corner pipes. Soon multiple sources demand parallel paths, color
matching prevents cross-contamination, and obstacles force creative detours.
Mid-game introduces special pipe types: cross junctions that allow two fluids
to pass without mixing, reservoir tanks that buy extra time, and acid-resistant
pipes for corrosive fluids. Late levels combine all mechanics with tight
timers and complex multi-source layouts.

When flow begins, fluid visibly travels through the pipes. Successful routing
fills the drain and completes the level. Overflow from dead ends or mixing
violations triggers a failure state. A results screen shows completion time
and efficiency rating. The campaign progresses through themed facilities with
escalating routing demands.

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

# 管道危机（Pipe Crisis）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Pipe Crisis**，一个 2D 管道布线解谜游戏。
玩家在网格上摆放和旋转管道段，在压力累积、系统溢流之前把彩色流体从源头引到
对应颜色的排放口。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款建立在流体布线之上、带时间压力的空间解谜游戏。每一关有一个或多个流体源，
在倒计时结束后开始泵送。玩家必须把队列中的管道段铺到网格上，通过旋转和摆放，
为每个源头到其对应排放口构造出连续的通路。张力来自倒计时和多种流体类型：红色
化学品不能与蓝色冷却液混合，绿色酸液会腐蚀普通管道，而交叉的路径需要特殊的接头
配件。最理想的版本会让人感觉像在应对一场手忙脚乱的管道抢险——当流体开始流动、
路径被颜色一路点亮时，此前每一秒的规划都得到了回报。

## 玩家体验流程

标题画面用管道意象和压力表营造出工业氛围。玩家进入以网格为基础的设施界面，
能看到流体源、排放口、障碍物和空白格。管道队列显示接下来会来的配件。倒计时
正一格格逼近流动开始的时刻。

前期关卡教基础布线：用简单的直管和弯管把一个源头连到一个排放口。很快，多个源头
就会要求并行通路，颜色匹配防止交叉污染，障碍物迫使玩家绕出创意路线。中期引入
特殊管道类型：允许两种流体通过而不混合的十字接头、能争取更多时间的储液罐，以及
用于腐蚀性流体的耐酸管道。后期关卡把所有机制结合起来，配上紧张的计时和复杂的
多源布局。

流动开始后，流体会可见地在管道中行进。布线成功会灌满排放口并完成该关卡。死路
造成的溢流或混合违规会触发失败状态。结算画面展示完成时间和效率评级。战役按主题
设施推进，布线要求层层升级。

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

