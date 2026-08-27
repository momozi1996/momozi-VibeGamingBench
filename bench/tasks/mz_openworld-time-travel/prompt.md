# Open-World Time Travel

Build a **2D open-world time-travel game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player discovers a time-travel device and explores the same open-world
location across multiple distinct eras — a lush ancient past, a bustling
industrial present, and a desolate high-tech future. Actions in one era ripple
forward and alter the landscape, inhabitants, and available paths in later eras.
The fantasy is **temporal cause and effect**: the player reads the world, makes
deliberate changes in the past, then jumps forward to witness consequences
unfold. Tension comes from the butterfly effect — a small act of kindness or
destruction cascades across centuries — and from paradox: the world resists
contradictions, and the player must think carefully about what they change and
when. The game should feel mind-bending and interconnected, like a puzzle box
made of history.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a "Begin Journey"
   or "Play" button, and a temporal backdrop (overlapping landscapes bleeding
   into each other, clock gears, aurora). No naked Godot grey.
2. **Three Eras** — The same geographical region rendered in three visually
   distinct time periods: an ancient wilderness with warm saturated greens, an
   industrial cityscape with muted greys and oranges, and a ruined future with
   cold blues and purples. The player walks freely in each era and recognises
   landmarks that persist across time.
3. **Time Travel** — The player activates a time-travel device to jump between
   eras. The transition plays a visible effect and the destination era loads
   with the player at the corresponding map coordinates, preserving spatial
   continuity.
4. **Butterfly Effect** — Actions in an earlier era alter later eras in visible,
   gameplay-meaningful ways. Multiple causal chains exist: planting something in
   the past changes the landscape in the future, destroying infrastructure
   reshapes routes, befriending NPCs leaves legacies for their descendants.
5. **Paradox Detection** — The game prevents or punishes paradoxical actions.
   Attempting to destroy something your future self depends on triggers warnings
   and instability until the paradox is resolved.
6. **Cross-Era Quests and NPCs** — Each era has unique NPCs whose quests span
   multiple time periods. Completing cross-era objectives unlocks new
   destinations or upgrades the time device.
7. **Temporal Inventory** — Items have era compatibility. Some survive time
   travel while others decay. The inventory communicates which items are stable
   and which will not survive the next jump.

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

# 开放世界时空穿越（Open-World Time Travel）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界时空穿越游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家发现了一台时空穿越装置，在多个截然不同的时代中探索同一处开放世界地点——
草木繁茂的远古过去、喧闹的工业当下，以及荒凉的高科技未来。在某个时代中的行为
会向后涟漪扩散，改变后续时代的地貌、居民和可通行的路径。这里的幻想是**时间上的
因与果**：玩家读懂世界，在过去做出有意的改动，然后跳向未来见证后果展开。张力
来自蝴蝶效应——一个微小的善举或破坏会跨越数个世纪层层放大——也来自悖论：世界
会抵抗矛盾，玩家必须仔细思考自己改变了什么、又是在何时改变的。游戏应当给人
一种令人脑洞大开、处处相互关联的感觉，就像一个由历史造就的谜题盒。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个"开始旅程"或"开始
   游戏"按钮，以及一幅时间主题背景（彼此交叠、相互渗透的地景、时钟齿轮、极光）。
   不要出现 Godot 的裸灰色。
2. **三个时代** —— 同一片地理区域被呈现为三个视觉上截然不同的时期：一片带有
   温暖高饱和绿色的远古荒野、一座色调低沉、灰橙交织的工业城景，以及一个冷蓝
   与紫色调的废墟未来。玩家可以在每个时代中自由行走，并认出跨越时间留存下来的
   地标。
3. **时空穿越** —— 玩家启动时空穿越装置在各时代间跳跃。转场会播放一段可见的
   效果，目标时代加载后玩家出现在对应的地图坐标上，从而保持空间上的连续性。
4. **蝴蝶效应** —— 在较早时代中的行为会以可见且对玩法有意义的方式改变后来的
   时代。存在多条因果链：在过去种下某物会改变未来的地貌，摧毁基础设施会重塑
   路线，与 NPC 结交会为其后代留下遗产。
5. **悖论检测** —— 游戏会阻止或惩罚构成悖论的行为。试图摧毁未来的自己所依赖
   之物会触发警告和不稳定状态，直到悖论被消解。
6. **跨时代任务与 NPC** —— 每个时代都有独特的 NPC，他们的任务横跨多个时期。
   完成跨时代目标可解锁新的目的地，或升级时间装置。
7. **时间物品栏** —— 物品具有时代兼容性。有些能经受时空穿越，有些则会腐坏。
   物品栏会告知哪些物品是稳定的、哪些无法在下一次跳跃中存留。

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

