# Courtroom Clue Trial

Build **Courtroom Clue Trial**, a compact **courtroom deduction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

The player is a junior advocate trying to expose a false account during a
dramatic trial. Each testimony line is a small puzzle: the witness says something
that sounds plausible, but one piece of evidence in the player's folder proves it
wrong. The tension comes from choosing when to press, what to present, and how
many mistakes the judge will tolerate before the case collapses. A wrong
accusation costs credibility; too many losses end in mistrial. The fantasy is
reading people, catching lies, and turning a courtroom on a single well-timed
objection.

## What the Player Experiences

The player opens to a case-file title screen that sets the tone: a courtroom
seal, a case number, the weight of a pending trial. Starting the case brings a
brief that lays out the charge, the suspect, and the evidence folder. Then the
witness takes the stand. Their testimony scrolls statement by statement, and the
player can press for more detail or advance to the next line. At any point the
player can open the evidence tray, inspect cards with facts like timestamps,
fingerprints, or locations, and present one against the current statement. A
correct match triggers an objection sequence: the witness falters, the testimony
updates, and the case shifts. A wrong match draws a penalty from the judge.
After the first contradiction breaks, a second layer emerges: a rebuttal, a new
clue, an alibi that does not quite hold. The player must navigate this deeper
puzzle to reach a verdict. Success means a styled victory with case-closed
fanfare. Failure means a mistrial screen with the option to retry. Both outcomes
feel like endings, not error states.

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

# 法庭线索审判（Courtroom Clue Trial）

在 `/workspace/game/` 用 Godot 4 开发 **Courtroom Clue Trial**——一款小体量的
**法庭推理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨
程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名初级律师，试图在一场戏剧性的审判中揭穿一份虚假的说法。每一句证词
都是一个小谜题：证人说的话听起来合情合理，但玩家卷宗里的某一份证据能证明它是
错的。张力来自于选择何时追问、呈上什么，以及在案子彻底崩盘前法官还能容忍多少
次失误。错误的指控会损耗信誉；失误过多则会以流审告终。游戏的幻想内核是察人
观心、揪出谎言，并用一次时机恰到好处的异议扭转整个法庭。

## 玩家体验流程

玩家开局看到的是一个卷宗风格的标题画面，它奠定了整体基调：法庭徽章、一个案件
编号、一场待审案件的沉重感。开始办案后，会出现一份案情摘要，列明指控、嫌疑人
以及证据卷宗。接着证人登上证人席。他们的证词一句一句滚动播出，玩家可以追问更多
细节，或推进到下一句。在任何时刻，玩家都可以打开证据托盘，查看载有时间戳、
指纹或地点等事实的卡片，并挑一份来对抗当前这句陈述。匹配正确会触发一段异议
演出：证人语塞，证词随之更新，案情发生转折。匹配错误则会招来法官的处罚。第一个
矛盾点被击破之后，会浮现出第二层：一次反驳、一条新线索、一个不太站得住脚的
不在场证明。玩家必须穿越这个更深的谜题才能抵达判决。成功意味着一场有设计感的
胜利，伴随结案的礼乐。失败意味着一个流审画面，并提供重试选项。两种结果都应当
感觉像结局，而不是错误状态。

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

