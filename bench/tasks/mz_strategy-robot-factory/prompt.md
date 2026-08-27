# Robot Factory

Build **Robot Factory**, a **robot programming arena strategy game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player programs robot behaviors using simple if/then rules, deploys them
into a grid arena, and watches them execute simultaneously against an
opponent's robots. The strategy is entirely in the programming phase: once
robots are deployed, they act on their own according to their instruction sets.
A robot might be told "if enemy adjacent, attack; if health low, retreat; else
advance." The tension is that both sides reveal their programs at the same
time, creating emergent interactions that reward prediction and counter-play.
The tone is retro-futuristic: chunky robots on a factory floor, sparks flying,
gears grinding.

## What the Player Experiences

From the title screen the player enters the workshop. Here they build robots
by assigning behavior rules from a visual list. Each robot has three to five
instruction slots, and each slot is an if/then pair: a condition (enemy in
range, health below threshold, ally nearby) and an action (move forward,
attack, turn, heal, wait). Rules execute top to bottom each turn.

After programming, the player positions robots on their half of a grid arena.
Different robot chassis have different stats — heavy bots have more HP but
fewer instruction slots, light bots move faster but break easily, support bots
can heal adjacent allies.

When both sides are ready, the battle plays out turn by turn with simultaneous
execution. Each turn, every robot evaluates its rules and acts. The player
watches their programming logic play out — sometimes brilliantly, sometimes
hilariously wrong. The round ends when one side's robots are all destroyed.

A campaign of escalating challenges teaches mechanics one at a time, and a
skirmish mode lets the player test builds against AI opponents. The result
screen shows battle replay highlights and robot performance stats.

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

# 机器人工厂（Robot Factory）

在 `/workspace/game/` 用 Godot 4 开发 **Robot Factory**，一款**机器人编程竞技场策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家用简单的 if/then 规则为机器人编写行为，把它们部署到格状竞技场中，然后看它们与对手的机器人同时执行各自的程序。策略完全在编程阶段：一旦机器人部署完毕，它们就按各自的指令集自行行动。一个机器人可能被设定为"若敌人相邻则攻击；若血量偏低则撤退；否则前进"。张力在于双方同时揭示自己的程序，从而产生涌现式的互动，奖励预判与反制。基调是复古未来主义：厂房地面上笨重的机器人、飞溅的火花、咬合摩擦的齿轮。

## 玩家体验流程

玩家从标题画面进入工坊。在这里，他们通过从一份可视化列表中指派行为规则来组装机器人。每个机器人有三到五个指令槽位，每个槽位是一组 if/then 对：一个条件（敌人在射程内、血量低于阈值、友军在附近）和一个动作（前进、攻击、转向、治疗、等待）。规则每回合自上而下执行。

编程完成后，玩家把机器人布置在格状竞技场自己那一半区域内。不同的机器人底盘有不同的属性——重型机体 HP 更高但指令槽位更少，轻型机体移动更快但脆弱易毁，支援机体则能治疗相邻友军。

双方都准备就绪后，战斗以同时执行的方式逐回合展开。每回合，每个机器人都评估自己的规则并行动。玩家看着自己的编程逻辑上演——有时精彩绝伦，有时错得可笑。当一方的机器人全部被摧毁时，本轮结束。

一场难度递增的战役会逐一教授各项机制，而遭遇战模式让玩家可以拿自己的配置去对抗 AI 对手。结算画面会展示战斗回放亮点与机器人性能数据。

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

