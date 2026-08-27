# Iron Vanguard

Build **Iron Vanguard**, a 2D top-down grid-based tactical tank defense game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A lone armored tank holds the line against relentless waves of automated
warmachines bearing down on a critical command core. The tension lives in
positioning and restraint: movement is grid-locked, only one shell can exist on
screen at a time, and every shot must count because the enemy never stops
advancing. The player is always choosing between pushing forward to intercept a
flanking column and falling back to guard the core from a breakthrough. Terrain
shapes every engagement — brick barricades offer temporary cover until they
crumble, steel walls funnel traffic into kill zones, and mud patches punish
careless repositioning. The risk is always the same: one shell slips past, one
enemy reaches the core, and the defense collapses instantly. The tone is gritty
dieselpunk — rust-iron plating, neon hazard lines, deep shadows, and the
percussive flash of shell impacts.

## What the Player Experiences

A dark industrial title screen sets the mood before the player enters a tactical
map showing available defense zones. Each zone is a distinct battlefield with its
own layout and enemy composition, inviting the player to choose where to make
their stand.

Combat drops the player's tank onto a grid battlefield adjacent to the glowing
command core. The field is a maze of destructible brick walls, impenetrable steel
barriers, and treacherous mud patches. Enemies pour from spawn points at the top
of the screen in waves, each wave more aggressive than the last. Some enemies
rush the core directly, others hunt the player, and specialized carriers glow
with salvageable cargo.

The player steers with grid-locked directional inputs and fires a single shell at
a time — no spray-and-pray, just deliberate aim. Destroying a carrier drops
battlefield salvage: armor repairs, temporary fortifications around the core, or
an EMP pulse that freezes everything on screen. Taking hits degrades the tank's
hull layer by layer; lose all armor and a life is spent.

Victory comes when the last enemy in the wave queue is destroyed, rewarding the
player with accuracy metrics and unlocking the next zone. Defeat is instant if
the core takes a single hit, or gradual if lives run out. Either way the player
returns to the map to regroup and try again.

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

# 铁血先锋（Iron Vanguard）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Iron Vanguard**，一款 2D 俯视视角、基于网格的战术坦克防守游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一辆孤零零的装甲坦克，独自挡住一波又一波扑向关键指挥核心的自动战争机械。张力就在于站位与克制：移动被锁定在网格上，屏幕上同时只能存在一枚炮弹，而且敌人从不停止推进，所以每一发都必须命中要点。玩家永远在两件事之间抉择：前压去截击一支侧翼纵队，还是回撤守住核心以防被突破。地形塑造着每一场交战——砖砌路障提供临时掩体，直到它们崩解；钢墙把敌人流量引入杀伤区；泥地则惩罚草率的重新占位。风险始终如一：一发炮弹漏过、一个敌人抵达核心，防线就会瞬间崩塌。整体调性是粗砺的柴油朋克——锈铁装甲板、霓虹警示条纹、深重阴影，以及炮弹命中时敲击般的闪光。

## 玩家体验流程

一个暗黑工业风的标题画面奠定气氛，随后玩家进入一张显示可选防守区域的战术地图。每个区域都是一处布局与敌人构成各异的战场，邀请玩家自行选择在何处坚守。

战斗把玩家的坦克投放到网格战场上，紧邻发光的指挥核心。战场是一座由可破坏砖墙、无法穿透的钢制屏障和危险泥地构成的迷宫。敌人成波地从屏幕顶部的出生点涌出，每一波都比上一波更凶悍。有些敌人直冲核心，有些猎杀玩家，而特殊的运输载具则闪着可回收物资的光。

玩家用网格锁定的方向输入操控，并且同时只发射一枚炮弹——没有乱扫乱射，只有刻意瞄准。摧毁一辆运输载具会掉落战场回收物：装甲修复、核心周围的临时防御工事，或是一记冻结全屏一切的 EMP 脉冲。受到打击会一层层削掉坦克的装甲；装甲全失就损失一条命。

当波次队列中的最后一个敌人被摧毁时便取得胜利，玩家会获得命中率数据并解锁下一个区域。若核心受到哪怕一次打击就是立刻失败，若生命耗尽则是渐进的失败。无论哪种情况，玩家都会回到地图重整并再次尝试。

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

