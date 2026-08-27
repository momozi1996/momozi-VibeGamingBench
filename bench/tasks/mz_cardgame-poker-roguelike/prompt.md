# Cardgame Poker Roguelike

Build a Cardgame Poker Roguelike as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A roguelike scoring game built on poker hand evaluation. The player is dealt
cards and must form poker hands (pairs, straights, flushes) to score points
against escalating blind targets. The twist: collectible Joker cards modify
scoring rules in wild ways — one might triple the value of all hearts, another
might make every pair count as a full house. Between rounds, a shop sells new
Jokers, card enhancements, and consumable items. The fantasy is discovering
absurd scoring combos that turn a humble pair of twos into a million-point
hand. Fail to meet the blind and the run ends.

## What the Player Experiences

1. **Title Screen** — A casino-noir aesthetic with the game name in gold
   embossed lettering on green felt, animated card shuffling in the background,
   and New Run / Stats buttons. No plain HTML grey.
2. **The Hand** — The player is dealt 8 cards from a standard deck. They select
   up to 5 cards to form a poker hand and submit it for scoring. Remaining
   cards can be discarded and redrawn (limited discards per round).
3. **Scoring** — Each hand type has a base chip value and multiplier (e.g.,
   Pair = 10 chips x2, Flush = 35 chips x4). Jokers and enhancements modify
   these values. The score animates with each modifier applied sequentially,
   building dramatic tension.
4. **Blinds** — Each round has a target score (the blind). Small Blind, Big
   Blind, and Boss Blind escalate. The player has multiple hands per round to
   meet the target. Failing to reach the blind ends the run.
5. **Joker Cards** — Up to 5 Joker slots. Each Joker has a unique rule-bending
   effect with illustrated art and a description. Jokers are purchased from
   the shop or earned from Boss Blinds. Synergies between Jokers create
   exponential scoring potential.
6. **Shop** — Between rounds, spend earned money on new Jokers, card
   enhancements (foil, holographic, polychrome — each with scoring bonuses),
   vouchers (permanent upgrades), or booster packs (new playing cards).
7. **Boss Blinds** — Special blinds with debuff conditions (e.g., "all clubs
   are face-down", "no discards this round", "first hand played is
   debuffed"). The player must adapt their strategy to the boss condition.

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

# 扑克 Roguelike（Cardgame Poker Roguelike）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`）：开发一个扑克 Roguelike 卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款建立在扑克牌型判定之上的 Roguelike 计分游戏。玩家被发到牌，必须组成牌型
（对子、顺子、同花）来得分，以达成不断攀升的底注目标。妙处在于：可收集的小丑牌
会以极其疯狂的方式改写计分规则——有的会让所有红桃的数值变成三倍，有的会让每一个
对子都算作葫芦。轮次之间，商店出售新的小丑牌、卡牌强化和消耗品。这份幻想在于：
发现荒诞离奇的计分组合，把区区一对 2 变成百万分的一手牌。达不到底注，这一轮就
结束了。

## 玩家体验流程

1. **标题画面** —— 赌场黑色电影风格，游戏名以烫金浮雕字体呈现在绿色台面呢上，
   背景中有洗牌动画，以及新的一轮 / 统计按钮。演出 GameX其灰色。
2. **手牌** —— 玩家从一副标准牌组中拿到 8 张牌。他们最多选出 5 张组成一个扑克
   牌型并提交计分。剩下的牌可以弃掉并重抽（每轮弃牌次数有限）。
3. **计分** —— 每种牌型都有基础筹码值和倍率（例如：对子 = 10 筹码 x2，同花 =
   35 筹码 x4）。小丑牌和强化会修改这些数值。分数会随着各个修正项依次生效而
   逐步累加显示，营造出戏剧性的张力。
4. **底注** —— 每一轮都有一个目标分数（底注）。小盲注、大盲注和 Boss 盲注依次
   攀升。玩家每轮有多手牌来达成目标。达不到底注，这一轮就结束。
5. **小丑牌** —— 最多 5 个小丑牌槽位。每张小丑牌都有独特的破坏规则效果，配有
   插画和说明文字。小丑牌可从商店购买，或从 Boss 盲注中获得。小丑牌之间的协同
   会造就指数级的计分潜力。
6. **商店** —— 轮次之间，把赚到的钱花在新的小丑牌、卡牌强化（箔面、全息、多彩
   ——各自带有计分加成）、券票（永久升级）或补充包（新的扑克牌）上。
7. **Boss 盲注** —— 带有减益条件的特殊底注（例如："所有梅花均为背面朝下"、
   "本轮不能弃牌"、"打出的第一手牌被减益"）。玩家必须针对该 Boss 条件调整策略。

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

