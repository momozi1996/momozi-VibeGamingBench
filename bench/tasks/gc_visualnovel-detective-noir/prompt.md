# Detective Noir

Build **Detective Noir**, a **detective deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A private investigator works cases in a rain-soaked city, examining crime
scenes, interviewing suspects, and piecing together who did what, when, and
why on a deduction board. Each case is a self-contained mystery with physical
evidence, witness statements, and a web of connections that the player must
untangle. The tension is cognitive: all the clues are available, but connecting
them correctly requires careful reading and logical elimination. Wrong
accusations waste credibility and lock out information. The tone is classic
noir: shadows, trench coats, jazz undertones, and morally grey characters who
all have something to hide.

## What the Player Experiences

From the title screen the player selects a case from a case board. Each case
opens with a crime scene — a location rendered in noir style with interactive
hotspots. Clicking hotspots reveals evidence: a bloodstain, a torn letter, a
misplaced object. Each piece of evidence is added to the player's notebook
with its details.

The player then visits locations to interview suspects and witnesses. Each
character has dialogue that reveals information — some truthful, some
misleading. The player can press on statements to probe deeper, sometimes
unlocking new evidence or contradictions.

The deduction board is the core puzzle interface: the player connects evidence
to suspects, timelines, and motives by dragging links between cards. When
enough connections are made, the player can make an accusation — selecting
who, what weapon, and when. A correct accusation solves the case with a
dramatic reveal sequence. An incorrect one costs credibility points; too many
wrong guesses and the case goes cold.

Multiple cases are available with different difficulty levels. A styled result
screen shows the case outcome, evidence found, and deduction accuracy.

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

# 黑色侦探（Detective Noir）

在 `/workspace/game/` 用 Godot 4 开发 **Detective Noir**——一款
**侦探推理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨
程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名私家侦探在一座浸满雨水的城市里办案：勘查犯罪现场、询问嫌疑人，并在一块
推理板上拼凑出谁在何时、为何做了什么。每个案件都是一桩自成一体的谜案，包含
物证、证人陈述，以及一张玩家必须解开的关系网。张力是认知层面的：所有线索都
摆在那里，但要正确地把它们连起来，需要仔细阅读和逻辑排除。错误的指控会白白
消耗信誉，并锁死部分信息。整体调性是经典黑色电影：阴影、风衣、爵士底韵，以及
一群人人都有所隐瞒的道德灰色角色。

## 玩家体验流程

从标题画面开始，玩家在案件板上选择一个案件。每个案件以一个犯罪现场开场——一处
以黑色电影风格呈现的地点，带有可交互热点。点击热点会揭示证据：一片血迹、一封
被撕碎的信、一件放错位置的物品。每一份证据都会连同其细节被加入玩家的笔记本。

随后玩家会走访各个地点，询问嫌疑人和证人。每个角色都有能揭示信息的对话——有些
是真话，有些是误导。玩家可以对某些陈述追问以深入挖掘，有时能解锁新的证据或
矛盾点。

推理板是核心的解谜界面：玩家通过在卡片之间拖出连线，把证据与嫌疑人、时间线和
动机连接起来。当连接足够多时，玩家就可以提出指控——选定何人、何种凶器、何时
作案。正确的指控会以一段戏剧性的揭晓演出破案。错误的指控则要付出信誉点数；
错得太多，案件就会变成悬案。

游戏提供多个难度不同的案件。一个有设计感的结算画面会展示案件结果、找到的证据
以及推理准确率。

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

