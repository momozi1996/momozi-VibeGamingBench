# Open-World Ghost Hunting

Build a **2D open-world ghost hunting game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player explores haunted locations across an open-world town, using
specialised equipment to detect, track, and capture ghosts. The game feels
**atmospheric, tense, and investigative** -- think *Phasmophobia* meets
*A Short Hike* at a smaller scale. The art style must be **coherent and
dark-atmospheric**: muted palettes, fog overlays, flickering light sources,
and readable sprites against shadowy backgrounds.

## What the Player Experiences

1. **Title and Entry** -- The player arrives at a styled title screen with a
   spooky backdrop (foggy graveyard, flickering lantern, silhouette of a house)
   and a "Begin Hunt" or "Play" button. Starting drops them into the open-world
   town hub.

2. **The Haunted World** -- The player walks freely across an open-world town
   with at least four visually distinct haunted locations: an abandoned mansion
   (dark, broken windows, overgrown garden), a haunted forest (twisted trees,
   fog, glowing eyes), an old lighthouse (coastal, waves, creaking wood), and a
   derelict hospital (corridors, flickering lights, wheelchairs). Each location
   has its own atmosphere and ghost type.

3. **Detection Equipment** -- The player carries at least three tools: an EMF
   reader (beep frequency increases near ghosts), a thermal camera (shows cold
   spots as blue overlays), and a spirit box (captures ghost voices as text).
   Each tool has distinct visual and audio feedback. Ghosts are invisible
   without equipment -- the tools are the only way to find them.

4. **Ghost Types and Evidence** -- At least four distinct ghost types with
   unique behaviours: poltergeist (throws objects), wraith (freezing breath,
   walks through walls), banshee (screams before attacking), and shade (hides
   in darkness, afraid of light). Each type leaves specific evidence that the
   player must collect and cross-reference on an evidence board to identify it.

5. **The Hunt Phase** -- When enough evidence is collected, the ghost becomes
   aggressive: lights flicker, the environment distorts, and a hunt timer
   counts down. The player must use defensive items (crucifix, salt circle,
   flashlight) to survive and capture the ghost before time runs out.

6. **Sanity and Pressure** -- A sanity meter drops in darkness, when seeing
   ghost activity, or when alone too long. Low sanity causes hallucinations
   (false readings, fake shadows) and makes the ghost more aggressive. Light
   sources and safe rooms restore sanity, creating a push-pull between
   investigation and self-preservation.

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

# 开放世界捉鬼（Open-World Ghost Hunting）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界捉鬼游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家探索一座开放世界小镇中各处闹鬼的地点，使用专门的器材来探测、追踪并捕捉
幽灵。游戏的感觉是**氛围浓厚、紧张、充满调查感**——可以想象成小体量的
*Phasmophobia* 结合 *A Short Hike*。美术风格必须**统一且具有黑暗氛围感**：
低饱和配色、雾气叠层、闪烁的光源，以及在阴影背景中依然清晰可辨的精灵图。

## 玩家体验流程

1. **标题与进入** —— 玩家看到一个有设计感的标题画面，配有阴森的背景（雾气
   笼罩的墓地、闪烁的提灯、一栋房子的剪影）以及一个"开始狩猎"或"开始游戏"
   按钮。开始后玩家进入开放世界小镇枢纽。

2. **闹鬼的世界** —— 玩家在一座开放世界小镇中自由行走，其中至少有四个视觉上
   截然不同的闹鬼地点：一栋废弃宅邸（黑暗、破窗、荒芜的花园）、一片鬼森林
   （扭曲的树木、浓雾、发光的眼睛）、一座旧灯塔（临海、浪涛、吱呀作响的木头），
   以及一所废弃医院（走廊、闪烁的灯、轮椅）。每个地点都有自己的氛围和幽灵类型。

3. **探测器材** —— 玩家携带至少三件工具：EMF 探测仪（靠近幽灵时蜂鸣频率升高）、
   热成像相机（把低温区域显示为蓝色叠层）以及灵魂盒（把幽灵的声音转成文字）。
   每件工具都有独特的视觉和音频反馈。没有器材时幽灵是不可见的——工具是找到
   它们的唯一途径。

4. **幽灵类型与证据** —— 至少四种截然不同的幽灵类型，各有独特行为：骚灵
   （投掷物体）、怨魂（冰冷的呼吸，可穿墙）、报丧女妖（攻击前尖叫）以及
   暗影（藏身于黑暗，畏惧光）。每种类型都会留下特定的证据，玩家必须收集它们
   并在证据板上交叉比对以确定其身份。

5. **狩猎阶段** —— 当收集到足够的证据后，幽灵会变得具有攻击性：灯光闪烁、
   环境扭曲，狩猎计时器开始倒数。玩家必须使用防御道具（十字架、盐圈、手电筒）
   来存活下来，并在时间耗尽前捕捉幽灵。

6. **理智与压力** —— 一条理智值量表会在黑暗中、目睹幽灵活动时或独处过久时
   下降。低理智会引发幻觉（虚假读数、假的影子），并使幽灵更具攻击性。光源和
   安全房间能恢复理智，从而在调查与自保之间形成一种拉扯。

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

