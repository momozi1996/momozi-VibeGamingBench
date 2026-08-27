# Arcane Academy

Build **Arcane Academy**, a magic-school stat-raising visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a first-year at a school of magic, and a term is short. There is never
enough time to master everything, so what you choose to study — elemental
sorcery, runecraft, alchemy, the tempting forbidden arts — slowly shapes the
mage you become. Arcane Academy is a **stat-raising visual novel**: between
story beats the player spends limited time and effort training different
disciplines, and the magician they grow into decides how classmates and
mentors treat them, which paths open, and how the term ends.

The fantasy is **becoming someone through the choices of a single term**. The
heart of the loop is **plan, train, live the consequences** — deciding where to
invest scarce time, watching abilities rise, and then meeting story moments
where who you have become matters as much as what you say. A student who poured
everything into forbidden magic walks a different road than a diligent
runescribe, and the writing should make that growth felt. It should play like a
warm, atmospheric school story with real stakes and genuinely different
outcomes, not a linear tour with a single ending.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player arrives at the
   academy and is introduced to the term ahead, the disciplines they might
   study, and the classmates and mentors around them, presented as illustrated
   scenes with characters and narration.
2. **Planning the Term** — Across the term the player repeatedly decides how to
   spend limited time and energy, choosing which magical disciplines to train.
   Time is scarce, so investing in one pursuit means neglecting another, and the
   player feels the weight of the trade-off.
3. **Growth That Shows** — Training visibly raises the player's abilities, and
   that progress is something the player can read and care about. The mage they
   are building takes shape over the term rather than staying fixed.
4. **Story Beats That Test You** — Between training, authored story scenes
   unfold — a rivalry, a mentor's offer, a forbidden temptation, a crisis at the
   school — where the player makes meaningful choices. What the player has
   trained matters here: some options, lines, or events are only available to a
   mage who built the right strengths, so growth and choice intertwine.
5. **A Term That Ends in Many Ways** — The term resolves in one of several
   genuinely different endings — honored graduate, fallen to the forbidden arts,
   expelled in disgrace, or the keeper of a hidden truth — each reachable
   through how the player trained and chose, and shown as an authored, styled
   conclusion that names what they became. The player can begin a new term to
   grow into someone else.

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

# 秘法学院（Arcane Academy）

在 `/workspace/game/` 用 Godot 4 开发 **Arcane Academy**——一款魔法学院题材的
属性养成视觉小说。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

你是一所魔法学校的一年级新生，而一个学期很短。时间永远不够你精通一切，因此
你选择研习什么——元素咒术、符文技艺、炼金术，还是那诱人的禁忌之术——会慢慢
塑造出你将成为的那个法师。Arcane Academy 是一款**属性养成视觉小说**：在剧情
节点之间，玩家把有限的时间与精力投入不同学科的修习，而他们养成出的这个魔法师
决定了同学与导师如何对待他们、哪些道路会开启，以及这个学期如何收场。

游戏的幻想内核是**通过一个学期的选择成为某个人**。循环的核心是
**规划、修习、承受后果**——决定把稀缺的时间投向何处，看着能力节节攀升，然后
迎来那些"你已成为谁"和"你说了什么"同等重要的剧情时刻。把一切都倾注在禁忌
魔法上的学生，与一位勤勉的符文抄写者走的是完全不同的路，而文本应当让这份
成长被真切感受到。它玩起来应当像一个温暖、氛围浓厚且真有代价的校园故事，
拥有确实不同的结局，而不是一趟只有单一结局的线性观光。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家抵达学院，被介绍
   即将到来的学期、他们可能研习的学科，以及身边的同学与导师，这些都以带有
   角色与旁白的插画场景呈现。
2. **规划这个学期** —— 整个学期中，玩家要反复决定如何分配有限的时间与精力，
   选择修习哪些魔法学科。时间是稀缺的，所以投入一项追求就意味着荒废另一项，
   玩家能感受到这种取舍的重量。
3. **看得见的成长** —— 修习会明显提升玩家的能力，而这份进展是玩家可以读取、
   也会在意的东西。他们正在塑造的那个法师会在整个学期中逐渐成形，而不是
   一成不变。
4. **考验你的剧情节点** —— 在修习之间，会展开精心编写的剧情场景——一场竞争、
   一位导师的提议、一次禁忌的诱惑、学校里的一场危机——玩家在其中做出有意义的
   选项。玩家修习过什么在这里至关重要：某些选项、台词或事件只对培养出相应
   强项的法师开放，于是成长与选择彼此交织。
5. **有多种收场方式的学期** —— 学期会以数个确实不同的结局之一收束——受表彰的
   毕业生、堕入禁忌之术、被耻辱地开除，或成为某个隐秘真相的守护者——每一个都
   通过玩家如何修习、如何选择来抵达，并以精心编排、有设计感的结语呈现，点明
   他们成为了什么。玩家可以开启一个新学期，成长为另一个人。

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

