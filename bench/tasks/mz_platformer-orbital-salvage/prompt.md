# Orbital Salvage

Build **Orbital Salvage**, a compact 2D space-salvage physics game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a polished micro-game about piloting a small tug through
orbital debris, latching onto wreckage with a tractor beam, and hauling it back
to a recovery station before fuel runs dry or hazards tear the payload loose.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a salvage pilot working the edge of a debris belt. The tug does
not stop on a dime — it drifts, coasts, and fights momentum every time the
thrusters fire. Attaching a tractor beam to a chunk of wreckage changes
everything: heavier salvage drags the tug off course, volatile pieces threaten
to rupture, and the route back to the station threads between gravity wells,
drifting mines, and radiation arcs. The decision space lives in choosing which
contract to accept, which salvage to grab first, how aggressively to burn fuel,
and whether to risk a shortcut through a hazard corridor for a bigger payout.
Between runs the player reinvests credits into thrust power, beam strength, or
hull plating, shaping how the next contract feels. The tone is tense and
industrial — a blue-collar space job where physics is the real antagonist.

## What the Player Experiences

A styled title screen sets the mood: the game name over a starfield with
drifting debris silhouettes, a tug outline, and a clear way to begin.

The player picks a contract from a board showing salvage type, estimated mass,
payout, and hazard warnings. The tug launches into a 2D orbital field where
inertia is king — tapping thrust accelerates, releasing it lets the ship coast,
and reversing burns fuel fast. Salvage floats among asteroid chunks and hazard
zones. The player maneuvers close, fires the tractor beam, and feels the tug
lurch as the mass latches on. Towing a heavy reactor core is nothing like
dragging a light panel — the ship wallows, turns wide, and fuel burns faster.

Hazards punctuate the route: gravity wells bend the flight path, mines detonate
if clipped, radiation arcs pulse warnings before firing. The player reads the
field, plans a line, and commits — or cuts the beam and abandons the payload to
save the tug. Delivering salvage to the station awards credits and advances the
contract. A result screen tallies earnings, fuel spent, hull damage, and offers
the next contract or a return to title.

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

# 轨道打捞（Orbital Salvage）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Orbital Salvage**，一款小巧的 2D 太空打捞物理游戏：这是一款打磨精良的微型游戏，讲述驾驶一艘小型拖船穿越轨道碎片、用牵引光束扣住残骸，并在燃料耗尽或危险物把载荷撕脱之前把它拖回回收站。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名在碎片带边缘作业的打捞飞行员。拖船不会说停就停——它会漂移、惯性滑行，每次点燃推进器都要与动量搏斗。把牵引光束接到一块残骸上会改变一切：更重的打捞物会把拖船拽偏航线，不稳定的残片有炸裂的危险，而返回空间站的航线要在引力井、漂移的水雷和辐射弧之间穿行。决策空间就在于选择接哪份合约、先抓哪块打捞物、烧燃料时多激进，以及是否为更高报酬冒险走一条穿过危险走廊的近道。轮次之间，玩家把积分重新投入到推力、光束强度或船体装甲上，从而塑造下一份合约的手感。整体调性紧张而工业——一份蓝领的太空工作，而物理才是真正的对手。

## 玩家体验流程

一个经过设计的标题画面奠定气氛：游戏名压在一片星空上，背景有漂移的碎片剪影和一道拖船轮廓，以及一个明确的开始入口。

玩家从一块任务板上挑选合约，板上显示打捞物类型、估算质量、报酬和危险警告。拖船升空进入一片 2D 轨道场域，那里惯性称王——轻点推进会加速，松手让船惯性滑行，而反向制动会飞快烧掉燃料。打捞物漂浮在小行星碎块和危险区之间。玩家机动靠近，发射牵引光束，感受到质量扣上时拖船的一顿。拖一枚沉重的反应堆核心和拖一块轻薄的面板完全不同——船会摇晃、转向半径变大，燃料也烧得更快。

危险物为整条航线打上标点：引力井会弯折飞行路径，水雷一旦擦碰就引爆，辐射弧则在放射前脉动出警告。玩家读场势、规划一条线路并全力投入——或者切断光束、放弃载荷以保住拖船。把打捞物送达空间站会奖励积分并推进合约。结算画面清点收入、燃料消耗和船体损伤，并提供下一份合约或返回标题的选项。

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

