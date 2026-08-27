# Cardgame Gwent War

Build a Cardgame Gwent War as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A row-based card battle game where bluffing is as important as card strength.
Each player places unit cards into one of three combat rows (melee, ranged,
siege), and the side with the higher total strength at round's end wins. But
matches are best-of-three — winning a round early by dumping your hand leaves
you empty for the next. The core tension is knowing when to push and when to
pass, baiting the opponent into overcommitting. Multiple faction decks with
unique abilities and a campaign of escalating AI opponents provide depth. The
fantasy is the poker-face moment of passing with a slim lead, daring the
opponent to waste cards chasing it.

## What the Player Experiences

1. **Title Screen** — A medieval war-table aesthetic with the game name in
   iron-forged lettering, faction banners flanking the sides, and Campaign /
   Quick Match / Deck Builder buttons. No plain HTML grey.
2. **Deck Builder** — At least 3 factions (Northern Realms, Monsters, Elves)
   each with 15+ unique cards. The player builds a deck of exactly 25 cards
   from their chosen faction plus neutral cards. Each card shows art, strength
   value, row placement, and any special ability.
3. **The Board** — Three rows per side (melee/ranged/siege) displayed
   horizontally. Cards are played from hand into their designated row. Total
   strength per row and overall total are shown. The opponent's rows mirror
   above.
4. **Turn Structure** — Players alternate playing one card or passing. Once
   both pass, the round ends. The side with higher total strength wins the
   round. Best of 3 rounds wins the match. A round tracker shows current
   standing.
5. **Bluffing and Passing** — The player can pass at any time, locking in their
   current strength. The opponent must then decide whether to keep playing
   cards (wasting resources for future rounds) or also pass. This creates
   rich mind-game dynamics.
6. **Special Abilities** — Cards have abilities: Spy (played on opponent's side
   but draws 2 cards), Medic (resurrects a card from discard), Weather (reduces
   all cards in a row to 1 strength), Commander's Horn (doubles a row's
   strength), Decoy (returns a played card to hand). Each ability has a
   distinct visual effect.
7. **Campaign** — A series of AI opponents with increasing difficulty and
   unique deck strategies. Winning matches earns new cards for the player's
   collection. A world map shows progression through the campaign.

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

# 昆特战争（Cardgame Gwent War）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个昆特战争卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款以排为基础的卡牌对战游戏，其中虚张声势与卡牌强度同等重要。双方各自把单位牌
打进三个战斗排之一（近战、远程、攻城），回合结束时总战力更高的一方胜出。但对局
采用三局两胜——过早地倾尽手牌赢下一轮，会让你在下一轮无牌可打。核心张力在于
判断何时该推进、何时该过牌，诱使对手过度投入。多个拥有独特能力的阵营牌组，以及
一条难度层层升级的 AI 对手战役，共同带来深度。这份幻想在于：以微弱优势过牌时那
一刻的扑克脸，赌对手会为追平而白白挥霍手牌。

## 玩家体验流程

1. **标题画面** —— 中世纪战争沙盘美学，游戏名以铁铸字体呈现，两侧列着阵营旗帜，
   并有战役 / 快速对战 / 牌组编辑器按钮。演出 GameX其灰色。
2. **牌组编辑器** —— 至少 3 个阵营（北方王国、怪物、精灵），每个阵营各有 15 张
   以上独特卡牌。玩家从所选阵营加上中立卡中构建一副恰好 25 张的牌组。每张卡牌
   展示卡面美术、战力数值、所属排位，以及任何特殊能力。
3. **棋盘** —— 每一方三排（近战/远程/攻城），横向排布。卡牌从手牌打进各自指定的
   排。每排战力和总战力都会显示。对手的各排在上方镜像呈现。
4. **回合结构** —— 双方轮流打出一张卡或过牌。一旦双方都过牌，该轮结束。总战力
   更高的一方赢下该轮。三局两胜赢下整场对局。一个轮次追踪器显示当前战况。
5. **虚张声势与过牌** —— 玩家可以随时过牌，锁定自己当前的战力。对手随后必须决定
   是继续打牌（为后续轮次白白消耗资源）还是同样过牌。这造就了丰富的心理博弈。
6. **特殊能力** —— 卡牌拥有各种能力：间谍（打在对手一侧，但抽 2 张牌）、军医
   （从弃牌堆复活一张卡）、天气（把某一排所有卡的战力降为 1）、指挥官号角
   （使某一排战力翻倍）、诱饵（把一张已打出的卡收回手牌）。每种能力都有独特的
   视觉效果。
7. **战役** —— 一系列难度递增、牌组策略各异的 AI 对手。赢下对局会为玩家的收藏
   赢得新卡牌。一张世界地图展示战役进度。

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

