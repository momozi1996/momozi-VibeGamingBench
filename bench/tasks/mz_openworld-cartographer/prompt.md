# Open-World Cartographer

Build an **Open-World Cartographer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a cartographer venturing into unmapped wilderness, drawing the map
as they explore. The fantasy is discovery and mastery of the unknown: every step
reveals new terrain, every landmark sketched onto the map brings profit and
prestige. Tension comes from dangerous terrain — cliffs, swamps, predator
territories — and limited supplies. Completed maps sell to merchants in town,
funding better equipment for deeper expeditions. The map itself is the primary
UI element, filling in as the player moves.

## What the Player Experiences

1. **Title Screen** — A parchment-styled title with the game name in hand-drawn
   lettering, an ink bottle and quill motif, and a play button.
2. **The Wilderness** — The player moves freely through procedurally varied
   terrain: forests, mountains, rivers, caves, and ruins. Fog of war hides
   unexplored areas.
3. **Map Drawing** — As the player explores, a minimap and full-screen map fill
   in with terrain details. Landmarks (ruins, unique trees, cave entrances) can
   be annotated for bonus value.
4. **Dangers** — Hostile wildlife, treacherous cliffs, and quicksand threaten the
   player. Health is limited and healing requires returning to camp or using
   scarce supplies.
5. **Supplies** — The player carries food, ink, and rope. Food depletes over time;
   ink is consumed when annotating landmarks; rope is needed to cross cliffs.
   Running out forces a retreat.
6. **Selling Maps** — Returning to the starting town lets the player sell completed
   map sections. Larger, more detailed maps with annotations fetch higher prices.
7. **Equipment Upgrades** — Profits buy better boots (faster movement), a compass
   (reveals terrain type ahead), a lantern (explores caves), and a sturdy pack
   (more supply capacity).

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

# 开放世界制图师（Open-World Cartographer）

在 `/workspace/game/` 用 Godot 4 开发一个**开放世界制图师（Open-World Cartographer）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名深入未测绘荒野的制图师，边探索边绘制地图。这里的幻想是发现并掌握
未知：每一步都揭开新的地形，每一个被绘上地图的地标都带来利润与声望。张力来自
危险的地形——悬崖、沼泽、猛兽领地——以及有限的补给。绘制完成的地图可以卖给镇上的
商人，为更深入的远征筹措更好的装备。地图本身就是最主要的 UI 元素，随玩家移动
而逐步填充。

## 玩家体验流程

1. **标题画面** —— 一个羊皮纸风格的标题，游戏名称采用手绘字体，配有墨水瓶与
   羽毛笔的图案，以及一个开始按钮。
2. **荒野** —— 玩家在程序化生成、变化多样的地形中自由移动：森林、山脉、河流、
   洞穴和遗迹。战争迷雾遮蔽未探索的区域。
3. **地图绘制** —— 随着玩家的探索，小地图和全屏地图会逐步填入地形细节。地标
   （遗迹、独特的树木、洞口）可以被标注，以获得额外价值。
4. **危险** —— 敌对的野生动物、险峻的悬崖和流沙威胁着玩家。生命值有限，治疗
   需要返回营地或消耗稀缺的补给。
5. **补给** —— 玩家携带食物、墨水和绳索。食物随时间消耗；标注地标时消耗墨水；
   跨越悬崖需要绳索。补给耗尽会迫使玩家撤退。
6. **出售地图** —— 返回起始小镇后，玩家可以出售绘制完成的地图区块。更大、更
   详尽且带有标注的地图能卖出更高的价格。
7. **装备升级** —— 利润可以购买更好的靴子（移动更快）、罗盘（显示前方地形
   类型）、提灯（用于探索洞穴）和结实的背包（更大的补给容量）。

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

