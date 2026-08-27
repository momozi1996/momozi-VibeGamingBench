# Strategy: Beast Clash

Build a **single-lane real-time animal-war strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

Two animal kingdoms clash across a single contested lane. The player commands
one side, spending food to send creatures marching toward the enemy den while
the opponent does the same. Every kill feeds growth, growth unlocks evolution,
and evolution turns a trickle of small critters into a roaring tide of apex
predators. The tension lives in the economy: food is scarce, creatures cost
real resources, and the wrong spend at the wrong moment hands the lane to the
enemy. The tone is lively but fierce — a sunlit savanna-and-jungle frontier
where war escalates from scurrying critters to towering, screen-shaking beasts.

## What the Player Experiences

From the title screen the player picks a kingdom — each feels like a real
faction with its own animals, identity, and fighting temperament, so the choice
is a strategy decision, not a skin swap.

The battle unfolds on a side-scrolling lane between two dens. Food ticks up
over time and the player spends it to send creatures out of their den. Each
creature marches on its own toward the enemy, clashing with whatever it meets
and pushing the front line back and forth. The player never pilots a creature
directly; the strategy is about when to spend, which creature to send, when to
invest in gatherers for more food, and when to save up for evolution.

Creatures come in distinct roles — sturdy blockers that hold the front, ranged
strikers that punish from behind, and gatherers that keep the economy flowing.
The best armies use cooperation: blockers absorb hits while ranged beasts deal
damage safely and gatherers sustain the pressure. The enemy fields its own mix
and grows more dangerous over time, so a static plan loses.

As skirmishes are won, a growth track fills. Reaching thresholds evolves the
kingdom into a new era, unlocking larger, fiercer creatures and visibly
upgrading the den. A later-era beast plainly outclasses an opening-era critter
and expands tactics rather than simply replacing everything before it.

Throughout the battle the player reads the war at a glance — food, evolution
progress, and the health of each den. Victory comes when the enemy den is
destroyed; defeat when the player's own den falls. Each ending lands on a
styled result screen that makes the outcome unmistakable and lets the player
fight again without restarting the application.

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

# 策略：兽群冲突（Strategy: Beast Clash）

在 `/workspace/game/` 用 Godot 4 开发一款**单路实时动物战争策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两个动物王国在一条争夺激烈的单路上碰撞。玩家指挥其中一方，花费食物派遣生物向敌方巢穴进军，对手也在做同样的事。每一次击杀都会喂养成长，成长解锁进化，而进化把涓涓细流般的小动物变成顶级掠食者的滔天巨浪。张力活在经济里：食物稀缺，生物要消耗真实资源，在错误的时机做出错误的花费就会把这条路让给敌人。基调活泼却凶悍——一片阳光普照的草原与丛林边境，战争从窜来窜去的小动物一路升级为高大到震屏的巨兽。

## 玩家体验流程

玩家从标题画面挑选一个王国——每一个都像一个真正的阵营，拥有自己的动物、身份认同与作战气质，因此这个选择是一次策略决定，而不是换个皮肤。

战斗在两座巢穴之间的横向卷轴路线上展开。食物随时间逐渐积累，玩家花费食物把生物从自家巢穴派出。每个生物都会自行向敌方进军，与遇到的一切交战，把前线来回推移。玩家从不直接操控某个生物；策略在于何时花费、派哪种生物、何时投资采集者以获取更多食物，以及何时攒资源用于进化。

生物有各自鲜明的定位——顶住前线的坚实阻挡者、从后方施加惩罚的远程打击者，以及维持经济运转的采集者。最强的军队靠的是配合：阻挡者承受伤害，远程巨兽安全输出，采集者则维持压制力。敌人也会派出自己的组合，并随时间变得更加危险，所以一成不变的方案必输。

随着一场场小规模交锋获胜，成长进度条会逐渐填满。达到阈值后，王国将进化到新的纪元，解锁更大更凶猛的生物，并让巢穴的外观明显升级。后期纪元的巨兽显然远胜开局纪元的小动物，而且是拓展战术，而不是简单地取代此前的一切。

在整场战斗中，玩家都能一眼读懂战况——食物、进化进度，以及双方巢穴的血量。摧毁敌方巢穴即胜利；自家巢穴陷落则失败。每种结局都落到一个精心设计的结算画面上，让结果一目了然，并让玩家无需重启应用程序就能再战一场。

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

