# Circuit Wizard

Build **Circuit Wizard**, a 2D logic-circuit puzzle game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player places and connects logic gates (AND, OR, NOT,
XOR) on a board to route signals from inputs to outputs, solving increasingly
complex signal-routing challenges across a campaign.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a digital logic puzzle where the player builds circuits from
discrete components. Each level provides fixed input signals (on/off or
patterned) and requires specific output signals. The player places gates from
a toolbox onto a grid board and draws wires between them to create the correct
logic path. The tension comes from spatial constraints (limited board space,
wire crossing rules) and logical complexity (multi-bit signals, timing
sequences, feedback loops). The best version feels like being an engineer
with a soldering iron, where each completed circuit produces a satisfying
cascade of signals lighting up from input to output.

## What the Player Experiences

A title screen sets the electronic workshop tone with circuit imagery and a
clear way to begin. The player enters a puzzle board where input terminals
(left side), output terminals (right side), and an empty grid workspace are
visible. A toolbox shows available gate types with quantities.

Early levels teach individual gates: connect an input through a NOT gate to
invert the signal, or wire two inputs through an AND gate. Soon levels require
multi-gate chains where the player must decompose a complex boolean expression
into a physical circuit. Mid-game introduces XOR gates, multi-bit buses,
signal splitters, and delay elements that add timing constraints. Late levels
present real-world-inspired challenges: build an adder, construct a
multiplexer, or create a latch with feedback.

Signals flow visually through wires when the player activates the test button.
Correct outputs light up green; incorrect ones flash red with the expected
value shown. A completion screen celebrates the solve and shows gate count
efficiency. The campaign progresses through themed chapters: basic logic,
arithmetic circuits, memory circuits, and challenge rounds.

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

# 电路奇才（Circuit Wizard）

在 `/workspace/game/` 用 Godot 4 开发 **Circuit Wizard**，一个 2D 逻辑电路解谜游戏。
玩家在电路板上摆放并连接逻辑门（AND、OR、NOT、XOR），把信号从输入端布线到输出端，
在整个战役中攻克难度不断攀升的信号布线挑战。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款数字逻辑解谜游戏，玩家用离散元件搭建电路。每一关提供固定的输入信号
（开/关或特定模式），并要求产出指定的输出信号。玩家从工具箱中取出逻辑门放到
网格电路板上，并在它们之间连线，构造出正确的逻辑通路。张力来自空间约束
（电路板空间有限、导线交叉规则）与逻辑复杂度（多位信号、时序、反馈回路）。
最理想的版本会让人感觉自己就是一名手持电烙铁的工程师——每完成一个电路，
都会看到信号从输入到输出层层点亮，带来极强的满足感。

## 玩家体验流程

标题画面以电路元素营造出电子工坊的氛围，并给出清晰的开始入口。玩家进入解谜
电路板界面，能看到输入端子（左侧）、输出端子（右侧）和一片空白的网格工作区。
工具箱列出可用的逻辑门类型及其数量。

前期关卡逐个教会单个逻辑门：把一个输入接过 NOT 门以反转信号，或把两个输入接过
一个 AND 门。很快，关卡就会要求多门串联，玩家必须把复杂的布尔表达式拆解成
物理电路。中期引入 XOR 门、多位总线、信号分路器，以及带来时序约束的延迟元件。
后期关卡呈现取材于现实的挑战：搭建一个加法器、构造一个多路选择器，或用反馈
做出一个锁存器。

玩家按下测试按钮后，信号会可视化地在导线中流动。正确的输出亮起绿色；错误的
输出闪红并显示期望值。完成画面为解题喝彩，并展示逻辑门用量的效率评价。战役
按主题章节推进：基础逻辑、算术电路、存储电路，以及挑战关卡。

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

