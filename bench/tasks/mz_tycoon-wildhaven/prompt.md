# Tycoon: Wildhaven

Build a **multi-industry frontier-economy tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a frontier boss carving a thriving outpost from lakeside
wilderness. The fantasy is juggling multiple industries that share one stretch
of land under a turning seasonal clock — pushing one too hard quietly starves
the others, so the real skill is reading cause-and-effect links and hedging
across production chains as the calendar turns. Seasons reshape what pays and
what stalls, weather and wildlife disrupt the best-laid plans, and reinvesting
earnings visibly transforms the camp from a lonely shack into a humming
operation. The tone is warm but demanding: nature is generous and punishing in
equal measure, and coasting is never an option.

## What the Player Experiences

The player opens a saved camp or starts fresh and sees the outpost spread before
them — forest, cleared land, lake, and a simple ledger of cash and season. Early
on, work is hands-on: fell a tree, plant a row, cast a line. Each action
visibly changes the land and feeds a production chain that turns raw nature into
goods into money.

As earnings accumulate the player reinvests — better tools, new buildings,
expanded capacity — and the outpost grows busier and more capable on the map.
The seasonal clock keeps turning: warm months favor crops, cold months freeze
the lake, timber demand shifts, and no single industry pays year-round. The
player learns to hedge, stockpile, and plan ahead.

Disruptions arrive without warning — storms flatten output, animals raid stores
— and the player adapts or absorbs the loss. Over time the deeper game reveals
itself: industries are interdependent, and overexploiting one degrades the
others. Balanced management visibly beats tunnel-vision. Progress is banked to a
save, so a returning player picks up the same outpost, season, and momentum.

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

# 经营：荒野港湾（Tycoon: Wildhaven）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**多产业边疆经济经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一位边疆老板，要从湖畔荒野中开辟出一座兴旺的哨站。这里的幻想是在一个转动的季节时钟下，同时经营共享同一片土地的多个产业——把其中一个逼得太狠，就会悄悄让其他产业断粮，所以真正的本领在于读懂因果链条，并随着日历推进在各条生产链之间对冲。季节会重塑什么赚钱、什么停滞，天气和野生动物会打乱最周密的计划，而把收益再投资进去会让营地从一间孤零零的棚屋可见地蜕变为一台嗡嗡运转的机器。整体基调温暖却严苛：大自然同样地慷慨与无情，而混日子从来不是一个选项。

## 玩家体验流程

玩家打开已存档的营地或从头开始，看到哨站在眼前铺展开来——森林、开垦地、湖泊，以及一本记着现金与季节的简单账簿。早期的工作是亲力亲为的：砍一棵树、种一垄地、抛一次钓线。每个动作都会可见地改变这片土地，并喂给一条把原始自然变成货物、再变成钱的生产链。

随着收益累积，玩家开始再投资——更好的工具、新的建筑、扩充的产能——哨站在地图上变得更忙碌、更有能力。季节时钟持续转动：温暖的月份适合作物，寒冷的月份冻住湖面，木材需求随之变化，而没有任何单一产业能全年赚钱。玩家学会对冲、囤货和提前规划。

打断毫无预警地到来——风暴压平产出，动物袭击库存——玩家要么适应，要么承受损失。随着时间推移，更深层的游戏显露出来：各产业相互依存，过度开采其中一个会让其他产业退化。均衡的管理会可见地胜过只盯一处的做法。进度会存入存档，因此回来的玩家接手的是同一座哨站、同一个季节、同样的势头。

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

