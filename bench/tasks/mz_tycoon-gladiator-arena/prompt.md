# Gladiator Arena

Build **Gladiator Arena**, a **gladiator arena management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player owns a gladiatorial arena in a fantasy-Roman setting, recruiting
fighters, training them, scheduling bouts, and upgrading the arena to attract
bigger crowds and richer sponsors. Each gladiator has stats, a fighting style,
and a personality — some are crowd favorites who draw spectators, others are
efficient killers who win but bore the audience. The tension is between
spectacle and survival: the crowd wants blood and drama, but dead gladiators
are expensive to replace. Betting adds a layer of risk-reward: the player can
wager on their own fighters for extra gold, but upsets happen. The tone is
sand-and-steel grandeur: roaring crowds, clashing weapons, and the drama of
the arena floor.

## What the Player Experiences

From the title screen the player starts a new arena season. The main view
shows the arena compound: training grounds, barracks, the arena floor, and a
management office. Time advances day by day toward scheduled fight nights.

Gladiators are recruited from a slave market or free-fighter pool — each has
combat stats (strength, speed, defense), a weapon preference, and a crowd
appeal rating. Training improves stats over days but costs food and trainer
fees. The player assigns training regimens: strength drills, sparring, or
showmanship practice.

Fight nights are scheduled on the calendar. The player picks matchups from
their roster against visiting challengers or rival arena fighters. During
fights, gladiators battle automatically based on their stats and style — the
player watches but cannot intervene. Crowd excitement builds with dramatic
moments (near-deaths, comebacks, finishing moves).

Revenue comes from ticket sales (based on crowd size), sponsor deals (based on
arena prestige), and betting winnings. Expenses include gladiator upkeep,
training costs, arena maintenance, and medical bills for injured fighters.

The game tracks gold, arena prestige, and season wins. A styled result screen
shows season statistics and champion gladiator highlights.

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

# 角斗竞技场（Gladiator Arena）

在 `/workspace/game/` 用 Godot 4 开发 **Gladiator Arena**，一款**角斗竞技场管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个奇幻罗马背景下拥有一座角斗竞技场，招募斗士、训练他们、安排比赛，并升级竞技场以吸引更大的观众和更阔绰的赞助商。每名角斗士都有属性、战斗风格和性格——有些是能招来看客的人群宠儿，有些则是能赢却让观众乏味的高效杀手。张力存在于观赏性与存活之间：人群想看鲜血和戏剧性，但死掉的角斗士替换起来很贵。博彩又加了一层风险与回报：玩家可以押注自己的斗士来多赚金币，但冷门翻盘时有发生。整体基调是黄沙与钢铁的恢弘：轰鸣的人群、交击的兵器，以及竞技场地面上的戏剧。

## 玩家体验流程

玩家从标题画面开始一个新的竞技场赛季。主视图展示竞技场建筑群：训练场、营房、竞技场地面和一间管理办公室。时间一天一天推进，走向已排定的比赛之夜。

角斗士从奴隶市场或自由斗士池中招募——每人都有战斗属性（力量、速度、防御）、武器偏好和人群吸引力评级。训练能在数日内提升属性，但要花费食物和教练费用。玩家为他们分配训练方案：力量操练、对练，或是表演技巧练习。

比赛之夜排在日历上。玩家从自己的名单中挑选对阵组合，对手是来访的挑战者或敌对竞技场的斗士。战斗过程中，角斗士依据各自属性与风格自动交战——玩家观看但无法干预。人群的兴奋度会随着戏剧性瞬间（濒死、反败为胜、终结技）而攀升。

收入来自门票销售（取决于观众规模）、赞助合约（取决于竞技场声望）以及博彩赢利。支出包括角斗士的日常开销、训练成本、竞技场维护，以及受伤斗士的医疗费用。

游戏会记录金币、竞技场声望和赛季胜场。一个经过美术处理的结算画面会展示赛季统计数据和冠军角斗士的高光时刻。

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

