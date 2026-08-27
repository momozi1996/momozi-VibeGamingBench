# Garden Ecosystem Keeper

Build **Garden Ecosystem Keeper**, a compact **ecosystem gardening management
game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

The player tends a small restoration garden where every tile is part of a living
web. Plants compete for moisture and light, pollinators follow bloom corridors,
pests exploit monoculture, and weather shifts the whole balance overnight. The
core tension is stewardship under scarcity: limited actions per turn, finite
water, unpredictable seasons, and biodiversity goals that punish brute-force
planting. A thriving garden is one the player composed, not one they clicked
into existence.

The tone is gentle but systemic — readable beds, seed packets, pollinator
trails, pest warnings, seasonal color shifts, and clear biodiversity meters.
The garden should feel alive and authored, not a raw grid of colored squares.

## What the Player Experiences

The player opens to a garden restoration scene and chooses a plot to tend. The
first planting is simple: a few seed types, moist soil, calm weather. Plants
grow visibly over turns, and the player learns the rhythm of water, wait,
harvest.

Soon the ecosystem asserts itself. A pollinator visits one flower bed but
ignores another. A pest cluster appears near a monoculture row. Companion
planting hints emerge — herbs near tomatoes deter aphids, wildflowers draw
bees toward fruit trees. The player starts composing beds rather than filling
them.

Weather and seasons raise the stakes. A dry spell forces triage: which beds
get the last water? An early frost threatens unprotected seedlings. A rainy
season floods low tiles but lets the pond habitat flourish. The player adapts
their plan each turn, balancing short-term survival against long-term
biodiversity targets.

Late game, the garden is a dense web of interactions. The player manages
pollinator corridors, pest barriers, moisture zones, and seasonal rotations.
When the restoration goal is met — a target biodiversity score, a bloom
festival, or a full habitat chain — the result screen reflects the garden's
health and composition. Failure shows what collapsed and why, inviting a
different strategy next time.

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

# 花园生态守护者（Garden Ecosystem Keeper）

在 `/workspace/game/` 用 Godot 4 开发 **Garden Ecosystem Keeper**，一款小体量的**生态园艺管理**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家照料一座小小的修复型花园，其中每一块图块都是一张活网络的一部分。植物争夺水分与光照，传粉者沿着花期走廊移动，害虫钻单一栽培的空子，而天气会在一夜之间改变整个平衡。核心张力是稀缺条件下的看护经营：每回合行动次数有限、水量有限、季节难以预料，还有会惩罚蛮力种植的生物多样性目标。兴旺的花园是玩家谱写出来的，而不是点几下就点出来的。

整体基调温和却有系统感——可读的花床、种子包、传粉者轨迹、害虫警告、随季节变化的色调，以及清晰的生物多样性计量表。花园应当显得鲜活且经过设计，而不是一片彩色方块的原始网格。

## 玩家体验流程

玩家一进入游戏，看到的是一处花园修复场景，并选择一块要照料的园地。第一次种植很简单：几种种子、湿润的土壤、平静的天气。植物在一回合回合中可见地生长，玩家学会浇水、等待、收获的节奏。

很快，生态系统开始显露自己的意志。传粉者造访了某一处花床，却无视了另一处。单一栽培的那一行附近出现了害虫聚集。伴生种植的线索逐渐浮现——番茄旁的香草能驱除蚜虫，野花能把蜜蜂引向果树。玩家开始谱写花床，而不只是把它们填满。

天气与季节抬高了赌注。一场干旱迫使玩家分诊：最后那点水给哪些花床？一次早霜威胁着没有防护的幼苗。多雨的季节淹没低洼图块，却让池塘栖息地繁荣起来。玩家每一回合都在调整自己的计划，在短期存活与长期生物多样性目标之间寻求平衡。

到了后期，花园成为一张交互密织的网。玩家要管理传粉者走廊、害虫屏障、湿度区域和季节轮作。当修复目标达成——某个目标生物多样性分数、一场花期庆典，或是一条完整的栖息地链条——结算画面会反映花园的健康状况与构成。失败时则展示是什么崩溃了、为什么崩溃，邀请玩家下次换一种策略。

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

