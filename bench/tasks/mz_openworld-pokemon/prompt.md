# Open World: WildRealm

Build a **creature-capture open-world RPG** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores a vibrant open world, stumbles upon wild creatures in tall
grass, and engages them in turn-based battles -- capturing, training, and
growing a personal squad. The interesting tension is resource management across
encounters: every capture ball spent, every HP lost, and every skill cooldown
used is a commitment that carries forward until the player finds a healer. The
pressure escalates as the player ventures further from town into tougher
territory, and the payoff is discovering a rare creature or finally defeating
the gym leader to unlock the next region. The game should feel **bright,
adventurous, and nostalgic** -- think creature-taming meets *A Short Hike* at
a smaller scale.

## What the Player Experiences

1. **Title and Entry** -- A charming title screen sets the tone with the game
   name, a scenic background, and a clear start button. The player hits start
   and arrives in a small town -- a hub with a healer, a trainer NPC, and a
   path leading into the wilds.

2. **Open-World Exploration** -- The player walks freely across a large map
   with at least three visually distinct regions: grassy fields, a small town,
   and a locked area beyond a natural barrier. Tall grass signals danger:
   stepping into it has a chance to trigger a wild creature encounter. The
   world reads clearly at a glance -- each region has its own terrain, palette,
   and props.

3. **Encounter and Battle** -- A brief transition effect whisks the player into
   a turn-based combat scene. The player sees both combatants with HP bars,
   levels, and skill buttons. Attacking triggers visible motion and animated HP
   depletion. The player can also throw a capture ball (visible arc, shake
   animation, success/failure feedback) or flee. Wild creatures vary in species
   and level.

4. **Growth and Progression** -- Defeating opponents yields experience; the
   creature levels up with visible feedback when enough XP accumulates. The
   player's squad grows stronger over time, and captured creatures join the
   roster.

5. **NPC Interaction** -- In town, a trainer challenges the player to a forced
   battle, and a healer restores the squad. Dialog appears in a styled speech
   panel. Defeating the gym leader awards a badge that unlocks the previously
   blocked region, opening new territory to explore.

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

# 开放世界：WildRealm（Open World: WildRealm）

在 `/workspace/game/` 用 Godot 4 开发一个**生物收集类开放世界 RPG**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家探索一个生机勃勃的开放世界，在高草丛中偶遇野生生物，与它们展开回合制
战斗——捕捉、培养并壮大一支属于自己的队伍。有趣的张力在于跨遭遇战的资源
管理：每消耗一颗捕捉球、每损失一点 HP、每用掉一次技能冷却，都是一种会一直
延续到玩家找到治疗师之前的投入。随着玩家离小镇越来越远、进入更艰难的地界，
压力不断攀升，而回报则是发现一只稀有生物，或者终于击败道馆馆主、解锁下一个
区域。游戏的感觉应当是**明亮、充满冒险感、令人怀旧**的——可以想象成小体量的
生物驯养结合 *A Short Hike*。

## 玩家体验流程

1. **标题与进入** —— 一个讨人喜欢的标题画面通过游戏名称、一幅风景背景和一个
   清晰的开始按钮来奠定基调。玩家按下开始，抵达一座小镇——一个枢纽，有治疗师、
   一位训练师 NPC，以及一条通往荒野的道路。

2. **开放世界探索** —— 玩家在一张大地图上自由行走，地图至少包含三个视觉上
   截然不同的区域：草原、一座小镇，以及一片位于天然屏障之外的封锁区域。高草丛
   意味着危险：踏入其中有一定概率触发野生生物遭遇战。整个世界一眼就能读懂——
   每个区域都有自己的地形、配色和场景道具。

3. **遭遇与战斗** —— 一个短暂的转场效果把玩家带入回合制战斗场景。玩家可以看到
   双方战斗者，以及 HP 条、等级和技能按钮。攻击会触发可见的动作和 HP 条的
   动画式下降。玩家也可以投出捕捉球（可见的抛物线弧、晃动动画、成功/失败反馈）
   或者逃跑。野生生物的物种和等级各不相同。

4. **成长与进程** —— 击败对手可获得经验；累积足够 XP 后，生物会伴随可见的
   反馈升级。玩家的队伍随时间变强，捕获的生物会加入名册。

5. **NPC 互动** —— 在镇上，一位训练师会向玩家发起一场强制战斗，而治疗师会
   恢复整支队伍。对话显示在一个有设计感的对话面板中。击败道馆馆主会奖励一枚
   徽章，解锁此前被封锁的区域，开放新的疆域供玩家探索。

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

