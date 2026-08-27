# Rhythm Garden

Build a Rhythm Garden as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A whimsical garden overworld connects a collection of eight or more timing
minigames, each themed around a different garden activity — watering flowers to
a beat, swatting bugs in rhythm, conducting a bird choir, bouncing seeds into
pots with timed taps. Each minigame teaches a different rhythmic skill (steady
pulse, syncopation, polyrhythm, call-and-response). Mastering individual games
unlocks a final "Remix" stage that weaves all mechanics together into one
climactic performance. The fantasy is a musical gardener tending a world that
blooms in response to rhythmic mastery.

## What the Player Experiences

1. **Title Screen** — A pastel garden scene with the game name in a playful
   hand-drawn font, flowers swaying to a gentle beat, and a "Play" button
   shaped like a watering can. No plain HTML grey.
2. **Garden Hub** — An overworld map showing garden plots, each representing a
   minigame. Completed games bloom with flowers; locked ones show wilted buds.
   The player clicks a plot to enter its minigame.
3. **Minigame Variety** — At least 8 distinct minigames, each with unique
   visuals and a different timing mechanic:
   - Tap to the beat (steady quarter notes)
   - Hold and release (sustained timing)
   - Call and response (echo a pattern)
   - Syncopation (off-beat hits)
   - Polyrhythm (two simultaneous patterns)
   - Speed ramp (accelerating tempo)
   - Pattern memory (repeat increasingly long sequences)
   - Free-form (improvise within a groove)
4. **Scoring** — Each minigame scores accuracy as a star rating (1-3 stars).
   Visual feedback during play shows timing quality with particle bursts for
   perfect hits and wilting effects for misses.
5. **Progression** — Earning stars unlocks later minigames. The garden visibly
   grows and blooms as the player progresses. New flowers, butterflies, and
   decorations appear with each milestone.
6. **Final Remix** — After completing all 8 minigames, a final challenge
   combines mechanics from multiple games into one extended performance. The
   remix transitions between styles every few measures.
7. **Results and Gallery** — A gallery screen shows total stars, best scores per
   minigame, and the fully-bloomed garden as a reward illustration.

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

# 节奏花园（Rhythm Garden）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个节奏花园游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一片充满奇趣的花园大地图串联起八个或更多的时机小游戏，每个都以一种不同的
园艺活动为主题——踩着节拍给花浇水、按节奏拍打虫子、指挥一支鸟儿合唱团、
用定时敲击把种子弹进花盆。每个小游戏教会玩家一种不同的节奏技巧（稳定脉动、
切分、复合节奏、一问一答）。逐一精通这些小游戏可解锁一个把所有机制编织在
一起的最终"混音"关卡，成为一场高潮式的演出。游戏的幻想核心是一位音乐园丁，
照料着一个会随着节奏造诣而绽放的世界。

## 玩家体验流程

1. **标题画面** —— 一幅粉彩色调的花园场景，游戏名采用活泼的手绘字体，花朵
   随着轻缓的节拍摇曳，还有一个做成洒水壶形状的"开始"按钮。不要出现 HTML 引擎
   默认的纯灰。
2. **花园枢纽** —— 一张大地图，展示一块块园圃，每块代表一个小游戏。已完成的
   游戏会开出花来；未解锁的则显示枯萎的花蕾。玩家点击某块园圃即可进入对应的
   小游戏。
3. **小游戏多样性** —— 至少 8 个截然不同的小游戏，各有独特的视觉表现和不同的
   时机机制：
   - 踩着节拍敲击（稳定的四分音符）
   - 长按与松开（持续时机）
   - 一问一答（复述一段模式）
   - 切分（脱拍击打）
   - 复合节奏（两段同时进行的模式）
   - 速度攀升（速度不断加快）
   - 模式记忆（重复越来越长的序列）
   - 自由发挥（在一段律动中即兴演奏）
4. **计分** —— 每个小游戏以星级（1-3 星）为准确度打分。游戏过程中的视觉反馈
   会体现时机质量：完美命中爆出粒子，失误则出现枯萎效果。
5. **进度推进** —— 赚取星星可解锁后续的小游戏。随着玩家推进，花园会明显地
   生长并绽放。每达成一个里程碑，就会出现新的花朵、蝴蝶和装饰。
6. **最终混音** —— 完成全部 8 个小游戏后，一个最终挑战会把多个游戏的机制
   组合成一场加长演出。这段混音每隔几个小节就在不同风格之间切换。
7. **结算与画廊** —— 一个画廊画面显示星星总数、各小游戏的最佳得分，以及作为
   奖励插画的完全绽放的花园。

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

