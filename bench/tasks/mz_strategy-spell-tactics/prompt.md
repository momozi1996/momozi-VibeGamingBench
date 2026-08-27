# Spell Tactics

Build **Spell Tactics**, a **grid-based wizard duel tactics game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

Two wizards face off on a destructible grid arena, casting spells from a hand
of cards while managing mana and positioning. Every spell has a shape — lines,
cones, areas — that interacts with the grid terrain: fire burns forests, ice
freezes water tiles, lightning chains through metal. The tension is spatial:
the perfect spell in the wrong position wastes mana, and the opponent is always
repositioning to dodge or set up their own combo. Terrain destruction reshapes
the arena mid-fight, turning a symmetrical duel into an asymmetric puzzle. The
tone is arcane and dramatic — glowing runes, crackling energy, and tiles that
shatter into particles.

## What the Player Experiences

From the title screen the player picks a spell deck from unlocked cards and
enters a duel. The arena is a grid with varied terrain tiles: stone, forest,
water, metal, and empty pits. Each wizard starts on opposite sides with full
HP and mana.

Turns alternate. On each turn the player draws a spell card, gains mana, and
can move their wizard up to two tiles then cast one spell. Spells cost mana
and affect grid areas: a fireball hits a 3x1 line, an ice wall creates
blocking terrain, a lightning bolt chains between metal tiles. Hitting the
opponent deals damage; hitting terrain transforms or destroys it.

The opponent AI plays by the same rules, choosing spells and positions
tactically. As the duel progresses, terrain destruction opens new lines of
sight and closes others, forcing constant adaptation.

The duel ends when one wizard reaches zero HP. A styled result screen shows
the winner, damage dealt, spells cast, and offers a rematch or return to the
menu. Winning duels unlock new spell cards for future deck-building.

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

# 法术战术（Spell Tactics）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Spell Tactics**，一款**基于网格的法师对决战术游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两名法师在一个可破坏的格状竞技场上对峙，一边管理法力与站位，一边从手牌中施放法术。每个法术都有形状——直线、锥形、区域——并会与网格地形互动：火焰烧毁森林，冰霜冻结水域图块，闪电在金属之间连锁。张力是空间性的：完美的法术放在错误的位置就是浪费法力，而对手始终在移动，或为躲闪，或为铺设自己的连击。地形破坏会在战斗中途重塑竞技场，把一场对称的对决变成一道不对称的谜题。基调是奥术而戏剧化的——发光的符文、噼啪作响的能量，以及碎裂成粒子的图块。

## 玩家体验流程

玩家从标题画面在已解锁的卡牌中挑选一套法术牌组，然后进入一场对决。竞技场是一张带有多样地形图块的网格：石地、森林、水域、金属，以及空的深坑。两名法师从相对两侧出发，HP 与法力全满。

回合交替进行。每个回合玩家抽一张法术卡、获得法力，并可以把自己的法师移动最多两格，然后施放一个法术。法术消耗法力并影响网格区域：火球术命中 3x1 的一条直线，冰墙创造出阻挡地形，闪电则在金属图块之间连锁。命中对手造成伤害；命中地形则会将其转化或摧毁。

对手 AI 遵循同样的规则，会战术性地选择法术与位置。随着对决推进，地形破坏会开辟出新的视线，也会封闭掉旧的视线，迫使双方不断调整。

当一名法师的 HP 归零时，对决结束。一个精心设计的结算画面会展示胜者、造成的伤害、施放的法术数量，并提供再战一局或返回菜单的选项。赢下对决会解锁新的法术卡，供后续构筑牌组使用。

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

