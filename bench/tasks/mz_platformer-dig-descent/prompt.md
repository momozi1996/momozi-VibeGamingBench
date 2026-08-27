# Dig Descent

Build **Dig Descent**, a vertical descent platformer with downward shooting and
combo scoring as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A diver plunges endlessly downward through procedurally assembled shafts,
firing a weapon beneath their feet to destroy blocks, slow their fall, and
chain kills into escalating combos. The gun is both offense and movement tool —
shooting downward provides upward recoil that buys precious milliseconds to
steer around hazards. Gems collected from destroyed blocks fund visits to
mid-run shops where weapon upgrades and health refills await. The deeper the
player descends, the faster the screen scrolls and the denser the hazards
become. Death resets to the surface with nothing carried over except skill.

## What the Player Experiences

A title screen shows the game name, high score, and a Start button. Pressing
Start begins the descent immediately.

The player character falls continuously. Pressing the fire button shoots
downward, destroying soft blocks and nudging the character upward slightly.
Enemies drift across the shaft — shooting them adds to a combo counter that
multiplies gem value. Landing on a platform resets the combo but provides a
safe moment to breathe. Touching spikes, enemies, or the top of the screen
costs health.

Every few depth tiers a shop platform appears with three purchasable upgrades:
weapon spread, fire rate, health refill, or a shield. The player spends
collected gems and continues downward. Procedural generation ensures no two
runs are identical. When health reaches zero, a game-over screen shows depth
reached, gems collected, max combo, and a retry button.

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

# 掘地下潜（Dig Descent）

在 `/workspace/game/` 用 Godot 4 开发 **Dig Descent**，一款带向下射击与连击计分的垂直下潜平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名潜行者无止境地向下坠入程序化拼接出的竖井，朝脚下开火来摧毁方块、减缓下落，并把击杀串成不断攀升的连击。枪既是攻击手段也是移动工具——向下射击会带来向上的后坐力，为绕开危险物争取到宝贵的几毫秒。从被摧毁的方块中收集到的宝石，可以用在一轮之中途经的商店里，那里备有武器升级和血量补充。玩家下潜得越深，屏幕滚动越快，危险物也越密集。死亡会把一切重置回地表，除了技术之外什么都带不走。

## 玩家体验流程

标题画面显示游戏名、最高分和一个开始按钮。按下开始立刻进入下潜。

玩家角色持续下落。按下开火键向下射击，摧毁软质方块并把角色略微向上顶起。敌人在竖井中横向游走——击中它们会增加连击计数，从而提升宝石价值。落在平台上会重置连击，但也提供一个安全的喘息瞬间。碰到尖刺、敌人或屏幕顶部会损失血量。

每隔几个深度层会出现一个商店平台，提供三项可购买的升级：武器散射、射速、血量补充或护盾。玩家花掉收集到的宝石后继续向下。程序化生成确保没有两轮是完全一样的。血量归零时，游戏结束画面显示抵达深度、收集的宝石数、最高连击，以及一个重试按钮。

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

