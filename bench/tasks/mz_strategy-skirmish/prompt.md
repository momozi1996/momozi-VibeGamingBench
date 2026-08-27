# Strategy: Skirmish

Build a **dark-fantasy tactical skirmish** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player commands a small, outnumbered squad through desperate grid-based
battles where every move is a commitment and every loss is permanent for the
fight. The fantasy is **grim tactical survival** — a handful of specialists
against a tide of enemies, where positioning is life and a single misread costs
a unit you cannot replace mid-battle. The tone channels *Into the Breach* meets
*Darkest Dungeon* at a smaller scale: limited palette, high contrast, tense
decisions. The best version makes the player feel like a cornered general
finding the one sequence of moves that turns impossible odds into a narrow
victory.

## What the Player Experiences

A moody title screen sets the dark-fantasy tone immediately. The player begins
and receives a brief tactical briefing — the squad's objective, the threat
ahead, the stakes — before the grid appears.

The battle is turn-based and deliberate. The player selects a unit, sees its
limited movement range light up on the grid, and commits it to a position.
Enemies are visible, aggressive, and numerous — the squad is always
outnumbered. After the player spends their actions, an End Turn command hands
control to the enemy, which advances with purpose: flanking, closing distance,
attacking when in range. Then control returns and the cycle repeats.

Combat is lethal and readable. Attacks require proximity or a clear range
indicator, reduce persistent HP, and kill. Dead units vanish from the board and
stop blocking or threatening. The player's squad members are specialists —
different movement ranges, attack patterns, HP pools, or abilities — so
choosing who moves where and who attacks what is the core decision space.

The battlefield itself adds tactical texture: terrain obstacles funnel movement,
hazards punish careless positioning, or objectives create time pressure beyond
simple elimination. Multiple battle layouts keep the experience from feeling
solved after one fight.

Victory comes from eliminating all enemies; defeat from losing the squad. Either
outcome lands on a styled result screen showing what happened, and the player
can retry or return to the title without relaunching. The entire arc — title,
briefing, battle, result — flows as one continuous authored experience.

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

# 策略：遭遇战（Strategy: Skirmish）

在 `/workspace/game/` 用 Godot 4 开发一款**黑暗奇幻战术遭遇战**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家指挥一支人数处于劣势的小队，穿越一场场绝境般的格状战斗，其中每一次移动都是一次不可撤回的承诺，每一次损失在这场战斗中都是永久的。核心幻想是**阴郁的战术求生**——寥寥数名专才对抗如潮的敌人，站位就是性命，而一次误判就会让你损失一个战斗中无法补充的单位。基调糅合了小规模版的 *Into the Breach* 与 *Darkest Dungeon*：受限的配色、高对比度、紧张的决策。最理想的版本让玩家感觉自己像一位被逼到墙角的将军，找到了那唯一一串把不可能的胜算扭转为险胜的行动序列。

## 玩家体验流程

一个氛围阴郁的标题画面立刻定下黑暗奇幻的基调。玩家开始游戏，收到一份简短的战术简报——小队的目标、前方的威胁、事关的利害——然后网格才出现。

战斗是回合制且审慎的。玩家选中一个单位，看到它有限的移动范围在网格上亮起，然后把它落定到某个位置。敌人可见、具有攻击性且数量众多——小队总是寡不敌众。玩家用完自己的行动后，一个"结束回合"指令把控制权交给敌方，敌方会带着明确意图推进：包抄、拉近距离、进入射程就攻击。随后控制权交回，循环重复。

战斗致命且清晰可读。攻击需要贴身或有明确的射程指示，会削减持续记录的 HP，并可致死。死亡单位从棋盘上消失，不再阻挡也不再构成威胁。玩家的队员都是专才——移动范围、攻击方式、HP 上限或能力各不相同——因此决定谁去哪里、谁打什么，就是核心的决策空间。

战场本身也增添了战术层次：地形障碍把移动收束进特定通道，危险区域惩罚草率的站位，或者目标设定带来超出单纯歼灭之外的时间压力。多种战斗布局让体验不会在打完一场后就被解穿。

歼灭所有敌人即胜利；失去整支小队则失败。任一结局都会落到一个精心设计的结算画面上，展示发生了什么，而玩家可以重试或返回标题画面，无需重新启动。整条弧线——标题、简报、战斗、结算——流畅地衔接为一段连续的、经过编排的体验。

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

