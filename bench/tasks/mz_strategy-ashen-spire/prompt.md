# Strategy: Ashen Spire

Build **Ashen Spire**, a compact **dark-fantasy roguelike deckbuilding card
battler** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam as
a polished vertical slice.

## Core Vision

The fantasy is climbing a cursed tower one floor at a time with nothing but a
thin deck of cards and whatever you scavenge along the way. Each combat is a
small tactical puzzle: energy is scarce, the enemy telegraphs its next move, and
every card played reshapes the odds for the rest of the run. The interesting
tension is that the deck is both your weapon and your liability -- adding
powerful cards dilutes consistency, while staying lean means fewer answers to
escalating threats. The pressure comes from reading enemy intent, rationing
energy across attack and defense, and gambling on which reward cards will pay off
three fights from now. The risk is always that one greedy pick or one misread
intent leaves you one hit from death with no block in hand.

## What the Player Experiences

The player arrives at a dark, atmospheric title screen that sets the tone of a
grim tower ascent. Starting a run reveals a branching route map -- a web of
nodes stretching upward toward a final confrontation, with forks that force the
player to choose which dangers to face and which to skip.

Entering a combat node drops the player into a turn-based card duel. A small
hand is drawn, energy refills, and the enemy displays what it intends to do next
turn. The player spends energy playing cards -- strikes that chip away at the
enemy, guards that raise a shield, and stranger tactical effects that poison,
burn, draw extra cards, or bend the rules. When the hand is spent or the player
is satisfied, ending the turn lets the enemy act, then a fresh hand is drawn and
the cycle repeats.

Winning a fight offers a choice of new cards to weave into the deck, each with
its own identity and cost. The map updates, the player picks the next node, and
the deck grows richer and riskier with every floor. Different encounters reveal
different pixel monsters with distinct silhouettes and behaviors, so no two
climbs feel identical.

The run resolves at the top: defeat the boss and a styled victory screen
celebrates the climb, or fall to zero health anywhere along the way and a defeat
screen marks how far you got. Either way, the player can retry or return to the
title without restarting the application.

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

# 策略：灰烬尖塔（Strategy: Ashen Spire）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ashen Spire**，一款小而精的**黑暗奇幻 Roguelike 构筑牌组类卡牌战斗游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

核心幻想是仅凭一副单薄的牌组和沿途搜刮到的东西，一层一层地攀爬一座受诅咒的高塔。每场战斗都是一道小型战术谜题：能量稀缺，敌人会预告自己的下一步行动，而每张打出的牌都会重塑这一轮余下部分的胜算。有意思的张力在于：牌组既是你的武器，也是你的负累——加入强力卡牌会稀释稳定性，而保持精简则意味着面对不断升级的威胁时手段太少。压力来自解读敌人意图、在进攻与防守之间分配能量，以及赌哪张奖励卡牌会在三场战斗之后开花结果。风险始终存在：一次贪心的选牌，或一次误读的意图，就可能让你手里没有格挡、离死亡只差一击。

## 玩家体验流程

玩家进入一个黑暗而富有氛围感的标题画面，为这场阴森的登塔之旅定下基调。开始一轮后，会展现一张分叉的路线图——节点织成的网络向上延伸，通向最终对决，其间的分岔迫使玩家选择要面对哪些危险、要避开哪些危险。

进入战斗节点后，玩家被投入一场回合制卡牌对决。抽出一手少量卡牌，能量回满，敌人则显示它下一回合打算做什么。玩家消耗能量打牌——削减敌人血量的打击牌、抬起护盾的防御牌，以及各种更奇特的战术效果：中毒、燃烧、额外抽牌，或是扭曲规则。当手牌用尽或玩家觉得满意时，结束回合让敌人行动，随后抽出新的一手牌，循环继续。

赢下一场战斗后，会提供若干新卡牌供玩家编入牌组，每张都有自己的特性与费用。地图随之更新，玩家挑选下一个节点，牌组则随着每一层变得更丰富也更危险。不同遭遇会出现不同的像素怪物，剪影与行为各具特色，因此没有两次攀爬的感受是相同的。

一轮的结局在塔顶揭晓：击败 Boss，一个精心设计的胜利画面为这次攀登喝彩；或者在途中任何地方血量归零，失败画面记录下你走到了多远。无论哪种结局，玩家都可以重试或返回标题画面，无需重启应用程序。

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

