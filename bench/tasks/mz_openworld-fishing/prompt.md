# Open-World Fishing

Build a **2D open-world fishing game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a tranquil open world dotted with lakes, rivers, and ocean
shores, casting a line to hook diverse fish species. The fantasy is patience
rewarded: reading the water, timing the cast, fighting a fish on the line, and
finally adding a rare catch to the journal. Tension comes from the reel
mini-game — pull too hard and the line snaps; too soft and the fish escapes.
Weather and time-of-day shift what bites, pushing the player to revisit
familiar spots under new conditions.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a play button, and a
   serene water backdrop. No naked HTML 引擎 grey.
2. **The World** — The player walks freely across an open landscape with several
   visually distinct water bodies — a calm lake, a rushing river with current
   effects, and a deep ocean shore. Each body looks and feels different, and
   different fish inhabit each.
3. **Casting** — The player charges a cast meter and releases to throw the line.
   Distance depends on timing. The line lands with a splash effect.
4. **Bite and Reel** — A bobber floats on the water. When a fish bites, the
   player hooks it with a timed press, then manages line tension by reeling and
   releasing. A tension meter shows stress — too much and the line snaps.
5. **Fish Variety** — Multiple distinct species with different appearances,
   sizes, and habitats. Catching a fish shows its name, size, and flavour text.
   Rare fish have unique visual flair.
6. **Fishing Journal** — A journal tracks caught species with silhouettes for
   uncaught ones, plus a completion percentage.
7. **Weather and Time** — Weather changes affect which fish appear. A day/night
   cycle shifts lighting and water colour, and some species only bite under
   certain conditions.

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

# 开放世界钓鱼（Open-World Fishing）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界钓鱼游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个宁静的开放世界中探索，其间点缀着湖泊、河流和海岸，抛出鱼线钓起
各种鱼类。这里的幻想是耐心得到回报：读懂水面、掌握抛竿时机、与咬钩的鱼周旋，
最终把一条稀有渔获记入图鉴。张力来自收线小游戏——拉得太猛线会断，太松鱼会跑。
天气和时间会改变上钩的鱼种，促使玩家在新的条件下重访熟悉的钓点。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮和一片
   宁静的水面背景。不要出现 HTML 引擎 的裸灰色。
2. **世界** —— 玩家在开放的地貌中自由行走，其中有几处视觉上截然不同的水域——
   一片平静的湖泊、一条带水流效果的湍急河流，以及一段深海岸线。每处水域的
   外观和感觉都不同，栖息的鱼类也各不相同。
3. **抛竿** —— 玩家蓄力一条抛竿力量条，松开后甩出鱼线。距离取决于时机。鱼线
   落水时带有水花效果。
4. **咬钩与收线** —— 浮标漂在水面上。鱼咬钩时，玩家通过一次限时按键把它钩住，
   然后通过收线和放线来控制线的张力。一条张力条显示受力程度——张力过大鱼线
   就会断。
5. **鱼类多样性** —— 多种截然不同的鱼种，外观、体型和栖息地各异。钓上一条鱼
   会显示它的名称、尺寸和风味文本。稀有鱼类有独特的视觉亮点。
6. **钓鱼图鉴** —— 一本图鉴记录已钓到的鱼种，未钓到的以剪影显示，并附带一个
   完成度百分比。
7. **天气与时间** —— 天气变化会影响出现哪些鱼。昼夜循环改变光照和水的颜色，
   有些鱼种只在特定条件下才会咬钩。

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

