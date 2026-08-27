# Kitchen Rush

Build **Kitchen Rush**, a 2D time-pressure cooking simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a restaurant kitchen during a dinner rush, juggling
multiple orders across different cooking stations while timers tick down and
customers grow impatient. The interesting tension is multitasking under pressure:
each recipe requires specific steps at specific stations in a specific order, and
the player must mentally track multiple dishes simultaneously. Burning food wastes
ingredients and time; serving wrong orders loses reputation. Between shifts the
player unlocks new recipes, upgrades stations, and expands the kitchen layout,
but more capacity means more complex orders and higher customer expectations.

## What the Player Experiences

The player opens to a restaurant storefront title screen, then enters the first
shift. The kitchen view shows stations arranged spatially: chopping board, stove,
fryer, oven, plating area, and serving window. Orders appear at the top with
recipe requirements and countdown timers. The player clicks a station to interact,
drags ingredients from the pantry to stations, and monitors cooking progress.

Recipes start simple — chop lettuce, plate it, serve — but quickly layer:
burger requires chopping, grilling, assembling bun with toppings, then plating.
Multiple orders run simultaneously. Overcooking triggers smoke and waste.
Completing orders earns coins and tips based on speed. Between shifts a shop
screen offers station upgrades (faster stove, larger fryer), new recipe unlocks,
and kitchen expansions. The campaign progresses through 10+ shifts with
increasing order complexity, customer volume, and recipe variety. A shift
summary shows orders completed, failed, tips earned, and star rating.

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

# 厨房争分夺秒（Kitchen Rush）

在 `/workspace/game/` 用 Godot 4 开发 **Kitchen Rush**，一款 2D 限时压力烹饪模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在晚餐高峰时段经营一家餐厅厨房，在不同的烹饪工位之间同时应付多张
订单，而计时器在倒数、顾客越来越不耐烦。有趣的张力来自压力下的多任务处理：
每道菜谱都要求在特定工位、按特定顺序完成特定步骤，玩家必须在脑中同时追踪多道
菜。烧糊食物会浪费食材与时间；上错订单会损失口碑。班次之间，玩家会解锁新菜谱、
升级工位并扩建厨房布局，但更大的产能意味着更复杂的订单和更高的顾客期待。

## 玩家体验流程

玩家进入游戏时看到一个餐厅门面的标题画面，随后进入第一个班次。厨房视图展示
按空间排布的各个工位：切菜板、炉灶、油炸锅、烤箱、摆盘区和出餐窗口。订单出现
在顶部，带有菜谱要求与倒计时。玩家点击一个工位进行交互，从储藏室把食材拖到
工位上，并监控烹饪进度。

菜谱一开始很简单——切生菜、摆盘、上菜——但很快就会层层叠加：汉堡需要切配、
炙烤、把配料组装进面包，然后摆盘。多张订单会同时进行。过火会触发冒烟与浪费。
完成订单可按速度赚取金币与小费。班次之间会有一个商店画面，提供工位升级
（更快的炉灶、更大的油炸锅）、新菜谱解锁和厨房扩建。战役推进 10 个以上班次，
订单复杂度、顾客流量与菜谱多样性持续增加。班次总结会显示完成的订单数、失败
的订单数、赚到的小费和星级评价。

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

