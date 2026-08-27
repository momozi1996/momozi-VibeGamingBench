# Escape Room

Build **Escape Room**, a **narrative escape room visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player wakes in a locked room with no memory of how they got there. Each
room is a self-contained puzzle box: examine objects, combine items, decode
ciphers, and find the exit. But this is also a narrative — choices made during
escape sequences branch the story, revealing different truths about why the
player is trapped. Multiple rooms connect into a larger mystery, and reaching
the true ending requires solving all rooms and making specific narrative
choices. The tension is dual: the intellectual satisfaction of puzzle-solving
layered with the narrative dread of discovering what is really happening. The
tone is atmospheric suspense: dim lighting, cryptic notes, and the ticking
pressure of confinement.

## What the Player Experiences

From the title screen the player enters the first room. The view shows a
first-person-style room illustration with interactive hotspots — drawers,
paintings, locks, scattered objects. Clicking hotspots examines them, sometimes
adding items to an inventory bar.

Items can be combined (key + lock, cipher + coded message) or used on hotspots.
Each room has a sequence of puzzles that gate progress: solving one reveals the
next. Puzzles include pattern matching, code deciphering, hidden object
finding, and logic deduction.

Between puzzle segments, narrative moments present dialogue choices that affect
the story branch. The player might find a note that reveals a character's
motive, and their response determines which version of events they believe —
affecting which rooms unlock next and which ending they reach.

Multiple rooms form a sequence, each harder than the last. The true ending
requires completing all rooms and making specific deduction choices. Other
endings are valid but incomplete — the player knows they missed something.

A styled result screen shows escape time, puzzles solved, and which ending
was reached, with a hint about paths not taken.

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

# 密室逃脱（Escape Room）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Escape Room**——一款
**叙事型密室逃脱视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一间锁死的房间中醒来，完全不记得自己是怎么来的。每个房间都是一个自成
一体的谜题盒：检视物品、组合道具、破译密码，并找到出口。但这同时也是一段叙事
——在逃脱过程中做出的选项会让故事分支，揭示出关于玩家为何被困的不同真相。多个
房间串联成一个更大的谜团，而要抵达真结局，就必须解开所有房间并做出特定的叙事
选项。张力是双重的：解谜带来的智性满足，叠加上发现真相时的叙事恐惧。整体调性
是氛围悬疑：昏暗的灯光、晦涩的字条，以及被禁闭时那种滴答逼近的压迫感。

## 玩家体验流程

从标题画面开始，玩家进入第一个房间。画面呈现一幅第一人称视角风格的房间插图，
带有可交互热点——抽屉、画作、锁具、散落的物件。点击热点会检视它们，有时会把
道具加入道具栏。

道具可以互相组合（钥匙 + 锁、密码本 + 加密信息），也可以用在热点上。每个房间
都有一串门槛式的谜题：解开一个，就会揭示下一个。谜题类型包括图案匹配、密码
破译、隐藏物品寻找和逻辑推演。

在解谜段落之间，会出现影响故事分支的叙事时刻，提供对话选项。玩家可能会找到一张
揭示某个角色动机的字条，而他们的回应决定了他们相信哪个版本的事件——从而影响
接下来解锁哪些房间、抵达哪个结局。

多个房间构成一条序列，一个比一个更难。真结局要求玩家完成所有房间并做出特定的
推理选项。其他结局同样有效，但并不完整——玩家会知道自己漏掉了什么。

一个有设计感的结算画面会展示逃脱用时、解开的谜题数量以及抵达的是哪个结局，
并附上一条关于未走之路的提示。

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

