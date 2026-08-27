# Rogue Joker Poker

Build **Rogue Joker Poker**, a compact **poker-hand roguelite score-chaser** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). The player builds a scoring engine from poker
hands, strange jokers, and shop upgrades to beat escalating blind targets in a
single high-stakes run.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player sits at a surreal felt table trying to beat a rising sequence of
score targets using nothing but poker hands and a growing roster of bizarre
jokers. Every round is a readable tactical choice: which cards to hold, which
to discard, when to spend a hand versus fishing for a better combination, and
how the current joker lineup warps the value of a flush, straight, pair, or
high-card play. The pressure comes from limited hands and discards per round,
escalating blind targets, and boss rules that twist the scoring math. The tone
is **sleek, strange, casino-arcade, and score-hungry**: felt tables, neon chips,
animated cards, odd joker portraits, compact tooltips, and clear score math
should make the game feel designed rather than assembled from default controls.

Do not clone a named commercial game's exact UI, art, copy, card names, or
iconography. Use original terminology, jokers, rules, palette, and screen
composition while preserving the broad genre fantasy of poker scoring plus
roguelite modifiers.

## What the Player Experiences

The run opens on a styled title screen that sets the casino-arcade mood and
invites the player to begin. Once started, the player faces a sequence of
blinds with rising score targets. Each round deals a hand of cards showing
rank, suit, and selection state. The player studies the hand, selects cards to
form a poker combination, and either plays them to score or discards unwanted
cards to draw replacements, burning limited resources either way.

When a hand is played, the scoring moment unfolds visibly: the poker hand type
is identified, base chips and multiplier are calculated, and then each active
joker fires in sequence, visibly altering the math. The score animates toward
the blind target. The player watches the joker row like a machine, learning
which combinations trigger which bonuses.

Between blinds, a shop offers new jokers, deck modifications, and upgrades.
Purchases reshape the scoring engine for future rounds. The run escalates
through small blinds, big blinds, and boss blinds. Boss rounds introduce
special rules that force the player to rethink hand evaluation: a disabled
suit, a discard tax, a hand-size cap, or a reversed joker.

Victory means beating the final target. Defeat means running out of hands
below a blind. Either way, a styled result screen offers retry or return to
title.

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

# 盗贼小丑扑克（Rogue Joker Poker）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Rogue Joker Poker**，一款小而精的**扑克牌型 Roguelite 刷分游戏**。玩家用扑克牌型、稀奇古怪的小丑牌与商店升级搭建出一台计分引擎，在一轮高风险的游戏中击破不断升级的盲注目标。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家坐在一张超现实的绒布赌桌前，仅凭扑克牌型和一支不断扩充的古怪小丑牌阵容，去击破一连串水涨船高的分数目标。每一轮都是一次清晰可读的战术选择：留哪些牌、弃哪些牌、何时用掉一次出牌机会而不是继续钓一手更好的组合，以及当前的小丑牌阵容如何扭曲同花、顺子、对子或高牌打法的价值。压力来自每轮有限的出牌与弃牌次数、不断升级的盲注目标，以及扭曲计分算法的 Boss 规则。基调是**利落、诡奇、赌场街机风、渴求分数**：绒布赌桌、霓虹筹码、动态卡牌、古怪的小丑肖像、紧凑的提示框，以及清晰的计分算式，应当让这款游戏显得是被设计出来的，而不是用默认控件拼凑出来的。

不要克隆任何具名商业游戏的确切 UI、美术、文案、卡牌名称或图标体系。请使用原创的术语、小丑牌、规则、配色与画面构图，同时保留"扑克计分加 Roguelite 修正"这一大类的类型幻想。

## 玩家体验流程

一轮游戏以一个精心设计的标题画面开场，定下赌场街机的情绪，并邀请玩家开始。开始之后，玩家会面对一连串分数目标不断攀升的盲注。每一轮会发一手卡牌，显示点数、花色与选中状态。玩家研究手牌，选出卡牌组成一个扑克组合，然后要么打出去计分，要么弃掉不想要的牌以抽取替补——两种做法都会烧掉有限的资源。

当一手牌被打出时，计分的瞬间会可见地展开：先识别扑克牌型，计算基础筹码与倍率，然后每张激活的小丑牌依次生效，肉眼可见地改变算式。分数会朝盲注目标动画攀升。玩家像看一台机器那样观察小丑牌行列，逐渐学会哪些组合会触发哪些加成。

盲注之间，一家商店会提供新的小丑牌、牌组改造与升级。购买会为后续轮次重塑计分引擎。一轮游戏会经由小盲、大盲与 Boss 盲逐级升级。Boss 轮会引入迫使玩家重新思考牌型评估的特殊规则：某个花色被禁用、弃牌需要额外代价、手牌上限被压缩，或某张小丑牌被反转。

击破最终目标即胜利。在某个盲注之下用尽出牌次数则为失败。无论哪种结局，一个精心设计的结算画面都会提供重试或返回标题画面的选项。

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

