# Horror Tape Archive

Build a **Horror Tape Archive** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player reviews surveillance tapes from a facility, scrubbing through footage
to find and timestamp anomalies. The fantasy is forensic dread: watching mundane
footage knowing something is wrong, catching the moment a shadow moves on its
own or a figure appears where none should be. Tension comes from a sanity meter
that drains as anomalies are witnessed, and from the growing realisation that
the tapes are watching back. Each correctly timestamped anomaly advances the
investigation but costs mental stability.

## What the Player Experiences

1. **Title Screen** — A VHS-styled title with tracking lines, the game name in
   monospace font, and a play button styled as a tape deck control.
2. **The Archive Room** — A desk with a CRT monitor, a tape shelf, a clipboard
   for notes, and a sanity gauge. The room is dimly lit with a single desk lamp.
3. **Tape Selection** — The player chooses from multiple labelled tapes on the
   shelf. Each tape covers a different camera location: hallway, lab, storage,
   courtyard. Tapes have different lengths and anomaly counts.
4. **Footage Review** — The monitor shows grainy surveillance footage. The player
   can play, pause, rewind, and fast-forward. A timestamp counter runs in the
   corner. The footage shows mostly normal activity with subtle anomalies hidden
   within.
5. **Anomaly Detection** — When the player spots something wrong (a shadow moving
   against the light, an object disappearing, a figure in the background), they
   pause and click "Mark Anomaly" with the current timestamp. Correct marks earn
   investigation points; false marks cost sanity.
6. **Sanity Meter** — Watching anomalies drains sanity. Low sanity causes visual
   corruption: the archive room distorts, phantom sounds play, and false
   anomalies appear in the footage to trick the player. At zero sanity, the
   session ends.
7. **Investigation Progress** — Correctly marked anomalies fill a case board,
   connecting events across tapes. Completing connections unlocks new tapes and
   reveals the facility's secret. The final tape shows what happened to the
   previous archivist.

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

# 恐怖录像档案（Horror Tape Archive）

在 `/workspace/game/` 用 Godot 4 开发一个**恐怖录像档案**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家要审查一处设施的监控录像带，来回拖动画面以找出异常并标记时间码。游戏的
幻想核心是取证式的恐惧：明知有什么地方不对劲，却只能盯着平淡无奇的画面，
去抓住某个影子自行移动、或某个身影出现在本不该有人之处的那一瞬。紧张感来自
一条理智值量表——每目睹一次异常它就下降，也来自一个逐渐浮现的认知：录像带
也在反过来看着你。每一次正确标记时间码都会推进调查，但要以精神稳定为代价。

## 玩家体验流程

1. **标题画面** —— 一个 VHS 风格的标题，带有走带扫描线，游戏名采用等宽字体，
   开始按钮做成录像机控制键的样式。
2. **档案室** —— 一张桌子，上面有一台 CRT 显示器、一个录像带架、一块记笔记的
   写字板，以及一个理智值量表。房间只由一盏台灯昏暗地照亮。
3. **录像带选择** —— 玩家从架子上多卷贴有标签的录像带中挑选。每卷带子对应
   一个不同的摄像机位置：走廊、实验室、储藏室、庭院。不同带子的时长和异常
   数量各不相同。
4. **画面审查** —— 显示器播放带颗粒感的监控画面。玩家可以播放、暂停、倒带和
   快进。角落里有一个时间码计数器在走动。画面大多是正常活动，其中藏着细微的
   异常。
5. **异常侦测** —— 当玩家发现有什么不对（影子逆着光移动、某个物体消失、
   背景里出现一个身影）时，就暂停并以当前时间码点击"标记异常"。标记正确可
   获得调查点数；误标则损耗理智值。
6. **理智值量表** —— 观看异常会消耗理智值。低理智会引发视觉损坏：档案室扭曲、
   响起幻听声、画面中出现虚假的异常来欺骗玩家。理智值归零时，本次审查结束。
7. **调查进度** —— 被正确标记的异常会填满一块案情板，把跨录像带的事件串联
   起来。完成串联可解锁新的录像带，并揭开这处设施的秘密。最后一卷带子展示了
   上一任档案员的遭遇。

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

