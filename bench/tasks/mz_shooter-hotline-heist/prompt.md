# Hotline Heist

Build **Hotline Heist**, a top-down fast-action shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is bursting through doors into rooms full of armed guards, clearing
entire floors in seconds with precise aim and brutal efficiency. The interesting
tension is fragility: both the player and enemies die in one hit, making every
room entry a lethal puzzle where hesitation means death. Combo scoring rewards
speed — chaining kills without pause multiplies the score, encouraging reckless
aggression balanced against the instant-death stakes. Weapon variety scattered
across floors forces improvisation: a shotgun clears a cluster but alerts the
next room, while a silenced pistol preserves surprise but demands accuracy.

## What the Player Experiences

The player sees a stylized title screen, selects a floor from the campaign list,
and spawns outside the building's entrance. The camera shows the full floor plan
from above — rooms, corridors, doors, and enemy patrol routes are partially
visible. The player moves with WASD, aims with the mouse, and clicks to attack.
Doors can be kicked open to stun enemies behind them.

Each floor is a self-contained puzzle of 4-8 rooms connected by doors and
hallways. Guards patrol set routes; some stand still, others pace. Weapons litter
the ground — bats, pistols, shotguns, SMGs, thrown knives — each with limited
ammo or single-use. Clearing all enemies on a floor triggers a score screen
showing time, combo chain, and weapon variety bonus. Dying restarts the floor
instantly. The campaign offers 8+ floors with escalating guard density, new enemy
types (armored, dogs, gunners), and tighter layouts.

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

# 热线劫案（Hotline Heist）

在 `/workspace/game/` 用 Godot 4 开发 **Hotline Heist**，一款俯视视角的快节奏动作射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是踹门冲进满是武装守卫的房间，凭精准的瞄准和残酷的效率在几秒内清空
整个楼层。有趣的张力来自脆弱性：玩家和敌人都是一击致命，这让每一次进门都成为
一道致命谜题，犹豫就等于死亡。连击计分奖励速度——不停顿地连续击杀会提升分数
倍率，鼓励不顾一切的进攻，与一击即死的赌注形成平衡。散落在各楼层的多样武器
迫使玩家临场应变：霰弹枪能清掉一堆敌人但会惊动下一个房间，而消音手枪能保住
突袭优势却要求精度。

## 玩家体验流程

玩家看到一个风格化的标题画面，从战役列表中选择一个楼层，然后在建筑入口外生成。
镜头从上方展示完整的楼层平面图——房间、走廊、门以及敌人巡逻路线部分可见。玩家
用 WASD 移动，用鼠标瞄准，点击攻击。门可以被踹开以震晕门后的敌人。

每个楼层都是一道自成一体的谜题，由 4-8 个房间通过门与走廊相连。守卫沿固定路线
巡逻；有些站着不动，有些来回踱步。武器散落在地上——棒球棍、手枪、霰弹枪、
冲锋枪、飞刀——每种弹药有限或只能用一次。清空一个楼层上的所有敌人会触发计分
画面，显示用时、连击链与武器多样性奖励。死亡会立刻重开该楼层。战役提供 8 个
以上楼层，守卫密度逐步升级，并加入新的敌人类型（重甲兵、猎犬、枪手）以及更
逼仄的布局。

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

