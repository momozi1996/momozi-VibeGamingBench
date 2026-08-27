# Sports Archery Quest

Build a **Sports Archery Quest** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is an archer on a quest through fantasy lands, using skill-based aiming
to hunt monsters, hit distant targets, and defeat bosses with precision shots.
The fantasy is the perfect shot: accounting for wind and distance, drawing the
bow to full power, and watching the arrow arc across the screen to strike a
weak point. Tension comes from limited arrows, wind that shifts mid-draw, and
monsters that close distance while the player aims. Upgrades improve the bow's
power, arrow types, and the player's draw speed.

## What the Player Experiences

1. **Title Screen** — A forest clearing with an arrow embedded in a target, the
   game name in runic-styled font, and a play button shaped like an arrowhead.
2. **World Map** — A node-based map showing locations: forest, canyon, ruins,
   dragon's peak. Each location has multiple stages. Completing stages unlocks
   the next area.
3. **Aiming Mechanics** — The player draws the bow by holding a button (power
   meter fills), aims with directional input, and releases to fire. Arrow
   trajectory follows a physics arc affected by gravity and wind. A wind
   indicator shows current direction and strength.
4. **Target Stages** — Some stages are pure marksmanship: hit bullseyes at
   increasing distances, shoot moving targets, or thread arrows through narrow
   gaps. Score is based on accuracy and speed.
5. **Monster Hunting** — Monsters approach from the right side. The player must
   hit weak points (glowing spots) to deal maximum damage. Different monsters
   have different weak point locations and movement patterns.
6. **Boss Targets** — Each area ends with a boss: a giant creature with multiple
   weak points that must be hit in sequence. Bosses have attack phases where the
   player must dodge (move vertically) while finding shot windows.
7. **Bow Upgrades** — Earned gold buys upgrades: longer range, faster draw,
   elemental arrows (fire for extra damage, ice to slow, lightning to chain).
   A shop screen shows available upgrades with clear stat comparisons.

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

# 弓箭手远征（Sports Archery Quest）

在 `/workspace/game/` 用 Godot 4 开发一个**弓箭手远征**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名弓箭手，踏上穿越奇幻大陆的旅程，靠技术性的瞄准去猎杀怪物、命中远处
的靶子，并用精准的射击击败 Boss。这里的幻想是那一记完美的箭：算准风力与距离，
将弓拉到满力，然后看着箭矢划过屏幕命中弱点。张力来自有限的箭数、拉弓中途会变向
的风力，以及在玩家瞄准时不断逼近的怪物。升级可以提升弓的力量、箭的种类，以及
玩家的拉弓速度。

## 玩家体验流程

1. **标题画面** —— 一片林间空地，一支箭插在靶子上，游戏名称采用符文风格的字体，
   以及一个箭头形状的开始按钮。
2. **世界地图** —— 一张基于节点的地图，展示各个地点：森林、峡谷、遗迹、龙之峰。
   每个地点包含多个关卡。完成关卡会解锁下一个区域。
3. **瞄准机制** —— 玩家按住按钮来拉弓（力度条填充），用方向输入瞄准，松开射出。
   箭的弹道遵循受重力和风力影响的物理抛物线。一个风力指示器显示当前的风向和
   强度。
4. **靶场关卡** —— 有些关卡是纯粹的射术考验：命中越来越远的靶心、射击移动靶，
   或者让箭穿过狭窄的缝隙。得分基于精度和速度。
5. **怪物狩猎** —— 怪物从右侧逼近。玩家必须击中弱点（发光的斑点）才能造成最大
   伤害。不同的怪物有不同的弱点位置和移动模式。
6. **Boss 靶标** —— 每个区域以一个 Boss 收尾：一头巨大的生物，身上有多个弱点，
   必须按顺序命中。Boss 有攻击阶段，此时玩家必须一边闪避（垂直移动）一边寻找
   出手的窗口。
7. **弓的升级** —— 赚到的金币可以购买升级：更长的射程、更快的拉弓、元素箭
   （火焰造成额外伤害、冰霜减速、闪电连锁）。一个商店画面展示可购买的升级项，
   并附有清晰的属性对比。

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

