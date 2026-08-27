# Bullet Cathedral

Build **Bullet Cathedral**, a bullet-hell roguelike as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is descending through a procedurally arranged cathedral of hostile
rooms, each one a dense bullet-hell encounter where survival depends on
split-second dodge-rolls through curtains of projectiles. The interesting tension
is roguelike impermanence: death sends the player back to the top with nothing,
but each run offers different gun pickups and room layouts, rewarding adaptation
over memorization. The dodge-roll grants brief invincibility frames, creating a
rhythm of rolling through danger and firing back during recovery windows. Gun
variety — from tight railguns to wide shotgun blasts to bouncing orbs — means
each run plays differently depending on what the cathedral offers.

## What the Player Experiences

The player sees a gothic-styled title screen, starts a run, and enters the first
room of the cathedral. The top-down view shows a confined arena with the player
character at center. Enemies spawn and immediately begin firing patterned bullet
spreads. The player moves with WASD, aims with mouse, fires with click, and
dodge-rolls with spacebar. Clearing all enemies in a room opens exits to the
next.

Each floor consists of 5-7 rooms with a boss room at the end. Between rooms the
player may find gun pedestals offering a weapon swap, health pickups, or passive
upgrades. Guns have distinct firing patterns and ammo behavior. Floor bosses fill
the screen with elaborate bullet patterns that require precise rolling and
positioning. After defeating a floor boss, a brief interstitial shows stats
before descending to the next floor. Three floors complete a run with a victory
screen; death at any point shows a run summary with rooms cleared and enemies
defeated.

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

# 弹幕教堂（Bullet Cathedral）

在 `/workspace/game/` 用 Godot 4 开发 **Bullet Cathedral**，一款弹幕 Roguelike。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是一路向下穿越一座由程序化排布的敌意房间组成的教堂，每一间都是一场
密集的弹幕遭遇战，能否生还取决于在弹幕帷幕中千钧一发的翻滚闪避。有趣的张力来自
Roguelike 的无常：死亡会让玩家一无所有地被送回顶层，但每一轮都会提供不同的枪械
拾取与房间布局，奖励随机应变而非死记硬背。翻滚闪避会赋予短暂的无敌帧，从而形成
一种节奏——翻滚穿过危险，再在恢复窗口期反击。枪械的多样性——从紧束的电磁炮到
宽幅的霰弹爆射再到弹跳光球——意味着每一轮的玩法都会随教堂给出的东西而不同。

## 玩家体验流程

玩家看到一个哥特风格的标题画面，开始一轮游戏，进入教堂的第一个房间。俯视视角
展示出一个封闭的竞技场，玩家角色位于中央。敌人生成后立刻开始发射成形的散射弹幕。
玩家用 WASD 移动，用鼠标瞄准，点击开火，用空格键翻滚闪避。清空一个房间里的所有
敌人会打开通往下一间的出口。

每个楼层由 5-7 个房间组成，末尾是一个 Boss 房。房间之间玩家可能会发现提供武器
替换的枪械基座、生命拾取物或被动升级。各类枪械有各自独特的射击形态与弹药机制。
楼层 Boss 会用精心编排的弹幕形态填满屏幕，要求精准的翻滚与站位。击败楼层 Boss
之后，会有一段简短的过场展示数据，然后下降到下一层。三层全部通过即完成一轮并
进入胜利画面；在任何时刻死亡都会显示一份本轮总结，含已清房间数与已击败敌人数。

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

