# Horror Floor 13

Build a **Horror Floor 13** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is an elevator operator in a cursed building where each floor is a
self-contained nightmare. The fantasy is being trapped in service: passengers
request floors, and the player must deliver them — but every floor visited warps
reality further. Tension comes from passenger requests that conflict (some floors
are dangerous, some passengers are not what they seem) and the elevator itself,
which malfunctions as the curse deepens. The building has thirteen floors, and
floor 13 should never be visited.

## What the Player Experiences

1. **Title Screen** — A dark art-deco elevator panel with floor numbers, the game
   name in brass lettering, and a play button styled as the door-close button.
2. **The Elevator** — The main view is the elevator interior: a floor selector
   panel, an indicator showing current floor, doors that open and close, and a
   small window showing the shaft.
3. **Passengers** — NPCs enter and request floors. Each has a distinct appearance
   and demeanour. Some are normal; others are unsettling (wrong number of eyes,
   flickering sprites, speaking backwards). The player must choose whether to
   comply with requests.
4. **Floor Visits** — When doors open on a floor, the player sees a vignette:
   a hotel hallway that stretches infinitely, an office where everyone is frozen,
   a ballroom with no floor. Each floor is a unique horror scene with a brief
   interactive element.
5. **Malfunctions** — The elevator increasingly misbehaves: going to wrong floors,
   lights flickering, buttons rearranging, the indicator spinning. The player
   must adapt and maintain control.
6. **Passenger Consequences** — Delivering passengers to wrong floors or refusing
   requests has consequences: the building grows more hostile, new impossible
   floors appear, and the elevator descends toward floor 13.
7. **Floor 13** — The final floor. Reaching it triggers the climax. What the
   player did with passengers determines the ending. Multiple endings exist based
   on choices made.

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

# 恐怖第 13 层（Horror Floor 13）

在 `/workspace/game/` 用 Godot 4 开发一个**恐怖第 13 层**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一栋被诅咒大楼里的电梯操作员，每一层楼都是一场自成一体的噩梦。游戏的
幻想核心是被困在职守之中：乘客提出楼层要求，玩家必须把他们送到——但每去过
一层，现实就会被进一步扭曲。紧张感来自互相冲突的乘客要求（有些楼层很危险，
有些乘客并非表面所见），以及电梯本身——随着诅咒加深，它会不断故障。这栋楼
有十三层，而第 13 层永远不该被造访。

## 玩家体验流程

1. **标题画面** —— 一块阴暗的装饰艺术风电梯面板，上面标着楼层数字，游戏名以
   黄铜字体呈现，开始按钮的样式则是关门按钮。
2. **电梯** —— 主视图是电梯内部：一块楼层选择面板、一个显示当前楼层的指示器、
   会开合的门，以及一扇可以看到井道的小窗。
3. **乘客** —— NPC 会走进来并提出楼层要求。每位乘客都有独特的外形和举止。
   有些是正常人；有些则令人不安（眼睛数量不对、精灵图闪烁、说话倒着来）。
   玩家必须选择是否照他们的要求执行。
4. **楼层造访** —— 当电梯门在某一层打开时，玩家会看到一段场景速写：无限延伸的
   酒店走廊、所有人都被冻住的办公室、没有地板的舞厅。每一层都是一个独特的
   恐怖场景，并附带一小段互动内容。
5. **故障** —— 电梯会越来越不听话：停到错误的楼层、灯光闪烁、按钮重新排列、
   指示器疯狂旋转。玩家必须随之应变并维持控制。
6. **乘客带来的后果** —— 把乘客送到错误楼层或拒绝他们的要求都有后果：大楼变得
   更加充满敌意，出现新的不可能存在的楼层，电梯也向第 13 层不断下降。
7. **第 13 层** —— 最后一层。抵达那里将触发高潮。玩家如何对待乘客决定了结局。
   游戏根据玩家做出的选择设有多个结局。

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

