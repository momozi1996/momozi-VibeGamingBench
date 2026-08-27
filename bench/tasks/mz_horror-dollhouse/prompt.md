# Horror Dollhouse

Build a **Horror Dollhouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a dollhouse that mirrors a real house, manipulating miniature
objects to affect the full-size world and escape. The fantasy is uncanny scale:
moving a tiny chair in the dollhouse causes a crash upstairs, opening a miniature
door reveals a hidden passage in the real house. Tension comes from the dollhouse
responding to the player — figures move on their own, rooms rearrange when not
watched, and the boundary between miniature and real blurs. The player must solve
puzzles across both scales to find the way out.

## What the Player Experiences

1. **Title Screen** — A split-view showing a dollhouse and its real counterpart,
   the game name in childlike handwriting that drips, and a play button.
2. **The Real House** — The player moves through a dark, full-size house in
   side-view. Doors are locked, passages blocked, and something is wrong — rooms
   do not connect logically.
3. **The Dollhouse** — Found in the attic, the dollhouse is a miniature replica
   of the real house. The player can zoom into it and interact with tiny objects:
   move furniture, open doors, flip switches.
4. **Mirror Mechanics** — Actions in the dollhouse affect the real house.
   Moving a miniature bookcase reveals a passage in the real house. Turning on a
   tiny lamp illuminates a dark real room. Locking a dollhouse door traps
   something in the real house.
5. **Puzzle Progression** — Each room has a puzzle requiring manipulation across
   both scales. The player alternates between exploring the real house and
   adjusting the dollhouse to progress.
6. **The Dollhouse Responds** — As the player progresses, the dollhouse changes
   on its own: figures appear in rooms the player just left, furniture moves
   back, and new rooms appear that do not exist in the real house. Investigating
   these anomalies reveals the horror.
7. **Escape** — The final puzzle requires the player to manipulate both scales
   simultaneously to open the front door. The ending depends on whether the
   player investigated the anomalous rooms or ignored them.

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

# 恐怖玩偶屋（Horror Dollhouse）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖玩偶屋**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家探索一座与真实房屋互为镜像的玩偶屋，通过操纵微缩物件来影响原尺寸世界并
逃出去。游戏的幻想核心是诡异的尺度感：在玩偶屋里移动一把小椅子，楼上就传来
一声巨响；打开一扇微缩的门，真实房屋里就会显露出一条隐藏通道。紧张感来自
玩偶屋会回应玩家——玩偶人形会自己移动，没人看着的时候房间会重新排布，微缩
与真实之间的界线逐渐模糊。玩家必须解开跨越两种尺度的谜题，才能找到出路。

## 玩家体验流程

1. **标题画面** —— 一个分屏视图，一边是玩偶屋、一边是它的真实对应物，游戏名
   以稚拙的手写体呈现并往下流淌，还有一个开始按钮。
2. **真实房屋** —— 玩家以侧视视角在一栋黑暗的原尺寸房屋中移动。门被锁住，
   通道被堵塞，而且有什么地方不对劲——房间之间的连接不符合逻辑。
3. **玩偶屋** —— 在阁楼里发现的玩偶屋是真实房屋的微缩复制品。玩家可以放大
   查看并与微小物件交互：搬动家具、开门、拨动开关。
4. **镜像机制** —— 玩偶屋中的动作会影响真实房屋。移动微缩书架会在真实房屋中
   显露出一条通道。点亮一盏小台灯会照亮真实中的黑暗房间。锁上玩偶屋的一扇门
   会把某种东西困在真实房屋里。
5. **谜题推进** —— 每个房间都有一个需要跨两种尺度操作的谜题。玩家要在探索
   真实房屋与调整玩偶屋之间来回切换才能推进。
6. **玩偶屋的回应** —— 随着玩家推进，玩偶屋会自行发生变化：玩偶人形出现在
   玩家刚刚离开的房间里、家具自己移回原位、出现真实房屋中并不存在的新房间。
   调查这些异常会揭开恐怖的真相。
7. **逃脱** —— 最终谜题要求玩家同时操纵两种尺度才能打开前门。结局取决于玩家
   是否调查过那些异常房间，还是对它们视而不见。

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

