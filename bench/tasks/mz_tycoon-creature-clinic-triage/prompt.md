# Creature Clinic Triage

Build **Creature Clinic Triage**, a compact **creature-care clinic simulation**
as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player runs a tiny fantasy veterinary clinic during a busy shift. Creatures
arrive faster than they can be treated, each carrying visible ailments that hint
at what they need. The core tension is triage under pressure: which patient do
you attend first, where do you send them, and what happens to the ones still
waiting? Correct reads and smart routing keep the clinic humming and build
reputation; mistakes, delays, or mismatches cost health and trust.

The tone is warm but operational. The clinic floor should feel alive with
queuing creatures, busy stations, and clear feedback when things go right or
wrong. Avoid spreadsheet aesthetics; make it feel like a working fantasy
infirmary.

## What the Player Experiences

The player opens to a themed clinic entrance and begins a shift. Patients start
filing in, each a distinct creature with visible symptoms and an urgency
indicator. Early arrivals are straightforward — one clear ailment, one obvious
destination. The player learns the rhythm: inspect, decide, route.

As the shift continues, the queue grows. New creature types appear with
unfamiliar or combined symptoms. Stations fill up or run low on supplies.
The player must now prioritize: stabilize the critical case or clear the easy
ones to free capacity? A wrong routing wastes time and worsens the patient.
Ignoring urgency lets conditions deteriorate.

Late in the shift, pressure peaks — emergencies, compound cases, resource
scarcity. The player juggles capacity against urgency, making rapid imperfect
decisions. When the shift ends, a results summary reflects how well they
managed: creatures healed, creatures lost, reputation earned, and whether
they unlocked harder shifts or upgrades.

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

# 生物诊所分诊（Creature Clinic Triage）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Creature Clinic Triage**，一款小体量的**生物护理诊所模拟**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个繁忙的班次里经营一家小小的奇幻兽医诊所。生物到诊的速度快于能被治疗的速度，每只身上都带着可见的病症，暗示它们需要什么。核心张力在于高压下的分诊：先接诊哪位病患，把它送去哪里，还在排队等候的那些又会怎样？判断正确、调度得当，诊所就能运转顺畅、积累声望；判断失误、延误或错配，则要付出健康与信任的代价。

整体基调温暖却讲究实务。诊所大厅应当显得生机勃勃：排队的生物、忙碌的工位，以及事情做对或做错时清晰的反馈。避免电子表格式的美学；要让它像一间真正运作中的奇幻医务室。

## 玩家体验流程

玩家一进入游戏，看到的是有主题感的诊所门厅，随后开始一个班次。病患陆续进门，每一只都是有明显症状和紧急程度指示的独特生物。最早到诊的都很直白——一种明确的病症，一个显而易见的去处。玩家从中学会节奏：查看、决断、分流。

随着班次推进，队伍越排越长。新的生物种类出现，带着陌生或复合的症状。工位被占满，或者物资见底。此时玩家必须权衡取舍：先稳住危重病例，还是先清掉简单的以腾出接诊能力？分流错误会浪费时间并让病患恶化。忽视紧急程度则会让病情持续劣化。

到了班次后期，压力达到顶点——急诊、复合病例、资源短缺。玩家要在接诊能力与紧急程度之间来回权衡，快速做出并不完美的决定。班次结束时，一份结算总览反映玩家的管理成效：治愈的生物、失去的生物、赢得的声望，以及是否解锁了更难的班次或升级。

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

