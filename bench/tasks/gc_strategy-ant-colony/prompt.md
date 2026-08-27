# Ant Colony

Build **Ant Colony**, a **top-down ant colony management strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player commands an ant colony from above, directing workers to dig tunnels,
gather food, tend larvae, and defend against invaders. The colony is a living
organism: ants need roles assigned, tunnels need planning for efficient flow,
and the food stockpile determines how many mouths can be fed. The tension comes
from competing priorities — every ant digging is an ant not foraging, every
tunnel extended is a new front to defend. Seasons change the surface: summer
brings abundant food but also predators; winter cuts supply lines and forces
the colony to survive on reserves. The fantasy is being the invisible mind of
the hive, orchestrating thousands of tiny decisions into a thriving
underground civilization.

## What the Player Experiences

From the title screen the player starts a new colony. The view shows a
cross-section of earth with the surface above and soil below. The queen sits
in a starting chamber and the player directs initial workers to dig outward.

Digging creates tunnels and chambers. The player designates chamber roles:
nurseries hatch eggs faster, food stores prevent spoilage, barracks train
soldiers. Workers are assigned roles by dragging them to task zones — foragers
go to the surface, diggers extend tunnels, nurses tend larvae, soldiers patrol
entrances.

Food appears on the surface as scattered resources. Foragers carry it back
along tunnel routes — shorter, wider paths mean faster delivery. The colony
grows as the queen produces eggs that hatch into new ants, but each ant
consumes food daily. Overexpansion without food income starves the colony.

Threats arrive periodically: rival insects invade through tunnel entrances,
rain floods shallow tunnels, and winter freezes surface food. The player must
balance growth against defense and plan tunnel depth for flood resistance.

The game tracks colony population and days survived. A styled result screen
shows colony statistics when the queen dies or a survival milestone is reached.

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

# 蚁群帝国（Ant Colony）

在 `/workspace/game/` 用 Godot 4 开发 **Ant Colony**，一款**俯视视角的蚁群经营策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家从高空俯瞰指挥一整个蚁群，指派工蚁挖掘隧道、采集食物、照料幼虫、抵御入侵者。蚁群是一个活的有机体：蚂蚁需要分配职责，隧道需要规划以保证流转效率，而食物储备决定了能养活多少张嘴。张力来自互相竞争的优先级——每一只在挖土的蚂蚁就是一只没在觅食的蚂蚁，每一条延伸出去的隧道都是一条新的防线。季节会改变地表：夏季食物充沛但捕食者也多；冬季则切断补给线，迫使蚁群靠存粮度日。核心幻想是成为蜂巢式群体的隐形大脑，把成千上万个微小决策编排成一个繁盛的地下文明。

## 玩家体验流程

玩家从标题画面开始一个新蚁群。视图呈现一幅大地剖面，上方是地表，下方是土壤。蚁后位于起始巢室中，玩家指挥最初的工蚁向外挖掘。

挖掘会形成隧道与巢室。玩家为巢室指定用途：育婴室让虫卵孵化更快，粮仓防止食物腐坏，兵营训练兵蚁。通过把蚂蚁拖到任务区域来分配职责——觅食蚁前往地表，挖掘蚁延伸隧道，护理蚁照料幼虫，兵蚁巡守出入口。

食物以零散资源的形式出现在地表。觅食蚁沿隧道路线把食物搬回——路径越短越宽，运送就越快。蚁后产卵孵化出新蚂蚁，蚁群随之壮大，但每只蚂蚁每天都要消耗食物。食物收入跟不上却过度扩张，蚁群就会饿死。

威胁会周期性到来：敌对昆虫从隧道入口入侵，雨水淹没浅层隧道，冬季冻结地表食物。玩家必须在扩张与防御之间取得平衡，并规划隧道深度以抵抗洪水。

游戏会记录蚁群人口与存活天数。当蚁后死亡或达成某个生存里程碑时，一个精心设计的结算画面会展示蚁群统计数据。

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

