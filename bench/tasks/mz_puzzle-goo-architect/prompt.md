# Goo Architect

Build **Goo Architect**, a 2D physics-based structure-building puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player attaches stretchy blob creatures to
each other to build towers, bridges, and other structures that reach a goal
pipe, while gravity and wind threaten to topple their creation.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a construction puzzle driven by soft-body physics. Each level
presents a landscape with a goal pipe placed in a hard-to-reach location. The
player has a limited supply of goo blobs that can be dragged and attached to
existing structure nodes, forming elastic bonds that stretch and sway under
gravity. The tension comes from structural engineering under constraint: too
tall and the tower buckles, too thin and it snaps, too heavy on one side and
it topples. Different goo types add strategic variety — rigid blobs for
foundations, balloon blobs for lift, flammable blobs that burn through
obstacles. The best version feels like building with living putty, where every
placement decision has visible physical consequences.

## What the Player Experiences

A title screen sets the whimsical tone with animated goo creatures and a clear
way to begin. The player enters a level where terrain, hazards, and a goal pipe
are visible. Available goo blobs sit in a supply area. The player drags a blob
from supply and attaches it near existing structure nodes; elastic bonds form
automatically to nearby attachment points.

Early levels teach basic tower-building: stack blobs upward to reach a pipe
above. Soon terrain gaps require bridges, wind gusts demand reinforced
structures, and spike hazards force creative routing. Multiple goo types
appear: standard green goo forms flexible bonds, rigid gray goo creates stiff
joints, balloon pink goo provides upward lift, and flammable red goo can be
ignited to clear obstacles. Each level has a minimum blob quota — saving extra
blobs earns bonus recognition.

The structure sways and settles in real-time as the player builds. When blobs
reach the goal pipe, they are sucked in with a satisfying animation and the
level completes. A results screen shows blobs saved and offers the next
challenge. The campaign progresses through themed worlds with escalating
structural demands.

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

# 黏球建筑师（Goo Architect）

在 `/workspace/game/` 用 Godot 4 开发 **Goo Architect**，一个 2D 基于物理的结构
搭建解谜游戏。玩家把有弹性的黏球生物一个个连接起来，搭出塔、桥和其他结构，
让它们伸到目标管道处，同时还要对抗随时可能把作品掀翻的重力与狂风。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款由软体物理驱动的建造解谜游戏。每一关呈现一片地形，目标管道被放在
难以到达的位置。玩家拥有数量有限的黏球，可以拖动它们并附着到已有结构的节点上，
形成会在重力下拉伸摇晃的弹性连接。张力来自约束条件下的结构工程学：塔太高会
失稳弯折，太细会断裂，一侧太重就会倾倒。不同的黏球类型带来策略多样性——刚性
黏球用作地基，气球黏球提供升力，易燃黏球可以烧穿障碍。最理想的版本会让人感觉
像是在用活的橡皮泥搭建结构，每一次放置决策都有肉眼可见的物理后果。

## 玩家体验流程

标题画面用会动的黏球生物营造出诡趣的氛围，并给出清晰的开始入口。玩家进入关卡后
能看到地形、危险物和目标管道。可用的黏球放在供应区。玩家从供应区拖出一颗黏球，
放到已有结构节点附近；弹性连接会自动与附近的附着点生成。

前期关卡教基础的搭塔：把黏球向上堆叠，去触及上方的管道。很快，地形裂口需要架桥，
阵风要求加固结构，尖刺陷阱迫使玩家另寻路线。多种黏球类型陆续登场：标准绿色黏球
形成柔性连接，刚性灰色黏球构成坚硬关节，气球粉色黏球提供向上的升力，易燃红色
黏球可被点燃来清除障碍。每关都有一个最低黏球回收指标——多救下的黏球会赢得额外
褒奖。

玩家搭建时，结构会实时摇摆并逐渐稳定。当黏球触及目标管道时，会伴随一段令人满足
的动画被吸进去，关卡随之完成。结算画面展示救下的黏球数量，并给出下一个挑战。
战役按主题世界推进，结构要求层层升级。

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

