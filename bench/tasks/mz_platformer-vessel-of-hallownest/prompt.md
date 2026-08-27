# Vessel of Hallownest

Build a **2D atmospheric metroidvania platform-action game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A silent bug knight descends into a ruined underground kingdom, armed only with
a nail and the will to press deeper. The fantasy is exploration under pressure:
every room might hold a new threat or a shortcut home, and the player is always
weighing aggression against survival. Combat is fast and punishing — each slash
refills the soul that fuels healing, so standing still means dying slowly. The
interesting tension is that the resource loop forces engagement: you heal by
fighting, but fighting risks the health you are trying to recover. Progression
gates the world behind abilities earned in earlier zones, rewarding mastery with
access rather than numbers. The tone is somber, desolate, and beautifully
tragic — cold underground ruins, glowing particles drifting through silence, and
the quiet weight of a kingdom that fell long ago.

## What the Player Experiences

A melancholic title screen greets the player with the game name and a lone
knight silhouette before they choose to begin or continue a saved journey.

The Kingdom Map appears — a network of named stages stretching downward, each
locked until the one before it falls. The player selects the first open stage
and drops in. Inside, the world is a continuous side-scrolling corridor of
connected rooms: platforms jut from cavern walls, thorn pits line the floor, and
infected husks patrol ledges. Movement feels tight and responsive — the knight
accelerates smoothly, jumps with a satisfying arc, clings to walls, and dashes
through gaps that demand precision.

Combat is immediate and visceral. Slashing an enemy staggers it, sprays geo
currency, and fills the soul meter. Taking a hit costs a mask of health and
triggers a brief flash of invincibility. When masks run low the player faces the
core dilemma: hold still to channel soul into healing — vulnerable, exposed — or
press forward and hope the next kill refills enough to survive. Enemies guard
room exits behind soul-barriers that lift only when every husk in the chamber is
dead.

Deeper rooms demand wall-clings and dashes to cross chasms the knight cannot
simply jump. Reaching the far end of a stage triggers a checkpoint that saves
progress and unlocks the next zone on the map. Death is costly — all carried geo
drops at the point of failure and the knight returns to the map to try again.

The final stage is a boss chamber: a large creature with telegraphed attack
patterns that test everything the player has learned. Victory crowns the run;
defeat sends the knight back with nothing but knowledge.

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

# 圣巢容器（Vessel of Hallownest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款 **2D 氛围类银河恶魔城平台动作游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位沉默的虫族骑士深入一座荒废的地下王国，随身只有一把骨钉和一股继续向前的意志。这里的幻想是压力之下的探索：每个房间都可能藏着新的威胁或一条回家的近道，而玩家永远在进攻与生存之间权衡。战斗迅捷且严苛——每一次挥砍都会补充驱动治疗的灵魂，因此站着不动就等于慢慢死去。有意思的张力在于资源循环逼迫你参战：你靠战斗来治疗，但战斗又会危及你正试图恢复的生命。进度把世界锁在前面区域中获得的能力之后，用通行权而不是数值来奖励熟练。整体调性阴郁、荒凉而美得悲怆——寒冷的地下废墟、在寂静中飘散的发光粒子，以及一个早已陨落的王国那份沉默的重量。

## 玩家体验流程

一个忧郁的标题画面以游戏名和一道孤独的骑士剪影迎接玩家，随后他们选择开始新旅程或继续已保存的旅程。

王国地图出现——一张由具名关卡组成、向下延伸的网络，每个关卡都锁着，直到它前面的那个被攻克。玩家选择第一个开放的关卡并落入其中。在里面，世界是一条由相连房间构成的连续横向滚动走廊：平台从洞穴壁上探出，荆棘坑铺在地面，感染的空壳在岩架上巡逻。移动手感紧凑而灵敏——骑士平顺加速，以令人满足的弧线跳跃，能贴附墙面，并能冲刺穿过要求精确的间隙。

战斗是即刻而切身的。挥砍敌人会使其硬直、喷出吉欧货币，并填充灵魂槽。受到打击会损失一个面具的生命，并触发短暂的无敌闪光。当面具剩得不多时，玩家面对核心困境：站着不动把灵魂引导为治疗——脆弱、暴露——还是继续向前，指望下一次击杀能补足到活下来。敌人守着房间出口后方的灵魂屏障，只有当房中每一个空壳都死掉时屏障才会升起。

更深处的房间要求用贴墙和冲刺来跨越骑士无法单靠跳跃通过的深渊。抵达一个关卡的尽头会触发一个保存进度并在地图上解锁下一区域的检查点。死亡代价高昂——所有随身携带的吉欧都会掉在失败地点，骑士则返回地图重新尝试。

最后一个关卡是一间 Boss 房：一头带有预示动作攻击套路的巨大生物，考验玩家学到的一切。胜利为这一轮加冕；失败则让骑士只带着经验退回。

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

