# Mech Sortie

Build **Mech Sortie**, a top-down mech shooter as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a heavily armed walking mech through hostile territory,
customizing its weapon hardpoints between missions to match the threats ahead.
The interesting tension is loadout planning: the mech has limited hardpoint slots
(arms, shoulders, back) and each weapon has weight, ammo, and range tradeoffs.
A missile rack dominates at range but leaves the mech vulnerable up close; dual
autocannons shred nearby targets but overheat. Missions yield salvage from
destroyed enemies that funds new weapons and chassis upgrades, creating a
satisfying loop of deploy, destroy, salvage, customize, redeploy.

## What the Player Experiences

The player opens to a hangar screen showing their mech with labeled hardpoints.
Available weapons are listed in an armory panel; dragging a weapon onto a
hardpoint equips it, with weight and energy constraints shown. Selecting a
mission from the campaign map deploys the mech into a top-down battlefield.

The mech moves with WASD (slower than infantry, with momentum), rotates the
torso independently with mouse aim, and fires equipped weapons with mouse
buttons and number keys. Missions have objectives: destroy all enemies, defend a
point, escort a convoy, or eliminate a target. Enemy variety includes infantry,
light vehicles, rival mechs, and turret emplacements. Destroying enemies drops
salvage crates collected on contact. Mission completion shows a debrief with
salvage earned, damage taken, and accuracy stats. The campaign spans 8+ missions
with escalating difficulty and a final boss mech encounter.

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

# 机甲出击（Mech Sortie）

在 `/workspace/game/` 用 Godot 4 开发 **Mech Sortie**，一款俯视视角的机甲射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一台重武装步行机甲穿越敌方领地，并在任务之间定制它的武器挂点
以应对前方的威胁。有趣的张力来自配装规划：机甲的挂点槽位有限（手臂、肩部、
背部），而每件武器都有重量、弹药和射程上的取舍。导弹巢在远距离上具有压制力，
却让机甲在近身时不堪一击；双联速射炮能撕碎近处目标但会过热。任务会从被摧毁的
敌人身上产出残骸物资，用于资助新武器与底盘升级，形成一个令人满足的循环——
部署、摧毁、回收残骸、定制、再部署。

## 玩家体验流程

玩家进入游戏时看到一个机库画面，展示他们的机甲及标注好的各个挂点。可用武器
列在军械库面板中；把一件武器拖到某个挂点即可装备，同时显示重量与能量约束。
从战役地图上选择一个任务后，机甲便被部署进一张俯视视角的战场。

机甲用 WASD 移动（比步兵更慢，且带惯性），躯干可通过鼠标瞄准独立旋转，并用
鼠标按键与数字键发射已装备的武器。任务带有目标：歼灭所有敌人、防守某一据点、
护送车队，或清除某个目标。敌人种类包括步兵、轻型载具、敌对机甲和炮塔工事。
摧毁敌人会掉落残骸箱，接触即可拾取。任务完成后会展示一份任务报告，含获得的
残骸物资、受到的伤害以及命中率数据。战役横跨 8 个以上任务，难度逐步升级，并
以一场最终 Boss 机甲遭遇战收尾。

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

