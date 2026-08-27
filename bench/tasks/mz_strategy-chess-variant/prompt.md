# Chess Variant

Build **Chess Variant**, a **tactical chess game with cooldowns and terrain** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

Classic chess pieces gain special abilities on cooldown timers, and the board
itself becomes terrain — some tiles heal, some damage, some block movement.
The result is a game that rewards chess intuition but demands new tactical
thinking: a knight's fork matters less when the bishop can teleport every four
turns, and controlling the healing fountain tile can swing an endgame. A
campaign mode unlocks new pieces and abilities level by level, teaching the
player each mechanic before combining them into complex puzzles. The tone is
medieval-fantasy: stone boards, glowing runes, and pieces that feel like
enchanted warriors.

## What the Player Experiences

From the title screen the player enters a campaign map with sequential levels.
Each level is a chess puzzle or skirmish on a themed board with specific terrain
tiles and piece rosters. Early levels teach one mechanic at a time — a piece
with a dash ability, a tile that blocks, a cooldown that must be tracked.

During play the board shows terrain overlays on specific tiles: green for
healing, red for damage, grey for impassable. Pieces move by standard chess
rules but each also has a unique ability (charge, shield, teleport, area
attack) shown as a button with a cooldown counter. Using an ability consumes
the turn and starts the cooldown.

The AI opponent uses the same rules and abilities. Capturing the enemy king
wins; losing yours loses. The campaign escalates by introducing new piece types
with new abilities and more complex terrain layouts. Completing a level unlocks
the next and sometimes adds a new piece to the player's roster for future
levels.

A styled result screen shows victory or defeat with the option to retry or
advance.

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

# 变体国际象棋（Chess Variant）

在 `/workspace/game/` 用 Godot 4 开发 **Chess Variant**，一款**带冷却与地形机制的战术国际象棋游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

经典的国际象棋棋子获得了带冷却计时的特殊能力，而棋盘本身也变成了地形——有的格子治疗，有的造成伤害，有的阻挡移动。其结果是一款既奖励国际象棋直觉、又要求全新战术思维的游戏：当主教每四回合就能传送一次时，骑士的双叉攻击就没那么要紧了；而控制住治疗泉眼所在的格子，可能左右整个残局。战役模式会逐关解锁新棋子与新能力，在把各项机制组合成复杂谜题之前先逐一教会玩家。基调是中世纪奇幻：石制棋盘、发光符文，以及仿佛被附魔战士般的棋子。

## 玩家体验流程

玩家从标题画面进入一张包含顺序关卡的战役地图。每个关卡都是一道国际象棋谜题或一场遭遇战，发生在带有特定地形格与棋子阵容的主题棋盘上。前期关卡一次只教一项机制——一个带冲刺能力的棋子、一个阻挡的格子、一段必须留意的冷却。

游玩时，棋盘会在特定格子上显示地形覆盖层：绿色代表治疗，红色代表伤害，灰色代表不可通行。棋子按标准国际象棋规则移动，但每个棋子还各有一项独特能力（冲锋、护盾、传送、范围攻击），以一个带冷却计数的按钮呈现。使用能力会消耗该回合并开始冷却。

AI 对手使用同样的规则与能力。吃掉敌方国王即胜利；自己的国王被吃则失败。战役通过引入具备新能力的新棋子类型以及更复杂的地形布局来逐步升级难度。完成一关会解锁下一关，有时还会为玩家在后续关卡中的阵容添加一个新棋子。

一个精心设计的结算画面会展示胜利或失败，并提供重试或继续前进的选项。

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

