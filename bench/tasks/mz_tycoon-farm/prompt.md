# Tycoon: Village Farm

Build a **2D village-farm tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player inherits a small plot of land and turns it into a living farm through
daily ritual. The fantasy is cozy accumulation — waking each morning to tend
crops that grew overnight, selling the harvest for just enough gold to plant
something new, and watching the homestead slowly fill with colour and life. The
interesting tension is that every day is finite: stamina runs out before
ambition does, so the player must choose which chores matter most right now.
The pressure is gentle but real — skip watering and crops stall, overextend and
tomorrow starts hungry. The risk is never catastrophic, just the quiet cost of
a wasted day. Over many mornings the farm transforms from bare dirt into a
thriving patchwork, and the satisfaction is entirely earned one tile at a time.

## What the Player Experiences

The player opens a saved farm or starts fresh and sees their homestead — a
fenced plot of tillable earth, a farmhouse, a shop, and water glinting at the
edge. Early mornings are simple: till a few squares, drop seeds, water them,
and head inside to sleep. Each action visibly marks the land and costs a sliver
of the day's energy.

As gold accumulates the player diversifies — new seed types with longer growth
but bigger payoffs, a fishing spot for side income, maybe an expanded field.
The daily loop stays the same but the decisions inside it deepen: which crops
to prioritize, when to harvest versus when to water the next batch, whether to
spend the last stamina fishing or saving it for tomorrow's planting.

Crops grow only overnight, so sleeping is the punctuation that gives each day
meaning. The morning reveal — seeing sprouts advance a stage, mature plants
ready to pick — is the hook that pulls the player into one more day. Progress
is banked at bedtime, so a returning player wakes to the same farm, the same
season of growth, and the same quiet momentum.

The art direction is warm, sunlit, cartoon-pastoral — greens, ochres, soft
wood — never naked HTML 引擎 grey. The tone is gentle and unhurried, the opposite
of a twitch game.

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

# 经营：乡村农场（Tycoon: Village Farm）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个 **2D 乡村农场经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家继承了一小块土地，通过日复一日的例行劳作把它变成一座充满生机的农场。这里的幻想是惬意的累积感——每天清晨醒来照料一夜之间长大的作物，卖掉收成换来刚够种下新东西的金币，看着自家庄园慢慢填满色彩与生命。有趣的张力在于每一天都是有限的：体力总在雄心之前耗尽，所以玩家必须选择当下哪些活儿最重要。压力温和但真实——不浇水作物就停滞，透支了明天就得饿着肚子开始。风险从不是灾难性的，只是虚度一天的那份静默代价。经过许多个清晨，农场从裸土变成生机盎然的拼布图景，而这份满足感完完全全是一块图块一块图块挣来的。

## 玩家体验流程

玩家打开已存档的农场或从头开始，看到自己的庄园——一块围起来的可耕土地、一间农舍、一家商店，还有边缘处闪着微光的水面。最初的清晨很简单：耕几格地、撒下种子、浇上水，然后回屋睡觉。每个动作都会在土地上留下可见的痕迹，也消耗掉一天精力中的一小片。

随着金币累积，玩家开始多元化经营——生长期更长但回报更高的新种子类型、带来副业收入的钓鱼点，也许还有一片扩建的田地。每日循环保持不变，但其中的决策变得更有深度：优先种哪些作物，什么时候该收割、什么时候该给下一批浇水，最后一点体力是拿去钓鱼还是留给明天播种。

作物只在夜间生长，所以睡觉就是赋予每一天意义的标点。清晨的揭晓时刻——看到幼苗推进一个阶段、成熟的植株已可采摘——正是把玩家拉进"再来一天"的钩子。进度在就寝时存档，因此回来的玩家醒来面对的是同一座农场、同一段生长季节、同样静静向前的势头。

美术方向是温暖、洒满阳光的卡通田园风——绿色、赭色、柔和的木质——绝不出现裸露的 HTML 引擎 灰。整体基调温和从容，与手速游戏截然相反。

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

