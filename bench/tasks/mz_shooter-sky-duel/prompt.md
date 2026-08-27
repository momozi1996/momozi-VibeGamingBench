# Sky Duel

Build **Sky Duel**, a 2D aerial combat game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a nimble fighter plane through open sky, using momentum
and gravity to outmaneuver waves of enemy aircraft in dogfights that feel like
violent dances. The interesting tension is physics-driven movement: the plane has
thrust, drag, and gravity, so climbing bleeds speed while diving builds it. The
player must manage energy state — trading altitude for velocity and vice versa —
while lining up shots on enemies who exploit the same physics. Customizable plane
parts earned through score milestones let the player tune handling, firepower,
and survivability to match their style.

## What the Player Experiences

The player opens to a hangar title screen showing their current plane loadout,
then launches into a sortie. The plane flies in a 2D side-view sky with
wraparound or bounded edges. Thrust is applied with a button; the plane rotates
with left/right input and is always subject to gravity. Firing sends bullets in
the facing direction. Enemy planes enter in formations, each with distinct
behavior — dive bombers, circling aces, heavy gunships.

Destroying enemies and completing objectives earns score that unlocks new parts
at thresholds: engine upgrades for more thrust, wing shapes for tighter turns,
weapon pods for spread or homing shots, armor plating that adds weight. Between
sorties the player equips parts in the hangar. Boss encounters feature large
aircraft with multiple turrets and attack phases. The campaign spans 6+ sorties
with increasing enemy variety and environmental hazards like storms and flak
towers.

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

# 长空决斗（Sky Duel）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Sky Duel**，一款 2D 空战游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一架灵巧的战斗机穿越开阔的天空，利用动量与重力在空战缠斗中
机动压制一波波敌机，让搏杀感觉像一场暴烈的舞蹈。有趣的张力来自物理驱动的运动：
飞机具有推力、阻力和重力，所以爬升会流失速度，而俯冲会积累速度。玩家必须管理
能量状态——用高度换速度，或反之——同时对那些利用同一套物理规则的敌人瞄准
射击。通过分数里程碑获得的可定制机体部件让玩家能按自己的风格调校操控性、
火力和生存力。

## 玩家体验流程

玩家进入游戏时看到一个机库标题画面，展示当前的飞机配装，随后升空进行一次出击。
飞机在一片 2D 侧视天空中飞行，边界可环绕或有界。推力通过一个按键施加；飞机用
左/右输入旋转，并始终受重力作用。开火会朝机头朝向发射子弹。敌机以编队入场，
每种都有独特的行为——俯冲轰炸机、盘旋王牌、重型武装飞艇。

摧毁敌人与完成目标可获得分数，在达到阈值时解锁新部件：提升推力的引擎升级、
带来更紧转弯的机翼形状、提供散射或追踪弹的武器吊舱、增加重量的装甲板。出击
之间，玩家在机库中装配部件。Boss 遭遇战会出现带多座炮塔与多攻击阶段的大型
飞行器。战役横跨 6 次以上出击，敌人种类不断增加，并加入风暴与高射炮塔等
环境危险。

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

