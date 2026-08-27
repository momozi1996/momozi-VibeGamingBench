# Open-World Bounty

Build a **2D open-world bounty hunter game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a lone hunter roaming a lawless frontier, picking contracts off a
weathered quest board and tracking dangerous marks across hostile terrain. The
fantasy is **pursuit under uncertainty** -- each bounty is a commitment to
venture deeper into unfamiliar ground, and the interesting tension is that the
hunter must read the landscape, manage limited resources, and choose when to
engage versus when to retreat. The pressure comes from escalating target
difficulty, dwindling supplies, and the knowledge that a failed hunt means
walking back empty-handed. The risk is always that the next mark fights harder
than expected, or that the hunter spent too much on an easy bounty and has
nothing left for the real threat.

## What the Player Experiences

1. **Title and Entry** -- A gritty, western-fantasy title screen sets the tone.
   The player hits start and arrives in a frontier town -- a hub with a tavern,
   a quest board, and a handful of NPCs who sell gear or patch wounds.

2. **Picking a Contract** -- The quest board displays available bounties, each
   with a target portrait, a difficulty rating, and a gold reward. The player
   reads the cards, weighs risk against payout, and commits to a mark. The
   chosen bounty becomes the active hunt, and the world shifts focus toward
   tracking.

3. **The Hunt** -- A compass or directional marker guides the player out of
   town and into the wilds. The world has multiple distinct regions -- forest
   hideouts, bandit camps, rocky canyons -- and the target waits somewhere
   inside, patrolling or lying in ambush. The journey itself is part of the
   experience: terrain changes, ambient threats, and the growing distance from
   safety.

4. **Confrontation** -- Finding the target triggers combat. The hunter has
   multiple attack options and must read the target's behavior to survive.
   Targets fight back with visible aggression; health bars deplete on both
   sides. Different marks demand different tactics -- one is fast and evasive,
   another is armored and punishing.

5. **Claiming the Reward** -- Returning to town after a successful hunt
   triggers a payout sequence. Gold is added to the purse, the bounty card is
   struck from the board, and the hunter can spend earnings on better gear or
   harder contracts. The loop resets with new marks and higher stakes.

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

# 开放世界赏金猎人（Open-World Bounty）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界赏金猎人游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名独行猎人，游荡在无法无天的边境地带，从一块风化的任务板上揭下契约，
穿越充满敌意的地形追踪危险的目标。这里的幻想是**在不确定中追猎**——每一份
赏金都意味着承诺深入陌生的地界，而有趣的张力在于猎人必须读懂地貌、
管理有限的资源，并决定何时交战、何时撤退。压力来自目标难度的不断攀升、日渐
枯竭的补给，以及"一次失败的狩猎就意味着空手而归"这个认知。风险始终存在：
下一个目标可能比预期更能打，或者猎人在一份轻松的赏金上花得太多，面对真正的
威胁时已一无所剩。

## 玩家体验流程

1. **标题与进入** —— 一个粗砺的西部奇幻风标题画面奠定基调。玩家按下开始，
   抵达一座边境小镇——一个枢纽，有酒馆、任务板，以及若干出售装备或替你包扎
   伤口的 NPC。

2. **接下契约** —— 任务板上展示可接的赏金，每一份都带有目标肖像、难度评级和
   金币报酬。玩家阅读这些卡片，权衡风险与收益，然后确定一个目标。选定的赏金
   成为当前狩猎任务，世界的焦点也随之转向追踪。

3. **狩猎** —— 一个罗盘或方向指示器引导玩家出镇、进入荒野。世界包含多个风格
   各异的区域——林间藏身处、匪帮营地、多岩的峡谷——目标就等在其中某处，或巡逡
   游走，或埋伏待机。旅途本身就是体验的一部分：地形在变化，环境中潜藏威胁，
   而离安全之地越来越远。

4. **对决** —— 找到目标即触发战斗。猎人有多种攻击选择，必须读懂目标的行为
   才能生存下来。目标会带着明显的攻击性反击；双方的血条都在消耗。不同的目标
   要求不同的战术——有的迅捷善避，有的披甲且下手极狠。

5. **领取赏金** —— 成功狩猎后返回小镇会触发结算流程。金币计入钱袋，赏金卡片
   从任务板上被划掉，猎人可以把收入花在更好的装备或更难的契约上。循环重置，
   带来新的目标和更高的赌注。

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

