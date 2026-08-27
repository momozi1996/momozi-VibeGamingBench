# Rhythm Conductor

Build a Rhythm Conductor as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a battlefield conductor issuing rhythmic commands to a squad of
warriors. Each command — march, attack, defend, charge — must be tapped in a
specific rhythm pattern. Nail the timing and your troops execute with power and
precision; fumble it and they stumble into disarray. Enemies advance in waves,
and the player must read the battlefield and choose the right command at the
right tempo. Between battles, the squad levels up and unlocks new command
patterns with more complex rhythms.

## What the Player Experiences

1. **Title Screen** — A war-drum themed menu with the game name in bold
   military-style lettering, a campaign button, and marching silhouettes in
   the background. No plain Godot grey.
2. **Command Input** — The bottom of the screen shows a rhythm bar. The player
   taps 4-beat patterns (e.g., tap-tap-hold-tap for "Attack") in time with a
   metronome pulse. Visual feedback shows timing accuracy per beat.
3. **Squad Response** — When a command is executed successfully, the squad
   performs the action with a power level proportional to timing accuracy.
   Perfect timing triggers a "Fever" version with bonus effects (extra damage,
   wider shield, faster march).
4. **Enemy Waves** — Enemies march from the right in formation. Different enemy
   types require different counter-strategies: shielded foes need the "Charge"
   command to break through; archers need "Defend" to block volleys; swarms
   need "Attack" for area damage.
5. **Battlefield View** — A side-scrolling battlefield shows the player's squad
   on the left and enemies on the right. Units animate their actions in sync
   with the rhythm. Health bars float above each unit group.
6. **Upgrades** — Between missions, the player spends earned resources to
   upgrade unit types (stronger attacks, faster movement) or unlock new command
   patterns (a 6-beat "Rally" that heals, a syncopated "Ambush" for critical
   hits).
7. **Boss Encounters** — Boss enemies have their own rhythm patterns that
   interfere with the player's commands. The player must maintain their own
   tempo while adapting to the boss's disruption beats.

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

# 节奏指挥官（Rhythm Conductor）

在 `/workspace/game/` 用 Godot 4 开发一个节奏指挥官游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是战场上的指挥官，向一支战士小队下达节奏性的指令。每一条指令——行军、
进攻、防守、冲锋——都必须按特定的节奏模式敲击出来。时机拿捏精准，部队就会
强力而精确地执行；一旦失手，他们就会踉跄陷入混乱。敌人以波次推进，玩家必须
读懂战场，并在正确的速度下选出正确的指令。战斗之间，小队会升级并解锁节奏
更复杂的新指令模式。

## 玩家体验流程

1. **标题画面** —— 一个以战鼓为主题的菜单，游戏名采用粗体军事风字体，配有
   一个战役按钮，背景是行军的剪影。不要出现 Godot 默认的纯灰。
2. **指令输入** —— 屏幕底部显示一条节奏条。玩家踩着节拍器的脉动敲出 4 拍的
   模式（例如"进攻"是 敲-敲-长按-敲）。视觉反馈会逐拍显示时机准确度。
3. **小队响应** —— 指令成功执行时，小队会以与时机准确度成正比的强度做出该
   动作。完美时机会触发"狂热"版本，附带额外效果（额外伤害、更宽的护盾、
   更快的行军速度）。
4. **敌人波次** —— 敌人从右侧列队行进而来。不同敌人类型需要不同的应对策略：
   持盾敌人需要用"冲锋"指令来突破；弓箭手需要用"防守"来挡住齐射；成群的
   敌人需要用"进攻"造成范围伤害。
5. **战场视图** —— 一个横向卷动的战场，玩家小队在左、敌人在右。各单位的动作
   动画与节奏同步。每组单位上方都浮着血条。
6. **升级** —— 在任务之间，玩家花费赚得的资源来升级单位类型（更强的攻击、
   更快的移动）或解锁新的指令模式（一个 6 拍的治疗用"集结"，一个切分节奏的
   暴击用"伏击"）。
7. **Boss 遭遇战** —— Boss 敌人有自己的节奏模式，会干扰玩家的指令。玩家必须
   一边维持自己的速度，一边适应 Boss 的干扰节拍。

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

