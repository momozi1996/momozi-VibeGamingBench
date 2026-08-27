# Racing Trick Runner

Build a Racing Trick Runner as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

An endless downhill runner where the player carves through procedurally varied
terrain, launching off ramps to perform aerial tricks that boost speed and
score. The slope never ends — the challenge is how far you can go before
crashing. Weather shifts from sunshine to blizzard, day cycles to night, and
the terrain grows steeper and more treacherous. Tricks are the key to survival:
they refill a boost meter that lets you power through flat sections. Unlockable
characters with different trick styles and visual flair provide long-term goals.

## What the Player Experiences

1. **Title Screen** — A snowy mountain vista with the game name in a frosty
   stylized font, a silhouetted rider mid-backflip, and Play/Collection
   buttons. No plain HTML grey.
2. **The Run** — Side-scrolling endless descent. The character automatically
   moves downhill; the player controls jump timing, trick execution, and
   landing angle. Terrain scrolls with parallax mountain backgrounds.
3. **Trick System** — While airborne, the player inputs trick commands (flip,
   spin, grab) using directional keys. Each trick has a point value and a
   time cost. Landing cleanly after a trick awards points and refills boost.
   Landing badly (wrong angle) causes a stumble that costs speed.
4. **Boost Mechanic** — A boost meter fills from successful tricks. Activating
   boost increases speed dramatically with a visual trail effect. Boost is
   essential for clearing flat sections and gaps.
5. **Weather and Day/Night** — Conditions change during a run: clear skies
   transition to fog (reduced visibility), then snow (slippery terrain), then
   blizzard (both). Day fades to night with reduced visibility. Each condition
   affects gameplay and visuals distinctly.
6. **Obstacles and Terrain** — Rocks, trees, and crevasses appear as obstacles.
   The terrain varies between smooth slopes, mogul fields, cliff drops, and
   ramp sequences. Hitting an obstacle ends the run.
7. **Character Collection** — At least 5 unlockable characters earned by
   reaching distance milestones or score targets. Each has a unique sprite,
   trick animation style, and one special ability (higher jumps, longer boost,
   extra hit point).

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

# 特技滑降跑者（Racing Trick Runner）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个特技滑降跑者游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款无尽下坡跑酷游戏，玩家在程序化变化的地形中劈波前行，借着坡道腾空做出空中
特技，以提升速度和分数。坡道永无尽头——挑战在于你能在摔车前跑多远。天气会从
晴朗转为暴风雪，白天循环到夜晚，地形也变得更陡、更险恶。特技是生存的关键：
它们会补满一条加速槽，让你能强行冲过平坦路段。可解锁的角色拥有不同的特技风格
与视觉花样，提供了长线目标。

## 玩家体验流程

1. **标题画面** —— 一幅雪山远景，游戏名称采用带霜感的风格化字体，一位剪影
   车手正在做后空翻，另有"开始"/"收藏"按钮。不要出现 HTML 引擎 的裸灰色。
2. **一轮滑降** —— 横向卷轴的无尽下坡。角色自动向坡下移动；玩家控制起跳时机、
   特技执行和落地角度。地形随视差山脉背景一同滚动。
3. **特技系统** —— 在空中时，玩家用方向键输入特技指令（翻转、旋转、抓板）。
   每个特技都有分值和时间代价。在特技后干净落地会奖励分数并补充加速。落地
   糟糕（角度不对）会导致一次踉跄，损失速度。
4. **加速机制** —— 加速槽由成功的特技填充。启动加速会大幅提升速度，并带有
   可见的尾迹特效。加速对于通过平坦路段和缺口至关重要。
5. **天气与昼夜** —— 一轮之中天况会变化：晴空转为浓雾（能见度降低），再转为
   降雪（地形滑溜），再转为暴风雪（两者兼有）。白天渐变为夜晚，能见度降低。
   每种天况对玩法和视觉的影响都各有区别。
6. **障碍与地形** —— 岩石、树木和冰裂缝会作为障碍出现。地形在平滑坡面、
   雪包坡、悬崖落差和坡道序列之间变化。撞上障碍物则本轮结束。
7. **角色收集** —— 至少 5 个可解锁角色，通过达成距离里程碑或分数目标获得。
   每个角色都有独特的精灵图、特技动画风格，以及一项特殊能力（跳得更高、
   加速更久、多一点生命值）。

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

