# Idle Spell Tower

Build an **Idle Spell Tower** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player builds a wizard's tower that generates mana passively, researches
spells, and automates magical casting for ever-increasing power. The fantasy is
arcane accumulation: watching mana flow from crystal to crystal, spells firing
automatically at targets, and the tower growing taller with each prestige cycle.
The idle loop generates mana continuously; the player's decisions shape which
spells to research and how to allocate mana between offence, defence, and
growth. Prestige collapses the tower and rebuilds it higher with better
foundations.

## What the Player Experiences

1. **Title Screen** — A tall wizard tower against a starry sky with magical
   particles flowing upward, the game name in arcane script, and a play button
   glowing with mana.
2. **Tower View** — A vertical tower cross-section showing floors. Each floor
   has a function: mana generators, spell labs, crystal storage, automated
   casters. The tower grows as floors are added.
3. **Mana Generation** — Base mana ticks up automatically. Mana generators on
   each floor contribute to the rate. The player can click a crystal to manually
   generate bursts. A large mana counter dominates the UI.
4. **Spell Research** — A research tree shows available spells. Each spell costs
   mana and time to research. Researched spells can be assigned to auto-casters
   or cast manually for immediate effect.
5. **Automated Casting** — Auto-caster floors fire spells at targets (monsters
   approaching the tower base) without player input. Each caster has a rate and
   spell assignment. Defeating monsters yields mana crystals.
6. **Tower Growth** — Spending mana builds new floors, each with a specific
   function. Higher floors generate more mana but cost exponentially more. The
   tower visually grows taller.
7. **Prestige** — When the tower reaches maximum height, the player can collapse
   it (prestige). The tower resets to one floor but gains a permanent height
   multiplier, faster mana generation, and access to higher-tier spells. Each
   rebuild reaches greater heights faster.

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

# 放置法术塔（Idle Spell Tower）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置法术塔**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家建造一座能被动产生魔力的巫师塔，研究法术，并把施法自动化以获得不断增长的
力量。游戏的幻想核心是奥术积累：看着魔力从一颗水晶流向另一颗、法术自动朝
目标发射，而塔身随着每一轮转生周期越建越高。放置循环持续产生魔力；玩家的
决策则决定研究哪些法术，以及如何在攻击、防御和成长之间分配魔力。转生会让塔
崩塌，并以更好的地基把它重建得更高。

## 玩家体验流程

1. **标题画面** —— 一座高耸的巫师塔矗立在星空下，魔法粒子向上流动，游戏名
   采用奥术手写体，还有一个泛着魔力光芒的开始按钮。
2. **塔视图** —— 一个垂直的塔身剖面图，展示各个楼层。每层都有一项功能：魔力
   生产者、法术实验室、水晶仓库、自动施法器。随着楼层增加，塔会不断长高。
3. **魔力生产** —— 基础魔力会自动跳动增长。每层的魔力生产者都会提升该速率。
   玩家可以点击一颗水晶手动产生一波爆发。一个巨大的魔力计数器占据 UI 的主位。
4. **法术研究** —— 一棵研究树展示可选法术。每个法术都需要花费魔力和时间来
   研究。研究完成的法术可以分配给自动施法器，也可以手动施放以立即生效。
5. **自动施法** —— 自动施法器楼层会在无需玩家输入的情况下，朝目标（逼近塔基的
   怪物）发射法术。每个施法器都有自己的施法速率和法术分配。击败怪物会产出
   魔力水晶。
6. **塔的成长** —— 花费魔力可建造新楼层，每层都有特定功能。更高的楼层能产生
   更多魔力，但成本呈指数上升。塔会在视觉上变得更高。
7. **转生** —— 当塔达到最大高度时，玩家可以让它崩塌（转生）。塔会重置为一层，
   但获得一个永久的高度倍率、更快的魔力生产速度，以及更高层级法术的使用权限。
   每次重建都能更快地达到更高的高度。

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

