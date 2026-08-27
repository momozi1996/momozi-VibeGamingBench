# Music Label

Build **Music Label**, a **music label management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player runs an independent music label, signing artists, producing albums,
marketing releases, and scheduling tours. Each artist has a genre, talent
level, morale, and fanbase that grow or shrink based on management decisions.
The market shifts — genres trend up and down, and timing a release to ride a
wave multiplies sales. The tension is resource allocation: studio time is
limited, marketing budgets are finite, and pushing an artist too hard burns
them out. The tone is creative-industry drama: recording studios, chart
battles, and the thrill of a breakout hit.

## What the Player Experiences

From the title screen the player starts a new label. The main view shows the
label dashboard: signed artists, upcoming releases, financial summary, and
genre trend charts. Time advances week by week.

Artists are scouted from a pool — each has a genre, talent rating, and
personality traits that affect studio behavior. Signing costs an advance and
commits to producing their album. In the studio, the player allocates
production weeks and chooses a producer style (polished, raw, experimental)
that affects album quality and genre fit.

Marketing is a budget allocation: spend on social media, radio, press, or
touring. Each channel reaches different audiences and has diminishing returns.
Timing matters — releasing during a genre's peak trend multiplies exposure.

Tours generate revenue and grow fanbases but cost money upfront and drain
artist morale. An exhausted artist produces worse albums and may leave the
label. The player must balance exploitation against artist care.

Revenue comes from album sales, streaming royalties, tour profits, and
merchandise. Expenses include studio rent, staff salaries, advances, and
marketing. The game tracks label reputation, total revenue, and chart
positions. A styled result screen shows label achievements each quarter.

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

# 唱片公司（Music Label）

在 `/workspace/game/` 用 Godot 4 开发 **Music Label**，一款**唱片公司管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一家独立唱片公司，签下艺人、制作专辑、为发行做营销，并安排巡演。每位艺人都有一个曲风、才华水平、士气和粉丝群，它们会随管理决策而增长或萎缩。市场是流动的——各种曲风的热度起起落落，把发行时机踩在浪头上能让销量倍增。张力在于资源分配：录音棚时间有限，营销预算有限，而把艺人逼得太紧会让他们燃尽。整体基调是创意产业的戏剧感：录音棚、榜单争夺，以及一首爆款单曲带来的兴奋。

## 玩家体验流程

玩家从标题画面开始经营一家新的唱片公司。主视图展示公司仪表盘：已签艺人、即将发行的作品、财务摘要和曲风趋势图表。时间一周一周推进。

艺人从一个候选池中挖掘——每人都有曲风、才华评级，以及影响录音棚表现的性格特质。签约需要支付预付金，并承诺为其制作专辑。在录音棚里，玩家分配制作周数，并选择一种制作人风格（精致、粗粝、实验性），这会影响专辑品质与曲风契合度。

营销是一次预算分配：把钱投在社交媒体、电台、媒体报道还是巡演上。每条渠道触达不同的受众，且都有边际收益递减。时机很关键——在某个曲风热度峰值期发行能让曝光倍增。

巡演能产生收入并扩大粉丝群，但需要预先投钱，还会消耗艺人士气。一位精疲力竭的艺人会做出更差的专辑，甚至可能离开公司。玩家必须在榨取与关照艺人之间取得平衡。

收入来自专辑销售、流媒体版税、巡演利润和周边商品。支出包括录音棚租金、员工薪水、预付金和营销。游戏会记录公司声誉、总收入和榜单排名。一个经过美术处理的结算画面会在每个季度展示公司的成就。

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

