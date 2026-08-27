# Open-World Archaeology

Build a **2D open-world archaeology game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).:
an expedition across ancient ruins where the player excavates buried artefacts,
deciphers forgotten inscriptions, and reconstructs lost civilisations one dig
at a time.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Unearth the past. The player is an archaeologist who travels to remote dig
sites, carefully removes layers of earth and stone, and discovers artefacts
that tell the story of vanished cultures. The fantasy is patient revelation:
each brush stroke peels back time, each shard connects to a larger picture, and
the deeper you dig the rarer and more fragile the finds become. One careless
swing of the pickaxe can shatter a legendary relic; one solved inscription can
unlock a hidden chamber no one has entered in millennia.

The pressure comes from the sites themselves. Sandstorms bury progress, floors
collapse underfoot, oxygen runs thin in flooded passages. The player must read
the terrain, choose the right tool, and decide when to push deeper versus when
to retreat and catalogue what they have. A growing museum back at base camp
makes every expedition feel worthwhile -- each new display fills in a gap in
the timeline and unlocks access to the next frontier.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen that
   establishes the mysterious, ancient tone -- torchlit stone, weathered maps,
   sand drifting across glyphs. Starting an expedition drops them into the
   overworld.

2. **Exploration** -- The world stretches across multiple biomes, each hiding
   its own dig sites. Desert temples shimmer under a scorching sun, jungle ruins
   drip with moss and vine, sunken pillars glow beneath turquoise water, and
   mountain tombs sit locked in ice. Walking between sites feels like a journey
   -- the terrain changes, the palette shifts, the ambient mood transforms.

3. **Excavation** -- At a dig site the player switches between tools -- a
   delicate brush for fragile surfaces, a trowel for packed earth, a pickaxe
   for solid rock. Each tool removes material at a different speed and risk.
   Layers peel away visually, revealing colour changes and texture shifts as
   depth increases, until an artefact edge glimmers into view.

4. **Discovery and Cataloguing** -- Unearthed artefacts range from common
   pottery shards to legendary golden idols. Each has a distinct look, a rarity
   tier, and a short historical description. Rare finds are buried deeper and
   demand more careful tool selection. The player feels the thrill of not
   knowing what lies beneath the next layer.

5. **Puzzles and Secrets** -- Some sites hide inscribed tablets or symbol murals
   that gate access to sealed chambers. The player manipulates symbols -- matching,
   rotating, tracing -- until the lock yields and a passage opens with a
   satisfying rumble. Inside waits a guaranteed rare artefact or a new wing of
   ruins to explore.

6. **Museum and Progression** -- Back at base camp, a museum tent displays
   every collected artefact on labelled shelves. Arranging finds by culture or
   era earns research points that unlock improved tools and new dig sites on the
   map. The museum grows from empty shelves to a rich gallery, charting the
   player's journey through history.

7. **Hazards and Tension** -- Each biome threatens the player differently:
   sandstorms obscure vision, jungle floors collapse, underwater oxygen depletes,
   mountain ice triggers avalanches. The player watches a health or safety gauge,
   decides whether to press on or retreat, and scavenges safety gear to push
   further next time.

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

# 开放世界考古（Open-World Archaeology）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界考古游戏**：
一场穿越远古遗迹的考察远征，玩家在其中挖掘埋藏的文物、解读被遗忘的铭文，
并一次次通过发掘重建失落的文明。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

发掘过去。玩家是一名考古学家，前往偏远的发掘现场，小心地剥离层层泥土与
岩石，发现讲述消亡文化故事的文物。这里的幻想是耐心的揭示：每一次刷扫都
拂开时间，每一块碎片都连向更大的图景，而挖得越深，出土之物越稀有、越脆弱。
一次不慎的鹤嘴锄挥击就能砸碎一件传说级遗物；一段解开的铭文则可能打开一间
千年无人踏入的密室。

压力来自遗址本身。沙暴会掩埋进度，地面会在脚下塌陷，被水淹没的通道里氧气
日渐稀薄。玩家必须读懂地形、选对工具，并判断何时该继续深入、何时该撤回去
整理已有的收获。大本营里不断扩充的博物馆让每一次远征都显得值得——每一件
新展品都填补了时间线上的一处空白，并解锁通往下一片未知疆域的资格。

## 玩家体验流程

1. **标题与进入** —— 玩家看到一个有设计感的标题画面，它奠定神秘而古老的
   基调——火把照亮的石墙、风化的地图、掠过刻纹的流沙。开启一次远征后，玩家
   进入大地图。

2. **探索** —— 世界横跨多个生态区，每个区域都藏着自己的发掘现场。沙漠神庙
   在灼热的日光下泛着微光，丛林遗迹上苔藓与藤蔓滴着水珠，沉没的石柱在青绿色
   的水下发亮，山地陵墓封锁在坚冰之中。在遗址之间行走本身就像一段旅程——
   地形在变，配色在变，环境氛围也随之转变。

3. **发掘** —— 在发掘现场，玩家在多种工具间切换——用于脆弱表面的精细毛刷、
   用于板结泥土的手铲、用于坚硬岩石的鹤嘴锄。每种工具的清除速度和风险都不同。
   土层在视觉上逐层剥落，随着深度增加显现出颜色变化与质感差异，直到一件文物的
   边缘闪入视野。

4. **发现与编目** —— 出土文物从常见的陶片到传说级的黄金神像不等。每一件都有
   独特的外观、稀有度等级和一段简短的历史描述。稀有发现埋得更深，也要求更谨慎
   的工具选择。玩家能感受到那种不知道下一层之下究竟藏着什么的兴奋。

5. **谜题与秘密** —— 有些遗址藏着刻字石板或符号壁画，它们把通往封闭密室的
   道路锁住。玩家操作这些符号——配对、旋转、描摹——直到机关松动，通道在一声
   令人满足的轰隆中打开。里面等着的是一件必定稀有的文物，或者一片可供探索的
   新遗迹区域。

6. **博物馆与进程** —— 回到大本营，一顶博物馆帐篷把收集到的每件文物陈列在
   带标签的架子上。按文化或年代整理藏品可获得研究点数，用来解锁更好的工具和
   地图上的新发掘现场。博物馆从空荡的货架成长为丰富的展廊，记录着玩家穿越
   历史的旅程。

7. **危险与张力** —— 每个生态区威胁玩家的方式各不相同：沙暴遮蔽视野，丛林
   地面塌陷，水下氧气耗尽，山地坚冰引发雪崩。玩家盯着一条生命值或安全度
   量表，决定是继续推进还是撤退，并搜集安全装备以便下次走得更远。

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

