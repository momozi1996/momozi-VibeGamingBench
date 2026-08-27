# Air Control

Build **Air Control**, a 2D air traffic control simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is directing aircraft safely to their runways from a radar-style
control screen, drawing flight paths through increasingly crowded airspace while
avoiding collisions and managing weather disruptions. The interesting tension is
spatial planning under time pressure: planes enter from screen edges at different
speeds and altitudes, each needing to reach a specific runway. The player draws
paths that planes follow, but new arrivals constantly force replanning. Near-miss
warnings create panic moments where quick rerouting prevents disaster. Weather
events close runways or create no-fly zones, demanding real-time adaptation of
carefully laid plans.

## What the Player Experiences

The player opens to a control-tower themed title screen, selects an airport from
a campaign list, and enters the radar view. The screen shows a stylized top-down
airport with runways, taxiways, and surrounding airspace. Planes appear at edges
with callsigns, types, and destination runway indicators. The player draws a
flight path from each plane to its assigned runway by clicking and dragging
waypoints.

Planes follow their paths at their own speed. Proximity warnings flash when two
planes get too close. Successful landings earn points; collisions or planes
leaving the screen without landing lose lives. Between levels the player can
upgrade: add runways, install weather radar, unlock speed-control commands, or
expand the airspace boundary. Weather events — fog reducing visibility, storms
creating no-fly zones, crosswinds affecting runway availability — increase
pressure. The campaign spans 12+ levels across 3 airports with escalating
traffic density and complexity. A level summary shows planes landed, near-misses,
and efficiency rating.

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

# 空中管制（Air Control）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Air Control**，一款 2D 空中交通管制模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一块雷达式管制屏幕前把飞机安全引导至它们各自的跑道，在越来越
拥挤的空域中绘制航路，同时避免相撞并应对天气扰动。有趣的张力来自时间压力下的
空间规划：飞机以不同的速度和高度从屏幕边缘进入，每一架都需要抵达某条特定跑道。
玩家绘制航路，飞机会沿之飞行，但不断到来的新飞机会持续迫使玩家重新规划。近距接近
告警会制造出恐慌时刻，此时迅速改航才能避免灾难。天气事件会关闭跑道或形成
禁飞区，要求玩家实时调整精心铺设好的计划。

## 玩家体验流程

玩家进入游戏时看到一个塔台主题的标题画面，从战役列表中选择一座机场，然后进入
雷达视图。屏幕展示一座风格化的俯视机场，含跑道、滑行道及周边空域。飞机出现在
边缘，带有呼号、机型和目标跑道标识。玩家通过点击并拖动航路点，为每一架飞机
绘制一条从当前位置通往其指定跑道的航路。

飞机会按自身速度沿航路飞行。当两架飞机靠得太近时会闪现接近告警。成功着陆可得分；
相撞或飞机未着陆便飞离屏幕会损失生命。关卡之间玩家可以升级：增建跑道、安装
气象雷达、解锁速度控制指令，或扩展空域边界。天气事件——降低能见度的雾、形成
禁飞区的风暴、影响跑道可用性的侧风——会加大压力。战役横跨 3 座机场共 12 个
以上关卡，交通密度与复杂度逐步升级。关卡总结会显示着陆架数、近距接近次数
以及效率评级。

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

