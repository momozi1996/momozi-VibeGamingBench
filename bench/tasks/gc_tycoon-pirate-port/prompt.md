# Pirate Port

Build **Pirate Port**, a **pirate haven management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player builds a hidden pirate port on a tropical island, attracting crews
with taverns and docks, sending them on raids for plunder, and defending
against the royal navy when notoriety grows too high. The economy loops through
three currencies: gold from raids funds buildings, reputation attracts better
crews, and notoriety draws navy attention. The tension is that the most
profitable actions raise notoriety fastest, forcing the player to balance
aggression against defense preparation. The tone is swashbuckling Caribbean:
palm trees, rickety docks, rum barrels, and cannon smoke.

## What the Player Experiences

From the title screen the player starts a new port. The view shows a coastal
island with a grid for building. The player constructs docks to berth ships,
taverns to attract pirate crews, warehouses to store plunder, and defenses
(walls, cannons, watchtowers) to repel navy raids.

Pirate crews arrive based on the port's reputation. Each crew has a ship type,
combat strength, and upkeep cost. The player sends crews on raids by selecting
a target from a map of trade routes — richer targets yield more gold but raise
notoriety higher. Raids play out automatically with a result summary.

Gold funds expansion: better docks attract larger ships, upgraded taverns keep
crews happy, and a shipyard allows repairing and upgrading vessels. Crew morale
depends on tavern quality, raid success, and pay.

When notoriety reaches thresholds, the navy attacks. Navy raids are tower-
defense encounters where the port's cannons and walls must hold against
incoming warships. Surviving a raid lowers notoriety slightly; failing means
losing buildings and crews.

The game tracks gold, fleet size, and raids completed. A styled result screen
shows port statistics when the port falls or reaches a prosperity milestone.

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

# 海盗港（Pirate Port）

在 `/workspace/game/` 用 Godot 4 开发 **Pirate Port**，一款**海盗巢穴管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一座热带岛屿上营建一处隐秘的海盗港，用酒馆和码头吸引船队，派他们出海掠夺战利品，并在恶名太盛时抵御皇家海军。经济在三种货币之间循环：掠夺得来的金币资助建筑，声望吸引更好的船队，恶名则招来海军的注意。张力在于最赚钱的行动同时也让恶名涨得最快，迫使玩家在进攻性与防御准备之间求平衡。整体基调是加勒比式的冒险豪情：棕榈树、摇摇晃晃的码头、朗姆酒桶和炮火硝烟。

## 玩家体验流程

玩家从标题画面开始经营一座新的港口。视图展示一座沿海岛屿，附带用于建造的网格。玩家建造码头来停泊船只、酒馆来吸引海盗船队、仓库来存放战利品，以及防御设施（城墙、火炮、瞭望塔）来击退海军的进袭。

海盗船队会依据港口的声望前来。每支船队都有船型、战斗强度和维持成本。玩家从一张贸易航线地图上选定目标，派出船队去掠夺——目标越富庶，产出的金币越多，但恶名也涨得越高。掠夺过程自动推演，并给出一份结果摘要。

金币资助扩张：更好的码头能吸引更大的船，升级过的酒馆让船队保持愉快，而一座船坞则允许修理和升级船只。船队士气取决于酒馆品质、掠夺成果和报酬。

当恶名达到阈值时，海军会来进攻。海军进袭是塔防式的遭遇战，港口的火炮和城墙必须顶住来袭的战舰。挺过一次进袭会让恶名略微下降；失败则意味着损失建筑和船队。

游戏会记录金币、舰队规模和已完成的掠夺次数。当港口陷落或达成某个繁荣里程碑时，一个经过美术处理的结算画面会展示港口统计数据。

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

