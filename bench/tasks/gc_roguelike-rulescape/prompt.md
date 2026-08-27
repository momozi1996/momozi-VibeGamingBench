# Roguelike: Rulescape

Build **Rulescape**, a top-down **rules-horror roguelike survival game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a polished vertical slice where the player
navigates haunted public spaces, deciphers unstable rules, and escapes before
the site consumes them.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being trapped inside a place that was once ordinary -- a
hospital, a school, a subway station -- now governed by rules that shift,
corrupt, and lie. Survival depends on reading the environment, deducing which
rules are real, and acting before time runs out. The pressure comes from an
advancing timetable that changes what is safe, anomalies whose behavior is
tied to the local mystery, and the knowledge that obeying the wrong rule is as
deadly as breaking the right one. Each site is a story before it is a level:
its rooms, props, clues, and escape condition should feel like one connected
mystery, not a generic dungeon with swapped textures. The tone is frightening,
bloody, investigative, and oppressive.

## What the Player Experiences

1. **Title and Survivor Choice** -- The player arrives at a dark, themed title screen and selects a survivor from a small roster. Each survivor brings a different tool or instinct that changes how the player reads danger and interacts with the site.
2. **Entering the Site** -- The run drops the player into a top-down anomaly site -- a real-feeling place with rooms, corridors, locked doors, scattered props, and environmental storytelling. The site has its own name, visual identity, local mystery, and set of posted rules that the player can inspect in-world.
3. **The Timetable** -- A visible clock or schedule advances during exploration. When it reaches authored thresholds the site's rhythm changes: new areas unlock, anomalies shift behavior, rules become more dangerous, or an escape window opens.
4. **Exploration and Deduction** -- The player moves through the site, searches objects for clues and items, reads rules (some incomplete, misleading, or corrupted), and pieces together what is actually true. Anomalies appear as spatial threats tied to the site's rules; the player responds by fleeing, hiding, using items, or obeying the correct rule -- wrong choices cost health, sanity, or time.
5. **Resolution** -- Victory comes from satisfying the site's escape condition; defeat comes from a fatal anomaly encounter, rule violation, or resource collapse. The result screen explains what rule, clue, or decision sealed the outcome.

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

# Roguelike：规则之地（Roguelike: Rulescape）

在 `/workspace/game/` 用 Godot 4 开发 **Rulescape**——一款俯视视角的**规则恐怖
Roguelike 生存游戏**：一个打磨精良的纵向切片，玩家在闹鬼的公共空间中穿行，
破译不稳定的规则，并在这处场所把他吞噬之前逃出去。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片
放到 itch.io 页面或 Steam 上。

## 核心构想

游戏的幻想核心是被困在一处曾经再普通不过的地方——一间医院、一所学校、一座地铁
站——如今却被会变动、会腐坏、会说谎的规则所支配。存活取决于读懂环境、推断哪些
规则是真的，并在时间耗尽之前采取行动。压力来自一张不断推进的时间表，它会改变
什么是安全的；来自行为与当地谜团绑定的异常；也来自这样一种认知——遵守错误的规则
和违反正确的规则一样致命。每处场所在成为一个关卡之前，首先是一个故事：它的房间、
道具、线索和逃脱条件应当感觉像一个彼此相连的谜团，而不是换了贴图的通用地牢。
整体调性是惊悚、血腥、调查向且令人压抑的。

## 玩家体验流程

1. **标题与幸存者选择** —— 玩家来到一个昏暗、有主题感的标题画面，从一小批幸存者中做出选择。每位幸存者带来不同的工具或本能，改变玩家读懂危险以及与场所互动的方式。
2. **进入场所** —— 这一轮把玩家投进一处俯视视角的异常场所——一个有真实感的地方，带有房间、走廊、锁住的门、散落的道具和环境叙事。该场所拥有自己的名称、视觉标识、当地谜团，以及一套玩家可以在游戏世界内查看的张贴规则。
3. **时间表** —— 一个可见的时钟或日程表在探索过程中推进。当它抵达设计好的阈值时，场所的节奏就会改变：新区域解锁、异常改变行为、规则变得更危险，或者一个逃脱窗口打开。
4. **探索与推理** —— 玩家在场所中移动，搜查物品以寻找线索和道具，阅读规则（有些不完整、有误导性或已被腐坏），并拼凑出真正为真的是什么。异常以与场所规则绑定的空间威胁形式出现；玩家的应对方式是逃跑、躲藏、使用道具，或遵守正确的规则——错误的选择会付出生命值、理智值或时间的代价。
5. **结局** —— 胜利来自满足场所的逃脱条件；失败来自一次致命的异常遭遇、一次规则违反，或资源崩溃。结算画面会解释是哪条规则、哪条线索或哪个决定锁定了这一结局。

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

