# Tiny Factory Foreman

Build **Tiny Factory Foreman**, a compact 2D automation and production-planning
game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is running a miniature factory floor where raw materials flow in one
end and finished goods roll out the other — if the player has wired everything
together correctly. The interesting tension is spatial: belts only carry forward,
sorters only split, and machines only accept certain inputs, so every tile
placement is a routing puzzle under time pressure. Orders arrive on a board with
ticking deadlines, and the player must decide whether to retool the line for a
new product or squeeze more throughput from the current layout. The risk is
always a cascade failure — one misrouted material jams a machine, the backup
stalls the belt, and suddenly three orders expire at once. Growth comes from
earning enough to unlock faster belts, smarter sorters, or multi-output machines,
but each upgrade reshapes the routing problem rather than simply solving it.

## What the Player Experiences

The player opens to a compact workshop view: a few raw-material sources on one
side, empty order bins on the other, and a grid of open floor between them. An
order board shows what products are needed and how long remains. The first
minutes are about laying a simple belt path from source to machine to bin and
watching the first coloured crate trundle across the floor.

As orders grow more complex the player drops sorters to split material streams,
places different machine types that transform inputs into intermediate or final
goods, and reroutes belts to avoid collisions. The floor fills with motion —
little icons sliding along conveyors, machines pulsing as they process, sorters
flicking left or right. A well-designed line hums; a badly planned one backs up
and flashes warnings.

Between rounds or when cash allows, the player visits an upgrade screen to
improve belt speed, unlock a new machine recipe, or expand storage capacity.
These choices shape what orders can be accepted next. Eventually the shift ends
and a result screen tallies fulfilled orders, missed deadlines, and coins earned,
offering a retry or a return to the title.

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

# 小工厂车间主管（Tiny Factory Foreman）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Tiny Factory Foreman**，一款小体量的 2D 自动化与生产规划游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是经营一座微缩的工厂车间：原材料从一端流入，成品从另一端滚出——前提是玩家把所有环节都正确接通了。有趣的张力是空间性的：传送带只能向前运送，分流器只能分流，而机器只接受特定的输入，所以每一次图块摆放都是一道有时间压力的路径规划谜题。订单会出现在一块看板上，带着倒计时的截止期限，玩家必须决定是为新产品改造生产线，还是从当前布局里再榨出一些产能。风险始终是级联失效——一份材料走错路就卡住一台机器，积压又拖停传送带，接着三笔订单突然同时过期。成长来自赚够钱去解锁更快的传送带、更聪明的分流器，或多输出机器，但每一次升级都是在重塑路径规划难题，而不是简单地解决它。

## 玩家体验流程

玩家一进入游戏，看到的是一个紧凑的车间视图：一侧是几处原材料来源，另一侧是空的订单料箱，两者之间是一片空地网格。一块订单看板显示需要哪些产品、还剩多少时间。最初几分钟是从来源到机器再到料箱铺出一条简单的传送带路径，看着第一只彩色板条箱咔哒咔哒穿过车间。

随着订单变得更复杂，玩家放下分流器来拆分材料流，摆放不同类型的机器把输入转化成中间品或成品，并重新布置传送带以避免冲突。车间填满了动感——小图标沿着传送带滑行，机器在加工时一下一下地脉动，分流器忽左忽右地拨动。设计良好的生产线嗡嗡运转；规划糟糕的生产线则积压堵塞、警告闪烁。

在两轮之间，或者现金允许时，玩家会进入升级画面来提升传送带速度、解锁新的机器配方，或扩充存储容量。这些选择决定了接下来能接哪些订单。最终班次结束，一个结算画面清点已完成的订单、错过的截止期限和赚到的金币，并提供重试或返回标题画面的选项。

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

