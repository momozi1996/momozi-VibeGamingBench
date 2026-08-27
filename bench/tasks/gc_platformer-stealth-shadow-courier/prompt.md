# Stealth: Shadow Courier

Build **Shadow Courier**, a compact **top-down stealth infiltration game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The fantasy is being a lone courier who survives not by fighting but by reading
the room -- memorizing patrol rhythms, threading gaps in overlapping vision
cones, and choosing the exact moment to slip through a door or kill the lights.
The interesting tension is that every objective changes the player's exposure:
picking up the key means crossing a lit corridor, stealing the document means
lingering in the most guarded room, and reaching the exit means retracing ground
where patrols have shifted. The pressure comes from the gap between what the
player can see (cone arcs, shadow pools, locked routes) and what they must risk
to advance. One miscalculated step collapses the whole plan into alarm bells and
closing nets.

## What the Player Experiences

The player arrives at a dark, atmospheric title screen that establishes the
covert tone -- the game name, a shadowy facility silhouette, and a way to begin.

A brief mission briefing sets the stakes: an archive holds a sealed document,
guards patrol the corridors, and the courier must get in, steal it, and get out
unseen.

Control begins in a top-down facility map. The courier moves smoothly through
rooms and corridors, hugging walls and cover objects. Guards walk visible patrol
routes, their vision cones sweeping ahead of them like searchlights. The player
reads the timing, waits for a gap, and slips past -- or finds another way
around.

Deeper in, a locked door blocks the direct path. The player hunts for a key or
credential, picks it up, and sees the HUD confirm possession. A light switch or
fuse box offers a different kind of power: flipping it plunges a section into
darkness, shrinking guard awareness and opening shadow routes that were
previously exposed.

The document sits in the most dangerous room. Stealing it updates the mission
state and shifts the objective to escape. The player retraces or finds a new
route to the exit, now aware that patrol timing has changed or alert levels have
risen.

Getting spotted triggers escalation -- a warning state, then capture if the
courier lingers. Reaching the exit with the document produces a styled success
screen; getting caught produces a failure screen. Either way, retry and
return-to-title controls keep the player in the loop without restarting the
application.

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

# 潜行：暗影信使（Stealth: Shadow Courier）

在 `/workspace/game/` 用 Godot 4 开发 **Shadow Courier**，一款小巧的**俯视视角潜行渗透游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是成为一名孤身信使，靠的不是打斗而是读懂现场——记住巡逻节奏、在层层叠叠的视野锥之间穿针引线，并挑准那个恰到好处的时机溜过一道门或掐掉灯光。有意思的张力在于：每一个目标都会改变玩家的暴露程度——去拿钥匙就意味着穿过一条亮着灯的走廊，去偷文件就意味着在守卫最森严的房间里逗留，而抵达出口又意味着重走一遍巡逻已经变了位的地面。压力来自玩家所能看见的东西（视野锥弧、阴影池、被锁的路线）与他们为了推进而必须冒的风险之间的落差。一步算错，整个计划就崩塌成刺耳的警铃和逐渐收紧的包围网。

## 玩家体验流程

玩家进入一个昏暗、氛围十足的标题画面，它确立了这场秘密行动的调性——游戏名、一道影影绰绰的设施剪影，以及一个开始的入口。

一段简短的任务简报交代了赌注：档案室里存放着一份密封文件，守卫在走廊上巡逻，而信使必须潜入、偷走它，再不被发现地脱身。

操控从一张俯视视角的设施地图开始。信使在房间和走廊之间平顺移动，贴着墙壁和掩体物件走。守卫沿可见的巡逻路线行走，视野锥像探照灯一样在他们前方扫过。玩家读时机、等一个空档，然后溜过去——或者另寻一条绕行的路。

再往深处，一道锁着的门挡住了直通路径。玩家去找一把钥匙或凭证，把它拾起，并看到 HUD 确认已持有。一个电灯开关或配电箱提供另一种力量：拉下它会让一整片区域陷入黑暗，缩小守卫的感知范围，并打开此前完全暴露的阴影路线。

文件就在最危险的那个房间里。偷到它会更新任务状态，并把目标切换为撤离。玩家原路返回或另找一条通往出口的路线，此时他们已经知道巡逻时机已变或警戒等级已升。

被发现会触发升级——先是警告状态，若信使继续逗留则被抓获。带着文件抵达出口会呈现一个经过设计的成功画面；被抓获则呈现失败画面。无论哪种情况，重试和返回标题的操作都让玩家留在循环之中，无需重启应用。

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

