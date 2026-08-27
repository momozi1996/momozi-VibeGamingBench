# Zoo Keeper

Build **Zoo Keeper**, a **zoo management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player builds and manages a zoo, constructing enclosures for diverse
animals, keeping visitors happy, and pursuing conservation goals. Each animal
species has habitat requirements — size, terrain type, temperature, companions
— and meeting them keeps animals healthy and breeds new ones. Visitors pay
admission and spend at gift shops and food stalls, but they come for the
animals: rare species and well-designed enclosures draw bigger crowds. The
tension is between commercial pressure (visitors want spectacle) and animal
welfare (cramped exhibits stress animals). The tone is bright and educational:
lush habitats, informational plaques, and the joy of seeing animals thrive.

## What the Player Experiences

From the title screen the player starts a new zoo. The view shows a top-down
park grid with an entrance gate. The player builds paths, enclosures, visitor
amenities, and staff buildings.

Enclosures are built by fencing an area and assigning a biome type (savanna,
arctic, jungle, aquatic). Animals are acquired from a catalog — each has a
purchase cost, habitat requirement, and popularity rating. Placing an animal
in a matching habitat keeps it happy; mismatched habitats cause stress shown
by a visible mood indicator.

Visitors enter through the gate, walk paths, view enclosures, and spend money.
Visitor happiness depends on animal variety, enclosure quality, path layout,
and amenity availability. Happy visitors stay longer and spend more.

Breeding is triggered when compatible animals share a well-maintained
enclosure. Baby animals are a major visitor draw and can be kept or traded for
conservation points. Conservation goals (breed endangered species, maintain
genetic diversity) provide bonus objectives beyond pure profit.

Staff (keepers, vets, janitors) must be hired and assigned. The game tracks
money, visitor count, animal welfare score, and conservation progress. A styled
result screen shows zoo statistics at the end of each season.

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

# 动物园管理员（Zoo Keeper）

在 `/workspace/game/` 用 Godot 4 开发 **Zoo Keeper**，一款**动物园管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家营建并管理一座动物园，为各种各样的动物建造围栏展区，让游客保持愉快，并追求保育目标。每个动物物种都有栖息地要求——面积、地形类型、温度、同伴——满足这些要求能让动物保持健康并繁育出新的个体。游客支付门票并在礼品店和食品摊消费，但他们是为动物而来：稀有物种和设计精良的围栏展区能招来更大的人群。张力存在于商业压力（游客想看奇观）与动物福利（拥挤的展区让动物应激）之间。整体基调明亮而富有教育意味：郁郁葱葱的栖息地、知识介绍牌，以及看到动物茁壮成长的那份喜悦。

## 玩家体验流程

玩家从标题画面开始一座新的动物园。视图展示一片俯视的园区网格，带有一座入口大门。玩家建造道路、围栏展区、游客便利设施和员工建筑。

围栏展区通过围起一块区域并指定生物群落类型（草原、极地、丛林、水生）来建造。动物从一份目录中获取——每种都有购置成本、栖息地要求和人气评级。把动物放进相符的栖息地能让它保持愉快；不匹配的栖息地会造成应激，并通过一个可见的情绪指示器显示出来。

游客从大门进入，沿道路行走，观赏围栏展区并花钱。游客愉快度取决于动物种类的丰富程度、围栏展区品质、道路布局和便利设施的可用性。愉快的游客会停留更久、花得更多。

当彼此相容的动物共处于一个维护良好的围栏展区时，就会触发繁育。幼崽动物是重要的游客卖点，可以留下，也可以换取保育点数。保育目标（繁育濒危物种、维持遗传多样性）在纯粹的利润之外提供额外的目标。

员工（饲养员、兽医、清洁工）必须招聘并分配岗位。游戏会记录资金、游客数量、动物福利评分和保育进度。一个经过美术处理的结算画面会在每个季度结束时展示动物园统计数据。

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

