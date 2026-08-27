# Space Station

Build **Space Station**, a 2D space station management simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is commanding a remote space station, balancing crew morale, system
maintenance, and resource management while random events — from meteor showers
to pirate raids — threaten to unravel everything. The interesting tension is
crew assignment: each crew member has skills and fatigue, and every system needs
someone manning it. Assigning the engineer to weapons during a pirate attack
means nobody is fixing the leaking oxygen recycler. Power generation limits how
many systems can run simultaneously, forcing hard choices about what to keep
online. The station grows module by module, but each new module is another system
that can break, another mouth to feed, another vulnerability.

## What the Player Experiences

The player opens to a starfield title screen with the station silhouette, then
enters the station overview. The view shows a cross-section of connected modules:
bridge, life support, power core, crew quarters, cargo bay, and docking port.
Each module has status indicators for power, integrity, and staffing. Crew
portraits line the bottom with skill icons and fatigue bars.

The player assigns crew to modules by dragging portraits, manages power
distribution through a allocation panel, and responds to events via choice
dialogs. Random events fire periodically: supply ships offer trades, distress
signals present rescue-or-ignore dilemmas, system malfunctions require immediate
crew response, and pirate attacks demand weapons be manned and shields powered.
Between event cycles the player can build new modules using accumulated
resources, research upgrades, or rest crew. The game spans 30+ cycles with
escalating event severity. A game-over triggers if life support fails or all
crew are incapacitated. Victory requires surviving a set number of cycles with
the station intact.

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

# 太空站（Space Station）

在 `/workspace/game/` 用 Godot 4 开发 **Space Station**，一款 2D 太空站经营模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是指挥一座偏远的太空站，在船员士气、系统维护与资源管理之间取得平衡，
同时从流星雨到海盗突袭的各种随机事件都在试图让一切崩解。有趣的张力来自船员
派工：每名船员都有技能与疲劳度，而每个系统都需要有人值守。在海盗袭击时把工程师
派去操作武器，就意味着没人去修那台漏气的氧气循环机。发电量限制了能同时运行的
系统数量，迫使玩家在保留哪些系统在线上做出艰难抉择。太空站会一个个模块地扩张，
但每个新模块都是又一个会坏掉的系统、又一张要喂的嘴、又一处脆弱点。

## 玩家体验流程

玩家进入游戏时看到一个星空标题画面，上有太空站的剪影，随后进入太空站总览。
视图展示互连模块的剖面：舰桥、生命维持、动力核心、船员舱、货舱和对接口。每个
模块都有电力、结构完整度与人员配置的状态指示。船员头像排列在底部，带有技能
图标与疲劳条。

玩家通过拖动头像把船员派到各模块，通过一个分配面板管理电力分配，并通过选择
对话响应事件。随机事件会定期触发：补给船提出交易、求救信号带来救与不救的
两难、系统故障要求船员立刻响应，而海盗袭击则要求武器有人值守、护盾通电。
事件周期之间，玩家可以用积累的资源建造新模块、研究升级，或让船员休息。游戏
横跨 30 个以上周期，事件严重度逐步升级。如果生命维持失效或全体船员失去行动
能力，则触发游戏结束。胜利要求在太空站保持完好的前提下存活满设定的周期数。

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

