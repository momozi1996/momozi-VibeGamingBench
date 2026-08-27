# Strategy: Tower-Defense

Build a **2D Tower-Defense Game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a field commander staring down a map of chokepoints and open
ground, watching a tide of hostiles pour along fixed corridors toward a
vulnerable endpoint. The only tool is a handful of deployable defenders and a
ticking resource clock. The fantasy is **spatial puzzle-solving under escalating
pressure** -- every tile placement is a commitment, every wave ratchets the
stakes, and the interesting tension is that resources spent now on a safe pick
could have been saved for a desperate answer later. The pressure comes from
reading the next wave's composition, choosing where to invest scarce Deployment
Points, and deciding whether to shore up a crumbling lane or gamble on a
high-cost unit that might turn the whole map. The risk is always that one
misread wave or one greedy save leaves the line too thin and enemies pour
through before the next DP tick arrives.

## What the Player Experiences

1. **Title and Campaign Entry** -- A cold, industrial title screen sets the tone.
   The player starts fresh or loads a save, then enters a stage-select map
   showing available missions, each hinting at the enemy composition and
   difficulty ahead.

2. **Deployment Phase** -- Inside a stage the player sees a grid battlefield with
   clearly marked paths, deployable tiles, and a base endpoint. DP ticks upward
   over time. The player drags unit cards from a hand onto legal tiles; each
   placement costs DP and commits a defender to that position. Invalid spots or
   insufficient funds refuse cleanly.

3. **The Assault** -- Enemies surge along the fixed path in discrete waves. Each
   wave is stronger or stranger than the last -- faster scouts, armored brutes,
   flying threats that bypass blockers. Defenders auto-attack within range,
   blockers hold the line, and the player watches HP bars tick down on both
   sides. Deaths remove units from the field; leaks chip away at the base's
   life total.

4. **Escalation and Adaptation** -- Later waves demand answers the opening
   roster cannot provide alone. The player weighs upgrades, repositions
   priorities, and stretches DP across competing needs. The map becomes a living
   puzzle of overlapping ranges and shifting pressure points.

5. **Resolution** -- The final wave breaks against the defense and victory is
   declared, or the base's life hits zero and defeat is acknowledged. Clearing
   a stage marks progress and unlocks the next. The player can retry, return to
   stage select, or quit to title without relaunching.

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

# 策略：塔防（Strategy: Tower-Defense）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款 **2D 塔防游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名前线指挥官，盯着一张布满咽喉要地与开阔地带的地图，看着敌潮沿固定通道涌向一个脆弱的终点。手上唯一的工具是少量可部署的防御者和一只不断走动的资源时钟。核心幻想是**在不断升级的压力下解空间谜题**——每一次图块摆放都是一次承诺，每一波敌人都在抬高赌注，而有意思的张力在于：现在花在稳妥选择上的资源，本可以攒下来作为日后绝境中的答案。压力来自解读下一波的构成、决定把稀缺的部署点数（DP）投到哪里，以及判断是要加固正在崩溃的一路，还是赌一个高价单位来翻转整张地图。风险始终存在：一次误读的波次或一次贪心的存钱，就会让防线过薄，敌人在下一次 DP 跳动到来之前就冲了进来。

## 玩家体验流程

1. **标题与战役入口** —— 一个冷峻的工业风标题画面定下基调。玩家从头开始或读取存档，然后进入一张关卡选择地图，其上显示可选任务，每个任务都暗示着前方的敌人构成与难度。

2. **部署阶段** —— 进入关卡后，玩家看到一张格状战场，其中路径、可部署图块与基地终点都有清晰标记。DP 随时间向上跳动。玩家把单位卡从手牌拖到合法图块上；每一次摆放都消耗 DP，并把一名防御者固定到该位置。无效位置或资金不足会被干净地拒绝。

3. **敌袭来临** —— 敌人沿固定路径以离散波次涌来。每一波都比上一波更强或更古怪——更快的斥候、带甲的猛兽、绕过阻挡者的飞行威胁。防御者在射程内自动攻击，阻挡者顶住防线，而玩家看着双方的血条不断下降。死亡会把单位从战场上移除；漏怪则一点点削减基地的生命总量。

4. **升级与应变** —— 后期波次要求的答案，开局阵容单靠自己给不出来。玩家权衡升级、重新调整优先级，并在互相竞争的需求之间摊开有限的 DP。地图变成一道由重叠射程与移动压力点组成的活谜题。

5. **收尾结算** —— 最后一波撞碎在防线上，胜利宣告；或者基地生命归零，失败被确认。通关一个关卡会记录进度并解锁下一关。玩家可以重试、返回关卡选择，或退回标题画面，无需重新启动。

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

