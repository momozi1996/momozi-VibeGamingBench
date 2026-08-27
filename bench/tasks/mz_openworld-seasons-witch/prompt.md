# Open-World Seasons Witch

Build an **Open-World Seasons Witch** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a witch who controls the seasons in a small valley, shifting between
spring, summer, autumn, and winter to solve problems and help villagers. The
fantasy is elemental mastery: freezing a river to cross it, blooming flowers to
attract bees for honey, melting snow to reveal buried items, or withering vines
blocking a path. Tension comes from villager requests that require specific
seasonal combinations and potion ingredients that only grow in certain seasons.
Each season transforms the entire world visually and mechanically.

## What the Player Experiences

1. **Title Screen** — A four-panel title showing the same valley in each season,
   with the game name in flowing script. A play button surrounded by seasonal
   icons.
2. **The Valley** — The player moves freely through a valley with a village,
   forest, lake, mountain path, and farmland. The entire world changes appearance
   based on the active season.
3. **Season Switching** — The player can cast a season spell to change the world.
   A radial menu shows four seasons; selecting one triggers a visual transition
   that transforms terrain, water, vegetation, and sky colour.
4. **World Reactions** — Each season has mechanical effects: winter freezes water
   and reveals ice caves; spring grows plants and fills rivers; summer dries
   swamps and ripens fruit; autumn drops leaves revealing hidden paths and
   weakens wooden structures.
5. **Villager Quests** — NPCs in the village request help that requires seasonal
   manipulation: a farmer needs rain (spring) then sun (summer) for crops; a
   builder needs frozen lake (winter) to transport stone; a healer needs autumn
   mushrooms.
6. **Potion Brewing** — Ingredients gathered in different seasons combine into
   potions at the witch's cottage. Potions grant abilities: speed boost, barrier
   shield, creature charm. A recipe book tracks discovered combinations.
7. **Progression** — Completing quests earns reputation and unlocks new areas of
   the valley. The mountain pass opens after helping enough villagers, revealing
   a final challenge that requires mastery of all four seasons.

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

# 开放世界四季女巫（Open-World Seasons Witch）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界四季女巫（Open-World Seasons Witch）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名掌控着一座小山谷四季的女巫，在春、夏、秋、冬之间切换以解决问题、
帮助村民。这里的幻想是元素掌控：冻结河流以便渡过，让花朵绽放以吸引蜜蜂产蜜，
融化积雪以显露埋藏的物品，或者让挡路的藤蔓枯萎。张力来自村民的委托——它们需要
特定的季节组合，以及只在某些季节生长的药剂材料。每个季节都会在视觉和机制上
彻底改变整个世界。

## 玩家体验流程

1. **标题画面** —— 一个四格标题，分别展示同一座山谷在四个季节中的样貌，游戏
   名称使用流畅的手写体。开始按钮四周环绕着季节图标。
2. **山谷** —— 玩家在一座山谷中自由移动，其中有村庄、森林、湖泊、山路和农田。
   整个世界的外观会随当前季节而变化。
3. **季节切换** —— 玩家可以施放季节法术来改变世界。一个环形菜单显示四个季节；
   选中其中一个会触发一段视觉转场，改变地形、水体、植被和天空的颜色。
4. **世界反应** —— 每个季节都有机制上的效果：冬天冻结水面并显露冰洞；春天使
   植物生长并让河流充盈；夏天使沼泽干涸并让果实成熟；秋天落叶，显露隐藏的
   小径，并削弱木质结构。
5. **村民任务** —— 村中的 NPC 会请求需要操控季节才能完成的帮助：一位农夫的
   作物需要先下雨（春）再有阳光（夏）；一位建造者需要冻结的湖面（冬）来运送
   石料；一位治疗师需要秋天的蘑菇。
6. **药剂调制** —— 在不同季节采集的材料可以在女巫的小屋里调配成药剂。药剂
   赋予各种能力：速度提升、屏障护盾、生物魅惑。一本配方书记录已发现的组合。
7. **进程** —— 完成任务可获得声望并解锁山谷的新区域。帮助足够多的村民后，
   山间隘口会开启，露出一个需要精通全部四个季节才能应对的最终挑战。

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

