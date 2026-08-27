# Action: Void Harvest

Build **Void Harvest**, a compact **survivor-like auto-attacking arena game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A fragile hero is dropped into an expanding hostile void where survival depends
on threading through swarms, harvesting the energy they leave behind, and
evolving into a strange weapon system before the arena overwhelms them. The
tension lives in the upgrade economy: each level-up reshapes how the run plays,
but the void does not wait — enemies grow denser, faster, and stranger with
every passing second. The player never fires manually; positioning and upgrade
choices are the only levers. The identity should feel cosmic and original —
void insects, rust alchemy, signal flares, magnetic rail bursts, tether drones,
shard mines — not a reskin of familiar vampire-hunter rosters.

## What the Player Experiences

From a styled title screen the player picks a hero from a small roster of
original characters, each with a distinct portrait, starting weapon, and
passive that makes the choice feel like a strategy decision.

The arena begins immediately: enemies pour in from the edges and the hero's
weapons fire on their own while the player weaves through gaps with the
keyboard. Defeated enemies scatter XP shards that pull toward the hero,
filling a level meter that interrupts the action with a choice of three
upgrades — a new weapon, a stat boost, or a weapon evolution. Each pick
visibly changes the run: more projectiles, wider arcs, new attack patterns
orbiting the hero.

Time pushes the run through a visible difficulty ladder. Early swarms give way
to mixed enemy roles — chargers, ranged attackers, splitters, shield bearers —
and eventually an elite or boss-like threat whose mechanic forces repositioning
rather than simply tanking damage. The run resolves in victory or defeat on a
styled result screen with retry and return-to-title options.

Throughout, the combat HUD keeps the player oriented: HP, XP bar, survival
timer, and a weapon loadout strip showing what the hero has become.

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

# 动作：虚空收割（Action: Void Harvest）

在 `/workspace/game/` 用 Godot 4 开发 **Void Harvest**——一款小巧的 **survivor-like
自动攻击竞技场游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位脆弱的英雄被投入一片不断扩张的敌意虚空，能否存活取决于在虫群缝隙中穿行、
收割它们遗落的能量，并在竞技场把他压垮之前进化出一套奇诡的武器系统。张力来自
升级经济：每一次升级都会重塑这一轮的玩法，但虚空不会等待——敌人每过一秒都变得
更密集、更快、更古怪。玩家永远不会手动开火；站位与升级选择是唯一的操作杠杆。
整体调性应当宇宙感十足且原创——虚空虫、锈蚀炼金、信号照明弹、磁轨爆发、系绳
无人机、碎片地雷——而不是把熟悉的吸血鬼猎人角色表换层皮。

## 玩家体验流程

从一个有设计感的标题画面开始，玩家从一小批原创角色中挑选英雄，每位都有独特的
立绘、初始武器和被动，让这个选择真正像一次策略决策。

竞技场立刻开始：敌人从边缘涌入，英雄的武器自行开火，而玩家用键盘在缝隙中穿行。
被击败的敌人会散落 XP 碎片并被吸向英雄，填满等级槽，随后中断战斗、给出三个升级
选项——一件新武器、一项属性提升，或一次武器进化。每次选择都会带来可见的变化：
更多弹幕、更宽的扇形、绕着英雄旋转的新攻击形态。

时间推动这一轮沿着一条可见的难度阶梯向上。早期的虫群会让位给混合的敌人职能——
冲锋者、远程攻击者、分裂者、持盾者——最终出现精英或类 Boss 的威胁，其机制迫使
玩家重新站位，而不是单纯硬吃伤害。这一轮以胜利或失败收场，在一个有设计感的结算
画面上给出重试与返回标题画面的选项。

全程中，战斗 HUD 让玩家始终掌握状况：HP、XP 条、存活计时器，以及一条展示英雄
已进化成什么样的武器配置栏。

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

