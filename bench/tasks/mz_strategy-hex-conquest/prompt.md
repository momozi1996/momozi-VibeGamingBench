# Hex Conquest

Build **Hex Conquest**, a **turn-based hex-grid conquest strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

Two factions clash over a hex-tiled continent shrouded in fog. Each turn the
player spends income from captured cities to recruit units, moves armies across
terrain that shapes every engagement, and pushes the fog back tile by tile. The
tension lives in incomplete information: the enemy builds behind the fog, and
every advance risks stumbling into a prepared defense. Victory demands balancing
expansion for income against consolidation for defense, reading the map's
chokepoints, and timing a decisive strike before the opponent's economy
outpaces yours.

## What the Player Experiences

From the title screen the player picks a faction — each has a distinct roster
and economic bonus that shapes early strategy. The map generates with cities,
forests, mountains, and plains on a hex grid, fog covering everything beyond
the player's starting territory.

Each turn has clear phases: collect income from owned cities, recruit units at
cities, move units across hexes, and attack adjacent enemies. Terrain matters —
forests slow movement, mountains block it, rivers cost extra to cross. Units
have types: infantry hold ground cheaply, cavalry strike fast, and siege units
crack fortified cities.

Fog lifts only around the player's units, so scouting is a real investment.
The AI opponent expands, builds, and attacks with its own strategy. Capturing
a city flips its income to the conqueror and pushes the front line forward.

The game ends when one faction controls all cities or destroys the enemy's last
unit. A styled result screen shows the outcome with territory statistics and
offers a rematch.

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

# 六边形征服（Hex Conquest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Hex Conquest**，一款**回合制六边形格征服策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两个阵营为一片笼罩在迷雾中的六边形图块大陆而交战。每回合玩家用占领城市带来的收入招募单位，让军队穿越塑造每一场交战的地形，并一格一格地把迷雾推开。张力活在不完整的信息里：敌人在迷雾背后发展，而每一次推进都有可能撞上一处早有准备的防线。胜利要求在"扩张换收入"与"收缩固防守"之间取得平衡，读懂地图上的咽喉要地，并在对手的经济反超之前发动决定性一击。

## 玩家体验流程

玩家从标题画面挑选一个阵营——每个阵营都有独特的单位阵容与经济加成，会塑造前期策略。地图会在六边形格上生成城市、森林、山脉与平原，迷雾覆盖玩家起始领土之外的一切。

每个回合都有清晰的阶段：从己方城市收取收入、在城市招募单位、让单位跨越六边形格移动、以及攻击相邻的敌人。地形至关重要——森林减缓移动，山脉阻断移动，河流需要额外代价才能渡过。单位分为不同类型：步兵以低成本据守阵地，骑兵快速突击，攻城单位则用于攻破设防城市。

迷雾只在玩家单位周围散开，因此侦察是一项实打实的投入。AI 对手会按自己的策略扩张、建设与进攻。攻下一座城市会把它的收入转给征服者，并把前线向前推进。

当一方控制所有城市或消灭敌方最后一个单位时，游戏结束。一个精心设计的结算画面会展示结果与领土统计数据，并提供再战一局的选项。

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

