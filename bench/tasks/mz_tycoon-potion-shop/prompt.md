# Potion Shop

Build **Potion Shop**, an **alchemy shop management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player runs a fantasy apothecary, brewing potions from gathered ingredients
and selling them to customers with specific ailments. The core loop is
recipe-driven: combine ingredients at a cauldron following discovered recipes,
stock shelves with the results, and set prices that balance profit against
customer satisfaction. Customers arrive with visible symptoms — a coughing
knight, a cursed merchant, a poisoned child — and buy the potion that matches
their need. The tension is inventory management: rare ingredients run out,
popular potions sell faster than they can be brewed, and a shop with empty
shelves loses reputation. The tone is cozy-magical: bubbling cauldrons, glowing
vials, and a cluttered shop full of character.

## What the Player Experiences

From the title screen the player opens their shop for the day. The shop view
shows shelves, a cauldron, an ingredient cabinet, and a counter where customers
queue. The day cycle drives the rhythm: morning for brewing, afternoon for
selling, evening for restocking.

Brewing happens at the cauldron: the player selects ingredients from their
cabinet and combines them. Known recipes show the required ingredients; new
recipes can be discovered by experimentation. Each potion has a type (healing,
curing, buffing) and quality level based on ingredient freshness and correct
procedure.

Customers enter with visible ailments shown as icons. They browse shelves and
buy matching potions at the set price. Happy customers return and spread word;
unhappy ones (wrong potion, too expensive, out of stock) leave bad reviews
that reduce foot traffic.

Gold earned buys ingredient restocks from a supplier menu, shop upgrades
(larger shelves, faster cauldron, ingredient garden), and recipe books that
unlock advanced potions. The game tracks gold, reputation, and days operated.
A styled result screen shows shop statistics at the end of each week.

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

# 魔药店（Potion Shop）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Potion Shop**，一款**炼金药店管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一家奇幻药铺，用采集来的材料调制魔药，卖给患有特定病症的顾客。核心循环由配方驱动：在坩锅前按照已发现的配方组合材料，把成品摆上货架，并设定在利润与顾客满意度之间取得平衡的价格。顾客带着可见的症状上门——咳嗽的骑士、被诅咒的商人、中毒的孩子——并买下与自己需求相符的魔药。张力在于库存管理：稀有材料会用尽，热销魔药卖得比能调制出来的更快，而货架空空的店铺会流失声誉。整体基调是惬意而魔幻的：咕嘟作响的坩锅、发光的药瓶，以及一间堆满趣味细节的店铺。

## 玩家体验流程

玩家从标题画面开始，为这一天开门营业。店铺视图展示货架、一口坩锅、一个材料柜，以及顾客排队的柜台。日循环驱动着节奏：上午调制，下午售卖，晚上补货。

调制在坩锅前进行：玩家从材料柜中选取材料并加以组合。已知配方会显示所需材料；新配方可以通过实验来发现。每瓶魔药都有类型（治疗、解除、增益）和品质等级，取决于材料新鲜度与操作是否正确。

顾客进店时带着以图标显示的可见病症。他们会浏览货架，并按设定的价格买走相符的魔药。满意的顾客会回头并口口相传；不满意的顾客（拿错魔药、太贵、缺货）会留下差评，从而减少客流。

赚来的金币可用于从供应商菜单补充材料、店铺升级（更大的货架、更快的坩锅、材料园圃），以及解锁高级魔药的配方书。游戏会记录金币、声誉和营业天数。一个经过美术处理的结算画面会在每周结束时展示店铺统计数据。

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

