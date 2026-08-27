# Word Spell

Build **Word Spell**, a word-forming spell-casting roguelike with letter tiles
and encounters as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A wizard battles through a dungeon by casting spells formed from letter tiles.
Each turn the player has a hand of letter tiles and must form a word — longer
words deal more damage, and specific letter combinations trigger elemental
effects (words containing "fire" deal burn damage, "ice" freezes, "heal"
restores health). Between encounters the player collects new letter tiles,
upgrades existing ones (a golden "E" scores double), and removes weak letters
from their pool. Enemies have visible health and telegraph attacks with a
countdown. The tension is vocabulary under pressure: finding the longest,
most synergistic word from a random hand before the enemy strikes.

## What the Player Experiences

A title screen shows letter tiles arranged into a spell effect. Starting a run
gives the player a starting pool of 20 common letter tiles.

In combat, 7 tiles are drawn from the pool. The player drags tiles onto a
spelling bar to form a word, then casts it. Valid words deal damage proportional
to length (3 letters = weak, 7 letters = devastating). Special letter combos
trigger bonus effects shown as elemental icons. Invalid words fizzle and waste
the turn. After casting, the enemy attacks (damage shown in advance as a
countdown number).

Between encounters, a reward screen offers new tiles (including rare consonants
and vowels with bonus effects), tile upgrades, or tile removal. A map shows
branching paths with combat nodes, rest nodes (heal), and shop nodes (buy/sell
tiles). The run ends at a boss with high health requiring multiple strong words.
Death shows a score based on floor reached and longest word cast.

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

# 咒文拼词（Word Spell）

在 `/workspace/game/` 用 Godot 4 开发 **Word Spell**——一款带字母图块和遭遇战的
拼词施法 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位巫师靠着用字母图块拼出的法术在地牢中一路厮杀。每回合玩家手中有一把字母图块，
必须拼出一个单词——单词越长伤害越高，而特定的字母组合会触发元素效果（含 "fire"
的单词造成燃烧伤害，"ice" 冰冻，"heal" 恢复生命）。遭遇战之间，玩家收集新的字母
图块、升级已有的（一个金色 "E" 计分翻倍），并从自己的池子里移除弱字母。敌人拥有
可见的生命值，并以倒计时预告攻击。张力在于压力之下的词汇量：在敌人出手之前，从
一手随机字母中找出最长、协同最强的单词。

## 玩家体验流程

标题画面展示排列成法术效果的字母图块。开始一轮时，玩家获得一个由 20 个常见字母
图块组成的初始池。

战斗中，从池里抽出 7 个图块。玩家把图块拖到拼写栏上组成单词，然后施放。有效单词
造成与长度成正比的伤害（3 个字母 = 弱，7 个字母 = 毁灭性）。特殊字母组合会触发以
元素图标显示的额外效果。无效单词会失效并浪费该回合。施放之后敌人发动攻击（伤害
以倒计时数字提前显示）。

遭遇战之间，奖励画面提供新图块（包括带额外效果的稀有辅音和元音）、图块升级或图块
移除。一张地图展示带战斗节点、休息节点（治疗）和商店节点（买卖图块）的分支路径。
这一轮在一位生命值极高、需要多个强力单词才能击败的 Boss 处终结。死亡时展示基于
抵达层数和施放过的最长单词计算的分数。

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

