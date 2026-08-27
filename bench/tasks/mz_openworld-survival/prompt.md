# Open-World Survival

Build a **2D open-world survival game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player awakens alone in a wilderness and must gather resources, craft tools,
build shelter, and survive the night. The fantasy is **self-reliance under
pressure** -- every decision matters because daylight is finite, hunger is
constant, and the world turns hostile after dark. The interesting tension is
choosing what to prioritize: food now or tools for later, exploration or
fortification, risk or safety. Temperature drops, visibility shrinks, and
survival depends on preparation. The art style should feel **earthy, raw, and
immersive** -- think *Don't Starve* meets *A Short Hike* at a smaller scale.

## What the Player Experiences

1. **Title Screen** -- A stylised opening with the game name, a play button, and
   a wilderness backdrop (forest, campsite, or mountain vista). No naked HTML 引擎
   grey.

2. **The Wilderness** -- The player spawns in an open-world map with multiple
   visually distinct biomes: grassy plains, dense forest, and rocky terrain or
   water. The player moves freely in 8 directions across a large explorable
   space.

3. **Resource Gathering** -- Scattered across the map are interactable resources:
   trees for wood, stone outcrops for stone, and berry bushes for food. The
   player approaches a resource and interacts to gather it, with visible feedback
   (animation, particle effect, or resource disappearing).

4. **Survival Metrics** -- Status bars are always visible (hunger, thirst, or
   temperature). They drain over time. When a bar hits critical levels, the
   player suffers consequences: slowed movement, screen vignette, health loss, or
   other visible penalties.

5. **Crafting** -- A crafting panel shows available recipes that consume gathered
   materials. Recipes produce useful items: a campfire for warmth, a shelter for
   protection, an axe for faster gathering. The player sees what they can and
   cannot afford to build.

6. **Building and Placement** -- Crafted structures can be placed into the world
   as persistent objects. A campfire provides warmth and light. A shelter
   restores health or blocks environmental damage. Placement has clear visual
   indicators.

7. **Day-Night Cycle** -- Time passes automatically. Day is bright and safe.
   Night darkens the map, shrinks visibility, and accelerates survival drain.
   Being near a campfire at night extends the player's safe radius. Surviving a
   full day-night cycle is the minimal success condition.

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

# 开放世界生存（Open-World Survival）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界生存游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一片荒野中孤身醒来，必须采集资源、制作工具、搭建庇护所，并活过夜晚。
这里的幻想是**压力之下的自力更生**——每一个决定都很重要，因为白昼有限、饥饿
不止，而世界在天黑之后变得充满敌意。有趣的张力在于优先级的取舍：是现在就找
食物还是为以后做工具，是探索还是加固，是冒险还是求稳。气温下降，视野收窄，
生存取决于准备。美术风格应当给人**质朴、粗糙、有沉浸感**的观感——可以想象成
小体量的 *Don't Starve* 结合 *A Short Hike*。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮，以及一幅
   荒野背景（森林、营地或山景）。不要出现 HTML 引擎 的裸灰色。

2. **荒野** —— 玩家出生在一张开放世界地图上，其中有多个视觉上截然不同的生态区：
   青草平原、茂密森林，以及多岩地形或水域。玩家可以在一片广阔的可探索空间中
   沿 8 个方向自由移动。

3. **资源采集** —— 地图上散布着可交互的资源：可获取木材的树、可获取石料的
   岩石露头，以及可获取食物的浆果丛。玩家靠近资源并交互即可采集，并伴有可见的
   反馈（动画、粒子效果，或资源本身消失）。

4. **生存数值** —— 状态条始终可见（饥饿、口渴或体温）。它们随时间下降。当某条
   状态条降到临界水平时，玩家会承受后果：移动变慢、屏幕暗角、生命值流失，
   或其他可见的惩罚。

5. **制作** —— 一个制作面板显示可用的配方，它们会消耗采集到的材料。配方产出
   有用的物品：取暖用的营火、提供保护的庇护所、加快采集的斧头。玩家能看到
   哪些可以造、哪些资源还不够。

6. **建造与放置** —— 制作出的建筑可以作为持久对象放置到世界中。营火提供温暖
   和光亮。庇护所可恢复生命值或阻挡环境伤害。放置时有清晰的视觉指示。

7. **昼夜循环** —— 时间自动流逝。白天明亮而安全。夜晚使地图变暗、视野收窄，
   并加快生存数值的消耗。夜间待在营火附近可以扩大玩家的安全半径。活过一个
   完整的昼夜循环是最低的成功条件。

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

