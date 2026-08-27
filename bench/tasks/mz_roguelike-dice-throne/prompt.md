# Dice Throne

Build **Dice Throne**, a dice-rolling roguelike with reroll mechanics and
equipment that modifies die faces as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

A warrior battles through a dungeon using dice as their combat system. Each
turn the player rolls a set of dice, then chooses which to keep and which to
reroll (up to two rerolls). Die faces map to abilities: swords deal damage,
shields block, hearts heal, and skulls trigger special attacks. The twist:
equipment found in the dungeon physically modifies die faces — a flame sword
replaces one sword face with a fire-sword that deals double damage, enchanted
armor adds a shield face to a die. The enemy rolls visible dice too, creating
a transparent contest where both sides see what is coming. Building a set of
dice with synergistic faces is the meta-progression within each run.

## What the Player Experiences

A title screen shows dice tumbling with glowing face icons. Starting a run
gives the player 5 standard dice (each with sword, sword, shield, heart,
skull, blank faces).

In combat, the player rolls all dice simultaneously with a satisfying tumble
animation. Results land face-up. The player selects dice to keep (they lock in
place) and rerolls the rest — up to two rerolls per turn. After finalizing,
faces activate: swords deal damage to the enemy, shields reduce incoming damage,
hearts heal, skulls trigger a special ability. The enemy then rolls their own
visible dice and resolves similarly.

Between encounters, loot screens offer equipment that modifies die faces —
replacing, upgrading, or adding faces. A map shows branching paths with combat,
elite, shop, and rest nodes. Shops sell face modifications and new dice. The
run ends at a boss with powerful custom dice. Death shows floor reached, best
roll, and equipment collected.

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

# 骰子王座（Dice Throne）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dice Throne**——一款带重掷机制、并且装备
会改造骰面的骰子 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位战士以骰子作为战斗系统，在地牢中一路厮杀。每个回合玩家掷出一组骰子，然后
选择保留哪些、重掷哪些（最多两次重掷）。骰面对应能力：剑造成伤害，盾进行格挡，
心恢复生命，骷髅触发特殊攻击。妙处在于：地牢中找到的装备会实际改造骰面——一把
烈焰之剑会把一个剑面替换成造成双倍伤害的火剑面，附魔护甲会给一颗骰子加上一个
盾面。敌人同样掷出可见的骰子，形成一场双方都能看到即将发生什么的透明较量。
把骰面凑成一套互有协同的骰组，就是每一轮之内的元进展。

## 玩家体验流程

标题画面展示翻滚的骰子和发光的骰面图标。开始一轮时，玩家获得 5 颗标准骰子
（每颗的骰面为剑、剑、盾、心、骷髅、空白）。

战斗中，玩家一次掷出所有骰子，配有令人满足的翻滚动画。结果朝上落定。玩家选择
要保留的骰子（它们会锁定在原位），并重掷其余的——每回合最多两次重掷。定案之后，
骰面开始生效：剑对敌人造成伤害，盾减少受到的伤害，心恢复生命，骷髅触发一个特殊
能力。随后敌人掷出自己那批可见的骰子，并以同样方式结算。

遭遇战之间，战利品画面提供能改造骰面的装备——替换、升级或增加骰面。一张地图展示
带有战斗、精英、商店和休息节点的分支路径。商店出售骰面改造和新骰子。这一轮在
一位持有强力定制骰子的 Boss 处终结。死亡时展示抵达的层数、最佳一掷和收集到的装备。

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

