# Border Check

Build **Border Check**, a 2D document-inspection simulation as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is working as a border checkpoint inspector in a fictional
authoritarian state, examining travelers' documents against an ever-changing
rulebook while trying to earn enough to keep your family alive. The interesting
tension is moral versus mechanical: the rules say deny this person, but their
story is sympathetic — and every wrong decision costs money your family needs for
heat and medicine. Speed matters because each day has a time limit and pay is
per-person processed, but rushing causes mistakes that trigger citations and
fines. The rules grow more complex each day — new document types, new
contraband checks, new exceptions — until the player is juggling five documents
simultaneously while a queue of desperate faces waits.

## What the Player Experiences

The player opens to a bleak title screen showing the checkpoint booth, then
begins Day 1. The workspace shows a desk surface with an inspection area, a
rulebook panel, and stamps for APPROVE and DENY. Travelers approach one at a
time, presenting documents that slide onto the desk. The player drags documents
around, opens the rulebook to check current rules, compares photo to face,
checks expiration dates, and cross-references permit numbers.

Each day introduces new rules: Day 1 might only require matching names, while
Day 5 requires valid work permits, vaccination records, and weight discrepancy
checks. End-of-day shows earnings, family expenses, and any citations received.
Story events interrupt between days — a guard offers bribes, a rebel asks for
help, family members fall ill. Choices affect the narrative path. The game spans
10+ days with escalating complexity and multiple ending conditions based on
accumulated choices and financial survival.

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

# 边境查验（Border Check）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Border Check**，一款 2D 证件查验模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一个虚构的威权国家里当一名边境检查站查验员，对照一本不断变化的
规则手册审查旅客的证件，同时努力挣到足够的钱让家人活下去。有趣的张力在于道德
与机械规程的冲突：规则说要拒绝这个人，但对方的故事却令人同情——而每一个错误
决定都会花掉家里买取暖与药品所需的钱。速度很重要，因为每一天都有时间限制、
薪酬按处理人数计算，但赶进度又会造成失误，从而引来传票与罚款。规则每天都变得
更复杂——新的证件类型、新的违禁品检查、新的例外条款——直到玩家要同时处理
五份文件，而一列绝望的面孔正在排队等待。

## 玩家体验流程

玩家进入游戏时看到一个灰暗的标题画面，展示检查站岗亭，随后开始第 1 天。工作
区展示一张桌面，上有查验区、规则手册面板，以及"批准"和"拒绝"两枚印章。旅客
一次一个地走近，把证件递到桌上。玩家拖动这些文件，翻开规则手册核对当前规则，
对比照片与面孔，检查有效期，并交叉核对许可证编号。

每一天都会引入新规则：第 1 天可能只要求姓名匹配，而第 5 天则要求有效的工作
许可、疫苗接种记录以及体重差异核查。一天结束时会显示收入、家庭开支，以及收到
的任何传票。剧情事件会在日与日之间插入——一名守卫提出行贿、一名反抗者请求
帮助、家人病倒。选择会影响叙事走向。游戏横跨 10 天以上，复杂度逐步升级，并
依据累积的选择与财务上的存活情况提供多种结局条件。

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

