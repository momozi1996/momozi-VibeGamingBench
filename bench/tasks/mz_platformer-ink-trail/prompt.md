# Ink Trail

Build **Ink Trail**, a platformer where the player leaves a trail that becomes
solid platform after a delay as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

An ink spirit dashes through empty voids, leaving behind a wet trail of ink
that solidifies into walkable platforms after a short delay. The spirit has
limited ink — once the reservoir empties, no more trail is created until
reaching an ink well refill. The core puzzle: plan a path through empty space
such that the trail you leave behind creates the platforms you need to reach
the exit. Sometimes you must double back to stand on your own trail. Sometimes
you must draw a bridge mid-jump and land on it as it solidifies. Ink wells are
sparse, forcing efficient routing. Thirty-six levels across six worlds
introduce wind that displaces wet ink, erasers that dissolve trails, color-coded
ink that only solidifies near matching surfaces, and timed ink that fades after
seconds.

## What the Player Experiences

A title screen shows ink dripping into the game name. A world-select grid shows
six worlds of six levels each.

The player moves and jumps normally. While moving, ink trails behind the
character as a visible wet line. After a 1-second delay, the wet ink hardens
into a solid platform with a satisfying visual pop. An ink meter shows remaining
supply — when empty, movement leaves no trail. Ink wells scattered in levels
refill the meter.

Early levels teach basic trail-platforming: cross a gap by running through air
and doubling back onto your solidified trail. Later levels add complexity: wind
pushes wet ink sideways before it hardens, erasers delete sections of trail,
and timed ink fades after a few seconds requiring speed. Each level has a
three-star rating based on ink efficiency. A level-complete screen shows ink
used, time, and stars earned.

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

# 墨痕（Ink Trail）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ink Trail**，一款玩家留下的轨迹会在延迟之后凝固成实体平台的平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一只墨灵在空荡的虚空中疾行，身后留下一道湿墨轨迹，短暂延迟之后凝固成可行走的平台。墨灵的墨量有限——一旦储墨见底，就再也留不下轨迹，直到抵达一处墨井补充。核心谜题是：在空无一物的空间里规划一条路径，使你留下的轨迹恰好构成你抵达出口所需的平台。有时你必须折返回来，踩在自己的轨迹上。有时你必须在跳跃途中画出一座桥，并在它凝固的瞬间落在上面。墨井分布稀疏，逼迫玩家高效规划路线。横跨六个世界的三十六个关卡会陆续引入吹散湿墨的风、溶解轨迹的橡皮、只在匹配表面附近才凝固的彩色墨水，以及数秒后消退的限时墨水。

## 玩家体验流程

标题画面显示墨水滴落汇成游戏名。一个世界选择网格展示六个世界，每个世界六个关卡。

玩家正常移动和跳跃。移动时，墨水以一条可见的湿线拖在角色身后。经过 1 秒延迟后，湿墨硬化成实体平台，并伴有令人满足的视觉弹跳。一个墨量条显示剩余存量——见底时，移动便不再留下轨迹。散布在关卡中的墨井可以补满墨量条。

前期关卡教授基础的轨迹平台跳跃：从空中跑过去再折返踩上自己已凝固的轨迹，从而跨越一道间隙。后期关卡增加复杂度：风会在湿墨硬化前把它横向推移，橡皮会删掉轨迹的一段，限时墨水会在数秒后消退、要求速度。每个关卡都有基于用墨效率的三星评级。关卡完成画面显示用墨量、时间和获得的星数。

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

