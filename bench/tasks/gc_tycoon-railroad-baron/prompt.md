# Railroad Baron

Build **Railroad Baron**, a **railroad empire tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player lays rail tracks across a map of cities, buys trains, and profits
from cargo demand. Each city produces and consumes different goods — connecting
a lumber town to a construction city creates a profitable route, but only if
the track is efficient and the train has capacity. Terrain drives costs:
mountains require expensive tunnels, rivers need bridges, and flat plains are
cheap but long. A competitor AI builds its own network, racing to claim the
most lucrative routes. The tension is capital allocation: every mile of track
is an investment that only pays off once trains run, and overbuilding before
revenue flows means bankruptcy. The tone is industrial-era ambition: steam,
iron, and the romance of connecting a frontier.

## What the Player Experiences

From the title screen the player starts a new map. The view shows a top-down
terrain map with cities marked by icons showing their goods (lumber, grain,
ore, manufactured goods). The player lays track by clicking city-to-city,
paying costs that vary by terrain crossed.

Once two cities are connected, the player buys a train and assigns it to the
route. Trains move automatically along tracks, picking up goods at one city
and delivering to another. Revenue depends on distance, cargo value, and
demand — delivering goods a city needs pays well; delivering surplus pays
poorly.

The player expands by connecting more cities, upgrading tracks for speed,
buying faster trains, and reading the demand map to find profitable routes.
A competitor AI builds its own network and competes for the same demand — if
they connect a route first, the player must find alternatives.

Money management is critical: track costs are upfront, train purchases are
large, and revenue trickles in over time. Taking on debt accelerates growth
but interest compounds. The game ends after a set number of years; the player
with the highest net worth wins. A styled result screen shows network maps,
revenue history, and final ranking.

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

# 铁路大亨（Railroad Baron）

在 `/workspace/game/` 用 Godot 4 开发 **Railroad Baron**，一款**铁路帝国经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一张城市地图上铺设铁轨、购买列车，并从货运需求中获利。每座城市生产和消耗不同的货物——把一座木材小镇连到一座建筑之城能造出一条赚钱的线路，但前提是轨道足够高效、列车有足够运力。地形决定成本：山地需要昂贵的隧道，河流需要桥梁，平坦的平原便宜但路途更长。一个竞争对手 AI 会营建自己的路网，抢着占下最有利可图的线路。张力在于资本配置：每一英里铁轨都是一笔只有在列车跑起来后才能回本的投资，而在收入流入之前过度建设就意味着破产。整体基调是工业时代的雄心：蒸汽、钢铁，以及连接一片边疆的浪漫。

## 玩家体验流程

玩家从标题画面开始一张新地图。视图展示一张俯视地形图，城市以图标标出各自的货物（木材、谷物、矿石、制成品）。玩家通过点击城市到城市来铺设轨道，成本随所穿越的地形而变化。

一旦两座城市连通，玩家便购买一列火车并把它分配到该线路上。列车沿轨道自动行驶，在一座城市装货，运往另一座城市。收入取决于距离、货物价值和需求——运送城市所需的货物报酬丰厚；运送过剩的货物则报酬微薄。

玩家通过连接更多城市、升级轨道以提速、购买更快的列车，以及研读需求地图来寻找赚钱线路，从而不断扩张。一个竞争对手 AI 会营建自己的路网并争夺同样的需求——如果对方先连通了某条线路，玩家就必须另寻他途。

资金管理至关重要：轨道成本是预付的，购买列车是大笔支出，而收入则随时间涓涓流入。举债能加速成长，但利息会复利累积。游戏在设定的年数之后结束；净资产最高的一方获胜。一个经过美术处理的结算画面会展示路网地图、收入历史和最终排名。

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

