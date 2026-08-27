# Open-World Beast Tamer

Build an **Open-World Beast Tamer** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player roams diverse biomes — jungle, tundra, desert, swamp — finding and
taming wild creatures with unique abilities. The fantasy is building a bond with
powerful beasts and using their skills to solve environmental puzzles and reach
new areas. Tension comes from the taming process itself: each creature requires
a different approach (stealth, bait, rhythm), and failed attempts spook the beast.
Tamed creatures evolve through use, gaining new forms and abilities.

## What the Player Experiences

1. **Title Screen** — A vibrant title showing the game name with creature
   silhouettes in various biomes. A play button starts the adventure.
2. **Biome Exploration** — The player walks freely across interconnected biomes,
   each with distinct terrain, colour palette, and ambient creatures. Biome
   boundaries are visually clear.
3. **Creature Discovery** — Wild creatures roam each biome with visible behaviour
   patterns. A bestiary silhouette hints at undiscovered species. Each creature
   has a unique sprite and idle animation.
4. **Taming** — Approaching a creature triggers a taming mini-game: the player
   must match a pattern (timing clicks, offering correct bait, or sneaking close
   without startling). Success adds the creature to the party.
5. **Creature Abilities** — Each tamed creature has a unique ability: fire breath
   melts ice barriers, a burrower digs through soft ground, a flyer carries the
   player over gaps. The player switches active creature to solve puzzles.
6. **Environmental Puzzles** — Blocked paths require specific creature abilities.
   A frozen river needs fire, a chasm needs flight, a sealed cave needs brute
   strength.
7. **Evolution** — Using a creature in puzzles and exploration fills an experience
   gauge. When full, the creature evolves into a stronger form with enhanced
   abilities and a new sprite.

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

# 开放世界驯兽师（Open-World Beast Tamer）

在 `/workspace/game/` 用 Godot 4 开发一个**开放世界驯兽师（Open-World Beast Tamer）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在多样的生态区中漫游——丛林、苔原、沙漠、沼泽——寻找并驯服拥有独特能力的
野生生物。这里的幻想是与强大的野兽建立羁绊，并用它们的技能解决环境谜题、抵达
新的区域。张力来自驯服过程本身：每种生物都需要不同的方式（潜行、诱饵、节奏），
而失败的尝试会惊走野兽。被驯服的生物会在使用中进化，获得新的形态和能力。

## 玩家体验流程

1. **标题画面** —— 一个色彩鲜明的标题，展示游戏名称以及各生态区中的生物剪影。
   一个开始按钮启动冒险。
2. **生态区探索** —— 玩家在彼此连通的生态区中自由行走，每个区域都有独特的地形、
   配色和环境生物。生态区的边界在视觉上清晰可辨。
3. **生物发现** —— 野生生物在各个生态区中游荡，行为模式可见。图鉴中的剪影
   暗示着尚未发现的物种。每种生物都有独特的精灵图和待机动画。
4. **驯服** —— 接近生物会触发驯服小游戏：玩家必须完成某种模式（掌握点击时机、
   提供正确的诱饵，或不惊动对方地潜行靠近）。成功后该生物加入队伍。
5. **生物能力** —— 每只驯服的生物都有一项独特能力：火焰吐息能融化冰障，钻地者
   能挖穿松软地面，飞行者能载着玩家越过沟壑。玩家切换当前生物来解决谜题。
6. **环境谜题** —— 被堵住的道路需要特定的生物能力。冰封的河流需要火焰，深渊
   需要飞行，封闭的洞穴需要蛮力。
7. **进化** —— 在解谜和探索中使用生物会填充一条经验量表。填满后，该生物进化为
   更强的形态，拥有增强的能力和新的精灵图。

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

