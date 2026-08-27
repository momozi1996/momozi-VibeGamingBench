# Rhythm DJ Arena

Build a Rhythm DJ Arena as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Two musical fighters face off on a neon stage, trading rhythmic attacks in a
battle of beats. Each fighter has a note highway; hitting notes charges special
moves that launch across the arena as musical projectiles. The opponent must
dodge or counter with their own charged abilities. The fantasy is a DJ battle
where musical skill translates directly into combat power — perfect combos
unleash devastating bass drops while missed notes leave you vulnerable. Multiple
characters with distinct musical styles and move sets provide variety.

## What the Player Experiences

1. **Title Screen** — A vibrant neon club aesthetic with the game name in
   glowing graffiti-style text, character select and versus mode buttons, and
   animated equalizer bars in the background. No plain Godot grey.
2. **Character Select** — At least 4 playable characters, each with a distinct
   musical theme (electronic, rock, jazz, hip-hop), unique sprite design, and
   different special move sets. Each character's selection shows a preview
   animation and their move list.
3. **Split Highway** — The screen splits: each side has a 3-lane note highway.
   The player hits notes on their side to build a charge meter. The AI opponent
   plays their own highway simultaneously.
4. **Charge and Attack** — When the charge meter fills a threshold, the player
   can spend it to launch a musical attack (bass wave, treble spike, chord
   blast). Attacks travel across the arena toward the opponent. Stronger charges
   (from higher combos) produce more powerful attacks.
5. **Defence and Dodge** — The opponent can dodge attacks by timing a key press
   as the projectile arrives, or absorb hits (losing health). A health bar
   depletes with each successful hit. First to zero loses the round.
6. **Best of Three** — Matches are best-of-3 rounds. Between rounds, a brief
   interlude shows score and lets the tempo increase for the next round.
7. **Arcade Mode** — A ladder of increasingly difficult AI opponents, each with
   faster note patterns and more aggressive attack usage. Defeating all
   opponents shows a character-specific victory screen.

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

# 节奏 DJ 竞技场（Rhythm DJ Arena）

在 `/workspace/game/` 用 Godot 4 开发一个节奏 DJ 竞技场游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两名音乐斗士在霓虹舞台上对峙，用节奏性的攻击展开一场节拍之战。每名斗士都有
一条音符轨道；击中音符可以为特殊技能充能，充满后会化作音乐弹幕横穿竞技场
发射出去。对手必须闪避，或用自己已充能的技能反制。游戏的幻想核心是一场 DJ
对战——音乐技巧直接转化为战斗力：完美连击会释放毁灭性的低音炸弹，而漏掉的
音符则让你门户大开。多名拥有截然不同音乐风格和招式组合的角色带来丰富变化。

## 玩家体验流程

1. **标题画面** —— 鲜艳的霓虹夜店美学，游戏名采用发光的涂鸦风字体，配有
   角色选择和对战模式按钮，背景是动态的均衡器条。不要出现 Godot 默认的纯灰。
2. **角色选择** —— 至少 4 名可玩角色，各有独特的音乐主题（电子、摇滚、爵士、
   嘻哈）、独特的精灵图设计和不同的特殊招式组合。选中每个角色时会显示一段
   预览动画及其招式列表。
3. **分屏轨道** —— 屏幕一分为二：每一侧都有一条 3 轨的音符轨道。玩家在自己
   那侧击中音符以积攒充能量表。AI 对手同时在自己的轨道上演奏。
4. **充能与攻击** —— 当充能量表达到某个阈值时，玩家可以消耗它发动一次音乐
   攻击（低音波、高音尖刺、和弦冲击）。攻击会横穿竞技场朝对手飞去。充能越强
   （来自更高的连击）产生的攻击就越强力。
5. **防御与闪避** —— 对手可以在弹幕抵达的瞬间按键闪避，或者硬吃伤害（损失
   生命值）。每次成功命中都会削减血条。先归零的一方输掉本回合。
6. **三局两胜** —— 比赛采用 3 局 2 胜制。回合之间有一段简短的间奏，显示得分
   并让下一回合的速度提升。
7. **街机模式** —— 一条难度递增的 AI 对手阶梯，每个对手的音符模式更快、攻击
   使用更具侵略性。击败所有对手会显示该角色专属的胜利画面。

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

