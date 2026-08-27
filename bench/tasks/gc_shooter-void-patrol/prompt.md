# Void Patrol

Build **Void Patrol**, a side-scrolling shoot-em-up as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is piloting a lone interceptor through hostile deep-space corridors,
weaving between curtains of enemy fire while chaining power-ups into an
ever-escalating weapons loadout. The interesting tension is greed versus safety:
each collected power-up extends the current weapon chain, but the orbs drift into
dangerous positions, tempting the player to fly into bullet patterns for the next
tier. Death resets the chain, and with limited lives the player must decide when
to play it safe and when to push for the devastating max-chain beam. Stages
scroll relentlessly, each ending with a multi-phase boss whose patterns demand
mastery of the ship's narrow hitbox and screen-clearing bomb reserve.

## What the Player Experiences

The player launches into a title screen showing the ship silhouetted against a
scrolling starfield, then selects Start to enter Stage 1. The viewport scrolls
right automatically; enemy formations sweep in from the edges in choreographed
waves, dropping bullets and occasionally releasing glowing power-up orbs. The
player moves freely within the screen bounds, fires a primary weapon with a held
button, and can trigger a limited bomb to clear all on-screen projectiles.

Collecting sequential power-ups without dying upgrades the weapon through visible
tiers — single shot, spread, laser, homing missiles — each with distinct
visual flair. Dying drops the chain back to base. Between stages a brief
interstitial shows score and lives remaining. Boss encounters fill the right side
of the screen with a large multi-part enemy whose segments flash and break away
as health depletes, cycling through distinct attack phases. After five stages the
game shows a victory tally; losing all lives triggers a continue screen with
limited continues before game over.

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

# 虚空巡航（Void Patrol）

在 `/workspace/game/` 用 Godot 4 开发 **Void Patrol**，一款横版卷轴清版射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一架孤身拦截机穿越敌意的深空走廊，在敌方火力的帷幕之间穿梭，
同时把强化道具串成不断升级的武器配装。有趣的张力在于贪婪与安全的抉择：每收集
一个强化道具都会延长当前的武器连锁，但那些光球会漂向危险位置，诱使玩家为了
下一个层级飞进弹幕形态之中。死亡会重置连锁，而生命有限，玩家必须决定何时求稳、
何时为那道毁灭性的满连锁光束而冒险推进。关卡无情地卷动，每一关都以一场多阶段
Boss 战收尾，其弹幕形态要求玩家精通飞船那狭小的判定框与可清屏的炸弹储备。

## 玩家体验流程

玩家进入一个标题画面，飞船的剪影映在卷动的星空之上，随后选择"开始"进入第 1 关。
视口自动向右卷动；敌人编队从边缘以精心编排的波次扫入，抛下弹幕，并不时释放
发光的强化道具光球。玩家可在屏幕边界内自由移动，按住一个按键发射主武器，并能
触发数量有限的炸弹来清除屏幕上的所有弹幕。

在不死亡的情况下连续收集强化道具会让武器沿可见的层级升级——单发、散射、
激光、追踪导弹——每一层都有独特的视觉表现。死亡会把连锁打回基础层级。关卡
之间会有一段简短的过场展示分数与剩余生命。Boss 遭遇战会用一个大型多部件敌人
填满屏幕右侧，随着血量下降，其各段会闪烁并断裂脱落，并在几个不同的攻击阶段
之间循环。五关之后游戏会显示胜利结算；失去所有生命会触发续关画面，续关次数
有限，用尽即为游戏结束。

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

