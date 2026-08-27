# Cardgame Inscription Dark

Build a Cardgame Inscription Dark as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A dark and atmospheric card battle game where creatures are summoned by
sacrificing other creatures. The player places cards on a grid battlefield,
but powerful cards demand blood — weaker creatures must be sacrificed to fuel
stronger summons. Each card bears sigils (passive abilities) that create
emergent interactions: a card with "Airborne" flies over blockers; one with
"Bifurcated Strike" hits two lanes. An overworld map connects encounters with
branching paths, and a creeping meta-narrative unfolds through environmental
storytelling. The fantasy is the unsettling thrill of sacrificing your own
creatures for power, wrapped in a cabin-horror atmosphere.

## What the Player Experiences

1. **Title Screen** — A dimly lit wooden table with the game name scratched
   into the surface in rough lettering, a flickering candle, and a "Begin"
   card the player clicks. No plain HTML grey.
2. **The Table** — Battles take place on a 4-lane grid. The player's row faces
   the opponent's row. Cards are played from hand into lanes. Each card has
   attack power, health, a blood cost, and zero or more sigils.
3. **Sacrifice Mechanic** — To play a card costing 2 blood, the player must
   first sacrifice 2 of their own creatures already on the field. Sacrificed
   creatures die with a visual effect. Free cards (0 cost) serve as sacrifice
   fodder. This creates a constant tension between board presence and power.
4. **Sigils** — At least 8 distinct sigils with unique icons: Airborne (attacks
   directly), Bifurcated Strike (hits adjacent lanes too), Mighty Leap (blocks
   Airborne), Stinky (adjacent enemies lose 1 attack), Unkillable (returns to
   hand on death), Fledgling (evolves after 1 turn), Touch of Death (kills
   anything it damages), Many Lives (has 3 extra lives).
5. **Damage Scale** — A balance scale tips as damage is dealt. When one side
   takes 5 more total damage than the other, that side loses. The scale
   visually tips with each hit, creating tension as it approaches the tipping
   point.
6. **Overworld Map** — Between battles, a branching path map shows nodes:
   card battles, totem poles (add a sigil to a card), campfires (merge two
   cards), and traders (buy/sell cards). The player chooses their route.
7. **Atmosphere** — Dark, muted colour palette. Cards look hand-drawn on
   parchment. The opponent is a shadowy figure whose eyes glow. Ambient
   effects (dust motes, candle flicker) reinforce the unsettling mood.

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

# 黑暗铭刻（Cardgame Inscription Dark）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个黑暗铭刻卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款黑暗且氛围浓厚的卡牌对战游戏，召唤生物需要献祭其他生物。玩家把卡牌放到网格
战场上，但强力卡牌索求鲜血——必须献祭较弱的生物来为更强的召唤供能。每张卡都刻有
印记（被动能力），它们会催生出涌现式的互动：带"飞行"的卡越过阻挡者；带"分叉打击"
的卡同时命中两条通道。一张大地图以分支路径串联起各场遭遇，一段悄然渗出的元叙事
则通过环境叙事层层展开。这份幻想在于：在木屋恐怖的氛围包裹下，为力量而献祭自己
生物时那种令人不安的快感。

## 玩家体验流程

1. **标题画面** —— 一张光线昏暗的木桌，游戏名以粗糙的字体刻在桌面上，一支摇曳的
   蜡烛，以及一张供玩家点击的"开始"卡牌。演出 GameX其灰色。
2. **牌桌** —— 战斗在 4 条通道的网格上展开。玩家的一排面对对手的一排。卡牌从手牌
   打进各条通道。每张卡都有攻击力、生命值、鲜血消耗，以及零个或多个印记。
3. **献祭机制** —— 要打出一张消耗 2 点鲜血的卡，玩家必须先献祭场上自己已有的
   2 个生物。被献祭的生物会伴随视觉效果死去。免费卡牌（0 消耗）可充当献祭素材。
   这在场面控制与力量之间制造出持续的张力。
4. **印记** —— 至少 8 种各具独特图标的印记：飞行（直接攻击）、分叉打击（同时命中
   相邻通道）、强力跃击（可阻挡飞行）、恶臭（相邻敌人攻击力 -1）、不灭（死亡时
   回到手牌）、雏鸟（1 回合后进化）、死亡之触（杀死任何被它伤害的目标）、九命
   （额外拥有 3 条命）。
5. **伤害天平** —— 一座天平会随伤害的造成而倾斜。当一方承受的总伤害比另一方多出
   5 点时，该方落败。天平每次受击都会在视觉上倾斜，随着逼近临界点而制造张力。
6. **大地图** —— 战斗之间会出现一张分支路径地图，上面有各类节点：卡牌对战、图腾柱
   （为一张卡添加印记）、营火（合并两张卡）、商人（买卖卡牌）。玩家自行选择路线。
7. **氛围** —— 黑暗、低饱和的配色。卡牌看起来像手绘在羊皮纸上。对手是一个双眼
   发光的黑影身形。环境效果（浮尘、烛火闪动）进一步强化这种令人不安的情绪。

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

