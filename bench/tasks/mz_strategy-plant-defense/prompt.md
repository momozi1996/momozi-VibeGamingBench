# Plant Defense

Build **Plant Defense**, a **lane-based tower defense strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A garden grid stands between a homestead and waves of encroaching creatures.
The player plants defenders on a multi-lane lawn, spending sunlight that must
be actively collected. Each plant type fills a tactical role — some shoot, some
block, some generate economy — and the creatures come in varieties that punish
a one-note defense. The tension is resource scarcity: sunlight arrives slowly,
plants cost real economy, and a misplaced defender means a lane falls before
reinforcements grow. An adventure map connects levels with escalating challenge
and new plant unlocks, giving the player a reason to master each tool before
the next threat arrives.

## What the Player Experiences

From the title screen the player enters an adventure map showing a trail of
levels. Selecting a level shows the upcoming creature types and lets the player
pick a loadout of plant defenders from their unlocked roster.

The level plays on a grid of lanes. Sunlight drops periodically and the player
clicks to collect it, building a resource pool. Plants are dragged from a
toolbar onto empty grid cells, each costing sunlight. Shooters fire
projectiles down their lane, walls absorb hits, and sun-producers accelerate
the economy. Creatures march from the right edge in waves, each lane
independent.

Creature variety forces adaptation: armored types shrug off weak shots, fast
types outrun slow-firing plants, and flying types bypass ground walls. Later
levels introduce night conditions where sun production drops, forcing the
player to rely on alternative economy plants.

A level is won when all waves are defeated; lost when any creature reaches the
left edge. Victory unlocks the next map node and sometimes a new plant type.
The result screen shows stars earned and the map updates visibly.

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

# 植物防御（Plant Defense）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Plant Defense**，一款**分路塔防策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一座花园网格横亘在家园与一波波逼近的生物之间。玩家在多路草坪上种下防御者，花费必须主动收集的阳光。每种植物都承担一项战术职责——有的射击，有的阻挡，有的产出经济——而来袭生物的种类会惩罚单一路数的防守。张力在于资源稀缺：阳光来得很慢，植物要消耗真金白银的经济，而一个放错位置的防御者就意味着某一路在援兵长成之前先被攻破。一张冒险地图把关卡串联起来，挑战逐级升级并解锁新植物，让玩家有理由在下一个威胁到来前先掌握好每一件工具。

## 玩家体验流程

玩家从标题画面进入一张呈现关卡路径的冒险地图。选择一个关卡后，会显示即将出现的生物类型，并让玩家从已解锁的阵容中挑选一套植物防御者配置。

关卡在多路网格上进行。阳光会周期性落下，玩家点击收集，积累资源池。植物从工具栏拖到空的网格格子上，每株都要消耗阳光。射手向本路发射弹丸，墙体吸收伤害，产阳光的植物则加速经济。生物成波从右侧边缘进军，各路彼此独立。

生物的多样性迫使玩家随时调整：带甲类型对弱小射击不痛不痒，高速类型能跑过射速慢的植物，飞行类型则绕过地面墙体。后期关卡引入夜间条件，阳光产出下降，迫使玩家依赖替代性的经济植物。

击败所有波次即通关；任何生物到达左侧边缘则失败。胜利会解锁下一个地图节点，有时还会解锁一种新植物。结算画面会展示获得的星数，地图也会有明显更新。

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

