# Space Colony

Build **Space Colony**, an **asteroid colony management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A small crew lands on a barren asteroid and must build a self-sustaining colony
from nothing. Oxygen, food, and power are the three lifelines — lose any one
and colonists die. The player builds modules on a grid surface: habitats for
living, farms for food, solar arrays for power, and oxygen generators to keep
everyone breathing. Each colonist has needs and a job assignment; idle colonists
consume without producing. The tension is that expansion requires resources
that are already stretched thin, and random meteor strikes can destroy modules
without warning. The fantasy is frontier survival in the void — every new
module is a small victory against the emptiness of space.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
top-down asteroid surface with a grid overlay. The initial lander provides
minimal oxygen, food, and power for a small crew.

The player builds modules by spending materials mined from the asteroid.
Habitats house colonists, farms grow food, solar panels generate power, and
oxygen recyclers keep the air breathable. Each module connects to adjacent
ones, and the colony must maintain positive balance in all three resources or
colonists begin dying.

Colonists are assigned to jobs: miners extract materials, farmers tend crops,
engineers maintain modules, and researchers unlock new building types. Each
colonist has morale affected by living conditions, workload, and whether their
habitat has amenities.

Meteor events strike randomly, damaging or destroying modules. The player must
maintain redundancy and repair capacity. Research unlocks advanced modules:
greenhouses, fusion reactors, shield generators, and deep-mining rigs.

The game tracks population, days survived, and colony rating. A styled result
screen shows colony achievements when the colony is lost or reaches a
population milestone.

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

# 太空殖民地（Space Colony）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Space Colony**，一款**小行星殖民地管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一支小队降落在一颗荒芜的小行星上，必须从零开始建起一座能自给自足的殖民地。氧气、食物和电力是三条生命线——任何一条断掉，殖民者就会死亡。玩家在网格化的表面上建造模块：居住舱供人生活，农场产出食物，太阳能阵列发电，氧气发生器让所有人有气可呼。每位殖民者都有需求和岗位分配；闲置的殖民者只消耗不产出。张力在于扩张需要的资源本就已经捉襟见肘，而随机的流星撞击还会毫无预警地摧毁模块。这里的幻想是在虚空中的边疆求生——每一个新模块都是对太空空虚的一次小小胜利。

## 玩家体验流程

玩家从标题画面开始一座新的殖民地。视图展示一片俯视的小行星表面，叠加着网格。最初的着陆舱只为一支小队提供最低限度的氧气、食物和电力。

玩家花费从小行星上开采的材料来建造模块。居住舱容纳殖民者，农场种植食物，太阳能板发电，氧气回收器让空气可供呼吸。每个模块都与相邻模块连接，且殖民地必须让三种资源都保持正向平衡，否则殖民者会开始死亡。

殖民者被分配到各类岗位：矿工开采材料，农民照料作物，工程师维护模块，研究员解锁新的建筑类型。每位殖民者都有士气，受居住条件、工作负荷，以及其居住舱是否配有便利设施的影响。

流星事件随机来袭，会损坏或摧毁模块。玩家必须维持冗余和维修能力。研究可解锁高级模块：温室、聚变反应堆、护盾发生器和深层采矿钻机。

游戏会记录人口、存活天数和殖民地评级。当殖民地覆灭或达成某个人口里程碑时，一个经过美术处理的结算画面会展示殖民地的成就。

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

