# Idle Ant Empire

Build an **Idle Ant Empire** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds an ant colony from a single queen, assigning workers to tasks,
unlocking new ant types, and growing exponentially through prestige resets. The
fantasy is watching a tiny empire scale to absurd proportions: from gathering
crumbs to harvesting entire gardens, from a handful of workers to millions. The
idle loop runs continuously — ants gather resources even when the player is not
clicking. Tension comes from resource allocation decisions and seasonal challenges
that threaten the colony.

## What the Player Experiences

1. **Title Screen** — A cross-section of underground tunnels with ants marching,
   the game name in earthy brown font, and a play button styled as a leaf.
2. **Colony View** — A side-view ant colony with visible chambers: nursery, food
   storage, queen's chamber, and tunnels connecting them. Ants visibly move
   between chambers carrying resources.
3. **Worker Assignment** — The player assigns ants to roles: gatherers (collect
   food), builders (dig new chambers), soldiers (defend), and nurses (hatch eggs).
   Sliders or buttons control allocation. Production rates update in real-time.
4. **Resource Generation** — Food accumulates automatically based on gatherer
   count. The player can click to manually boost gathering. Resources fund new
   chambers, ant hatching, and upgrades.
5. **Ant Types** — Unlockable ant types with special abilities: leaf-cutters
   (bonus food), fire ants (defence), flying ants (exploration), and mega-ants
   (10x production). Each type has a distinct sprite.
6. **Prestige System** — When the colony reaches a threshold size, the player can
   prestige: reset the colony but gain permanent multipliers (queen fertility,
   gathering speed, defence strength). Each prestige makes the next run faster.
7. **Seasonal Challenges** — Periodic events threaten the colony: rain floods
   tunnels (need builders), predators attack (need soldiers), winter reduces food
   (need stockpiles). Surviving challenges grants bonus resources.

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

# 放置蚂蚁帝国（Idle Ant Empire）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置蚂蚁帝国**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家从一只蚁后开始建立一个蚂蚁殖民地，把工蚁分派到各项任务上，解锁新的蚂蚁
类型，并通过转生重置实现指数级增长。游戏的幻想核心是看着一个微小的帝国扩张到
荒谬的规模：从捡食面包屑到收割整座花园，从寥寥几只工蚁到数以百万计。放置循环
持续运转——即使玩家不点击，蚂蚁也在采集资源。紧张感来自资源分配决策，以及
威胁殖民地存亡的季节性挑战。

## 玩家体验流程

1. **标题画面** —— 一幅地下隧道的剖面图，蚂蚁在其中行进，游戏名采用土褐色
   字体，还有一个做成叶片样式的开始按钮。
2. **殖民地视图** —— 一个侧视视角的蚂蚁殖民地，可以看到各个巢室：育婴室、
   食物仓库、蚁后寝宫，以及连接它们的隧道。蚂蚁会明显地在巢室之间搬运资源。
3. **工蚁分派** —— 玩家把蚂蚁分配到各个岗位：采集蚁（收集食物）、建造蚁
   （挖掘新巢室）、兵蚁（防御）和护理蚁（孵卵）。用滑块或按钮来控制分配比例。
   产出速率会实时更新。
4. **资源生产** —— 食物会根据采集蚁数量自动累积。玩家可以点击手动提升采集
   效率。资源用于修建新巢室、孵化蚂蚁和购买升级。
5. **蚂蚁类型** —— 可解锁的蚂蚁类型带有特殊能力：切叶蚁（食物加成）、火蚁
   （防御）、飞蚁（探索）和巨型蚁（10 倍产出）。每种类型都有独特的精灵图。
6. **转生系统** —— 当殖民地规模达到某个阈值时，玩家可以转生：重置殖民地，
   但获得永久倍率（蚁后繁殖力、采集速度、防御强度）。每次转生都会让下一轮
   变得更快。
7. **季节性挑战** —— 周期性事件会威胁殖民地：暴雨淹没隧道（需要建造蚁）、
   捕食者来袭（需要兵蚁）、冬季食物减少（需要存粮）。挺过挑战可获得额外资源。

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

