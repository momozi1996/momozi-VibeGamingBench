# Spy Handler

Build **Spy Handler**, a **spy operations management visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a handler running field agents from a command desk, receiving
messages, making real-time decisions, and managing multiple simultaneous
operations. Information is unreliable — agents may be compromised, intel may
be planted, and time pressure forces decisions before full clarity. The player
reads incoming transmissions, chooses responses from limited options, and lives
with consequences that cascade across operations. The tension is information
management under pressure: too many threads, not enough time, and the constant
question of who to trust. The tone is cold-war espionage: encrypted messages,
dossier files, red pins on maps, and the weight of lives hanging on a single
reply.

## What the Player Experiences

From the title screen the player enters the operations room — a desk with a
message terminal, a map with agent positions, and dossier files. Time advances
in real-time (acceleratable) and messages arrive from field agents.

Each message presents a situation: an agent reports a target sighting, requests
extraction, warns of a tail, or asks for instructions. The player reads the
message and selects a response from two to four options. Responses have
consequences: sending backup costs resources, ordering an agent to proceed
risks their safety, and waiting may cause the window to close.

Multiple operations run simultaneously. While handling one agent's crisis,
another's message arrives. The player must triage — some situations are urgent,
others can wait. A priority system helps but does not eliminate the pressure.

Information reliability is the core challenge. Some messages contain
disinformation from compromised agents. The player must cross-reference
reports, check agent trust ratings, and sometimes sacrifice an operation to
protect the network. Trust ratings update based on whether agent intel proves
accurate.

Operations conclude with success or failure. A styled result screen shows
mission outcomes, agent status (safe, captured, turned), and overall
intelligence gathered.

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

# 间谍主控（Spy Handler）

在 `/workspace/game/` 用 Godot 4 开发 **Spy Handler**——一款
**间谍行动管理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名主控官，在指挥席上调度外勤特工、接收讯息、做出实时决策，并同时
管理多项行动。信息是不可靠的——特工可能已被渗透，情报可能是被人塞进来的，而
时间压力逼着你在还没完全弄清之前就做决定。玩家阅读传入的电讯、从有限的选项中
挑选回应，并承受那些在各项行动之间连锁扩散的后果。张力在于高压下的信息管理：
线头太多、时间不够，还有那个挥之不去的问题——该信谁。整体调性是冷战间谍：加密
电文、档案卷宗、地图上的红色图钉，以及数条人命悬于一条回复之上的重量。

## 玩家体验流程

从标题画面开始，玩家进入行动室——一张办公桌，上面有一台讯息终端、一幅标示特工
位置的地图，以及若干档案卷宗。时间以实时方式推进（可加速），外勤特工的讯息陆续
传来。

每条讯息都呈现一个处境：某位特工报告发现目标、请求撤离、警告有人跟踪，或询问
指令。玩家阅读讯息，并从两到四个选项中选出一个回应。回应各有后果：派出支援要
消耗资源，命令特工继续行动会危及他的安全，而等待可能导致窗口关闭。

多项行动同时进行。在处理一名特工的危机时，另一名特工的讯息又到了。玩家必须做
分诊——有些状况十万火急，有些可以等。优先级系统能帮上忙，但并不能消除压力。

信息的可靠性是核心挑战。有些讯息含有来自已被渗透特工的虚假情报。玩家必须交叉
比对各方报告、查看特工的信任评级，有时还得牺牲一项行动来保护整个网络。信任评级
会根据特工情报是否被证实准确而更新。

行动以成功或失败告终。一个有设计感的结算画面会展示任务结果、特工状态（安全、
被捕、被收买）以及总体收集到的情报。

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

