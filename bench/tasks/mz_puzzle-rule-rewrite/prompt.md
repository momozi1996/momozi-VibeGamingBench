# Rule Rewrite

Build **Rule Rewrite**, a 2D grid-based word-block puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player pushes word-blocks around a tile grid to form
sentences that rewrite the rules of the level, transforming what objects do and
how the world behaves.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a spatial logic puzzle where the level itself is made of language.
Nouns, verbs, and properties exist as pushable blocks on the same grid as the
objects they describe. Forming a sentence like "WALL IS STOP" makes walls solid;
breaking that sentence by pushing a word away makes walls passable. The player
character is not fixed either — "YOU" is a property that can be reassigned to
any noun. The tension comes from the recursive nature of the rules: every move
can redefine what is dangerous, what is the goal, and what the player even
controls. The best version feels like a logic puzzle wrapped in a language game,
where each level teaches a new interaction between familiar English words.

## What the Player Experiences

A title screen introduces the game with stylized word-block imagery and a clear
way to begin. The player enters a grid where objects (walls, flags, skulls,
keys) coexist with word-blocks (nouns like WALL, FLAG; verbs like IS, HAS;
properties like STOP, WIN, PUSH, DEFEAT, YOU). Moving with arrow keys pushes
word-blocks and objects alike, one tile at a time.

Early levels teach the basics: push "FLAG IS WIN" together to make the flag the
goal, then walk into it. Soon the player discovers they can break rules apart,
reassign properties, and even change which object they control. Mid-game levels
introduce conditional chains, multiple rule sentences active simultaneously, and
objects that transform when rules change. Late levels demand planning several
moves ahead, where breaking one rule to form another creates cascading state
changes across the board.

An undo system lets the player step back freely. Level completion celebrates
with a styled screen and advances to the next puzzle. The campaign has 20+
levels with escalating complexity, grouped into worlds that each introduce a
new word or mechanic.

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

# 规则改写（Rule Rewrite）

在 `/workspace/game/` 用 Godot 4 开发 **Rule Rewrite**，一个 2D 基于网格的
文字方块解谜游戏。玩家在图块网格上推动词块，拼成句子来改写这一关的规则，
从而改变物体的作用和世界的运行方式。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款空间逻辑解谜游戏，而关卡本身就是由语言构成的。名词、动词和属性以可推动
的方块形式存在，与它们所描述的物体处在同一张网格上。拼出 "WALL IS STOP" 这样的
句子会让墙壁变得坚实；把某个词推开、打断这个句子，墙壁就变得可以穿过。玩家角色
本身也不是固定的——"YOU" 是一个属性，可以被重新指派给任何名词。张力来自规则的
递归特性：每一步移动都可能重新定义什么是危险、什么是目标，甚至玩家究竟在操控
什么。最理想的版本会让人感觉像是一道包裹在文字游戏里的逻辑谜题，每一关都在教你
熟悉的英文单词之间一种新的相互作用。

## 玩家体验流程

标题画面用风格化的词块意象介绍这款游戏，并给出清晰的开始入口。玩家进入一张网格，
其中物体（墙、旗、骷髅、钥匙）与词块（名词如 WALL、FLAG；动词如 IS、HAS；
属性如 STOP、WIN、PUSH、DEFEAT、YOU）共存。用方向键移动会一格一格地推动词块
和物体。

前期关卡教基础操作：把 "FLAG IS WIN" 推到一起，让旗子成为目标，然后走进去。很快，
玩家就会发现自己可以打散规则、重新指派属性，甚至改变自己操控的是哪个物体。中期
关卡引入条件链、同时生效的多条规则句，以及会在规则变化时发生形变的物体。后期
关卡要求提前规划好几步，因为打破一条规则去组成另一条会在整个棋盘上引发级联的
状态变化。

撤销系统让玩家可以自由回退。关卡完成时会用一个风格化画面来庆祝，并推进到下一道
谜题。战役共有 20 个以上关卡，复杂度层层升级，并被分组为若干世界，每个世界都
引入一个新的单词或机制。

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

