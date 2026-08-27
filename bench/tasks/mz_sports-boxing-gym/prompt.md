# Sports Boxing Gym

Build a **Sports Boxing Gym** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a boxer rising through the ranks, reading opponent tells, timing
dodges and counters, and managing stamina across multi-round bouts. The fantasy
is the sweet science: not brute force but pattern recognition, knowing when to
slip a jab and answer with a hook. Tension comes from stamina — every punch
thrown and every dodge costs energy, and a tired boxer drops their guard. Between
fights, training mini-games improve stats and unlock new techniques.

## What the Player Experiences

1. **Title Screen** — A boxing ring under spotlights with the game name in bold
   block letters, a play button styled as a bell.
2. **Career Menu** — The player sees their boxer's stats, upcoming opponent, and
   training options. A fight card shows the next bout with the opponent's
   silhouette and record.
3. **Training** — Before each fight, the player completes training mini-games:
   heavy bag (timing combos), speed bag (rhythm clicking), jump rope (pattern
   matching). Training improves power, speed, or stamina stats.
4. **The Fight** — Side-view boxing with two fighters. The opponent telegraphs
   attacks with visible tells (shoulder dip, foot shift, glove pull-back). The
   player must read the tell and respond: dodge high/low, block, or counter.
5. **Punch Mechanics** — The player throws jabs, hooks, and uppercuts with
   different keys. Each punch type has different speed, power, and stamina cost.
   Combos (sequences of punches) deal bonus damage.
6. **Stamina System** — A stamina bar depletes with every action. Low stamina
   slows punches and weakens blocks. Between rounds, stamina partially recovers.
   The player must pace themselves across rounds.
7. **Career Progression** — Winning fights advances rank. Opponents get harder
   with faster tells and more varied patterns. Reaching the championship requires
   mastering all defensive techniques.

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

# 拳击馆（Sports Boxing Gym）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**拳击馆**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一位在排名中步步高升的拳手，读取对手的预备动作、把握闪避与反击的时机，
并在多回合的比赛中管理体力。这里的幻想是"甜美的科学"：靠的不是蛮力，而是模式
识别——知道何时该躲开一记刺拳，并用一记勾拳回敬。张力来自体力——每一次出拳、
每一次闪避都消耗能量，而疲惫的拳手会放下防守。在两场比赛之间，训练小游戏能提升
属性并解锁新技术。

## 玩家体验流程

1. **标题画面** —— 聚光灯下的拳击台，游戏名称采用粗厚的方块字母，以及一个做成
   铃铛样式的开始按钮。
2. **生涯菜单** —— 玩家可以看到自己拳手的属性、即将迎战的对手以及训练选项。
   一张赛程卡展示下一场比赛，附有对手的剪影和战绩。
3. **训练** —— 每场比赛前，玩家要完成训练小游戏：沙袋（连击时机）、速度球
   （节奏点击）、跳绳（模式匹配）。训练可以提升力量、速度或体力属性。
4. **比赛** —— 侧视视角的拳击，台上有两名拳手。对手会用可见的预备动作预告攻击
   （沉肩、移步、收拳）。玩家必须读出这些预备动作并应对：上/下闪避、格挡，
   或者反击。
5. **出拳机制** —— 玩家用不同的按键打出刺拳、勾拳和上勾拳。每种拳的速度、力量
   和体力消耗各不相同。连击（一连串出拳）能造成额外伤害。
6. **体力系统** —— 体力条随每一个动作而下降。体力低时出拳变慢、格挡变弱。
   回合之间体力会部分恢复。玩家必须在各回合之间控制好节奏。
7. **生涯进程** —— 赢下比赛可以提升排名。对手会变得更难对付，预备动作更快、
   模式更多变。想打进冠军赛，必须精通所有的防守技术。

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

