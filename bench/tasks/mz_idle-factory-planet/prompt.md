# Idle Factory Planet

Build an **Idle Factory Planet** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player places machines on a planet surface that automatically produce
resources, chains production lines together, and researches upgrades until the
planet is depleted — then prestiges to a new planet with better technology. The
fantasy is industrial scale: watching conveyor belts carry ore to smelters to
fabricators, output numbers climbing exponentially, and the planet surface
filling with an intricate factory network. The idle loop runs production
continuously; the player optimises layouts and unlocks new machine types.

## What the Player Experiences

1. **Title Screen** — A small planet covered in tiny factories with conveyor
   belts, the game name in industrial stencil font, and a play button shaped
   like a gear.
2. **Planet Surface** — A top-down grid representing the planet surface. The
   player places machines on tiles. Conveyor belts connect machines visually,
   showing resources flowing between them.
3. **Machine Placement** — Machines include: miners (extract raw ore), smelters
   (ore to metal), fabricators (metal to parts), and sellers (parts to credits).
   Each machine auto-produces when supplied. The player drags machines from a
   panel onto the grid.
4. **Production Chains** — Machines must be connected in sequence. Output from
   one feeds input of the next via conveyor. Longer chains produce more valuable
   goods. A production rate display shows throughput.
5. **Research** — Credits fund research that unlocks better machines: faster
   miners, multi-input fabricators, and storage buffers. A tech tree shows
   available upgrades with costs and effects.
6. **Planet Depletion** — The planet has finite resources. A depletion meter
   shows remaining ore. As resources thin, miners slow down. When depleted, the
   player must prestige.
7. **Prestige (New Planet)** — Prestiging moves to a fresh planet with more
   resources. The player keeps research progress and gains a permanent production
   multiplier. Each new planet starts faster and scales higher.

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

# 放置工厂星球（Idle Factory Planet）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置工厂星球**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在星球表面放置能自动生产资源的机器，把生产线串联起来，研究各种升级，
直到这颗星球被开采枯竭——然后转生到一颗新星球，带着更好的科技重新开始。
游戏的幻想核心是工业级的规模感：看着传送带把矿石送往冶炼厂、再送往加工厂，
产出数字指数级攀升，星球表面被一张精密的工厂网络逐渐填满。放置循环让生产
持续进行；玩家则优化布局并解锁新的机器类型。

## 玩家体验流程

1. **标题画面** —— 一颗被密布传送带的小型工厂覆盖的行星，游戏名采用工业模板
   字体，还有一个齿轮形状的开始按钮。
2. **星球表面** —— 一个代表星球表面的俯视网格。玩家在图块上放置机器。传送带
   在视觉上把机器连接起来，展示资源在它们之间流动。
3. **机器放置** —— 机器包括：采矿机（开采原矿）、冶炼厂（矿石转金属）、
   加工厂（金属转零件）和售卖站（零件转信用点）。每台机器在有供料时都会自动
   生产。玩家从一个面板中把机器拖到网格上。
4. **生产链** —— 机器必须按顺序连接。前一台的产出通过传送带送入下一台的输入。
   更长的生产链能产出更值钱的货物。一个生产速率显示会给出吞吐量。
5. **研究** —— 信用点用于资助研究，从而解锁更好的机器：更快的采矿机、多输入
   加工厂和存储缓冲区。一棵科技树展示可用的升级及其成本与效果。
6. **星球枯竭** —— 星球的资源是有限的。一个枯竭量表显示剩余矿石。资源变稀薄
   时，采矿机会变慢。资源枯竭后，玩家必须转生。
7. **转生（新星球）** —— 转生会前往一颗资源更丰富的新星球。玩家保留研究进度，
   并获得一个永久的生产倍率。每颗新星球起步更快、上限更高。

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

