# Dread Wings

Build **Dread Wings**, a **one-button endless flyer** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).: a dark cyberpunk score-chaser where a fragile metallic bird
fights gravity through an infinite corridor of industrial hazards.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player fights physics with a single input. Every tap buys a moment of lift
against relentless downward pull, threading the bird through narrow gaps that
demand precise timing and rhythm. The tension comes from the gap between what
the player sees coming and what their reflexes can execute -- each successful
pass raises the stakes because the score is now worth protecting. Death is
instant, retry is instant, and the "just one more try" loop is the entire
product. The world is a dark industrial wasteland: neon-lit pipes, smog, and
a distant ruined skyline scrolling beneath a crimson sky.

## What the Player Experiences

The player opens to a moody title screen showing their all-time best score and
a clear way to launch. Once they begin, the bird hovers in place, waiting for
the first tap. The moment input arrives, gravity takes hold and the corridor
begins scrolling. Each tap fires an upward impulse that fights the bird's
falling arc, creating a rhythmic bobbing flight path. Paired hazards scroll in
from the right with randomized vertical placement but a consistent gap size,
demanding constant micro-adjustments. Passing a hazard pair ticks the score
upward. Over time the challenge escalates -- faster scrolling, tighter margins,
or new hazard presentations keep the player adapting. Contact with any surface
ends the run immediately: the world freezes, a result panel reveals the final
score and whether a new record was set, and a single button drops the player
back to the ready state without restarting the executable. The high score
persists between sessions.

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

# 惧翼（Dread Wings）

在 `/workspace/game/` 用 Godot 4 开发 **Dread Wings**，一款**单按键无尽飞行游戏**：这是一场暗黑赛博朋克风格的分数追逐，一只脆弱的金属飞鸟在无限延伸的工业危险物走廊中对抗重力。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家用单一输入对抗物理。每一次点击都为对抗无休止的下坠拉力买来一瞬升力，把飞鸟穿过要求精准时机与节奏感的狭窄缝隙。张力来自玩家看到的来势与反射神经能执行的操作之间的落差——每一次成功通过都会抬高赌注，因为分数如今值得保护了。死亡是瞬间的，重试也是瞬间的，而"再来一次就好"的循环就是整个产品。世界是一片暗黑的工业废土：霓虹点亮的管道、烟尘，以及在血色天幕下滚动而过的远方废墟天际线。

## 玩家体验流程

玩家打开游戏，迎面是一个气氛阴郁的标题画面，显示其历史最高分和一个明确的开始入口。开局之后，飞鸟悬停在原地，等待第一次点击。输入到来的那一刻，重力开始生效，走廊开始滚动。每一次点击都触发一股向上的冲量来对抗飞鸟的下坠弧线，形成一条起伏有节奏的飞行轨迹。成对的危险物从右侧滚入，纵向位置随机但缝隙尺寸恒定，要求玩家不断做微调。通过一对危险物会让分数向上跳动。随着时间推移，挑战不断升级——更快的滚动、更紧的余量，或是新的危险物呈现方式，让玩家持续适应。碰到任何表面都会立刻结束这一轮：世界冻结，结算面板揭示最终分数以及是否创造了新纪录，一个按钮就能把玩家送回待命状态，无需重启可执行程序。最高分在多次会话之间持久保存。

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

