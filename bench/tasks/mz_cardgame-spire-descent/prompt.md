# Cardgame Spire Descent

Build a Cardgame Spire Descent as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A deckbuilder roguelike where the player ascends a spire floor by floor,
fighting enemies with a deck of cards that grows and evolves through drafting
choices. Each combat is a tactical puzzle: play attack cards to deal damage,
skill cards to gain block, and power cards for lasting buffs — all constrained
by a per-turn energy budget. Between fights, the player drafts new cards from
a reward selection, visits shops, and collects relics that bend the rules.
Three distinct character classes with different starting decks and card pools
ensure replayability. The fantasy is crafting a broken combo engine that
trivializes the final boss — if you survive long enough to assemble it.

## What the Player Experiences

1. **Title Screen** — A dark tower silhouette against a stormy sky with the
   game name in ornate fantasy lettering, and New Run / Continue buttons. No
   plain HTML 引擎 grey.
2. **Class Select** — Three character classes (Warrior, Rogue, Mage) each with
   a unique portrait, starting deck description, and signature mechanic
   (Warrior: strength scaling; Rogue: shiv generation; Mage: orb channelling).
3. **Map Navigation** — A branching path map showing the current act. Nodes
   represent combat encounters, elite fights, shops, rest sites, and events.
   The player chooses their path through the act, balancing risk and reward.
4. **Card Combat** — Turn-based battles. The player draws 5 cards per turn,
   has 3 energy to spend, and plays cards to attack or defend. Enemies show
   their intent (attack amount, buff, debuff) so the player can plan. Health
   persists between fights.
5. **Card Rewards** — After combat, choose 1 of 3 cards to add to the deck.
   Cards have rarities (Common, Uncommon, Rare) with distinct border colours.
   The player can skip the reward to keep the deck lean.
6. **Relics** — Passive items that modify rules (e.g., "gain 1 energy per
   turn", "draw 2 extra cards on turn 1"). Relics display in a bar at the top
   of the screen with tooltip descriptions. Elite enemies always drop a relic.
7. **Three Acts** — The run spans 3 acts, each with a boss at the end. Bosses
   have unique mechanics and multi-phase patterns. Defeating the final boss
   wins the run with a victory screen showing stats.

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

# 尖塔沉降（Cardgame Spire Descent）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个尖塔沉降卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款构筑牌组类 Roguelike：玩家一层一层地攀登尖塔，用一副通过抽选决策不断成长和
演化的牌组与敌人作战。每场战斗都是一道战术谜题：打出攻击牌造成伤害，技能牌获得
格挡，能力牌带来持续增益——全部受制于每回合的能量预算。战斗之间，玩家从奖励选择
中抽选新卡、光顾商店，并收集能扭曲规则的遗物。三个各具特色的角色职业，拥有不同
的初始牌组和卡池，确保了重玩价值。这份幻想在于：打造出一套能把最终 Boss 玩成
儿戏的破坏级连击引擎——前提是你能活得够久，把它拼齐。

## 玩家体验流程

1. **标题画面** —— 风暴天空映衬下一座黑暗塔楼的剪影，游戏名以华丽的奇幻字体呈现，
   并有新的一轮 / 继续按钮。演出 GameX其灰色。
2. **职业选择** —— 三个角色职业（战士、盗贼、法师），各有独特的立绘、初始牌组
   描述和标志性机制（战士：力量叠加；盗贼：飞刀生成；法师：法球引导）。
3. **地图导航** —— 一张展示当前章节的分支路径地图。节点代表战斗遭遇、精英战、
   商店、休息点和事件。玩家在权衡风险与收益中选择自己穿越该章节的路线。
4. **卡牌战斗** —— 回合制战斗。玩家每回合抽 5 张牌，拥有 3 点能量可供消耗，通过
   打出卡牌来攻击或防御。敌人会显示其意图（攻击数值、增益、减益），便于玩家规划。
   生命值在战斗之间延续。
5. **卡牌奖励** —— 战斗结束后，从 3 张牌中选 1 张加入牌组。卡牌分稀有度（普通、
   罕见、稀有），边框颜色各不相同。玩家也可以跳过奖励，让牌组保持精简。
6. **遗物** —— 修改规则的被动物品（例如："每回合获得 1 点能量"、"第 1 回合额外
   抽 2 张牌"）。遗物显示在屏幕顶部的一条栏中，带有提示说明。精英敌人必定掉落
   一件遗物。
7. **三个章节** —— 一轮游戏横跨 3 个章节，每个章节末尾都有一个 Boss。Boss 拥有
   独特机制和多阶段模式。击败最终 Boss 即赢下这一轮，并弹出展示统计数据的胜利
   画面。

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

