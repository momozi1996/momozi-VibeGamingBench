# Open-World Submarine

Build an **Open-World Submarine** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player pilots a submarine through a vast deep ocean, using sonar to navigate
the darkness and discover sunken wrecks, underwater caves, and strange creatures.
The fantasy is the thrill of the abyss: descending into crushing depths where
light fades and pressure mounts, finding treasures no one else has reached.
Tension comes from oxygen management, hull pressure limits, and the unknown
shapes that appear on sonar. Salvaged treasures fund upgrades that let the
submarine dive deeper.

## What the Player Experiences

1. **Title Screen** — A dark oceanic title with the game name in glowing
   bioluminescent lettering, bubbles rising, and a play button.
2. **The Ocean** — The player pilots the submarine freely in a large 2D ocean
   cross-section. Depth increases downward with visible pressure zones marked by
   colour shifts from light blue to deep navy to black.
3. **Sonar** — Visibility is limited. The player pings sonar to reveal terrain,
   wrecks, and creatures in a radius. Sonar pulses are visible as expanding
   rings. Passive sonar shows moving contacts as blips.
4. **Exploration** — Sunken ships, underwater caves, and coral formations dot the
   ocean. The player docks with wrecks to salvage cargo, enters caves to find
   rare minerals, and photographs creatures for research bounties.
5. **Oxygen** — A constantly depleting oxygen meter forces the player to surface
   periodically or find air pockets in caves. Running out causes a blackout and
   forced ascent with cargo loss.
6. **Depth Pressure** — Descending past the submarine's rated depth causes hull
   stress. A hull integrity meter drops; if it reaches zero, the sub implodes.
   Upgrades increase depth rating.
7. **Upgrades** — Salvage funds better hull plating (deeper dives), larger oxygen
   tanks, improved sonar range, cargo hold expansion, and a headlight for
   visibility without sonar.

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

# 开放世界潜艇（Open-World Submarine）

在 `/workspace/game/` 用 Godot 4 开发一个**开放世界潜艇（Open-World Submarine）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶一艘潜艇穿行于浩瀚的深海，用声呐在黑暗中导航，发现沉船残骸、水下洞穴
和奇异的生物。这里的幻想是深渊的刺激：下潜到光线消失、压力递增的极深处，找到
无人抵达过的宝藏。张力来自氧气管理、船体耐压极限，以及声呐上浮现的未知轮廓。
打捞到的宝藏可用于资助升级，让潜艇能下潜得更深。

## 玩家体验流程

1. **标题画面** —— 一个黑暗的海洋主题标题，游戏名称以发光的生物荧光字体呈现，
   气泡上升，并配有一个开始按钮。
2. **海洋** —— 玩家在一片大型 2D 海洋剖面中自由驾驶潜艇。深度向下递增，可见的
   压力分区通过颜色从浅蓝渐变为深海军蓝再到黑色来标示。
3. **声呐** —— 视野受限。玩家发出声呐脉冲，在一定半径内显现地形、残骸和生物。
   声呐脉冲以不断扩散的圆环形式可见。被动声呐把移动的接触目标显示为光点。
4. **探索** —— 沉船、水下洞穴和珊瑚群散布在海洋中。玩家与残骸对接以打捞货物，
   进入洞穴寻找稀有矿物，并拍摄生物以领取研究悬赏。
5. **氧气** —— 一条持续消耗的氧气量表迫使玩家定期上浮，或者在洞穴中寻找气室。
   氧气耗尽会导致昏迷并被强制上浮，同时损失货物。
6. **深度压力** —— 下潜超过潜艇的额定深度会造成船体压力。船体完整度量表随之
   下降；一旦归零，潜艇便会被压毁。升级可提高额定深度。
7. **升级** —— 打捞所得可用于购置更好的船体装甲板（下潜更深）、更大的氧气罐、
   更远的声呐范围、货舱扩容，以及一盏在不用声呐时也能保证视野的探照灯。

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

