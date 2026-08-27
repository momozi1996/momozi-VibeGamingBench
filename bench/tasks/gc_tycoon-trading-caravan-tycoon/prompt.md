# Tycoon: Trading Caravan

Build a **route-planning and market trading tycoon** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a merchant captain steering a small caravan across a network of
towns that each want different things at different prices. The fantasy is reading
the map like a puzzle — spotting where silk is cheap and where it is gold, then
gambling on the road between. Every route is a bet: the short path is safe but
dull, the mountain pass saves days but invites bandits, and the cargo you chose
might spoil before you arrive. Growth compounds — better wagons carry more, hired
guards open dangerous shortcuts, cold crates unlock perishables — but so does
risk, because a bigger haul means a bigger loss when things go wrong. The
pressure is that markets shift while you travel, so yesterday's sure profit can
become tomorrow's dead weight. The tone is parchment-and-ink merchant strategy:
a world of trade routes, price boards, and calculated gambles.

## What the Player Experiences

The player opens a stylized map dotted with towns connected by roads of varying
length and danger. A caravan marker sits at the current town, and a ledger shows
cash, cargo hold, and any active contracts. The first minutes are about scanning
prices — this town sells spices cheap, the one across the river pays double —
and loading up the wagon.

Choosing a destination means weighing route options: the safe road costs more in
feed and tolls, the shortcut through bandit territory risks losing cargo
entirely. Once committed, the caravan moves and events unfold — a storm delays
travel, a toll gate demands coin, a merchant on the road offers a side deal. The
player watches cargo, money, and risk shift in real time.

Arriving at a new town, the player sells at local prices, checks what is scarce
here, and decides whether to restock or push onward. Earnings fund upgrades —
extra carts for capacity, scouts who reveal hazards ahead, cold storage that
opens perishable goods to trade. Each upgrade reshapes which routes and cargoes
become profitable.

Over time the network opens up: new towns appear, higher-value contracts become
available, and the caravan grows from a lone wagon into a proper trading
operation. The arc ends when the player hits a profit milestone and sees a
success screen, or when debt and failed contracts pile up into bankruptcy. Both
outcomes are navigable without restarting.

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

# 经营：贸易商队（Tycoon: Trading Caravan）

在 `/workspace/game/` 用 Godot 4 开发一个**路线规划与市场贸易经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一位商队船长，驾着一支小小的商队穿行于一张城镇网络之间，而每座城镇想要的东西和给出的价格都各不相同。这里的幻想是把地图当谜题来读——找出丝绸在哪儿便宜、在哪儿贵如黄金，然后在中间那段路上下注。每条路线都是一场赌博：短路安全但乏味，山口能省下好几天却招来盗匪，而你选的货物可能在抵达之前就变质了。成长会复利累积——更好的货车装得更多，雇来的护卫打开危险的捷径，冷藏箱解锁易腐货物——但风险同样如此，因为更大的一批货意味着出事时更大的损失。压力在于你赶路时市场也在变动，所以昨天板上钉钉的利润会变成明天的累赘。整体基调是羊皮纸与墨水味的商人策略：一个由贸易路线、价格板和精算过的赌注组成的世界。

## 玩家体验流程

玩家打开一张风格化的地图，上面散布着由长度与危险程度各异的道路相连的城镇。一枚商队标记停在当前城镇，一本账簿显示现金、货舱和任何进行中的契约。最初几分钟是扫读价格——这座城镇香料便宜，河对岸那座出价翻倍——然后把货车装满。

选定目的地意味着权衡路线选项：安全的大路在草料和过路费上花得更多，穿过盗匪地盘的捷径则有全部货物尽失的风险。一旦下定决心，商队便开始移动，事件随之展开——一场风暴延误行程，一道关卡索要钱币，路上的一位商人提出一笔额外交易。玩家实时看着货物、金钱和风险此起彼伏。

抵达一座新城镇后，玩家按当地价格出售，查看这里缺什么，再决定是补货还是继续前行。收益资助升级——增加运力的额外车厢、能提前揭示危险的斥候、把易腐货物纳入可交易范围的冷藏设施。每一项升级都会重塑哪些路线和货物才划得来。

随着时间推移，网络逐渐打开：新城镇出现，更高价值的契约变得可接，商队也从孤零零一辆货车成长为一支正经的贸易队伍。当玩家达到某个利润里程碑并看到成功画面，或是债务与失败契约堆积成破产时，这段弧线便告结束。两种结局都无需重启即可继续操作导航。

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

