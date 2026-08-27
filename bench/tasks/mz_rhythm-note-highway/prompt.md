# Rhythm Note Highway

Build a Rhythm Note Highway as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Notes cascade down a multi-lane highway toward a judgement line at the bottom
of the screen. The player must press the matching lane key precisely as each
note crosses the line. Accuracy builds a combo multiplier that amplifies the
score; misses break the streak and drain a life bar. The fantasy is performing
a concert — nailing every note in a flow state while the background stage
lights react to your accuracy. A full campaign of procedurally-timed songs
provides hours of escalating challenge.

## What the Player Experiences

1. **Title Screen** — A neon-lit stage backdrop with the game name in a bold
   stylized font, a campaign button, and a free-play button. No plain grey.
2. **Song Select** — A scrollable list of at least 10 songs with difficulty
   ratings (Easy/Medium/Hard), best scores, and completion grades (S/A/B/C/F).
   Songs unlock sequentially through the campaign.
3. **The Highway** — 4 lanes with colour-coded note gems falling toward a
   judgement bar. The player presses D/F/J/K (or arrow keys) to hit notes.
   Timing windows: Perfect, Great, Good, Miss — each with distinct visual
   feedback (burst, glow, shake).
4. **Combo System** — A combo counter increments on consecutive hits. The
   multiplier (x2, x4, x8) scales score. Breaking combo resets the counter
   with a visible shatter effect.
5. **Life Bar** — Misses drain health. If health hits zero, the song fails
   with a game-over screen showing stats. Perfects restore a small amount.
6. **Hold Notes and Slides** — Some notes require holding the key for their
   duration (a trailing tail). Others slide across lanes, requiring the player
   to follow with their finger position.
7. **Results Screen** — After each song: total score, max combo, accuracy
   percentage, grade, and a breakdown of Perfect/Great/Good/Miss counts.
   New high scores trigger a celebration animation.

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

# 节奏音符轨道（Rhythm Note Highway）

在 `/workspace/game/` 用 Godot 4 开发一个节奏音符轨道游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

音符沿着一条多轨道的音符轨道倾泻而下，奔向屏幕底部的判定线。玩家必须在每个
音符越过判定线的一瞬间，精准按下对应轨道的按键。准确度会积累出连击倍率来
放大得分；失误则会中断连击，并消耗一条生命条。游戏的幻想核心是举办一场
演唱会——在流畅的心流状态中打准每一个音符，同时背景舞台灯光会随你的准确度
作出反应。一整套程序化定时的歌曲战役提供了数小时不断升级的挑战。

## 玩家体验流程

1. **标题画面** —— 一片霓虹灯照亮的舞台背景，游戏名采用粗体风格化字体，配有
   一个战役按钮和一个自由演奏按钮。不要出现纯灰。
2. **选曲** —— 一份可滚动的列表，至少 10 首歌曲，标有难度评级（简单/中等/
   困难）、最佳得分和通关评级（S/A/B/C/F）。歌曲会随战役进程依次解锁。
3. **轨道** —— 4 条轨道，颜色编码的音符宝石朝判定条落下。玩家按 D/F/J/K
   （或方向键）来击中音符。判定窗口分为 Perfect、Great、Good、Miss——各有
   截然不同的视觉反馈（爆裂、发光、震动）。
4. **连击系统** —— 连续命中会让连击计数器递增。倍率（x2、x4、x8）会放大得分。
   中断连击会重置计数器，并伴有可见的碎裂特效。
5. **生命条** —— 失误会消耗生命值。生命值归零时歌曲失败，出现显示统计数据的
   游戏结束画面。Perfect 判定会回复少量生命值。
6. **长按音符与滑动音符** —— 有些音符需要按住按键持续其时长（带有一条拖尾）。
   还有些音符会横跨轨道滑动，要求玩家用手指位置跟随。
7. **结算画面** —— 每首歌结束后显示：总得分、最大连击、准确率百分比、评级，
   以及 Perfect/Great/Good/Miss 各判定数量的明细。刷新最高分会触发一段庆祝
   动画。

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

