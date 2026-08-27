# Idle Dungeon Guild

Build an **Idle Dungeon Guild** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player runs an adventurer's guild, sending heroes on automated dungeon quests
that yield loot and experience. The fantasy is the guild master: recruiting heroes,
equipping them with found gear, and watching them grow from novices to legends.
The idle loop sends parties into dungeons continuously; the player's decisions
shape party composition, equipment allocation, and guild upgrades. Prestige
retires the current generation of heroes and starts a new one with inherited
guild reputation bonuses.

## What the Player Experiences

1. **Title Screen** — A guild hall interior with a quest board and hero
   silhouettes, the game name in fantasy serif font, and a play button styled
   as a wax-sealed letter.
2. **Guild Hall** — The main view shows the guild hall with hero roster, quest
   board, equipment rack, and a reputation meter. Heroes mill about when not on
   quests.
3. **Hero Recruitment** — The player recruits heroes from a pool. Each hero has a
   class (warrior, mage, rogue, healer), stats, and a level. Heroes have distinct
   sprites per class.
4. **Quest Dispatch** — The quest board shows available dungeons with difficulty,
   duration, and reward preview. The player assigns a party (1-4 heroes) and
   sends them. A progress bar shows quest completion over time.
5. **Auto-Combat Results** — When a quest completes, a results screen shows loot
   found, experience gained, and any injuries. Heroes level up automatically.
   Better dungeons yield rarer loot.
6. **Equipment & Loot** — Found gear (weapons, armour, accessories) is assigned
   to heroes from the equipment rack. Better gear improves stats and enables
   harder dungeons. A comparison tooltip shows stat changes.
7. **Prestige (New Generation)** — When guild reputation maxes out, the player
   can prestige: retire all heroes, keep equipment and guild upgrades, and start
   with a new generation that levels faster. Each generation reaches higher
   dungeon tiers.

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

# 放置地牢公会（Idle Dungeon Guild）

在 `/workspace/game/` 用 Godot 4 开发一个**放置地牢公会**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一家冒险者公会，派遣英雄去执行自动化的地牢任务，从中获取战利品和
经验。游戏的幻想核心是当一名公会会长：招募英雄、用捡来的装备武装他们，
看着他们从新手成长为传奇。放置循环会持续把队伍送进地牢；玩家的决策则塑造
队伍配置、装备分配和公会升级。转生会让当前这一代英雄退役，并以继承下来的
公会声望加成开启新的一代。

## 玩家体验流程

1. **标题画面** —— 一个公会大厅内景，配有任务板和英雄剪影，游戏名采用奇幻
   衬线字体，开始按钮做成蜡封信件的样式。
2. **公会大厅** —— 主视图展示公会大厅，包含英雄名册、任务板、装备架和一个
   声望量表。英雄不在执行任务时会在大厅里闲逛。
3. **英雄招募** —— 玩家从一个候选池中招募英雄。每位英雄都有职业（战士、法师、
   盗贼、治疗者）、属性和等级。不同职业的英雄有各自独特的精灵图。
4. **任务派遣** —— 任务板列出可选地牢及其难度、时长和奖励预览。玩家指定一支
   队伍（1-4 名英雄）并派出。一条进度条会显示任务随时间推进的完成度。
5. **自动战斗结果** —— 任务完成时，结算画面会显示获得的战利品、取得的经验，
   以及任何伤情。英雄会自动升级。更好的地牢会产出更稀有的战利品。
6. **装备与战利品** —— 找到的装备（武器、护甲、饰品）可以从装备架分配给英雄。
   更好的装备能提升属性并让英雄挑战更难的地牢。一个对比提示框会显示属性变化。
7. **转生（新一代）** —— 当公会声望达到上限时，玩家可以转生：让所有英雄退役，
   保留装备和公会升级，并以升级更快的新一代重新开始。每一代都能触及更高的
   地牢层级。

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

