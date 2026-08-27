# Meat Gauntlet

Build **Meat Gauntlet**, a die-and-retry speed platformer with saw blades and
replay ghosts as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A tiny square of meat hurls itself through rooms bristling with spinning saw
blades, retracting spikes, and crumbling ledges. Death is instant and restart
is instantaneous — the loop is attempt, die, learn, attempt again until the
room clicks. After clearing a room, a ghost of the successful run replays
alongside the next attempt, turning past mastery into a visible companion. Fifty
compact levels across five worlds escalate from simple jumps to frame-tight
gauntlets that demand wall-slides, mid-air direction changes, and split-second
timing. The game celebrates speed: each level tracks completion time and a
global death counter reminds the player how far they have come.

## What the Player Experiences

A punchy title screen shows the game name, a level-select grid (unlocked
progressively), and a death counter. Selecting a level drops the player in
instantly.

Each level is a single screen. The meat character runs and jumps with tight,
responsive controls. Saw blades spin in fixed or patrolled paths. Spikes
retract and extend on timers. Crumbling platforms vanish after contact. Touching
any hazard kills instantly — the screen flashes, and the player respawns at the
start within a fraction of a second.

On clearing a level, the completion time displays and a ghost recording is
saved. Re-entering the level shows the ghost replaying the best run as a
translucent afterimage. Clearing all levels in a world unlocks the next world
with new hazard types. A results screen per world shows times and death counts.

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

# 肉块试炼场（Meat Gauntlet）

在 `/workspace/game/` 用 Godot 4 开发 **Meat Gauntlet**，一款带锯片和重放幽灵的"死了再来"竞速平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一小块方形的肉把自己抛进遍布旋转锯片、伸缩尖刺和崩塌岩架的房间。死亡是瞬间的，重开也是瞬间的——循环就是尝试、死亡、学习、再尝试，直到这个房间被彻底吃透。清掉一个房间之后，那次成功的幽灵会与下一次尝试并行重放，把过去的熟练变成一个可见的同行者。横跨五个世界的五十个紧凑关卡，从简单的跳跃一路升级到帧级精确的试炼场，要求贴墙下滑、空中变向和瞬间掐时。游戏为速度喝彩：每个关卡都记录完成时间，一个全局死亡计数器提醒玩家他们已经走了多远。

## 玩家体验流程

一个有冲击力的标题画面显示游戏名、一个（逐步解锁的）选关网格，以及一个死亡计数器。选中一个关卡就立刻把玩家投进去。

每个关卡都是单屏。肉块角色以紧凑灵敏的操控奔跑和跳跃。锯片沿固定或巡逻路径旋转。尖刺按计时器缩回和伸出。崩塌平台在接触后消失。碰到任何危险物都会立刻致死——屏幕闪一下，玩家在不到一秒的时间里于起点重生。

清掉一个关卡后会显示完成时间，并保存一份幽灵录像。再次进入该关卡时，会看到幽灵以半透明残影的形式重放最佳的那一轮。清掉一个世界中的全部关卡会解锁下一个世界，并带来新的危险物类型。每个世界都有一个结算画面，显示各关时间和死亡次数。

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

