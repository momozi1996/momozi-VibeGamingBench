# Thunder Valkyrie

Build **Thunder Valkyrie**, a 2D vertical scrolling bullet-hell shoot-'em-up as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A lone starfighter threads through mathematically dense curtains of enemy fire,
where every pixel of the hitbox matters and every split-second dodge buys another
breath. The tension lives in reading bullet geometry: patterns sweep, spiral, and
converge while the player traces the one safe seam through the chaos. Between
sorties the pilot reinvests plundered gold into hull upgrades, sub-weapons, and
wingman attachments, reshaping how the next wave feels. The tone is bright,
kinetic, and relentless — an arcade reflex challenge wrapped in deep-space neon
and spectacular particle destruction.

## What the Player Experiences

A styled title screen introduces the game with a cosmic backdrop and a clear
path into the hangar.

In the hangar the player reviews their persistent loadout — starfighter level,
shield type, sub-weapon, wingman — and spends gold earned from prior runs to
upgrade slots. Each upgrade visibly changes projectile patterns or survivability
for the next sortie.

From a sector map the player selects a constellation stage. Each stage has a
distinct stellar backdrop and its own enemy composition. Locked stages remain
gated until the previous boss falls.

Once deployed, the screen scrolls vertically over a layered starfield. The
starfighter moves smoothly in response to input, its tiny glowing core hitbox
the only vulnerable point. Primary lasers fire continuously; sub-weapons and
wingmen add flanking fire. Waves of enemy interceptors enter in geometric
formations, releasing scripted bullet configurations that sweep downward. Elite
capital ships drop red power crystals; collecting them triggers a frenzy state
that doubles fire rate and vacuums nearby pickups.

Each stage culminates in a multi-phase boss that locks the scroll and floods the
arena with layered patterns. Taking damage degrades the shield; if it breaks the
run ends with a results overlay showing gold earned and waves survived. Defeating
the boss unlocks the next stage and awards premium components.

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

# 雷霆女武神（Thunder Valkyrie）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Thunder Valkyrie**，一款 2D 纵向卷轴弹幕射击游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一架孤零零的星际战机在数学般密集的敌方火力帷幕中穿行，判定框上的每一个像素都举足轻重，每一次毫秒级的闪避都换来又一口呼吸。张力就在于读懂弹幕几何：弹道会横扫、旋绕、汇聚，而玩家要在混乱之中描出那唯一一道安全的缝隙。出击之间，飞行员把掠夺来的黄金重新投入到船体升级、副武器和僚机挂件上，重塑下一波的手感。整体调性明亮、动感而不留余地——一场包裹在深空霓虹与壮观粒子爆破中的街机反应挑战。

## 玩家体验流程

一个经过设计的标题画面以宇宙背景介绍这款游戏，并给出一条通往机库的清晰路径。

在机库里，玩家查看自己持久保存的配装——星际战机等级、护盾类型、副武器、僚机——并花掉先前几轮赚来的黄金去升级各个槽位。每项升级都会明显改变下一次出击的弹道形态或生存能力。

玩家从一张星区地图上选择一个星座关卡。每个关卡都有独特的星空背景和自己的敌人构成。被锁定的关卡会一直封着，直到前一个 Boss 倒下。

一旦部署，画面便在层叠的星空之上纵向滚动。星际战机随输入平顺移动，其微小的发光核心判定框是唯一的可受伤部位。主激光持续开火；副武器和僚机则补上侧翼火力。一波波敌方截击机以几何编队入场，释放出向下横扫的脚本化弹幕配置。精英主力舰会掉落红色能量水晶；拾取它们会触发一种狂热状态，使射速翻倍并把附近的拾取物吸过来。

每个关卡都以一场多阶段 Boss 战收尾，Boss 会锁住卷轴并用层叠弹幕淹没整个场地。受到伤害会削减护盾；若护盾破碎，这一轮就以一个显示所得黄金和存活波数的结算浮层结束。击败 Boss 会解锁下一个关卡并奖励高级组件。

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

