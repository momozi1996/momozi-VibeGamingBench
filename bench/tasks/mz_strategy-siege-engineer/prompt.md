# Siege Engineer

Build **Siege Engineer**, a **physics-based siege weapon strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player builds and aims siege weapons to demolish castle fortifications
using realistic projectile physics. Each level presents a castle with walls,
towers, and defenders that must be reduced to rubble within a limited number
of shots. The player chooses weapon type, adjusts angle and power, and fires —
watching the projectile arc through the air and crash into destructible
terrain. The tension is resource scarcity: ammunition is limited, each shot
must count, and the castle's geometry creates puzzles about where to strike
for maximum structural collapse. The tone is medieval engineering: wood and
iron machines, stone dust, and the satisfying crunch of masonry giving way.

## What the Player Experiences

From the title screen the player enters a campaign map of increasingly
fortified castles. Each level shows the target castle on the right and the
player's siege position on the left, with terrain between them.

The player selects from available weapon types: trebuchets for high arcs over
walls, ballistae for flat direct shots, and catapults for medium-range
bombardment. Each weapon has different projectile weight, speed, and blast
radius. The player aims by adjusting angle and power with a drag interface,
seeing a trajectory preview line.

Firing launches the projectile with physics-based flight. On impact, castle
blocks take damage and can crack, crumble, or collapse depending on structural
support — removing a load-bearing wall brings everything above it down. The
player has a limited shot count per level and must destroy enough of the castle
to meet a destruction threshold.

Later levels add wind that shifts projectile paths, armored walls that resist
certain weapon types, and defenders that repair damage between shots. The
campaign escalates from simple walls to complex multi-tower fortresses.

A styled result screen shows destruction percentage, shots used, and stars
earned. Three stars require efficient demolition with minimal shots.

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

# 攻城工程师（Siege Engineer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Siege Engineer**，一款**基于物理的攻城武器策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家搭建并瞄准攻城武器，利用真实的抛射物物理去拆毁城堡工事。每个关卡都会给出一座带有城墙、塔楼与守军的城堡，必须在有限的射击次数内把它化为废墟。玩家选择武器类型，调整角度与力度，然后开火——看着抛射物划过空中的弧线，砸进可破坏的地形。张力在于资源稀缺：弹药有限，每一发都必须算数，而城堡的几何结构本身构成了谜题：该打哪里才能造成最大的结构性崩塌。基调是中世纪工程学：木铁机械、石粉飞扬，以及砖石垮塌时那令人满足的碎裂声。

## 玩家体验流程

玩家从标题画面进入一张由防御日益坚固的城堡组成的战役地图。每个关卡在右侧显示目标城堡，左侧显示玩家的攻城阵位，二者之间是地形。

玩家从可用的武器类型中选择：投石机用于高抛越墙，弩炮用于平直直射，抛石机用于中程轰击。每种武器的抛射物重量、速度与爆炸半径各不相同。玩家通过拖拽界面调整角度与力度来瞄准，并能看到一条弹道预览线。

开火后抛射物按物理规律飞行。命中时，城堡砖块会受到伤害，并可能开裂、崩落或整体倒塌，具体取决于结构支撑——移除一段承重墙会让它上方的一切都塌下来。玩家每关的射击次数有限，必须摧毁足够多的城堡部分以达到破坏阈值。

后期关卡会加入改变抛射物路径的风、抵抗特定武器类型的装甲墙，以及在两次射击之间修补损伤的守军。战役从简单的城墙一路升级到复杂的多塔要塞。

一个精心设计的结算画面会展示破坏百分比、已用射击次数与获得的星数。要拿到三星，必须以最少的射击次数完成高效拆除。

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

